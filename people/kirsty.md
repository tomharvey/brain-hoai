---
title: Kirsty Alexandre
created: 2026-03-27
updated: 2026-06-30
type: person
role: Senior Analytics Engineer
team: Finance (reports to Christian Nielsen, CFO)
tags: [data, finance, visualisation]
ai_activation_stage: 2
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-30
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

**Stage**: 2 — Context and tools
**Confidence**: medium
**Assessed**: 2026-06-30
**Evidence**: Got new Moss MCP server installed successfully (Jun 29). Previously had installed an older version that didn't work properly. Understands the need for proper API configuration. Willing to help install on Jade and Dave's machines. Interested in month-end automation via Moss. Has tools connected and is actively using Claude with Moss MCP, though dependent on others for initial setup.

**Not Stage 1**: Has MCP tools installed and functioning, actively using Claude with connected data sources. Not just running basic queries — understands the tooling landscape and is helping others get set up.
**Not Stage 3**: Dependent on others for Moss MCP setup. Not yet building her own workflows or skills around Moss. Using the tool once installed rather than creating new capabilities from it.
**To progress**: Build a Moss month-end automation workflow independently. Create a reusable skill or process around Moss expense management. Move from using the MCP to building on top of it.

### Prior assessment (2026-06-18)

Previously assessed at Stage 4 (Delegation) based on Looker MCP work: built Looker→Claude MCP integration, automated FP&A pod metric sheet generation, presented at AI Breakfasts, de facto AI infrastructure owner for Finance. That evidence remains valid for Looker-based workflows. The current assessment reflects the Moss-specific context where she is earlier in the adoption curve.

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

