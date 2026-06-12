#!/usr/bin/env python3
"""
MOSS Finance MCP Server
Exposes MOSS expense checks as tools in Claude Desktop / Claude Co-Work.

Credentials (in priority order):
  1. Environment variables set in claude_desktop_config.json:
       MOSS_API_PUBLIC_KEY  — Key ID (kid_...)
       MOSS_API_SECRET_KEY  — Secret Key (sk_...)
  2. moss-config.json in the same directory as this file (CLI fallback)
"""

from __future__ import annotations

import calendar
import json
import os
import time
from collections import defaultdict
from datetime import date
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from fastmcp import FastMCP

# ── Constants ──────────────────────────────────────────────────────────────

BASE_URL               = "https://public-api.getmoss.com"
RECURRENCE_THRESHOLD   = 10   # months out of last 12 to be "recurring"
CONSISTENCY_MIN_MONTHS = 3    # minimum appearances before checking consistency
APPROVED_STATUSES      = {"approved", "exported", "paid", "completed", "booked", "posted", "processed"}

# ── Credentials ────────────────────────────────────────────────────────────

def _load_credentials() -> tuple[str, str]:
    pub = os.environ.get("MOSS_API_PUBLIC_KEY")
    sec = os.environ.get("MOSS_API_SECRET_KEY")
    if pub and sec:
        return pub, sec
    config_file = Path(__file__).parent / "moss-config.json"
    if config_file.exists():
        cfg = json.loads(config_file.read_text())
        return cfg["public_key"], cfg["secret_key"]
    raise RuntimeError(
        "MOSS credentials not found.\n"
        "Set MOSS_API_PUBLIC_KEY and MOSS_API_SECRET_KEY in your Claude Desktop config,\n"
        "or create moss-config.json next to server.py."
    )

# ── API client ─────────────────────────────────────────────────────────────

class MossClient:
    def __init__(self) -> None:
        self._pub, self._sec = _load_credentials()
        self._token: str | None = None
        self._token_expiry: float = 0.0

        # Session with built-in 429 retry.
        # respect_retry_after_header=True (default) makes urllib3 sleep for
        # exactly the Retry-After value before each retry — no custom logic needed.
        # backoff_factor is the fallback when no Retry-After header is present:
        # sleep = backoff_factor * 2^(attempt-1) → 1s, 2s, 4s, 8s, 16s
        _retry = Retry(
            total=6,
            status_forcelist=[429],
            backoff_factor=1,
            respect_retry_after_header=True,
            raise_on_status=False,  # return the last response; we raise below
        )
        self._session = requests.Session()
        self._session.mount("https://", HTTPAdapter(max_retries=_retry))

        # Proactive rate-limit state per scope ("read" / "write")
        self._rl: dict[str, dict[str, int | None]] = {
            "read":  {"remaining": None, "reset": None},
            "write": {"remaining": None, "reset": None},
        }

    def _update_rate_limit(self, headers: requests.structures.CaseInsensitiveDict) -> None:
        scope = headers.get("X-RateLimit-Scope", "read").lower()
        if scope not in self._rl:
            scope = "read"
        remaining = headers.get("X-RateLimit-Remaining")
        reset     = headers.get("X-RateLimit-Reset")
        if remaining is not None:
            self._rl[scope]["remaining"] = int(remaining)
        if reset is not None:
            self._rl[scope]["reset"] = int(reset)

    def _throttle(self, scope: str = "read") -> None:
        """Sleep proactively if we've exhausted the current window."""
        info      = self._rl.get(scope, {})
        remaining = info.get("remaining")
        reset_ts  = info.get("reset")
        if remaining is not None and remaining <= 1 and reset_ts:
            wait = max(0.0, reset_ts - time.time()) + 0.5  # 0.5 s buffer
            if wait > 0:
                time.sleep(wait)

    def _ensure_token(self) -> None:
        if self._token and time.time() < self._token_expiry - 60:
            return
        resp = self._session.post(
            f"{BASE_URL}/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type":    "client_credentials",
                "client_id":     self._pub,
                "client_secret": self._sec,
            },
            timeout=30,
        )
        if resp.status_code == 401:
            raise RuntimeError("MOSS authentication failed — check your API keys.")
        resp.raise_for_status()
        body = resp.json()
        self._token = body["access_token"]
        self._token_expiry = time.time() + body.get("expires_in", 3600)

    def get(self, path: str, params: dict | None = None) -> dict | list:
        self._ensure_token()
        self._throttle("read")
        resp = self._session.get(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {self._token}"},
            params=params or {},
            timeout=30,
        )
        self._update_rate_limit(resp.headers)
        if resp.status_code == 429:
            # Retry adapter exhausted all attempts
            raise RuntimeError("MOSS API read rate limit exceeded after retries.")
        resp.raise_for_status()
        return resp.json()

    def fetch_expenses(self, start: str, end: str) -> list[dict]:
        all_items: list[dict] = []
        page = 1
        while True:
            data = self.get("/v1/expenses", {"from": start, "to": end, "limit": 100, "page": page})
            items = (
                data if isinstance(data, list)
                else data.get("data", data.get("items", data.get("expenses", [])))
            )
            if not items:
                break
            all_items.extend(items)
            page += 1
        return all_items

