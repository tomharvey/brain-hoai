"""Tests for MOSS month-end server using vcrpy cassettes and direct extractor tests."""
from __future__ import annotations

import json
import os
import pytest
import vcr

# Ensure credentials are available for MossClient instantiation
os.environ.setdefault("MOSS_API_PUBLIC_KEY", "kid_test_key")
os.environ.setdefault("MOSS_API_SECRET_KEY", "sk_test_secret")

from server import (
    MossClient,
    _vendor,
    _month,
    _amount,
    _status,
    _category_id,
    _cost_centre_id,
    _analyse,
    list_expenses,
    list_expense_accounts,
    list_users,
    list_suppliers,
    list_dimensions,
    list_teams,
    list_departments,
    list_tax_rates,
    list_payment_terms,
    list_bank_accounts,
    get_bank_account_balance,
    search_bank_transactions,
    search_files,
    get_file,
)

# ── Fixtures: realistic MOSS expense shapes ────────────────────────────────

def _make_expense(
    merchant_name: str = "TRAINLINE",
    expense_time: str = "2026-06-15T10:00:00Z",
    amount: str = "100.00",
    currency: str = "GBP",
    status: str = "APPROVED",
    expense_account_id: str = "acct-001",
    dimension_item_id: str = "cc-001",
    booking_text: str | None = None,
) -> dict:
    """Build a realistic MOSS expense dict matching the live API shape."""
    return {
        "id": "exp-001",
        "expenseSubType": "EXPENSE",
        "bookingText": booking_text,
        "description": None,
        "createTime": expense_time,
        "updateTime": expense_time,
        "expenseMetadata": {
            "type": "CARD_TRANSACTION",
            "merchantDetails": {
                "name": merchant_name,
                "address": "123 Street",
                "city": "London",
                "country": "GB",
            },
            "invoiceDate": expense_time,
            "bookingDate": expense_time[:10],
            "settlementDate": expense_time[:10],
        },
        "expenseType": "CARD_TRANSACTION",
        "status": status,
        "expenseTime": expense_time,
        "homeAmount": {"amount": amount, "currency": currency},
        "lines": [
            {
                "id": "line-001",
                "expenseAccountId": expense_account_id,
                "grossAmount": {"amount": amount, "currency": currency},
                "amount": {"amount": amount, "currency": currency},
                "netAmount": {"amount": amount, "currency": currency},
                "dimensions": [
                    {
                        "dimensionId": "00000000-0000-0000-0000-000000000001",
                        "dimensionItemId": dimension_item_id,
                    }
                ],
            }
        ],
    }


# ── Extractor tests ────────────────────────────────────────────────────────

class TestVendorExtractor:
    def test_extracts_merchant_name(self):
        e = _make_expense(merchant_name="Ocado")
        assert _vendor(e) == "Ocado"

    def test_strips_whitespace(self):
        e = _make_expense(merchant_name="  UBER   * PENDING  ")
        assert _vendor(e) == "UBER   * PENDING"

    def test_falls_back_to_booking_text(self):
        e = _make_expense()
        e["expenseMetadata"]["merchantDetails"]["name"] = ""
        e["bookingText"] = "Office supplies"
        assert _vendor(e) == "Office supplies"

    def test_returns_unknown_when_empty(self):
        e = _make_expense()
        e["expenseMetadata"] = {}
        e["bookingText"] = None
        assert _vendor(e) == "Unknown"


class TestMonthExtractor:
    def test_extracts_from_expense_time(self):
        e = _make_expense(expense_time="2026-03-15T10:00:00Z")
        assert _month(e) == "2026-03"

    def test_falls_back_to_create_time(self):
        e = _make_expense(expense_time="2026-04-01T09:00:00Z")
        del e["expenseTime"]
        assert _month(e) == "2026-04"

    def test_falls_back_to_nested_dates(self):
        e = _make_expense()
        del e["expenseTime"]
        del e["createTime"]
        del e["updateTime"]
        e["expenseMetadata"]["invoiceDate"] = "2026-05-20T00:00:00Z"
        assert _month(e) == "2026-05"

    def test_returns_empty_when_no_dates(self):
        e = _make_expense()
        del e["expenseTime"]
        del e["createTime"]
        del e["updateTime"]
        e["expenseMetadata"] = {}
        assert _month(e) == ""


