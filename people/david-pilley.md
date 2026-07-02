---
title: David Pilley
created: 2026-06-24
updated: 2026-06-30
domain: operational-tooling
type: person
role: Finance Analyst
team: Finance
tags: [finance, dashboards, operational-tooling, mi-reporting]
ai_activation_stage: 3
ai_activation_confidence: medium
ai_activation_assessed: 2026-07-02
---

# David Pilley

**Role:** Finance Analyst
**Company:** Flockcover
**Email:** david.pilley@flockcover.com

## Role

Finance Analyst

## Team

Finance

## Relationship

AI discovery session 2026-06-24. Previously on parental leave — returned (or partially returned) by mid-2026.

## Working style notes

- Practical, results-oriented: built the MI dashboard skill independently before the discovery call
- Comfortable with HTML output and Google Drive workflows
- Interested in insight tracking as a feedback loop (track how insights change week-over-week)
- Not focused on calculations — skill is "99% fetch and layout"

## AI Activation

**Stage**: 3 — Fluency
**Confidence**: medium
**Assessed**: 2026-07-02
**Evidence**: Built and runs a weekly Finance MI dashboard Claude skill independently (3 Looker explores, under 10 minutes; Kevin reviews output). Built a submission-mix and pricing analysis dashboard for Christian and Tom. Conceived the insight-delta feedback loop (track novelty and whether insights were acted on). Moss MCP now installed and working (Jun 30, first query successful).

**Not Stage 2**: Builds his own reusable tools (MI dashboard skill in weekly use) — verified in the Jul 2 builder audit. Beyond connecting data sources.
**Not Stage 4**: Doesn't delegate whole workflows; and the review muscle is the gap — Kevin's flag ("they think it's magic... cede to it") is the classic Stage 3 over-trust danger zone. Progression is review skill, not more tools.
**To progress**: Own the quality of outputs — spot-check dashboard numbers against source before circulating; use Moss MCP for a real month-end task and validate it himself.

### Re-assessment note (2026-07-02)

The Jun 30 Stage 1 score conflated an environment problem (no Python on his machine, guided terminal setup) with AI capability — the framework scores AI practice, not machine administration. His sustained Looker/dashboard practice was and is Stage 3; the Moss blocker is now resolved anyway (install completed with Tom, Jun 30 — see [[2026-06-30-david-pilley-moss-install]]).

### Prior assessments

- 2026-06-30: Stage 1 (Moss-context — superseded, see note above)
- 2026-06-24: Stage 3 (MI dashboard work — restored as the operative assessment)

## Actions outstanding

- [ ] Add save step + daily schedule to MI dashboard → [[AI-138]]
- [ ] Add Milan's pricing data to Claude folder
- [ ] Build insight delta tracking into daily dashboard
- [ ] Present dashboard-sharing workflow at next AI Breakfast

## 1:1 Log

### 2026-06-24 — AI Discovery

- Finance weekly MI dashboard: 3 Looker explores, under 10 mins, Kevin Berg reviewing and wanting more clickable elements
- Distribution options tested live: Google Drive sync works (HTML opens in Safari), Slack (raw code on mobile), Notion
- Agreed: add save step to skill and get end-to-end working today
- Scheduling plan: daily (pull previous day), YYYY-MM-DD file naming, archive by year/month + always overwrite "current"
- Submission mix + pricing analysis dashboard: built for Christian and Tom, tracks segment conversion rates YTD/current quarter, one-page narrative summary
- Next step: add Milan's pricing model change data to overlay on conversion rate graphs
- Key idea: AI-generated insights as feedback loop — track delta, novelty, and whether insights were acted on
- Francesco customer transcript summaries became repetitive — better to surface delta than repeat same insight
- See: [[2026-06-24-david-pilley-ai-discovery]]