# ── Field extractors ───────────────────────────────────────────────────────

def _get(d: dict, *keys: str, default: str = "Unknown") -> str:
    for k in keys:
        if "." in k:
            v: object = d
            for part in k.split("."):
                v = v.get(part) if isinstance(v, dict) else None  # type: ignore[union-attr]
            if v:
                return str(v).strip()
        elif d.get(k):
            return str(d[k]).strip()
    return default

def _vendor(e: dict) -> str:
    return _get(e, "merchantName", "merchant_name", "vendor", "supplier",
                "merchant.name", "creditor", "payee", "description")

def _category(e: dict) -> str:
    return _get(e, "expenseAccount", "expenseAccount.name", "expense_account",
                "category", "accountName", "account_name", "costAccount")

def _cost_centre(e: dict) -> str:
    return _get(e, "costCenter", "costCenter.name", "cost_center",
                "costCentre", "cost_centre", "team", "department", default="")

def _month(e: dict) -> str:
    for k in ("date", "transactionDate", "transaction_date",
              "invoiceDate", "invoice_date", "createdAt", "created_at"):
        v = str(e.get(k, ""))
        if len(v) >= 7:
            return v[:7]
    return ""

def _status(e: dict) -> str:
    return _get(e, "status", "approvalStatus", "approval_status",
                "workflowStatus", "workflow_status", default="unknown").lower()

def _amount(e: dict) -> float | None:
    for k in ("amount", "totalAmount", "total_amount",
              "grossAmount", "gross_amount", "netAmount", "net_amount"):
        v = e.get(k)
        if v is not None:
            try:
                return float(str(v).replace(",", "").replace("£", "").strip())
            except ValueError:
                pass
    return None

# ── Analysis ───────────────────────────────────────────────────────────────