class TestAmountExtractor:
    def test_extracts_from_home_amount(self):
        e = _make_expense(amount="574.68")
        assert _amount(e) == 574.68

    def test_handles_commas(self):
        e = _make_expense(amount="1,234.56")
        assert _amount(e) == 1234.56

    def test_falls_back_to_line_item(self):
        e = _make_expense(amount="99.99")
        del e["homeAmount"]
        assert _amount(e) == 99.99

    def test_returns_none_when_missing(self):
        e = {"id": "empty"}
        assert _amount(e) is None


class TestStatusExtractor:
    def test_extracts_and_lowercases(self):
        e = _make_expense(status="APPROVED")
        assert _status(e) == "approved"

    def test_draft_status(self):
        e = _make_expense(status="DRAFT")
        assert _status(e) == "draft"

    def test_defaults_to_unknown(self):
        assert _status({}) == "unknown"


class TestCategoryIdExtractor:
    def test_extracts_expense_account_id(self):
        e = _make_expense(expense_account_id="acct-xyz")
        assert _category_id(e) == "acct-xyz"

    def test_returns_empty_when_no_lines(self):
        e = {"id": "no-lines"}
        assert _category_id(e) == ""


class TestCostCentreIdExtractor:
    def test_extracts_dimension_item_id(self):
        e = _make_expense(dimension_item_id="cc-tech")
        assert _cost_centre_id(e) == "cc-tech"

    def test_returns_empty_when_no_dimensions(self):
        e = _make_expense()
        e["lines"][0]["dimensions"] = []
        assert _cost_centre_id(e) == ""


# ── Analysis tests ─────────────────────────────────────────────────────────

class MockClient:
    """Minimal mock that resolves UUIDs without HTTP calls."""
    _accounts = {
        "acct-001": "Staff Travel",
        "acct-002": "Platform Software",
        "acct-003": "Office Supplies",
    }
    _cost_centres = {
        "cc-001": "Technology",
        "cc-002": "Distribution",
        "cc-003": "Marketing",
    }

    def expense_account_name(self, account_id: str) -> str:
        return self._accounts.get(account_id, "Unknown")

    def cost_centre_name(self, dimension_item_id: str) -> str:
        return self._cost_centres.get(dimension_item_id, "")


def _build_recurring_vendor(
    name: str,
    months: list[str],
    account_id: str = "acct-001",
    cc_id: str = "cc-001",
    amount: str = "100.00",
    status: str = "APPROVED",
) -> list[dict]:
    """Build expenses for a vendor appearing in the given months."""
    return [
        _make_expense(
            merchant_name=name,
            expense_time=f"{m}-15T10:00:00Z",
            amount=amount,
            status=status,
            expense_account_id=account_id,
            dimension_item_id=cc_id,
        )
        for m in months
    ]


class TestAnalysis:
    def test_no_findings_when_all_consistent(self):
        """A vendor coded the same way every month should produce no inconsistencies."""
        months = [f"2025-{m:02d}" for m in range(7, 13)] + [f"2026-{m:02d}" for m in range(1, 7)]
        expenses = _build_recurring_vendor("AWS", months)
        report = _analyse(expenses, "2026-06", MockClient())
        assert "CODING INCONSISTENCIES (0 found)" in report
        assert "MISSING RECURRING VENDORS (0 found)" in report

    def test_detects_coding_inconsistency(self):
        """Same vendor coded to different accounts across months → flagged."""
        months_a = [f"2025-{m:02d}" for m in range(7, 13)]
        months_b = [f"2026-{m:02d}" for m in range(1, 7)]
        expenses = (
            _build_recurring_vendor("Stripe", months_a, account_id="acct-001")
            + _build_recurring_vendor("Stripe", months_b, account_id="acct-002")
        )
        report = _analyse(expenses, "2026-06", MockClient())
        assert "CODING INCONSISTENCIES (1 found)" in report
        assert "Stripe" in report

    def test_detects_missing_recurring_vendor(self):
        """Vendor present 10+ of last 12 months but absent in target → flagged."""
        # Present in 11 months (Jul 2025 – May 2026), absent in Jun 2026
        months = [f"2025-{m:02d}" for m in range(7, 13)] + [f"2026-{m:02d}" for m in range(1, 6)]
        expenses = _build_recurring_vendor("AWS", months)
        report = _analyse(expenses, "2026-06", MockClient())
        assert "MISSING RECURRING VENDORS (1 found)" in report
        assert "AWS" in report
        assert "avg £100.00/mo" in report

    def test_detects_unapproved_recurring_item(self):
        """Recurring vendor with a DRAFT item in the target month → flagged."""
        months = [f"2025-{m:02d}" for m in range(7, 13)] + [f"2026-{m:02d}" for m in range(1, 6)]
        expenses = _build_recurring_vendor("Slack", months, status="APPROVED")
        # Add a draft item in the target month
        expenses.append(
            _make_expense(
                merchant_name="Slack",
                expense_time="2026-06-10T10:00:00Z",
                status="DRAFT",
                expense_account_id="acct-002",
            )
        )
        report = _analyse(expenses, "2026-06", MockClient())
        assert "UNAPPROVED RECURRING ITEMS (1 found)" in report
        assert "Slack" in report
        assert "draft" in report

    def test_vendor_below_threshold_not_flagged(self):
        """Vendor appearing in only 5 months should not be flagged as missing."""
        months = [f"2026-{m:02d}" for m in range(1, 6)]
        expenses = _build_recurring_vendor("OneOff Ltd", months)
        report = _analyse(expenses, "2026-06", MockClient())
        assert "OneOff Ltd" not in report

    def test_deleted_expenses_excluded(self):
        """Deleted expenses should not count towards any checks."""
        months = [f"2025-{m:02d}" for m in range(7, 13)] + [f"2026-{m:02d}" for m in range(1, 6)]
        expenses = _build_recurring_vendor("Slack", months, status="APPROVED")
        # Add a deleted item in the target month — should NOT appear in unapproved
        expenses.append(
            _make_expense(
                merchant_name="Slack",
                expense_time="2026-06-10T10:00:00Z",
                status="DELETED",
                expense_account_id="acct-002",
            )
        )
        report = _analyse(expenses, "2026-06", MockClient())
        assert "UNAPPROVED RECURRING ITEMS (0 found)" in report
        assert "Excluded (deleted/cancelled): 1" in report

    def test_expense_count_in_report(self):
        expenses = _build_recurring_vendor("Test", ["2026-05", "2026-06"])
        report = _analyse(expenses, "2026-06", MockClient())
        assert "Expenses analysed: 2" in report


