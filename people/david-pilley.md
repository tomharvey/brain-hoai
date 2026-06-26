---
title: David Pilley
created: 2026-06-24
updated: 2026-06-24
domain: operational-tooling
type: person
role: Finance Analyst
team: Finance
tags: [finance, dashboards, operational-tooling, mi-reporting]
ai_activation_stage: 3
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-24
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

**Stage**: 3 — Fluency / Plan mode
**Confidence**: medium
**Assessed**: 2026-06-24
**Evidence**: Built a Claude skill that generates the weekly Finance MI dashboard autonomously — three Looker explores (Kirsty's FP&A explore, policy data platform, HubSpot), runs in under 10 minutes. Separate submission mix and pricing analysis dashboard for Christian and Tom. Agreed to add save-to-Google-Drive step and daily schedule in the session. Tested Google Drive sync live during the call (HTML opened in Safari from desktop — worked). Building insight delta tracking: track how AI-generated insights change week-over-week, flag new vs recurring.

**Not Stage 2**: Two production dashboards running; skill generates HTML artifacts without manual intervention. Past context-and-tools.
**Not Stage 4**: Still manually initiating skills. The daily schedule would push toward Stage 4, but not there yet.
**To progress**: Add Google Drive save step and daily schedule to MI dashboard (→ [[AI-138]]). Add Milan's pricing data to Claude folder to overlay on conversion rate graphs. Build insight delta tracking.

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
