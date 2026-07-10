#!/usr/bin/env python3
"""Normalise vendor AI usage reports into the uptake schema.

Schema v0.1 — see initiatives/ai-tool-uptake-measurement.md
Grain: person x vendor x product x period (summed across models).

Raw reports live in reference/ai-tool-usage-reports/<vendor>/YYYY-MM.csv
(or YYYY-MM-partial-to-DD.csv). Output is regenerated in full on every run:
reference/ai-tool-usage-reports/normalised.csv
"""

import calendar
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parents[2] / "reference" / "ai-tool-usage-reports"
OUT_PATH = REPORTS_DIR / "normalised.csv"

FIELDS = [
    "person_email", "is_person", "vendor", "product",
    "period_start", "period_end", "requests", "spend_usd",
]


def period_from_filename(path):
    """YYYY-MM.csv -> full month; YYYY-MM-partial-to-DD.csv -> month start to DD."""
    m = re.match(r"(\d{4})-(\d{2})(?:-partial-to-(\d{2}))?\.csv$", path.name)
    if not m:
        raise ValueError(f"unrecognised report filename: {path.name}")
    year, month, last_day = int(m[1]), int(m[2]), m[3]
    end = int(last_day) if last_day else calendar.monthrange(year, month)[1]
    return f"{year}-{month:02d}-01", f"{year}-{month:02d}-{end:02d}"


def normalise_anthropic(path):
    start, end = period_from_filename(path)
    agg = defaultdict(lambda: {"requests": 0, "spend_usd": 0.0})
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            email = row["user_email"].strip()
            key = (email, row["product"])
            agg[key]["requests"] += int(row["total_requests"] or 0)
            agg[key]["spend_usd"] += float(row["total_net_spend_usd"] or 0)
    for (email, product), totals in agg.items():
        is_person = "@" in email
        yield {
            "person_email": email if is_person else "",
            "is_person": str(is_person).lower(),
            "vendor": "anthropic",
            "product": product,
            "period_start": start,
            "period_end": end,
            "requests": totals["requests"],
            "spend_usd": round(totals["spend_usd"], 2),
        }


# Vendor name -> normaliser. Add cursor/openai here when their reports arrive;
# each takes a raw CSV path and yields rows in the v0.1 schema.
NORMALISERS = {
    "anthropic": normalise_anthropic,
}


def main():
    rows = []
    for vendor, fn in NORMALISERS.items():
        vendor_dir = REPORTS_DIR / vendor
        for path in sorted(vendor_dir.glob("*.csv")) if vendor_dir.is_dir() else []:
            rows.extend(fn(path))
    if not rows:
        sys.exit("no raw reports found")
    rows.sort(key=lambda r: (r["period_start"], r["vendor"], r["person_email"], r["product"]))
    with open(OUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    people = {r["person_email"] for r in rows if r["is_person"] == "true"}
    print(f"wrote {len(rows)} rows, {len(people)} people -> {OUT_PATH}")


if __name__ == "__main__":
    main()