def _analyse(expenses: list[dict], target_month: str) -> str:
    # Build: vendor → month → [transaction dicts]
    vendor_months: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    all_months: set[str] = set()

    for e in expenses:
        v, m = _vendor(e), _month(e)
        if not m:
            continue
        all_months.add(m)
        vendor_months[v][m].append({
            "category":    _category(e),
            "cost_centre": _cost_centre(e),
            "status":      _status(e),
            "amount":      _amount(e),
        })

    last_12 = sorted(m for m in all_months if m < target_month)[-12:]

    recurring: set[str] = {
        v for v, months in vendor_months.items()
        if sum(1 for m in last_12 if m in months) >= RECURRENCE_THRESHOLD
    }

    # Check 1 — coding inconsistencies
    inconsistencies: list[dict] = []
    for v, months in vendor_months.items():
        if len(months) < CONSISTENCY_MIN_MONTHS:
            continue
        combos: set[tuple[str, str]] = set()
        month_detail: dict[str, str] = {}
        for m, txns in sorted(months.items()):
            for t in txns:
                cat, cc = t["category"], t["cost_centre"] or "—"
                if cat != "Unknown":
                    combos.add((cat, cc))
                    month_detail[m] = f"{cat} / {cc}"
        if len(combos) > 1:
            inconsistencies.append({"vendor": v, "months": month_detail})
    inconsistencies.sort(key=lambda x: x["vendor"])

    # Check 2 — missing recurring vendors
    missing: list[dict] = []
    for v in sorted(recurring):
        if target_month not in vendor_months[v]:
            amounts = [
                t["amount"]
                for m in last_12
                for t in vendor_months[v].get(m, [])
                if t["amount"] is not None
            ]
            avg = sum(amounts) / len(amounts) if amounts else None
            last_seen = max((m for m in vendor_months[v] if m in last_12), default="?")
            missing.append({"vendor": v, "avg": avg, "last_seen": last_seen})

    # Check 3 — unapproved recurring items this month
    unapproved: list[dict] = []
    for v in sorted(recurring):
        for t in vendor_months[v].get(target_month, []):
            if t["status"] not in APPROVED_STATUSES and t["status"] != "unknown":
                unapproved.append({
                    "vendor":   v,
                    "status":   t["status"],
                    "category": t["category"],
                    "amount":   t["amount"],
                })

    # Report
    lines = [
        f"MOSS Month-End Review — {target_month}",
        "=" * 60,
        f"Expenses analysed: {len(expenses)}  |  Recurring vendors tracked: {len(recurring)}",
        "",
        f"=== CODING INCONSISTENCIES ({len(inconsistencies)} found) ===",
    ]

    if inconsistencies:
        for item in inconsistencies:
            lines.append(f"\n  {item['vendor']}")
            for m, combo in sorted(item["months"].items()):
                lines.append(f"    {m}  →  {combo}")
    else:
        lines.append("  ✓ No inconsistencies found")

    lines += ["", f"=== MISSING RECURRING VENDORS ({len(missing)} found) ==="]
    if missing:
        for item in missing:
            avg_str = f"  avg £{item['avg']:,.2f}/mo" if item["avg"] else ""
            lines.append(f"  {item['vendor']}{avg_str}  —  last seen {item['last_seen']}")
    else:
        lines.append("  ✓ All recurring vendors have submitted this month")

    lines += ["", f"=== UNAPPROVED RECURRING ITEMS ({len(unapproved)} found) ==="]
    if unapproved:
        for item in unapproved:
            amt_str = f"  £{item['amount']:,.2f}" if item["amount"] else ""
            lines.append(f"  {item['vendor']}{amt_str}  —  status: {item['status']}  —  {item['category']}")
    else:
        lines.append("  ✓ All recurring items are approved")

    lines.append("")
    return "\n".join(lines)

# ── MCP server ─────────────────────────────────────────────────────────────

mcp = FastMCP("MOSS Finance")


@mcp.tool()
def run_month_end_check(month: str = "") -> str:
    """
    Run MOSS month-end consistency checks and return a formatted report.

    Fetches 13 months of expense history and checks for:
    - Invoice coding inconsistencies (same merchant coded to different categories or cost centres across months)
    - Missing recurring vendors (appear in 10+ of last 12 months but absent this month — likely need accruing)
    - Unapproved recurring items in the current month that may need accruing before month-end close

    Args:
        month: Target month in YYYY-MM format, e.g. "2026-05". Defaults to current month.

    Returns:
        A formatted text report with findings for each check.
    """
    if not month:
        today = date.today()
        month = f"{today.year}-{today.month:02d}"

    year, m = map(int, month.split("-"))
    sy, sm = year, m
    for _ in range(12):
        sm -= 1
        if sm == 0:
            sm, sy = 12, sy - 1

    start = f"{sy}-{sm:02d}-01"
    end   = f"{year}-{m:02d}-{calendar.monthrange(year, m)[1]:02d}"

    client   = MossClient()
    expenses = client.fetch_expenses(start, end)
    return _analyse(expenses, month)


