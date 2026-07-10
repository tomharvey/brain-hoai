#!/usr/bin/env python3
"""Compute per-person uptake metrics and buckets from the normalised layer.

Reads reference/ai-tool-usage-reports/normalised.csv (regenerate first with
normalise.py), joins AI capability stage scores from people/ frontmatter and
stage justifications from stage-justifications.psv, and writes:
  reference/ai-tool-usage-reports/uptake-metrics.csv   (gitignored, full data)
plus a markdown table on stdout for embedding in reports.

Methodology: initiatives/ai-tool-uptake-measurement.md
  - never compare raw request counts across products
  - within-product percentile, product class, breadth -> bucket
  - buckets are a screen against the Stage 1-4 capability scores, not a score
"""

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
REPORTS_DIR = VAULT / "reference" / "ai-tool-usage-reports"

PRODUCT_CLASS = {
    "Chat": "chat",
    "ChatGPT": "chat",
    "Claude in Chrome": "assisted",
    "Claude Design": "assisted",
    "Cowork": "agentic",
    "Claude Code": "agentic",
    "Cursor": "agentic",
    "Office Agents": "agentic",
    "Research": "agentic",
}
CLASS_RANK = {"chat": 0, "assisted": 1, "agentic": 2}

# email -> people/ slug where filename heuristics are wrong or ambiguous.
# None = known to have no people file (or excluded from scoring join).
SLUG_OVERRIDES = {
    "christian@flockcover.com": "christian-leth-nielsen",  # chris.md is Chris Fothergill
    "matthew.smith@flockcover.com": "matt-smith-uw",       # matt.md is Matthew Price
    "matthew.price@flockcover.com": "matt",
    "kayleigh.bradbury@flockcover.com": "kaylee",          # kaylee.md "surname TBC" = Bradbury
    "daisie.baker@flockcover.com": "daisy-mae-baker",
    "aleksandra.yaneva@flockcover.com": "aleks-yanova",
    "alexander.dyball@flockcover.com": "alex-dyball",
    "tom.harvey@flockcover.com": None,                     # self
    "antton@flockcover.com": None,
    "billy.bone@flockcover.com": None,
    "charlie.dowrick@flockcover.com": None,
    "connie.fitzpatrick@flockcover.com": None,
    "craig.hill@flockcover.com": None,
    "jai.patel@flockcover.com": None,
    "joan.canellas@flockcover.com": None,
    "pavel@flockcover.com": None,
}
NICKNAMES = {"oliver": "ollie", "aleksandra": "aleks", "jemima": "mima",
             "matthew": "matt", "ismael": "ishmael", "christian": "chris"}


def load_people():
    people = {}
    for p in (VAULT / "people").glob("*.md"):
        text = p.read_text()
        if not text.startswith("---"):
            continue
        fm = text.split("---")[1]
        def field(name):
            m = re.search(rf"^{name}:\s*(.+)$", fm, re.M)
            return m[1].strip().strip('"') if m else None
        people[p.stem] = {
            "title": field("title") or p.stem,
            "stage": field("ai_activation_stage"),
            "confidence": field("ai_activation_confidence"),
            "email": field("email"),
            "role": field("role") or "",
        }
    return people


def email_to_slug(email, people):
    if email in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[email]
    by_email = {v["email"]: k for k, v in people.items() if v["email"]}
    if email in by_email:
        return by_email[email]
    local = email.split("@")[0]
    parts = local.split(".")
    first, last = parts[0], parts[1] if len(parts) > 1 else None
    for f in dict.fromkeys([first, NICKNAMES.get(first, first)]):
        for cand in ([f"{f}-{last}", f] if last else [f]):
            if cand in people:
                return cand
    return None


def load_justifications():
    path = REPORTS_DIR / "stage-justifications.psv"
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text().splitlines():
        if line.strip():
            slug, _stage, _conf, just = line.split("|", 3)
            out[slug] = just
    return out