# ── VCR cassette tests (HTTP layer) ────────────────────────────────────────

CASSETTE_DIR = os.path.join(os.path.dirname(__file__), "cassettes")


def _make_cassette_response(body: dict, status_code: int = 200) -> dict:
    return {
        "status": {"code": status_code, "message": "OK"},
        "headers": {
            "Content-Type": ["application/json"],
            "X-RateLimit-Remaining": ["99"],
            "X-RateLimit-Reset": ["9999999999"],
            "X-RateLimit-Scope": ["read"],
        },
        "body": {"string": json.dumps(body)},
    }


def _token_interaction() -> dict:
    """Auth token exchange interaction for VCR cassettes."""
    return {
        "request": {
            "method": "POST",
            "uri": "https://public-api.getmoss.com/oauth2/token",
            "body": None,
            "headers": {"Content-Type": ["application/x-www-form-urlencoded"]},
        },
        "response": _make_cassette_response({
            "access_token": "test_token_abc",
            "expires_in": 3600,
            "token_type": "bearer",
        }),
    }


def _expenses_interaction(expenses: list[dict], page: int = 1, has_more: bool = False) -> dict:
    return {
        "request": {
            "method": "GET",
            "uri": f"https://public-api.getmoss.com/v1/expenses?from=2025-06-01&to=2026-06-30&page_size=100&page={page}",
            "body": None,
            "headers": {"Authorization": ["Bearer test_token_abc"]},
        },
        "response": _make_cassette_response({
            "data": expenses,
            "meta": {
                "pagination": {
                    "type": "offset",
                    "page": page,
                    "pageSize": 20,
                    "hasMore": has_more,
                    "totalPages": 1,
                    "totalItems": len(expenses),
                }
            },
            "errors": [],
        }),
    }


CASSETTE_DIR = os.path.join(os.path.dirname(__file__), "cassettes")


def _cassette(name: str):
    return vcr.VCR().use_cassette(os.path.join(CASSETTE_DIR, name), record_mode="none")


# ── Client-level VCR tests ────────────────────────────────────────────────

