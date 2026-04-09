---
title: "Explore Looker→HubSpot direct flow for renewals"
id: AI-007
created: 2026-04-02
updated: 2026-04-09
due: 2026-04-14
origin: "[[2026-04-02-anna-ai-discovery]]"
domain: operational-tooling
type: issue
status: todo
priority: medium
assignee: tom
tags: [looker, hubspot, renewals, underwriting, process]
---

## Description

The renewals process currently flows: Looker → PMT spreadsheet → Billy allocates → Renewals Tracker → Zapier → HubSpot. The direction is to eliminate the two spreadsheets and go Looker→HubSpot direct. This depends on AI-006 (understanding Kirsty's Looker→Claude connection).

## Acceptance criteria

- [x] AI-006 completed (Kirsty's Looker connection understood)
- [x] Feasibility assessed: can renewal data flow from Looker into HubSpot deals/pipeline directly?
- [ ] Identify what changes Billy's allocation workflow needs (PMT → HubSpot views)
- [ ] Check if old HubSpot renewal pipeline can be revived
- [ ] Align with Adam + Emily's HubSpot clean-up project

## Notes

- Anna agrees spreadsheets should go: "ideally we would just cut out all of these unnecessary steps"
- Billy won't delegate allocation — any solution must give him a view in HubSpot equivalent to what he has in PMT
- Zapier currently reads the Renewals Tracker to create HubSpot deals — if data is already in HubSpot, Zapier step also goes away
- Google MCP hosting question is now moot — we're not automating spreadsheets, we're removing them
- **2026-04-09 (Kirsty call)**: Confirmed technically viable. Kirsty's MCP setup gives full bi-directional Looker access. Looker API can feed HubSpot directly. Kirsty was unaware the team uses Zapier to push spreadsheet data back to HubSpot — "that's crazy." **Blocked on AI-010** — the renewals team (Anna, Billy) don't have local Looker MCP setups, so cloud deployment is a prerequisite for them to use this flow.

## Links

- [[2026-04-09-kirsty-ai-discovery]]
- [[2026-04-02-anna-ai-discovery]]
- [[underwriting-assistance-ai]]
- Depends on: [[AI-006-kirsty-looker-claude]] (done)
- Depends on: [[AI-010-looker-mcp-cloud-deployment]]
