---
title: Kirsty Alexandre
created: 2026-03-27
updated: 2026-04-09
type: person
role: Senior Analytics Engineer
team: Finance (reports to Christian Nielsen, CFO)
tags: [data, finance, visualisation]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-18
---

## Role

Senior Analytics Engineer

## Team

Finance

## Relationship

<!-- to be confirmed -->

## Working style notes

- Building broker deck skill — customer context compilation
- Showed dynamic visualisation work that impressed (not bound to tables — graphs, clickable exploration)
- Integrated all distribution trading data into **Looker via MCP** — enables rapid AI-driven analysis of broker panels
- Can auto-generate review packs from trading data
- Presented this work at AI breakfasts
- Key enabler for distribution team — Adam wants his team to book sessions with her to get integrated
- **Key dependency for renewals simplification** — her Looker→Claude connection is the enabler for eliminating PMT and Renewals Tracker spreadsheets (Looker→HubSpot direct flow)
- Anna saw her demo at a 4 o'clock session — impressive visualisations
- Self-described "absolutely obsessed with Claude"
- Consulting background — thinks in financial models and driver trees
- Technically capable — can hack things together but needs infrastructure support for production
- Wants help productionising her work, not direction on what to build

## AI Activation

**Stage**: 4 — Delegation
**Confidence**: high
**Assessed**: 2026-06-18
**Evidence**: Built Looker→Claude MCP integration deployed locally and trialled across Finance and Distribution teams. Automated FP&A pod metric sheet generation — a task that "was spinning our wheels for four months" completed in "a week of iterating with Claude." Presents at AI Breakfasts, de facto AI infrastructure owner for Finance. Other departments (Distribution) book sessions with her. "Absolutely obsessed with Claude."

**Not Stage 3**: Running infrastructure others depend on. Pod metrics automation, review pack auto-generation, and Looker integration are systems, not personal tools.
**Not Stage 5**: Has not yet handed workflows off to run autonomously without her involvement. Cloud MCP deployment (AI-010) blocked pending infrastructure support. Single primary data pipeline (Looker→Claude).
**To progress**: Productionise Looker MCP on shared cloud infrastructure (AI-010). Connect pipeline to multi-step automated output (query → synthesise → format → distribute). Build feedback loops so insight quality is tracked over time.
**Framework note**: Moves fast. Cloud MCP deployment is the single biggest unlock in the Finance department.

## 1:1 Log

### 2026-04-09 — AI Discovery

- Confirmed Looker→Claude via MCP on local machine. Christian, Kevin, David trialling.
- Needs cloud MCP deployment (AI-010) — Tom has the keys
- Tree diagram visualisation: drew wireframe on paper, photographed, Claude built HTML dashboard from Looker data
- AI-generated paragraph insights are the breakthrough — solves "users see numbers but don't interpret"
- Fleet Evolution insight: lost on interest-free payment terms, not price. Challenges "we're too expensive" narrative.
- Trade segment: 57% submissions, 19% win rate — actionable segmentation insight
- Discussed multi-layered data architecture and persistent insight problem (Q2 experiment, Q3-Q4 productionise)
- ICP analysis: Kirsty to test Claude on "what's our actual ideal customer" vs Adam's assumptions (AI-012)
- Renewals Looker→HubSpot: confirmed viable. Kirsty unaware of the Zapier spreadsheet loop.
- Asks: cloud MCP deployment, help productionising the insights dashboard
- Sharing: [Notion page (Looker setup)](https://www.notion.so/flockcover/How-to-Connect-Claude-to-Looker-2fee4b915259800d841dcc5fd0d27359) + HTML dashboard file (still waiting)