def main():
    people = load_people()
    justifications = load_justifications()

    # aggregate normalised rows per person x product over the whole window
    per_product = defaultdict(lambda: defaultdict(lambda: {"requests": 0, "active_days": 0, "spend": 0.0}))
    months_active = defaultdict(set)  # email -> {"2026-06", "2026-07"} (anthropic/cursor only)
    for r in csv.DictReader(open(REPORTS_DIR / "normalised.csv")):
        if r["is_person"] != "true":
            continue
        d = per_product[r["person_email"]][r["product"]]
        d["requests"] += int(r["requests"])
        d["active_days"] += int(r["active_days"] or 0)
        d["spend"] += float(r["spend_usd"] or 0)
        if r["period_start"][:7] == r["period_end"][:7]:  # single-month row
            months_active[r["person_email"]].add(r["period_start"][:7])

    # within-product percentile over the window
    product_totals = defaultdict(list)
    for email, prods in per_product.items():
        for prod, d in prods.items():
            product_totals[prod].append(d["requests"])
    def percentile(prod, requests):
        vals = product_totals[prod]
        if len(vals) == 1:
            return 100
        below = sum(1 for v in vals if v < requests)
        return round(100 * below / (len(vals) - 1))

    rows = []
    matched_slugs = set()
    for email, prods in sorted(per_product.items()):
        slug = email_to_slug(email, people)
        if slug:
            matched_slugs.add(slug)
        person = people.get(slug, {})
        classes = {PRODUCT_CLASS.get(p, "chat") for p in prods}
        top_class = max(classes, key=lambda c: CLASS_RANK[c])
        breadth = len(prods)
        pcts = {p: percentile(p, d["requests"]) for p, d in prods.items()}
        max_pct_product = max(pcts, key=pcts.get)
        max_pct = pcts[max_pct_product]
        agentic_pcts = [v for p, v in pcts.items() if PRODUCT_CLASS.get(p) == "agentic"]
        agentic_pct = max(agentic_pcts) if agentic_pcts else None
        sustained = {"2026-06", "2026-07"} <= months_active[email]
        active_days = sum(d["active_days"] for d in prods.values()) or None
        spend = round(sum(d["spend"] for d in prods.values()), 2)
        total_requests = sum(d["requests"] for d in prods.values())

        if agentic_pct is not None and agentic_pct >= 60 and breadth >= 3 and sustained:
            bucket = "power"
        elif breadth >= 2 or max_pct >= 75:
            bucket = "regular"
        else:
            bucket = "light"

        stage = person.get("stage")
        mismatch = ""
        is_self = email == "tom.harvey@flockcover.com"
        if is_self:
            pass  # vault owner — outside the scoring population
        elif stage and int(stage) >= 3 and bucket == "light":
            mismatch = "stage>=3 but light telemetry"
        elif bucket == "power" and (not stage or int(stage) <= 2):
            mismatch = "power telemetry but stage<=2/unscored"

        rows.append({
            "person": "Tom Harvey (self)" if is_self else (person.get("title") or email.split("@")[0]),
            "email": email,
            "role": person.get("role", ""),
            "ai_stage": stage or "",
            "stage_confidence": person.get("confidence") or "",
            "bucket": bucket,
            "top_class": top_class,
            "breadth": breadth,
            "products": "; ".join(f"{p}:{d['requests']}" for p, d in sorted(prods.items(), key=lambda x: -x[1]["requests"])),
            "total_requests": total_requests,
            "max_percentile": max_pct,
            "max_percentile_product": max_pct_product,
            "agentic_percentile": agentic_pct if agentic_pct is not None else "",
            "active_days_cursor": active_days if any(PRODUCT_CLASS.get(p) == "agentic" and p == "Cursor" for p in prods) else "",
            "jun_active": "2026-06" in months_active[email],
            "jul_active": "2026-07" in months_active[email],
            "sustained": sustained,
            "spend_usd": spend,
            "mismatch": mismatch,
            "stage_justification": justifications.get(slug, ""),
        })

    # scored people with no telemetry at all -> dormant
    for slug, v in sorted(people.items()):
        if v["stage"] and slug not in matched_slugs:
            rows.append({
                "person": v["title"], "email": v.get("email") or "", "role": v["role"],
                "ai_stage": v["stage"], "stage_confidence": v["confidence"] or "",
                "bucket": "dormant", "top_class": "", "breadth": 0, "products": "",
                "total_requests": 0, "max_percentile": "", "max_percentile_product": "",
                "active_days_cursor": "", "jun_active": False, "jul_active": False,
                "sustained": False, "spend_usd": 0,
                "mismatch": "stage>=3 but no telemetry" if int(v["stage"]) >= 3 else "",
                "stage_justification": justifications.get(slug, ""),
            })

    bucket_order = {"power": 0, "regular": 1, "light": 2, "dormant": 3}
    rows.sort(key=lambda r: (bucket_order[r["bucket"]], -(r["total_requests"] or 0)))

    out = REPORTS_DIR / "uptake-metrics.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    counts = defaultdict(int)
    for r in rows:
        counts[r["bucket"]] += 1
    print(f"wrote {len(rows)} people -> {out}", file=sys.stderr)
    print(f"buckets: {dict(counts)}", file=sys.stderr)

    # markdown table on stdout for the report
    print("| Person | Stage | Conf | Bucket | Class | Breadth | Products (requests) | Top %ile | Cursor days | Jun/Jul | Spend $ | Flag |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        jj = ("✓" if r["jun_active"] else "–") + "/" + ("✓" if r["jul_active"] else "–")
        pct = f"{r['max_percentile']} ({r['max_percentile_product']})" if r["max_percentile"] != "" else ""
        print(f"| {r['person']} | {r['ai_stage'] or '—'} | {r['stage_confidence'] or '—'} | {r['bucket']} | {r['top_class']} | {r['breadth']} | {r['products']} | {pct} | {r['active_days_cursor']} | {jj} | {r['spend_usd']} | {r['mismatch']} |")


if __name__ == "__main__":
    main()