class TestClientVCR:
    def test_fetch_expenses_paginates(self):
        """fetch_expenses follows hasMore across pages."""
        with _cassette("pagination.yaml"):
            client = MossClient()
            expenses = client.fetch_expenses("2025-06-01", "2026-06-30")
            assert len(expenses) == 5

    def test_fetch_expenses_stops_on_empty(self):
        """fetch_expenses stops when data is empty."""
        with _cassette("empty.yaml"):
            client = MossClient()
            expenses = client.fetch_expenses("2025-06-01", "2026-06-30")
            assert expenses == []

    def test_rate_limit_headers_tracked(self):
        """Rate limit headers are parsed from responses."""
        with _cassette("ratelimit.yaml"):
            client = MossClient()
            client.fetch_expenses("2025-06-01", "2026-06-30")
            assert client._rl["read"]["remaining"] == 99

    def test_expense_account_lookup_cached(self):
        """Expense account names are fetched once and cached."""
        with _cassette("accounts.yaml"):
            client = MossClient()
            assert client.expense_account_name("acct-001") == "Staff Travel"
            assert client.expense_account_name("acct-002") == "Software"
            assert client.expense_account_name("acct-999") == "Unknown"

    def test_cost_centre_lookup(self):
        """Cost centre names are resolved via dimensions endpoint."""
        with _cassette("dimensions.yaml"):
            client = MossClient()
            assert client.cost_centre_name("cc-001") == "Technology"
            assert client.cost_centre_name("cc-002") == "Distribution"
            assert client.cost_centre_name("cc-999") == ""


# ── Tool-level VCR tests (one per API endpoint) ───────────────────────────

class TestToolVCR:
    """Each test covers one MCP tool backed by a real MOSS API endpoint."""

    # GET /v1/expenses
    def test_list_expenses(self):
        with _cassette("list_expenses.yaml"):
            result = list_expenses(from_date="2026-06-01", to_date="2026-06-30")
            assert "TRAINLINE" in result
            assert "£99.50" in result

    # GET /v1/expense-accounts
    def test_list_expense_accounts(self):
        with _cassette("accounts.yaml"):
            result = list_expense_accounts()
            assert "Staff Travel" in result
            assert "[1001]" in result
            assert "2 total" in result

    # GET /v1/users
    def test_list_users(self):
        with _cassette("users.yaml"):
            result = list_users()
            assert "Jane Smith" in result
            assert "jane@example.com" in result
            assert "2 total" in result

    # GET /v1/suppliers
    def test_list_suppliers(self):
        with _cassette("suppliers.yaml"):
            result = list_suppliers(page=1)
            assert "Acme Corp" in result
            assert "Widget Ltd" in result
            assert "page 1" in result.lower()

    # GET /v1/dimensions + /v1/dimensions/{id}/items
    def test_list_dimensions(self):
        with _cassette("dimensions.yaml"):
            result = list_dimensions()
            assert "Cost Center" in result
            assert "Technology" in result
            assert "Distribution" in result

    # GET /v1/teams
    def test_list_teams(self):
        with _cassette("teams.yaml"):
            result = list_teams()
            assert "Engineering" in result
            assert "Finance" in result
            assert "2 total" in result

    # GET /v1/departments
    def test_list_departments_empty(self):
        with _cassette("departments.yaml"):
            result = list_departments()
            assert "No departments found" in result

    # GET /v1/tax-rates
    def test_list_tax_rates(self):
        with _cassette("tax_rates.yaml"):
            result = list_tax_rates()
            assert "Standard Rate" in result
            assert "Zero Rate" in result
            assert "[SR]" in result

    # GET /v1/payment-terms
    def test_list_payment_terms(self):
        with _cassette("payment_terms.yaml"):
            result = list_payment_terms()
            assert "Net 30" in result
            assert "Net 60" in result

    # GET /v1/bank-accounts
    def test_list_bank_accounts(self):
        with _cassette("bank_accounts.yaml"):
            result = list_bank_accounts()
            assert "Main Operating Account" in result
            assert "1 total" in result

    # GET /v1/bank-accounts/{id}/balance
    def test_get_bank_account_balance(self):
        with _cassette("bank_account_balance.yaml"):
            result = get_bank_account_balance("ba-001")
            assert "125000.50" in result
            assert "GBP" in result

    # POST /v1/bank-transactions/search-query
    def test_search_bank_transactions(self):
        with _cassette("bank_transactions.yaml"):
            result = search_bank_transactions()
            assert "Payment to Acme" in result

    # POST /v1/files/search-query
    def test_search_files(self):
        with _cassette("search_files.yaml"):
            result = search_files(expense_ids=["exp-001"])
            assert "ACME" in result
            assert "file-001" in result
            assert "45,000 bytes" in result

    # GET /v1/files/{id}/content
    def test_get_file(self):
        with _cassette("get_file.yaml"):
            result = get_file("file-001")
            parsed = json.loads(result)
            assert parsed["mime_type"] == "image/png"
            assert parsed["size_bytes"] > 0
            assert len(parsed["content_base64"]) > 0