@mcp.tool()
def get_vendor_history(vendor_name: str, months: int = 6) -> str:
    """
    Look up the expense history for a specific vendor.

    Useful for investigating a flagged inconsistency or checking what a vendor
    has been coded to in recent months.

    Args:
        vendor_name: The vendor name to search for (case-insensitive, partial match).
        months: How many months of history to fetch. Default 6, max 13.

    Returns:
        Month-by-month breakdown of category, cost centre, amount, and status for that vendor.
    """
    months = min(max(1, months), 13)
    today  = date.today()
    year, m = today.year, today.month
    sy, sm  = year, m
    for _ in range(months - 1):
        sm -= 1
        if sm == 0:
            sm, sy = 12, sy - 1

    start = f"{sy}-{sm:02d}-01"
    end   = f"{year}-{m:02d}-{calendar.monthrange(year, m)[1]:02d}"

    client   = MossClient()
    expenses = client.fetch_expenses(start, end)

    needle = vendor_name.lower()
    matched = [e for e in expenses if needle in _vendor(e).lower()]

    if not matched:
        return f"No expenses found matching '{vendor_name}' in the last {months} months."

    # Group by month
    by_month: dict[str, list[dict]] = defaultdict(list)
    for e in matched:
        by_month[_month(e)].append(e)

    lines = [f"Vendor history: '{vendor_name}' (last {months} months)", "=" * 50, ""]
    for mo in sorted(by_month.keys(), reverse=True):
        for e in by_month[mo]:
            amt  = _amount(e)
            amt_str = f"  £{amt:,.2f}" if amt else ""
            lines.append(
                f"  {mo}  {_vendor(e)}{amt_str}\n"
                f"         Category: {_category(e)}  |  Cost centre: {_cost_centre(e) or '—'}\n"
                f"         Status: {_status(e)}"
            )
    lines.append("")
    return "\n".join(lines)


# ── REST API — resource tools ──────────────────────────────────────────────
#
# One tool per major MOSS resource. Each returns a page of results; use
# page= to walk through larger sets. These complement the tailored tools
# above and give Claude direct access to the underlying data.

def _items_from(data: dict | list) -> list[dict]:
    """Normalise paginated and non-paginated MOSS responses to a plain list."""
    if isinstance(data, list):
        return data
    for key in ("data", "items", "results", "expenses", "invoices",
                "costCenters", "cost_centers", "expenseAccounts",
                "teamMembers", "users", "cards", "vendors"):
        if key in data and isinstance(data[key], list):
            return data[key]
    return []

def _pagination_note(data: dict | list, page: int, shown: int) -> str:
    if not isinstance(data, dict):
        return ""
    total = data.get("total") or data.get("count") or data.get("totalCount") or data.get("totalItems")
    if total and int(total) > shown:
        return f"\nShowing {shown} of {total}. Pass page={page + 1} for the next page."
    return ""


@mcp.tool()
def list_expenses(
    from_date: str = "",
    to_date: str = "",
    status: str = "",
    page: int = 1,
    limit: int = 50,
) -> str:
    """
    List expenses (card transactions and out-of-pocket) from MOSS.

    Args:
        from_date: Start date in YYYY-MM-DD format.
        to_date:   End date in YYYY-MM-DD format.
        status:    Filter by status, e.g. "approved", "pending", "exported".
        page:      Page number (default 1).
        limit:     Results per page (default 50, max 100).

    Returns:
        Formatted list of expenses with vendor, amount, category, cost centre, and status.
    """
    params: dict = {"page": page, "limit": min(limit, 100)}
    if from_date: params["from"]   = from_date
    if to_date:   params["to"]     = to_date
    if status:    params["status"] = status

    client = MossClient()
    data   = client.get("/v1/expenses", params)
    items  = _items_from(data)

    if not items:
        return "No expenses found for the given filters."

    lines = [f"Expenses — page {page} ({len(items)} results)", ""]
    for e in items:
        amt     = _amount(e)
        amt_str = f"  £{amt:,.2f}" if amt else ""
        lines.append(
            f"  {_month(e)}  {_vendor(e)}{amt_str}\n"
            f"    {_category(e)} / {_cost_centre(e) or '—'}  |  {_status(e)}"
        )
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


