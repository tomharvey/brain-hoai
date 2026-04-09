---
title: Insight layer across trips, claims, and quotes
created: 2026-03-30
updated: 2026-04-09
domain: product-ai
type: initiative
status: proposed
origin: directed
owner: TBD
tags: [insight, data, product, telemetry, strategic]
---

## Summary

Create a base-layer of insight across multiple domains — each trip, each claim, each quote — so the company treats insight as naturally as it treats telemetry data. This is the "what AI makes possible" bet, not the "what AI makes faster" work.

## Goal

Aggregated, pipeline-driven insight that customers and internal teams can act on. AI doesn't just automate existing workflows — it surfaces patterns and knowledge that weren't previously accessible.

## Current state

- Conceptual but with a concrete first proof point (Kirsty's Looker insights dashboard)
- Related capabilities exist in isolation:
  - Milan Chavda: Head of Pricing Intelligence — pricing data and models
  - Kirsty Alexandre: Senior Analytics Engineer — Looker→Claude MCP, AI-generated paragraph insights, tree diagram visualisations. **Closest thing to a working insight layer prototype.**
  - Darren McCauley: excited about driver-level risk management
  - Geran's time/motion study captures workflow data that could feed insight
  - Emily's forecasting work uses historical HubSpot data
- No unified view across trips, claims, quotes
- Telemetry data infrastructure exists (PostHog, safety scoring) but insight layer doesn't

## Dependencies

- Process documentation — need to understand what data flows through each domain
- Agent framework — insight pipelines may be implemented as agents
- Product-ai direction — needs product ownership and a customer-facing vision

## Risks

- Too ambitious for the first 90 days — should be "Later" on the roadmap
- No clear owner or product champion yet
- Could become a boil-the-ocean data project without tight scoping

## Next actions

- [x] Identify a narrow first use case — Kirsty's AI-generated insights from Looker data is the prototype
- [ ] Deploy Looker MCP to cloud (AI-010) — prerequisite for scaling Kirsty's work
- [ ] Design persistent insight feedback loop (Q2 experiment, Q3-Q4 productionise)
- [ ] Discuss with Matt (Head of Product) where this fits in the product vision
- [ ] Connect with Milan Chavda on pricing intelligence as potential second domain

## Log

### 2026-03-30

- Created from pitch document review
- Positioned as "Later" on the board roadmap — strategic bet, not Q2 delivery
- From pitch: "treat insight as naturally as we treat telemetry data"
- **Jordi 1:1**: concept solidifying — Tom framing a 3-month horizon for an "insights database"
  - Data sources: CC data (Abs's tool), virtual imagery, HubSpot, PDFs, submissions
  - "There's just a big pile of data that no one had time to analyse" — AI changes that
  - Virtual imagery team has only scratched the surface despite it being their core job
  - This may move from "Later" to "Next" on the roadmap — needs a narrow first use case to anchor it
- **Adam discovery (2026-04-02)**: Distribution team's Granola folder = accidental broker knowledge base. HubSpot thin on broker data. Ideal pipeline: Granola → HubSpot → Claude via MCP. Semantic naming consistency across systems flagged as prerequisite. Hypothesis validation use case: can Claude objectively challenge assumptions about broker performance? Strongly reinforces the insight layer direction — distribution data is another pool.

### 2026-04-09

- **Kirsty discovery**: This is the insight layer's first concrete proof point.
  - AI-generated paragraph insights from Looker data solve the "users see numbers but don't interpret" problem
  - Example: Fleet Evolution lost to AIG on interest-free payment terms, not pricing — challenges the "we're too expensive" narrative. Actionable, buried in data, surfaced by AI.
  - Trade segment: 57% of submissions, 19% win rate — "stop concentrating on trade" is insight-layer logic
  - Tom and Kirsty discussed the **multi-layered data architecture**:
    1. Highly structured (Looker — current)
    2. Semi-structured (less tightly modelled)
    3. Unstructured with flow (submission PDFs)
    4. Completely unstructured (user feedback, insight text itself)
  - The insight paragraphs are themselves a **new corpus of data** — not ephemeral
  - **Persistent insight problem**: insights need to feed future insights, know what's been actioned, avoid repeating stale findings. Human-in-the-loop for priority setting. Cf. Francesco's weekly for Ben hitting "fatigue."
  - **Timeline agreed**: Q2 experiment with approach, Q3-Q4 productionise
  - **ICP analysis as insight layer test case**: Kirsty testing whether Claude can derive the actual narrowest ICP from 5 years of Looker data, then compare it to Adam's assumptions. This is a two-layer insight problem:
    1. **Insight into our own thinking** — can AI be more data-driven than our intuitions? Does what we *think* our ICP is match reality?
    2. **Recurring insight over time** — how does the ICP change year-on-year? The answer isn't a one-shot; it's a question that should be re-asked and compared against previous answers. This is exactly the persistent, self-referencing insight pattern discussed above.
  - This initiative should move from "Later" to "Next" on the roadmap — Kirsty's work is the anchor use case
