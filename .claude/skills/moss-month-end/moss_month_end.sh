#!/usr/bin/env bash
# MOSS Month-End Consistency Checker
#
# Requires: bash, curl (both pre-installed on macOS)
#           python3 for JSON processing (install once via: xcode-select --install)
#
# Usage:
#   bash moss_month_end.sh             # current month
#   bash moss_month_end.sh 2026-05     # specific month
#
# Credentials: create moss-config.json in the same directory as this script:
#   {"public_key": "kid_...", "secret_key": "sk_..."}

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="${SCRIPT_DIR}/moss-config.json"
TARGET_MONTH="${1:-$(date +%Y-%m)}"
BASE_URL="https://public-api.getmoss.com"

# ── Helpers ────────────────────────────────────────────────────────────────

die() { echo "Error: $*" >&2; exit 1; }

# Extract a string value from a simple flat JSON file — no python3 needed
json_str() {
  grep -o "\"${1}\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" "$2" \
    | sed 's/.*:[[:space:]]*"\(.*\)"/\1/'
}

# ── Pre-flight ─────────────────────────────────────────────────────────────

[[ -f "$CONFIG" ]] \
  || die "moss-config.json not found at $SCRIPT_DIR
Create it with the content:
  {\"public_key\": \"kid_...\", \"secret_key\": \"sk_...\"}"

command -v python3 >/dev/null 2>&1 \
  || die "python3 is required for JSON processing.
Install it once with:  xcode-select --install"

PUBLIC_KEY=$(json_str "public_key" "$CONFIG")
SECRET_KEY=$(json_str "secret_key" "$CONFIG")
[[ -n "$PUBLIC_KEY" ]] || die "public_key not found in $CONFIG"
[[ -n "$SECRET_KEY" ]] || die "secret_key not found in $CONFIG"

# ── Temp files (cleaned up on exit) ────────────────────────────────────────

RESP_FILE=$(mktemp "/tmp/moss_resp.XXXXXX")
DATA_FILE=$(mktemp "/tmp/moss_data.XXXXXX.json")
trap 'rm -f "$RESP_FILE" "$DATA_FILE"' EXIT

echo '[]' > "$DATA_FILE"

# ── Authenticate ───────────────────────────────────────────────────────────

echo "Authenticating with MOSS..." >&2

curl -sf \
  -X POST "${BASE_URL}/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "client_id=${PUBLIC_KEY}" \
  --data-urlencode "client_secret=${SECRET_KEY}" \
  > "$RESP_FILE" \
  || die "Auth failed — check your keys in $CONFIG"

TOKEN=$(python3 -c "
import json, sys
d = json.load(open('${RESP_FILE}'))
t = d.get('access_token') or d.get('token')
if not t:
    sys.stderr.write('Auth response missing access_token\n')
    sys.exit(1)
print(t)
")

# ── Calculate date range ───────────────────────────────────────────────────

python3 - "$TARGET_MONTH" > "$RESP_FILE" << 'PYEOF'
import sys, calendar
year, m = map(int, sys.argv[1].split('-'))
sy, sm = year, m
for _ in range(12):
    sm -= 1
    if sm == 0:
        sm = 12
        sy -= 1
end_day = calendar.monthrange(year, m)[1]
print(f"{sy}-{sm:02d}-01")
print(f"{year}-{m:02d}-{end_day:02d}")
PYEOF

START_DATE=$(sed -n '1p' "$RESP_FILE")
END_DATE=$(sed -n '2p' "$RESP_FILE")

echo "Fetching expenses $START_DATE → $END_DATE..." >&2

# ── Fetch all pages ────────────────────────────────────────────────────────

PAGE=1
TOTAL=0

while true; do
  # Retry loop for rate limits
  for ATTEMPT in 1 2 3; do
    HTTP_CODE=$(curl -s -o "$RESP_FILE" -w "%{http_code}" \
      -H "Authorization: Bearer $TOKEN" \
      "${BASE_URL}/v1/expenses?from=${START_DATE}&to=${END_DATE}&limit=100&page=${PAGE}")

    if [[ "$HTTP_CODE" == "200" ]]; then
      break
    elif [[ "$HTTP_CODE" == "429" ]]; then
      WAIT=$((ATTEMPT * 10))
      echo "  Rate limited — waiting ${WAIT}s..." >&2
      sleep "$WAIT"
    else
      die "API error HTTP $HTTP_CODE on page $PAGE"
    fi
  done

  ADDED=$(python3 - "$RESP_FILE" "$DATA_FILE" << 'PYEOF'
import json, sys

resp = json.load(open(sys.argv[1]))
# Handle various response shapes MOSS might use
if isinstance(resp, list):
    items = resp
else:
    items = resp.get('data', resp.get('items', resp.get('expenses', [])))

existing = json.load(open(sys.argv[2]))
existing.extend(items)
json.dump(existing, open(sys.argv[2], 'w'))
print(len(items))
PYEOF
)

  TOTAL=$((TOTAL + ADDED))
  printf "  Page %d: %d items (running total: %d)\n" "$PAGE" "$ADDED" "$TOTAL" >&2
  [[ "$ADDED" -eq 0 ]] && break
  PAGE=$((PAGE + 1))
done

echo "$TOTAL expenses fetched. Running checks..." >&2
echo >&2

# ── Analysis and report ────────────────────────────────────────────────────

python3 - "$DATA_FILE" "$TARGET_MONTH" << 'PYEOF'
import json, sys
from collections import defaultdict
import calendar

expenses  = json.load(open(sys.argv[1]))
target_month = sys.argv[2]
target_year, target_m = map(int, target_month.split('-'))

RECURRENCE_THRESHOLD  = 10   # months out of last 12 to count as recurring
CONSISTENCY_MIN_MONTHS = 3   # minimum appearances before consistency is checked

APPROVED_STATUSES = {
    'approved', 'exported', 'paid', 'completed', 'booked', 'posted', 'processed'
}

# ── Field extractors (priority-ordered key lists for resilience) ──────────

def get(d, *keys, default='Unknown'):
    """Extract first matching field from a dict, handling dotted paths."""
    for k in keys:
        if '.' in k:
            v, parts = d, k.split('.')
            for p in parts:
                v = v.get(p) if isinstance(v, dict) else None
            if v:
                return str(v).strip()
        elif d.get(k):
            return str(d[k]).strip()
    return default

def vendor(e):
    return get(e,
        'merchantName', 'merchant_name', 'vendor', 'supplier',
        'merchant.name', 'creditor', 'payee', 'description')

def category(e):
    return get(e,
        'expenseAccount', 'expenseAccount.name', 'expense_account',
        'category', 'accountName', 'account_name', 'costAccount')

def cost_centre(e):
    return get(e,
        'costCenter', 'costCenter.name', 'cost_center',
        'costCentre', 'cost_centre', 'team', 'department',
        default='')

def tx_month(e):
    for k in ('date', 'transactionDate', 'transaction_date',
              'invoiceDate', 'invoice_date', 'createdAt', 'created_at'):
        v = str(e.get(k, ''))
        if len(v) >= 7:
            return v[:7]
    return ''

def tx_status(e):
    return get(e,
        'status', 'approvalStatus', 'approval_status',
        'workflowStatus', 'workflow_status',
        default='unknown').lower()

def tx_amount(e):
    for k in ('amount', 'totalAmount', 'total_amount', 'grossAmount',
              'gross_amount', 'netAmount', 'net_amount'):
        v = e.get(k)
        if v is not None:
            try:
                return float(str(v).replace(',', '').replace('£', '').strip())
            except ValueError:
                pass
    return None

# ── Build data structure: vendor → month → list of transactions ───────────

vendor_months = defaultdict(lambda: defaultdict(list))
all_months = set()

for e in expenses:
    v = vendor(e)
    m = tx_month(e)
    if not m:
        continue
    all_months.add(m)
    vendor_months[v][m].append({
        'category':    category(e),
        'cost_centre': cost_centre(e),
        'status':      tx_status(e),
        'amount':      tx_amount(e),
    })

last_12 = sorted(m for m in all_months if m < target_month)[-12:]

# ── Check 1: Coding inconsistencies ───────────────────────────────────────

inconsistencies = []
for v, months in vendor_months.items():
    if len(months) < CONSISTENCY_MIN_MONTHS:
        continue
    seen_combos = set()
    month_detail = {}
    for m, txns in sorted(months.items()):
        for t in txns:
            cat = t['category']
            cc  = t['cost_centre'] or '—'
            if cat != 'Unknown':
                seen_combos.add((cat, cc))
                month_detail[m] = f"{cat} / {cc}"
    if len(seen_combos) > 1:
        inconsistencies.append({'vendor': v, 'months': month_detail, 'combos': seen_combos})

inconsistencies.sort(key=lambda x: x['vendor'])

# ── Check 2: Missing recurring vendors ────────────────────────────────────

recurring = {
    v for v, months in vendor_months.items()
    if sum(1 for m in last_12 if m in months) >= RECURRENCE_THRESHOLD
}

missing = []
for v in sorted(recurring):
    if target_month not in vendor_months[v]:
        amounts = [
            t['amount']
            for m in last_12
            for t in vendor_months[v].get(m, [])
            if t['amount'] is not None
        ]
        avg = sum(amounts) / len(amounts) if amounts else None
        last_seen = max((m for m in vendor_months[v] if m in last_12), default='?')
        missing.append({'vendor': v, 'avg': avg, 'last_seen': last_seen})

# ── Check 3: Unapproved recurring items this month ────────────────────────

unapproved = []
for v in sorted(recurring):
    for t in vendor_months[v].get(target_month, []):
        s = t['status']
        if s not in APPROVED_STATUSES and s != 'unknown':
            unapproved.append({
                'vendor':   v,
                'status':   s,
                'category': t['category'],
                'amount':   t['amount'],
            })

# ── Print report ──────────────────────────────────────────────────────────

W = 60
print()
print(f"MOSS Month-End Review — {target_month}")
print("=" * W)
print(f"Expenses analysed: {len(expenses)}  |  Recurring vendors: {len(recurring)}")

# Check 1
print()
print(f"=== CODING INCONSISTENCIES ({len(inconsistencies)} found) ===")
if inconsistencies:
    for item in inconsistencies:
        print(f"\n  {item['vendor']}")
        for m, combo in sorted(item['months'].items()):
            print(f"    {m}  →  {combo}")
else:
    print("  All clear — no inconsistent coding found")

# Check 2
print()
print(f"=== MISSING RECURRING VENDORS ({len(missing)} found) ===")
if missing:
    for item in missing:
        avg_str = f"  avg £{item['avg']:,.2f}/mo" if item['avg'] else ''
        print(f"  {item['vendor']}{avg_str}  —  last seen {item['last_seen']}")
else:
    print("  All clear — all recurring vendors have submitted this month")

# Check 3
print()
print(f"=== UNAPPROVED RECURRING ITEMS ({len(unapproved)} found) ===")
if unapproved:
    for item in unapproved:
        amt_str = f"  £{item['amount']:,.2f}" if item['amount'] else ''
        print(f"  {item['vendor']}{amt_str}  —  status: {item['status']}  —  {item['category']}")
else:
    print("  All clear — all recurring items are approved")

print()
PYEOF