@mcp.tool()
def list_invoices(
    from_date: str = "",
    to_date: str = "",
    status: str = "",
    page: int = 1,
    limit: int = 50,
) -> str:
    """
    List supplier invoices from MOSS.

    Args:
        from_date: Start date in YYYY-MM-DD format.
        to_date:   End date in YYYY-MM-DD format.
        status:    Filter by status, e.g. "approved", "pending", "paid".
        page:      Page number (default 1).
        limit:     Results per page (default 50, max 100).

    Returns:
        Formatted list of invoices with supplier, amount, due date, and status.
    """
    params: dict = {"page": page, "limit": min(limit, 100)}
    if from_date: params["from"]   = from_date
    if to_date:   params["to"]     = to_date
    if status:    params["status"] = status

    client = MossClient()
    data   = client.get("/v1/invoices", params)
    items  = _items_from(data)

    if not items:
        return "No invoices found for the given filters."

    lines = [f"Invoices — page {page} ({len(items)} results)", ""]
    for inv in items:
        supplier = _get(inv, "supplierName", "supplier_name", "vendor", "supplier",
                        "creditor", "merchant.name", "description")
        amt      = _amount(inv)
        amt_str  = f"  £{amt:,.2f}" if amt else ""
        due      = _get(inv, "dueDate", "due_date", "paymentDue", default="")
        due_str  = f"  due {due}" if due else ""
        status_  = _status(inv)
        cat      = _category(inv)
        lines.append(f"  {supplier}{amt_str}{due_str}  |  {cat}  |  {status_}")
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


@mcp.tool()
def list_cost_centres() -> str:
    """
    List all cost centres configured in this MOSS account.

    Returns:
        Names and IDs of every cost centre.
    """
    client = MossClient()
    data   = client.get("/v1/cost-centers")
    items  = _items_from(data)

    if not items:
        return "No cost centres found (or endpoint path differs — try moss_get('/v1/cost-centers') to inspect the raw response)."

    lines = [f"Cost centres ({len(items)} total)", ""]
    for cc in items:
        name = _get(cc, "name", "title", "label")
        id_  = cc.get("id", cc.get("costCenterId", cc.get("cost_center_id", "")))
        lines.append(f"  {name}  (id: {id_})")
    return "\n".join(lines)


@mcp.tool()
def list_expense_accounts() -> str:
    """
    List all expense accounts (coding categories) configured in this MOSS account.

    Returns:
        Names and IDs of every expense account / GL code.
    """
    client = MossClient()
    # MOSS may use either of these paths
    for path in ("/v1/expense-accounts", "/v1/categories", "/v1/accounts"):
        try:
            data  = client.get(path)
            items = _items_from(data)
            if items:
                break
        except Exception:
            continue
    else:
        return "Could not retrieve expense accounts. Try moss_get('/v1/expense-accounts') to inspect the available paths."

    lines = [f"Expense accounts ({len(items)} total)", ""]
    for acct in items:
        name = _get(acct, "name", "title", "label", "accountName", "account_name")
        id_  = acct.get("id", acct.get("accountId", acct.get("account_id", "")))
        code = acct.get("code", acct.get("glCode", acct.get("gl_code", "")))
        code_str = f"  [{code}]" if code else ""
        lines.append(f"  {name}{code_str}  (id: {id_})")
    return "\n".join(lines)


@mcp.tool()
def list_team_members() -> str:
    """
    List all team members / users in this MOSS account.

    Returns:
        Names, emails, and roles of every team member.
    """
    client = MossClient()
    for path in ("/v1/team-members", "/v1/users", "/v1/members"):
        try:
            data  = client.get(path)
            items = _items_from(data)
            if items:
                break
        except Exception:
            continue
    else:
        return "Could not retrieve team members. Try moss_get('/v1/team-members') to inspect the available paths."

    lines = [f"Team members ({len(items)} total)", ""]
    for u in items:
        name  = _get(u, "name", "fullName", "full_name", "displayName")
        email = _get(u, "email", "emailAddress", "email_address", default="")
        role  = _get(u, "role", "userRole", "user_role", default="")
        parts = [f"  {name}"]
        if email != "Unknown": parts.append(email)
        if role  != "Unknown": parts.append(f"({role})")
        lines.append("  ".join(parts))
    return "\n".join(lines)


