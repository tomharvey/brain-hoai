---
title: "Understand Kirsty's Looker→Claude connection"
id: AI-006
created: 2026-04-02
updated: 2026-04-09
due: 2026-04-07
origin: "[[2026-04-02-anna-ai-discovery]]"
domain: operational-tooling
type: issue
status: done
priority: high
assignee: tom
tags: [kirsty, looker, claude, renewals, underwriting]
---

## Description

Kirsty has connected Looker to Claude and produced visualisations (demoed at a 4 o'clock session). This connection is the key enabler for eliminating the PMT and Renewals Tracker spreadsheets — if we can go Looker→HubSpot direct, the entire renewals process simplifies.

## Acceptance criteria

- [x] Speak to Kirsty — understand how she connected Looker to Claude (MCP? API? Export?)
- [x] Assess whether the same approach can feed renewal data into HubSpot directly
- [ ] Report back to Anna on feasibility

## Resolution (2026-04-09)

- **Setup**: Claude talking to Looker via MCP, running locally on Kirsty's machine. Christian, Kevin, David also trialling locally.
- **Data access**: Full bi-directional — can query all Looker data and build reports/dashboards
- **Visualisation**: HTML output from Claude using Looker data. Currently hardcoded numbers, could go live via Looker API.
- **Renewals path**: Confirmed viable — Looker→Claude→HubSpot direct flow is technically feasible via MCP + Looker API
- **Key blocker**: Needs cloud MCP deployment (same pattern as data lake) to scale beyond local machines. Tom has access keys. → AI-010
- **Bonus**: AI-generated paragraph insights from dashboard data — solves the "users see numbers but don't interpret them" problem. Fleet Evolution insight (interest-free payment terms, not price) is a standout example.

## Notes

- Kirsty presented this at a 4 o'clock session last week — Anna saw it
- Anna currently thinks of Looker as "a rogue thing that does its own thing and we can't do anything with it"
- Kirsty also powers the distribution team's review packs via Looker MCP (Adam call context)
- This is a dependency for the renewals process simplification AND for the insight layer strategic direction

## Links

- [[2026-04-09-kirsty-ai-discovery]]
- [[2026-04-02-anna-ai-discovery]]
- [[underwriting-assistance-ai]]
- [[kirsty]]
