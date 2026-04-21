#!/usr/bin/env python3
"""Export LLM conversations from Datadog LLM Observability API.

Groups spans by session_id when available, otherwise reconstructs
conversations from the span tree using parent_id and time proximity.

Usage:
    python tools/datadog/export_conversations.py [--days N] [--service NAME]

Defaults to last 7 days, all services.
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
import hashlib

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install requests")
    sys.exit(1)

SECRETS_FILE = Path(__file__).parent / "secrets.txt"
BASE_URL = "https://api.datadoghq.eu/api/v2/llm-obs/v1/spans/events/search"
OUTPUT_DIR = Path(__file__).parents[1] / "outbox" / "datadog-exports"
PAGE_LIMIT = 100


def load_secrets():
    secrets = {}
    with open(SECRETS_FILE) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                secrets[key.strip()] = value.strip()
    return secrets


def fetch_spans(secrets, from_dt, to_dt, service=None, cursor=None):
    headers = {
        "DD-API-KEY": secrets["DD-API-KEY"],
        "DD-APPLICATION-KEY": secrets["DD-APPLICATION-KEY"],
        "Content-Type": "application/vnd.api+json",
    }

    filter_obj = {
        "from": from_dt.isoformat(),
        "to": to_dt.isoformat(),
    }
    if service:
        filter_obj["tags"] = [f"service:{service}"]

    page_obj = {"limit": PAGE_LIMIT}
    if cursor:
        page_obj["cursor"] = cursor

    payload = {
        "data": {
            "type": "spans",
            "attributes": {
                "filter": filter_obj,
                "page": page_obj,
                "sort": "timestamp",
            },
        }
    }

    resp = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def extract_session_id(span):
    for tag in span.get("attributes", {}).get("tags", []):
        if tag.startswith("session_id:"):
            return tag.split(":", 1)[1]
    return None


def extract_service(span):
    for tag in span.get("attributes", {}).get("tags", []):
        if tag.startswith("service:"):
            return tag.split(":", 1)[1]
    return "unknown"


def simplify_span(span):
    attrs = span.get("attributes", {})
    return {
        "span_id": attrs.get("span_id"),
        "parent_id": attrs.get("parent_id"),
        "span_kind": attrs.get("span_kind"),
        "name": attrs.get("name"),
        "start_ns": attrs.get("start_ns"),
        "duration_ns": attrs.get("duration"),
        "status": attrs.get("status"),
        "input": attrs.get("input", {}).get("value"),
        "output": attrs.get("output", {}).get("value"),
        "metadata": attrs.get("metadata"),
        "metrics": attrs.get("metrics"),
        "model_name": attrs.get("model_name"),
        "model_provider": attrs.get("model_provider"),
    }


def group_orphans_into_conversations(orphan_spans, gap_seconds=60):
    """Reconstruct conversations from spans missing session_id.

    Groups spans into conversations using the span tree (parent_id) and
    time proximity. Root workflow spans within gap_seconds of each other
    are considered part of the same conversation.
    """
    simplified = [simplify_span(s) for s in orphan_spans]

    # Build parent->children index
    by_id = {s["span_id"]: s for s in simplified}
    roots = [s for s in simplified if s["parent_id"] == "undefined"]
    children = defaultdict(list)
    for s in simplified:
        if s["parent_id"] != "undefined":
            children[s["parent_id"]].append(s)

    # Sort roots by time
    roots.sort(key=lambda s: s.get("start_ns") or 0)

    # Group roots by time proximity
    conversations = []
    current_group = []

    for root in roots:
        ts = root.get("start_ns") or 0
        if current_group:
            prev_ts = max(s.get("start_ns") or 0 for s in current_group)
            gap = (ts - prev_ts) / 1e9
            if gap > gap_seconds:
                conversations.append(current_group)
                current_group = []
        current_group.append(root)

    if current_group:
        conversations.append(current_group)

    # Attach children to each conversation's root spans
    results = []
    for conv_roots in conversations:
        all_spans = []
        for root in conv_roots:
            all_spans.append(root)
            # Recursively collect children
            stack = [root["span_id"]]
            while stack:
                pid = stack.pop()
                for child in children.get(pid, []):
                    all_spans.append(child)
                    stack.append(child["span_id"])

        all_spans.sort(key=lambda s: s.get("start_ns") or 0)

        first_ts = all_spans[0].get("start_ns") or 0
        dt = datetime.fromtimestamp(first_ts / 1e9, tz=timezone.utc)

        # Generate a stable ID from the first span's timestamp + id
        conv_id = hashlib.sha256(
            f"{first_ts}:{all_spans[0]['span_id']}".encode()
        ).hexdigest()[:16]

        results.append({
            "session_id": f"reconstructed_{conv_id}",
            "started": dt.isoformat(),
            "span_count": len(all_spans),
            "turns": len(conv_roots),
            "spans": all_spans,
        })

    return results


def write_conversation(conversation, service, output_dir):
    """Write a single conversation to a JSON file."""
    dt = datetime.fromisoformat(conversation["started"])
    date_str = dt.strftime("%Y-%m-%d_%H%M")
    session_short = conversation["session_id"][:16]
    filename = f"{date_str}_{service}_{session_short}.json"
    filepath = output_dir / filename

    with open(filepath, "w") as f:
        json.dump(conversation, f, indent=2, default=str)

    return filepath


def main():
    parser = argparse.ArgumentParser(description="Export Datadog LLM conversations")
    parser.add_argument("--days", type=int, default=7, help="Number of days to look back (default: 7)")
    parser.add_argument("--service", type=str, default=None, help="Filter by service name")
    args = parser.parse_args()

    secrets = load_secrets()
    to_dt = datetime.now(timezone.utc)
    from_dt = to_dt - timedelta(days=args.days)

    print(f"Fetching spans from {from_dt.date()} to {to_dt.date()}...")
    if args.service:
        print(f"Filtering by service: {args.service}")

    # Paginate through all results
    all_spans = []
    cursor = None
    page = 0

    while True:
        page += 1
        result = fetch_spans(secrets, from_dt, to_dt, args.service, cursor)
        spans = result.get("data", [])
        all_spans.extend(spans)
        print(f"  Page {page}: {len(spans)} spans (total: {len(all_spans)})")

        if len(spans) < PAGE_LIMIT:
            break

        # Look for pagination cursor
        meta = result.get("meta", {})
        cursor = meta.get("page", {}).get("after")
        if not cursor:
            break

    if not all_spans:
        print("No spans found.")
        return

    # Split into spans with and without session_id
    sessions = defaultdict(list)
    no_session = []

    for span in all_spans:
        session_id = extract_session_id(span)
        if session_id:
            sessions[session_id].append(span)
        else:
            no_session.append(span)

    print(f"\nFound {len(all_spans)} spans across {len(sessions)} sessions"
          f" ({len(no_session)} spans without session_id)")

    # Reconstruct conversations from orphan spans
    reconstructed = []
    if no_session:
        reconstructed = group_orphans_into_conversations(no_session)
        print(f"Reconstructed {len(reconstructed)} conversations from orphan spans"
              f" (grouped by parent_id + 60s time gap)")

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0

    # Write sessions with proper session_id
    for session_id, spans in sessions.items():
        spans.sort(key=lambda s: s.get("attributes", {}).get("start_ns", 0))
        service = extract_service(spans[0])
        first_ts = spans[0].get("attributes", {}).get("start_ns", 0)
        dt = datetime.fromtimestamp(first_ts / 1e9, tz=timezone.utc)

        conversation = {
            "session_id": session_id,
            "service": service,
            "started": dt.isoformat(),
            "span_count": len(spans),
            "spans": [simplify_span(s) for s in spans],
        }
        write_conversation(conversation, service, OUTPUT_DIR)
        written += 1

    # Write reconstructed conversations
    for conv in reconstructed:
        service = "reconstructed"
        write_conversation(conv, service, OUTPUT_DIR)
        written += 1

    print(f"\nExported {written} conversations to {OUTPUT_DIR}/")
    print(f"  {written - len(reconstructed)} from session_id, {len(reconstructed)} reconstructed")
    for f in sorted(OUTPUT_DIR.iterdir()):
        if f.suffix == ".json":
            print(f"  {f.name}")


if __name__ == "__main__":
    main()