@mcp.tool()
def list_cards(page: int = 1, limit: int = 50) -> str:
    """
    List virtual and physical cards in this MOSS account.

    Args:
        page:  Page number (default 1).
        limit: Results per page (default 50).

    Returns:
        Card names, holders, status, and spend limits.
    """
    client = MossClient()
    data   = client.get("/v1/cards", {"page": page, "limit": limit})
    items  = _items_from(data)

    if not items:
        return "No cards found."

    lines = [f"Cards — page {page} ({len(items)} results)", ""]
    for c in items:
        name   = _get(c, "name", "cardName", "card_name", "label")
        holder = _get(c, "holderName", "holder_name", "cardHolder",
                      "owner.name", "user.name", default="")
        status = _get(c, "status", "cardStatus", default="")
        limit_ = c.get("limit") or c.get("spendLimit") or c.get("spend_limit")
        limit_str = f"  limit £{float(str(limit_).replace(',','')):,.2f}" if limit_ else ""
        holder_str = f"  ({holder})" if holder and holder != "Unknown" else ""
        lines.append(f"  {name}{holder_str}  {status}{limit_str}")
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


@mcp.tool()
def list_vendors(page: int = 1, limit: int = 50) -> str:
    """
    List vendors / suppliers / merchants known to MOSS.

    Args:
        page:  Page number (default 1).
        limit: Results per page (default 50).

    Returns:
        Vendor names, categories, and any available metadata.
    """
    client = MossClient()
    for path in ("/v1/vendors", "/v1/merchants", "/v1/suppliers"):
        try:
            data  = client.get(path, {"page": page, "limit": limit})
            items = _items_from(data)
            if items:
                break
        except Exception:
            continue
    else:
        return "Could not retrieve vendors. Try moss_get('/v1/vendors') to inspect the available paths."

    lines = [f"Vendors — page {page} ({len(items)} results)", ""]
    for v in items:
        name = _get(v, "name", "merchantName", "merchant_name", "supplierName")
        cat  = _get(v, "category", "expenseAccount", "accountName", default="")
        cat_str = f"  [{cat}]" if cat and cat != "Unknown" else ""
        lines.append(f"  {name}{cat_str}")
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


# ── REST API — generic escape hatch ───────────────────────────────────────

@mcp.tool()
def moss_get(path: str, params: str = "{}") -> str:
    """
    Make a GET request to any MOSS API endpoint and return the raw response.

    Use this when none of the specific tools cover your query — it gives
    direct access to the full MOSS REST API.

    Args:
        path:   API path starting with /, e.g. "/v1/expenses" or "/v1/cost-centers".
                See https://developers.getmoss.com for the full endpoint reference.
        params: Query parameters as a JSON object string,
                e.g. '{"from": "2026-01-01", "limit": 10, "status": "pending"}'.
                Omit or pass "{}" for no parameters.

    Returns:
        Raw API response as formatted JSON.

    Examples:
        moss_get("/v1/expenses", '{"from": "2026-05-01", "to": "2026-05-31", "limit": 5}')
        moss_get("/v1/cost-centers")
        moss_get("/v1/invoices", '{"status": "pending", "page": 2}')
    """
    try:
        parsed_params = json.loads(params) if params.strip() not in ("", "{}") else {}
    except json.JSONDecodeError as exc:
        return f"Invalid params JSON: {exc}\nPass a valid JSON object, e.g. '{{\"limit\": 10}}'."

    client = MossClient()
    result = client.get(path, parsed_params)
    return json.dumps(result, indent=2, default=str)


if __name__ == "__main__":
    mcp.run()
