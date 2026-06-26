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

import base64
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
EXCLUDED_STATUSES      = {"deleted", "cancelled", "rejected"}

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

        # Lookup caches (UUID → name), loaded lazily
        self._expense_accounts: dict[str, str] | None = None
        self._cost_centres: dict[str, str] | None = None

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

    def post(self, path: str, body: dict | None = None) -> dict | list:
        self._ensure_token()
        self._throttle("write")
        resp = self._session.post(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {self._token}", "Content-Type": "application/json"},
            json=body or {},
            timeout=30,
        )
        self._update_rate_limit(resp.headers)
        if resp.status_code == 429:
            raise RuntimeError("MOSS API write rate limit exceeded after retries.")
        resp.raise_for_status()
        return resp.json()

    def get_raw(self, path: str) -> requests.Response:
        """GET that returns the raw response (for binary file downloads)."""
        self._ensure_token()
        self._throttle("read")
        resp = self._session.get(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {self._token}"},
            timeout=60,
        )
        self._update_rate_limit(resp.headers)
        if resp.status_code == 429:
            raise RuntimeError("MOSS API read rate limit exceeded after retries.")
        resp.raise_for_status()
        return resp

    def _fetch_all_pages(self, path: str, params: dict | None = None) -> list[dict]:
        """Paginate through a MOSS endpoint, returning all items."""
        all_items: list[dict] = []
        page = 1
        base_params = dict(params or {})
        base_params.setdefault("page_size", 100)
        while True:
            base_params["page"] = page
            data = self.get(path, base_params)
            items = data.get("data", []) if isinstance(data, dict) else data
            if not items:
                break
            all_items.extend(items)
            # Stop if no more pages
            if isinstance(data, dict):
                pagination = data.get("meta", {}).get("pagination", {})
                if not pagination.get("hasMore", False):
                    break
            page += 1
        return all_items

    def fetch_expenses(self, start: str, end: str) -> list[dict]:
        return self._fetch_all_pages("/v1/expenses", {"from": start, "to": end})

    def expense_account_name(self, account_id: str) -> str:
        if self._expense_accounts is None:
            items = self._fetch_all_pages("/v1/expense-accounts")
            self._expense_accounts = {item["id"]: item.get("name", "Unknown") for item in items}
        return self._expense_accounts.get(account_id, "Unknown")

    def cost_centre_name(self, dimension_item_id: str) -> str:
        if self._cost_centres is None:
            self._cost_centres = {}
            dims = self.get("/v1/dimensions")
            for d in (dims.get("data", []) if isinstance(dims, dict) else dims):
                dim_items = self._fetch_all_pages(f"/v1/dimensions/{d['id']}/items")
                for item in dim_items:
                    self._cost_centres[item["id"]] = item.get("name", "Unknown")
        return self._cost_centres.get(dimension_item_id, "")

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
    # MOSS nests merchant name under expenseMetadata.merchantDetails.name
    md = e.get("expenseMetadata") or {}
    merchant = (md.get("merchantDetails") or {}).get("name")
    if merchant:
        return merchant.strip()
    # Fallback: bookingText or description
    return _get(e, "bookingText", "description")

def _category_id(e: dict) -> str:
    """Return the expense account UUID from the first line item."""
    lines = e.get("lines") or []
    if lines:
        return lines[0].get("expenseAccountId", "")
    return ""

def _cost_centre_id(e: dict) -> str:
    """Return the cost centre dimension item UUID from the first line item."""
    lines = e.get("lines") or []
    if lines:
        dims = lines[0].get("dimensions") or []
        if dims:
            return dims[0].get("dimensionItemId", "")
    return ""

def _month(e: dict) -> str:
    for k in ("expenseTime", "createTime", "updateTime"):
        v = str(e.get(k, ""))
        if len(v) >= 7:
            return v[:7]
    # Fallback: nested dates
    md = e.get("expenseMetadata") or {}
    for k in ("invoiceDate", "bookingDate", "settlementDate"):
        v = str(md.get(k, ""))
        if len(v) >= 7:
            return v[:7]
    return ""

