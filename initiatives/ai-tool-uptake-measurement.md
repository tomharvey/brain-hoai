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
| `reference/ai-tool-usage-reports/cursor/` | Raw Cursor team usage-events CSVs (event-level, `events-<start>-to-<end>.csv`) |
| `reference/ai-tool-usage-reports/openai/` | Hand-transcribed ChatGPT workspace analytics (`chatgpt-messages-<start>-to-<end>.csv` + source screenshot + `name-to-email.csv` mapping). No export exists — the UI table is transcribed manually (~5 min/period) |
| `reference/ai-tool-usage-reports/normalised.csv` | Generated output — gitignored, rebuild with `python3 tools/ai-usage/normalise.py` |

**Raw reports are the source of truth.** The normalised layer is disposable and regenerated from raw, so schema changes never require touching source data — just update the normaliser and re-run.

Naming convention for raw files: `YYYY-MM.csv` for a full month, `YYYY-MM-partial-to-DD.csv` for an incomplete month. The normaliser derives the period from the filename.

## Normalised schema — v0.2

Grain: **one row per person × vendor × product × period** (calendar month, possibly partial; summed across models). Exception: OpenAI rows span the UI export window (an aggregate can't be sliced by month) — currently Jun 10 – Jul 9, crossing the month boundary. Metrics comparing calendar months must handle or exclude these rows until the capture moves to Custom calendar-month ranges.

| Field | Type | Notes |
|---|---|---|
| `person_email` | string | Empty for non-person rows. Joins cleanly across vendors — all Cursor users verified present in Anthropic data by email |
| `is_person` | bool | `false` for org/service usage (e.g. Anthropic "(org service usage)" rows) — kept so spend reconciles, excluded from uptake counts |
| `vendor` | string | `anthropic`, `cursor`, `openai` |
| `product` | string | Vendor's product name as reported (Chat, Cowork, Claude Code, Cursor, …) |
| `period_start` | date | Clipped to actual export coverage — a rolling-window export yields honest partial months |
| `period_end` | date | As above |
| `requests` | int | Vendor's primary activity count. **Not comparable across products/vendors** — only for within-product percentiles |
| `active_days` | int? | v0.2. Distinct days with any activity in the period. Populated where raw data is event-level (Cursor); empty for aggregate exports (Anthropic). The preferred frequency signal wherever present |
| `spend_usd` | float | Net/marginal spend as reported. Cursor: on-demand overage only — subscription seat fees not in the export |

v0.1 → v0.2 (2026-07-10): added `active_days` when Cursor's event-level export arrived, exactly the evolution predicted below. Cursor raw files: `cursor/events-YYYY-MM-DD-to-YYYY-MM-DD.csv` (event grain, range in filename).

### Design principles

1. **Core fields only if derivable from every vendor.** Person, tool, period, an activity count, and spend are the intersection we can rely on. Everything vendor-specific (tokens, cache reads, models, Cursor tab-completions accepted, etc.) stays in the raw files until we have a proven cross-vendor need for it.
2. **Schema is versioned and expected to evolve.** v0.1 is deliberately minimal, fitted to one vendor. When Cursor and OpenAI reports arrive, expect changes — likely candidates:
   - `requests` may not be comparable across vendors (an Anthropic API request ≠ a Cursor completion ≠ a ChatGPT message). We may need `activity_count` + `activity_unit`, or per-vendor activity tiers mapped to a common `engagement_level` (e.g. none / light / regular / heavy).
   - Product taxonomies won't align — we may need a `category` mapping (chat / coding / agents / other) on top of vendor `product`.
   - Period granularity may differ (Cursor reports daily; OpenAI monthly?) — the period fields already tolerate this, but aggregation rules will need defining.
   - If evolution gets messy, cut a **v1.0 consolidated schema** informed by all three vendors rather than patching v0.1 incrementally. Migration is cheap because we regenerate from raw.
3. **Uptake metrics are computed from the normalised layer, not stored in it**: active users, product breadth per person, MoM retention, new activations.

## Measurement constraints (decided 2026-07-10)

Anthropic's per-user, per-day activity data lives behind the **Claude Enterprise Analytics API** — Enterprise plans only. **We are not on Enterprise**, so:

- **No active-days metric from Anthropic.** The claude.ai admin spend export (what we have) is an aggregate over an arbitrary date range, not daily.
- **Baseline grain is monthly.** All uptake metrics must be computable from monthly per-user × product aggregates.
- **Optional frequency proxy: active-weeks.** The export accepts arbitrary date ranges, so four weekly exports per month would give active-weeks per user (appears in export = active that week). Decent frequency signal at ~4× the export effort; adopt only if monthly metrics prove too coarse.
- **Revisit if we move to Enterprise.** The Analytics API would make this whole layer self-updating: per-user daily activity across all products, org-level DAU/WAU/MAU, seat counts (the denominator), and Anthropic's own active-user definition. This measurement use case is itself part of the business case for Enterprise.

## Ranking / bucketing methodology (proposed)

Raw `requests` are not comparable across products (one Claude Code session ≈ hundreds of API requests; one Chat message ≈ 1). Never sum or compare raw counts across products. Instead:

1. **Within-product percentiles** — rank each person against other users of the same product; combine via max/mean percentile across their products.
2. **Product class** — map products to leverage tiers: *chat* (Chat) < *assisted* (Chrome, Design) < *agentic* (Cowork, Claude Code, Cursor, Office Agents, Research). Highest class used is volume-independent and maps onto the Stage 1–4 capability model (agentic-class usage ≈ Stage 3–4 behaviour in telemetry). Class is role-blind by design: no dev/non-dev split — a non-dev on Cursor or Claude Code is agentic-class, full stop.
3. **Breadth** — number of products used in the period.

Buckets (legible criteria, not a weighted composite index — composites are opaque and gameable once attached to targets):

| Bucket | Signal |
|---|---|
| **Dormant** | No activity in period |
| **Light** | Chat-only, low within-product percentile |
| **Regular** | 2+ products, or high percentile in one |
| **Power** | Agentic-class product + breadth + sustained presence across periods |

Relationship to capability stages: telemetry buckets are a **screen, not a score**. They scale automatically past the ~70-person ceiling of evidence-based scoring and flag mismatches to investigate (scored Stage 4 but telemetry-dormant; telemetry-power but unscored). Stage scores remain ground truth.

## First findings (Anthropic, Jun 1 – Jul 9 2026)

- **65 distinct team members** used Anthropic tools; 61 active in June, 57 in the first 9 days of July.
- **53 people active in both periods**; 4 newly activated in July (Charlie Dowrick, Daisie Baker, Joan Canellas, Kayleigh Bradbury).
- June product reach: Chat 56, Cowork 48, Claude Code 22, Claude in Chrome 16, Claude Design 11, Office Agents 6. **49 of 61 people used 2+ products.**
- June net spend $2,392; July 1–9 $495. Median ~1,600 requests/user in June (max 36,701).
- "Claude Tag" usage is entirely org-level service usage, not attributable to individuals.
- **ChatGPT (Jun 10 – Jul 9)**: 35 active users, 3,011 messages, zero credit spend. Top users: Adam Smith (458), **Antton Pena (332 — on the unassessed list with "no signal"; heavy AI user on a different tool)**, Emily Staton (248), Ben Allen (240), Ed Klinger (236). Alex Dyball is ChatGPT-only — appears in no Anthropic report.
- **Cursor (Jun 10 – Jul 9)**: 7 users, all also on Anthropic tools. Oliver Crowe active 30/30 days.

## Actions

- [x] Ingest Anthropic June + July reports, establish raw-data home — 2026-07-10
- [x] Define normalised schema v0.1 + normaliser script — 2026-07-10
- [x] Add Cursor reports; normaliser extended, schema bumped to v0.2 (`active_days`) — 2026-07-10. 7 users, all also on Anthropic tools; Jun 10 – Jul 9 window (Jun 1–9 missing — pull a fuller export if Cursor admin allows custom ranges)
- [x] Add OpenAI (ChatGPT) data via UI transcription — 2026-07-10. 20 users ingested; known gaps below
- [ ] Improve the OpenAI capture: re-screenshot with **Custom** range = calendar months (currently rolling 1M, assumed Jun 10 – Jul 9); capture **all 4 pages** (current: page 1 of 4 — ~15 active users with ≤25 messages missing); check **Codex analytics** (agentic-class signal if non-empty)
- [ ] Verify `alex.dyball@flockcover.com` (email guessed from convention — he's ChatGPT-only, so no cross-vendor confirmation)
- [ ] Compute first monthly uptake buckets (dormant/light/regular/power) from June + July data per the methodology above
- [ ] Get headcount per department for coverage % (denominator — not in any vendor report)
- [ ] Decide whether active-weeks (weekly exports) is worth the effort after seeing monthly buckets
- [ ] Decide reporting cadence and audience (monthly summary to C-suite?)

## Open questions

- What's the **denominator**? Coverage % needs headcount, ideally per department. Emails give us person identity; department mapping doesn't exist yet in the data.
- Do partial-month reports stay in the record, or get replaced by the full-month export when the month closes? (Current assumption: replaced.)
- Same person across vendors — email should join cleanly, but watch for alias/domain differences in Cursor/OpenAI exports.
