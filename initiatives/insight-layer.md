---
title: Insight layer across trips, claims, and quotes
created: 2026-03-30
updated: 2026-03-30
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

- Not started — conceptual
- Related capabilities exist in isolation:
  - Milan Chavda: Head of Pricing Intelligence — pricing data and models
  - Kirsty Alexander: Senior Analytics Engineer — broker deck visualisations, analytics
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

- [ ] Park for Now — track as a strategic direction, not an active project
- [ ] Identify a narrow first use case (e.g. submission quality scoring, or claim pattern detection)
- [ ] Discuss with Matt (Head of Product) where this fits in the product vision
- [ ] Connect with Milan Chavda on pricing intelligence as potential first domain

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
