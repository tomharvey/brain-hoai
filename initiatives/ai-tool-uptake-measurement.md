---
title: AI Tool Uptake Measurement
created: 2026-07-10
updated: 2026-07-10
domain: ai-enablement
type: initiative
status: active
tags: [measurement, adoption, metrics]
---

# AI Tool Uptake Measurement

Measure **uptake** of AI tools across the company — who is using what, how often, and how broadly — not just spend. Spend is a lagging, price-distorted proxy; uptake (active users, frequency, breadth, retention) is the signal that tells us whether enablement is working.

## Why

- The [[ai-enablement]] domain goal is frequency/coverage/skill of AI usage across all departments. This initiative is the measurement backbone for that.
- Vendor reports (Anthropic today; Cursor and OpenAI incoming) each use their own shapes and metrics. Without a normalised layer, cross-tool questions ("how many people are active on *any* AI tool?", "who uses 2+ tools?") are unanswerable.

## Data

| Location | Contents |
|---|---|
| `reference/ai-tool-usage-reports/anthropic/` | Raw Anthropic spend/usage CSVs, one per period (`2026-06.csv`, `2026-07-partial-to-09.csv`) |
| `reference/ai-tool-usage-reports/cursor/` | (pending) Cursor reports |
| `reference/ai-tool-usage-reports/openai/` | (pending) OpenAI reports |
| `reference/ai-tool-usage-reports/normalised.csv` | Generated output — gitignored, rebuild with `python3 tools/ai-usage/normalise.py` |

**Raw reports are the source of truth.** The normalised layer is disposable and regenerated from raw, so schema changes never require touching source data — just update the normaliser and re-run.

Naming convention for raw files: `YYYY-MM.csv` for a full month, `YYYY-MM-partial-to-DD.csv` for an incomplete month. The normaliser derives the period from the filename.

## Normalised schema — v0.1

Grain: **one row per person × vendor × product × period** (summed across models).

| Field | Type | Notes |
|---|---|---|
| `person_email` | string | Empty for non-person rows |
| `is_person` | bool | `false` for org/service usage (e.g. Anthropic "(org service usage)" rows) — kept so spend reconciles, excluded from uptake counts |
| `vendor` | string | `anthropic`, `cursor`, `openai` |
| `product` | string | Vendor's product name as reported (Chat, Cowork, Claude Code, …) |
| `period_start` | date | From filename |
| `period_end` | date | From filename |
| `requests` | int | Vendor's primary activity count |
| `spend_usd` | float | Net spend |

### Design principles

1. **Core fields only if derivable from every vendor.** Person, tool, period, an activity count, and spend are the intersection we can rely on. Everything vendor-specific (tokens, cache reads, models, Cursor tab-completions accepted, etc.) stays in the raw files until we have a proven cross-vendor need for it.
2. **Schema is versioned and expected to evolve.** v0.1 is deliberately minimal, fitted to one vendor. When Cursor and OpenAI reports arrive, expect changes — likely candidates:
   - `requests` may not be comparable across vendors (an Anthropic API request ≠ a Cursor completion ≠ a ChatGPT message). We may need `activity_count` + `activity_unit`, or per-vendor activity tiers mapped to a common `engagement_level` (e.g. none / light / regular / heavy).
   - Product taxonomies won't align — we may need a `category` mapping (chat / coding / agents / other) on top of vendor `product`.
   - Period granularity may differ (Cursor reports daily; OpenAI monthly?) — the period fields already tolerate this, but aggregation rules will need defining.
   - If evolution gets messy, cut a **v1.0 consolidated schema** informed by all three vendors rather than patching v0.1 incrementally. Migration is cheap because we regenerate from raw.
3. **Uptake metrics are computed from the normalised layer, not stored in it**: active users, product breadth per person, MoM retention, new activations.

## First findings (Anthropic, Jun 1 – Jul 9 2026)

- **65 distinct team members** used Anthropic tools; 61 active in June, 57 in the first 9 days of July.
- **53 people active in both periods**; 4 newly activated in July (Charlie Dowrick, Daisie Baker, Joan Canellas, Kayleigh Bradbury).
- June product reach: Chat 56, Cowork 48, Claude Code 22, Claude in Chrome 16, Claude Design 11, Office Agents 6. **49 of 61 people used 2+ products.**
- June net spend $2,392; July 1–9 $495. Median ~1,600 requests/user in June (max 36,701).
- "Claude Tag" usage is entirely org-level service usage, not attributable to individuals.

## Actions

- [x] Ingest Anthropic June + July reports, establish raw-data home — 2026-07-10
- [x] Define normalised schema v0.1 + normaliser script — 2026-07-10
- [ ] Add Cursor reports when available; extend normaliser, revisit schema
- [ ] Add OpenAI reports when available; extend normaliser, revisit schema
- [ ] Define headline uptake metrics (weekly/monthly active, breadth, retention) once denominators are known (need headcount per department for coverage %)
- [ ] Decide reporting cadence and audience (monthly summary to C-suite?)

## Open questions

- What's the **denominator**? Coverage % needs headcount, ideally per department. Emails give us person identity; department mapping doesn't exist yet in the data.
- Do partial-month reports stay in the record, or get replaced by the full-month export when the month closes? (Current assumption: replaced.)
- Same person across vendors — email should join cleanly, but watch for alias/domain differences in Cursor/OpenAI exports.