def _status(e: dict) -> str:
    return _get(e, "status", default="unknown").lower()

def _amount(e: dict) -> float | None:
    # MOSS stores amounts as nested dicts: {"amount": "5.98", "currency": "GBP"}
    for k in ("homeAmount", "amount"):
        v = e.get(k)
        if isinstance(v, dict):
            raw = v.get("amount")
            if raw is not None:
                try:
                    return float(str(raw).replace(",", ""))
                except ValueError:
                    pass
        elif v is not None:
            try:
                return float(str(v).replace(",", "").replace("£", "").strip())
            except ValueError:
                pass
    # Fallback: first line item
    lines = e.get("lines") or []
    if lines:
        for k in ("grossAmount", "amount", "netAmount"):
            v = lines[0].get(k)
            if isinstance(v, dict) and v.get("amount") is not None:
                try:
                    return float(str(v["amount"]).replace(",", ""))
                except ValueError:
                    pass
    return None

# ── Analysis ───────────────────────────────────────────────────────────────

def _analyse(expenses: list[dict], target_month: str, client: MossClient) -> str:
    # Build: vendor → month → [transaction dicts], excluding deleted/cancelled
    vendor_months: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    all_months: set[str] = set()
    skipped = 0

    for e in expenses:
        s = _status(e)
        if s in EXCLUDED_STATUSES:
            skipped += 1
            continue
        v = _vendor(e)
        m = _month(e)
        if not m:
            continue
        all_months.add(m)
        vendor_months[v][m].append({
            "category_id":    _category_id(e),
            "cost_centre_id": _cost_centre_id(e),
            "status":         s,
            "amount":         _amount(e),
        })

    last_12 = sorted(m for m in all_months if m < target_month)[-12:]

    recurring: set[str] = {
        v for v, months in vendor_months.items()
        if sum(1 for m in last_12 if m in months) >= RECURRENCE_THRESHOLD
    }

    # Check 1 — coding inconsistencies (resolve UUIDs to names)
    inconsistencies: list[dict] = []
    for v, months in vendor_months.items():
        if len(months) < CONSISTENCY_MIN_MONTHS:
            continue
        combos: set[tuple[str, str]] = set()
        month_detail: dict[str, str] = {}
        for m, txns in sorted(months.items()):
            for t in txns:
                cat = client.expense_account_name(t["category_id"]) if t["category_id"] else "Unknown"
                cc = client.cost_centre_name(t["cost_centre_id"]) if t["cost_centre_id"] else "—"
                if not cc:
                    cc = "—"
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
                cat = client.expense_account_name(t["category_id"]) if t["category_id"] else "Unknown"
                unapproved.append({
                    "vendor":   v,
                    "status":   t["status"],
                    "category": cat,
                    "amount":   t["amount"],
                })

    # Report
    lines = [
        f"MOSS Month-End Review — {target_month}",
        "=" * 60,
        f"Expenses analysed: {len(expenses) - skipped}  |  Excluded (deleted/cancelled): {skipped}  |  Recurring vendors: {len(recurring)}",
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

mcp = FastMCP(
    "MOSS Finance",
    instructions=(
        "Read-only MOSS finance tools. All tools in this server only read data — "
        "none of them create, update, or delete anything in MOSS. They are safe "
        "to run without confirmation."
    ),
)


@mcp.tool()
def run_month_end_check(month: str = "") -> str:
    """
    [Read-only] Run MOSS month-end consistency checks and return a formatted report.

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
    return _analyse(expenses, month, client)


@mcp.tool()
def get_vendor_history(vendor_name: str, months: int = 6) -> str:
    """
    [Read-only] Look up the expense history for a specific vendor.

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
            cat_id = _category_id(e)
            cc_id  = _cost_centre_id(e)
            cat  = client.expense_account_name(cat_id) if cat_id else "Unknown"
            cc   = client.cost_centre_name(cc_id) if cc_id else "—"
            lines.append(
                f"  {mo}  {_vendor(e)}{amt_str}\n"
                f"         Category: {cat}  |  Cost centre: {cc or '—'}\n"
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
    pagination = data.get("meta", {}).get("pagination", {})
    total = pagination.get("totalItems") or data.get("total") or data.get("count")
    if total and int(total) > shown:
        return f"\nShowing {shown} of {total}. Pass page={page + 1} for the next page."
    return ""


@mcp.tool()
def list_expenses(
    from_date: str = "",
    to_date: str = "",
    status: str = "",
    page: int = 1,
) -> str:
    """
    [Read-only] List expenses (card transactions, invoices, reimbursements) from MOSS.

    MOSS treats all spend types as expenses — card transactions, supplier
    invoices, reimbursements, mileage, and per diem are all returned here.
    Filter by date range and/or status.

    Args:
        from_date: Start date in YYYY-MM-DD format.
        to_date:   End date in YYYY-MM-DD format.
        status:    Filter by status, e.g. "APPROVED", "DRAFT", "SUBMITTED".
        page:      Page number (default 1). Each page returns up to 100 results.

    Returns:
        Formatted list of expenses with vendor, amount, category, cost centre, and status.
    """
    params: dict = {"page": page, "page_size": 100}
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
        cat_id = _category_id(e)
        cc_id  = _cost_centre_id(e)
        cat  = client.expense_account_name(cat_id) if cat_id else "Unknown"
        cc   = client.cost_centre_name(cc_id) if cc_id else "—"
        lines.append(
            f"  {_month(e)}  {_vendor(e)}{amt_str}\n"
            f"    {cat} / {cc or '—'}  |  {_status(e)}"
        )
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


@mcp.tool()
def list_expense_accounts() -> str:
    """
    [Read-only] List all expense accounts (GL codes / coding categories) in this MOSS account.

    Use this to understand what categories are available when reviewing how
    expenses have been coded. The IDs returned here match the expenseAccountId
    on expense line items.

    Returns:
        Names, GL codes, and IDs of every expense account.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/expense-accounts")

    if not items:
        return "No expense accounts found."

    lines = [f"Expense accounts ({len(items)} total)", ""]
    for acct in items:
        name = _get(acct, "name")
        code = acct.get("code", "")
        code_str = f"  [{code}]" if code else ""
        lines.append(f"  {name}{code_str}  (id: {acct['id']})")
    return "\n".join(lines)


@mcp.tool()
def list_users() -> str:
    """
    [Read-only] List all users in this MOSS account.

    Use this to look up who created or owns an expense, or to find a user's
    ID for filtering. The user IDs returned here match the createdBy field
    on expenses.

    Returns:
        Names, emails, and roles of every user.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/users")

    if not items:
        return "No users found."

    lines = [f"Users ({len(items)} total)", ""]
    for u in items:
        name  = _get(u, "name", "fullName", "displayName")
        email = _get(u, "email", "emailAddress", default="")
        role  = _get(u, "role", "userRole", default="")
        parts = [f"  {name}"]
        if email != "Unknown": parts.append(email)
        if role  != "Unknown": parts.append(f"({role})")
        lines.append("  ".join(parts))
    return "\n".join(lines)


@mcp.tool()
def list_suppliers(page: int = 1) -> str:
    """
    [Read-only] List suppliers (vendors / merchants) known to MOSS.

    A supplier is any company or individual that has appeared on an expense.
    The supplier IDs returned here match the supplierId field on expenses.

    Args:
        page: Page number (default 1). Each page returns up to 100 results.

    Returns:
        Supplier names and IDs.
    """
    client = MossClient()
    data   = client.get("/v1/suppliers", {"page": page, "page_size": 100})
    items  = _items_from(data)

    if not items:
        return "No suppliers found."

    lines = [f"Suppliers — page {page} ({len(items)} results)", ""]
    for s in items:
        name = _get(s, "name", "merchantName", "supplierName")
        lines.append(f"  {name}  (id: {s.get('id', '')})")
    lines.append(_pagination_note(data, page, len(items)))
    return "\n".join(lines)


@mcp.tool()
def list_dimensions() -> str:
    """
    [Read-only] List all dimensions and their items (e.g. cost centres, cost carriers).

    Dimensions are custom groupings used to tag expenses. The most common
    dimension is "Cost Center". The dimension item IDs match the dimensionItemId
    on expense line items.

    Returns:
        Each dimension with all its items (names, codes, and IDs).
    """
    client = MossClient()
    dims   = client.get("/v1/dimensions")
    dim_list = dims.get("data", []) if isinstance(dims, dict) else dims

    if not dim_list:
        return "No dimensions found."

    lines = []
    for d in dim_list:
        dim_items = client._fetch_all_pages(f"/v1/dimensions/{d['id']}/items")
        lines.append(f"{d.get('name', 'Unknown')}  ({len(dim_items)} items)")
        for item in dim_items:
            code = item.get("code", "")
            code_str = f"  [{code}]" if code else ""
            lines.append(f"    {item.get('name', 'Unknown')}{code_str}  (id: {item['id']})")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def list_teams() -> str:
    """
    [Read-only] List all teams configured in this MOSS account.

    Returns:
        Team names and IDs.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/teams")

    if not items:
        return "No teams found."

    lines = [f"Teams ({len(items)} total)", ""]
    for t in items:
        name = _get(t, "name")
        lines.append(f"  {name}  (id: {t.get('id', '')})")
    return "\n".join(lines)


@mcp.tool()
def list_departments() -> str:
    """
    [Read-only] List all departments configured in this MOSS account.

    Returns:
        Department names and IDs.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/departments")

    if not items:
        return "No departments found."

    lines = [f"Departments ({len(items)} total)", ""]
    for d in items:
        name = _get(d, "name")
        lines.append(f"  {name}  (id: {d.get('id', '')})")
    return "\n".join(lines)


@mcp.tool()
def list_tax_rates() -> str:
    """
    [Read-only] List all tax rates configured in this MOSS account.

    Useful for understanding VAT treatment on expenses. The tax rate IDs
    match the taxRateId on expense line items.

    Returns:
        Tax rate names, percentages, codes, and IDs.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/tax-rates")

    if not items:
        return "No tax rates found."

    lines = [f"Tax rates ({len(items)} total)", ""]
    for t in items:
        name = _get(t, "name")
        rate = t.get("rate", t.get("percentage", ""))
        rate_str = f"  {rate}%" if rate else ""
        code = t.get("code", "")
        code_str = f"  [{code}]" if code else ""
        lines.append(f"  {name}{rate_str}{code_str}  (id: {t.get('id', '')})")
    return "\n".join(lines)


@mcp.tool()
def list_payment_terms() -> str:
    """
    [Read-only] List all payment terms configured in this MOSS account.

    Payment terms define when supplier invoices are due (e.g. Net 30, Net 60).

    Returns:
        Payment term names and IDs.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/payment-terms")

    if not items:
        return "No payment terms found."

    lines = [f"Payment terms ({len(items)} total)", ""]
    for pt in items:
        name = _get(pt, "name")
        lines.append(f"  {name}  (id: {pt.get('id', '')})")
    return "\n".join(lines)


@mcp.tool()
def list_bank_accounts() -> str:
    """
    [Read-only] List all bank accounts connected to this MOSS account.

    Returns:
        Bank account names, IBANs (masked), and IDs.
    """
    client = MossClient()
    items  = client._fetch_all_pages("/v1/bank-accounts")

    if not items:
        return "No bank accounts found."

    lines = [f"Bank accounts ({len(items)} total)", ""]
    for ba in items:
        name = _get(ba, "name", "accountName")
        iban = _get(ba, "iban", "maskedIban", default="")
        iban_str = f"  {iban}" if iban != "Unknown" else ""
        lines.append(f"  {name}{iban_str}  (id: {ba.get('id', '')})")
    return "\n".join(lines)


@mcp.tool()
def get_bank_account_balance(bank_account_id: str) -> str:
    """
    [Read-only] Get the current balance of a specific bank account.

    Use list_bank_accounts first to find the bank account ID.

    Args:
        bank_account_id: The UUID of the bank account.

    Returns:
        The current balance with currency.
    """
    client = MossClient()
    data   = client.get(f"/v1/bank-accounts/{bank_account_id}/balance")
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
def search_bank_transactions(
    from_date: str = "",
    to_date: str = "",
    bank_account_id: str = "",
) -> str:
    """
    [Read-only] Search bank transactions in MOSS.

    This uses the write rate limit (20/min) as it is a POST endpoint.
    Use sparingly and batch queries where possible.

    Args:
        from_date:        Start date in YYYY-MM-DD format.
        to_date:          End date in YYYY-MM-DD format.
        bank_account_id:  Filter to a specific bank account UUID.

    Returns:
        Bank transactions as formatted JSON.
    """
    filters: dict = {}
    if from_date:        filters["from"] = from_date
    if to_date:          filters["to"] = to_date
    if bank_account_id:  filters["bankAccountId"] = bank_account_id

    client = MossClient()
    data   = client.post("/v1/bank-transactions/search-query", {"filters": filters})
    return json.dumps(data, indent=2, default=str)


# ── Files / receipts ──────────────────────────────────────────────────────

@mcp.tool()
def search_files(expense_ids: list[str]) -> str:
    """
    [Read-only] Search for files (receipts, invoices, attachments) linked to specific expenses.

    Use this to check whether an expense has a receipt attached, or to get
    file IDs for downloading with get_file. You can pass up to 50 expense IDs
    at once — batch them to stay within the 20 requests/minute write limit.

    This is the first step before downloading a file. Get expense IDs from
    list_expenses or run_month_end_check, then pass them here to find
    attached files.

    Args:
        expense_ids: List of expense UUIDs to search for attached files.

    Returns:
        A list of files with their IDs, names, sizes, and linked expense.
        Use the file ID with get_file to download the actual document.
    """
    client = MossClient()
    data = client.post("/v1/files/search-query", {"filters": {"expenseIds": expense_ids}})
    items = data.get("data", []) if isinstance(data, dict) else data

    if not items:
        return "No files found for the given expense IDs."

    lines = [f"Files found: {len(items)}", ""]
    for f in items:
        name = f.get("name", "unnamed")
        size = f.get("size")
        size_str = f"  ({size:,} bytes)" if size else ""
        created = f.get("createTime", "")[:10]
        lines.append(f"  {name}{size_str}  uploaded {created}")
        lines.append(f"    file_id: {f['id']}")
    return "\n".join(lines)


@mcp.tool()
def get_file(file_id: str) -> str:
    """
    [Read-only] Download a file from MOSS and return it as base64-encoded content.

    Use this after search_files to retrieve the actual receipt, invoice,
    or attachment. In Claude co:work the image will render inline.
    In Claude Desktop the base64 data is returned as text.

    Args:
        file_id: The file UUID returned by search_files.

    Returns:
        A JSON object with the file's MIME type, name, and base64-encoded content.
    """
    client = MossClient()
    resp = client.get_raw(f"/v1/files/{file_id}/content")

    content_type = resp.headers.get("Content-Type", "application/octet-stream")
    encoded = base64.b64encode(resp.content).decode("ascii")

    return json.dumps({
        "mime_type": content_type,
        "size_bytes": len(resp.content),
        "content_base64": encoded,
    })


if __name__ == "__main__":
    mcp.run()
