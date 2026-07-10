#!/usr/bin/env python3
"""Normalise vendor AI usage reports into the uptake schema.

Schema v0.2 — see initiatives/ai-tool-uptake-measurement.md
Grain: person x vendor x product x period (calendar month, possibly partial).
v0.2 adds active_days: distinct days with any activity in the period, where
the raw data supports it (Cursor event-level exports); empty where it doesn't
(Anthropic monthly aggregates).

Raw reports live in reference/ai-tool-usage-reports/<vendor>/. Filenames
encode coverage:
  anthropic/YYYY-MM.csv                     full month, aggregate rows
  anthropic/YYYY-MM-partial-to-DD.csv       month start to DD, aggregate rows
  cursor/events-YYYY-MM-DD-to-YYYY-MM-DD.csv  event-level, arbitrary range

Output is regenerated in full on every run:
reference/ai-tool-usage-reports/normalised.csv
"""

import calendar
import csv
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parents[2] / "reference" / "ai-tool-usage-reports"
OUT_PATH = REPORTS_DIR / "normalised.csv"

FIELDS = [
    "person_email", "is_person", "vendor", "product",
    "period_start", "period_end", "requests", "active_days", "spend_usd",
]


def month_end(d):
    return date(d.year, d.month, calendar.monthrange(d.year, d.month)[1])


def parse_spend(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return 0.0  # Cursor uses "Free" / "-" for subscription-covered events


def normalise_anthropic(path):
    m = re.match(r"(\d{4})-(\d{2})(?:-partial-to-(\d{2}))?\.csv$", path.name)
    if not m:
        raise ValueError(f"unrecognised anthropic report filename: {path.name}")
    year, month, last_day = int(m[1]), int(m[2]), m[3]
    start = date(year, month, 1)
    end = date(year, month, int(last_day)) if last_day else month_end(start)
    agg = defaultdict(lambda: {"requests": 0, "spend_usd": 0.0})
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            key = (row["user_email"].strip(), row["product"])
            agg[key]["requests"] += int(row["total_requests"] or 0)
            agg[key]["spend_usd"] += parse_spend(row["total_net_spend_usd"])
    for (email, product), totals in agg.items():
        is_person = "@" in email
        yield {
            "person_email": email if is_person else "",
            "is_person": str(is_person).lower(),
            "vendor": "anthropic",
            "product": product,
            "period_start": start.isoformat(),
            "period_end": end.isoformat(),
            "requests": totals["requests"],
            "active_days": "",  # not derivable from aggregate exports
            "spend_usd": round(totals["spend_usd"], 2),
        }


def normalise_cursor(path):
    m = re.match(r"events-(\d{4}-\d{2}-\d{2})-to-(\d{4}-\d{2}-\d{2})\.csv$", path.name)
    if not m:
        raise ValueError(f"unrecognised cursor report filename: {path.name}")
    range_start, range_end = date.fromisoformat(m[1]), date.fromisoformat(m[2])
    # one bucket per person per calendar month; errored events still count as
    # activity (the person was using the tool) and are included in requests
    agg = defaultdict(lambda: {"requests": 0, "spend_usd": 0.0, "days": set()})
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            day = date.fromisoformat(row["Date"][:10])
            key = (row["User"].strip(), date(day.year, day.month, 1))
            agg[key]["requests"] += 1
            agg[key]["spend_usd"] += parse_spend(row["Cost"])
            agg[key]["days"].add(day)
    for (email, month_start), totals in agg.items():
        is_person = "@" in email
        yield {
            "person_email": email if is_person else "",
            "is_person": str(is_person).lower(),
            "vendor": "cursor",
            "product": "Cursor",
            # clip the period to what the export actually covers, so a
            # rolling-window export yields honest partial months
            "period_start": max(month_start, range_start).isoformat(),
            "period_end": min(month_end(month_start), range_end).isoformat(),
            "requests": totals["requests"],
            "active_days": len(totals["days"]),
            "spend_usd": round(totals["spend_usd"], 2),
        }


# Vendor name -> normaliser. Add openai here when its reports arrive;
# each takes a raw CSV path and yields rows in the v0.2 schema.
NORMALISERS = {
    "anthropic": normalise_anthropic,
    "cursor": normalise_cursor,
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
    vendors = sorted({r["vendor"] for r in rows})
    print(f"wrote {len(rows)} rows, {len(people)} people, vendors: {', '.join(vendors)} -> {OUT_PATH}")


if __name__ == "__main__":
    main()
