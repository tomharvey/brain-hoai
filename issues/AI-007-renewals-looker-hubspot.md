---
title: "Explore Looker→HubSpot direct flow for renewals"
id: AI-007
created: 2026-04-02
updated: 2026-04-02
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

- [ ] AI-006 completed (Kirsty's Looker connection understood)
- [ ] Feasibility assessed: can renewal data flow from Looker into HubSpot deals/pipeline directly?
- [ ] Identify what changes Billy's allocation workflow needs (PMT → HubSpot views)
- [ ] Check if old HubSpot renewal pipeline can be revived
- [ ] Align with Adam + Emily's HubSpot clean-up project

## Notes

- Anna agrees spreadsheets should go: "ideally we would just cut out all of these unnecessary steps"
- Billy won't delegate allocation — any solution must give him a view in HubSpot equivalent to what he has in PMT
- Zapier currently reads the Renewals Tracker to create HubSpot deals — if data is already in HubSpot, Zapier step also goes away
- Google MCP hosting question is now moot — we're not automating spreadsheets, we're removing them

## Links

- [[2026-04-02-anna-ai-discovery]]
- [[underwriting-assistance-ai]]
- Depends on: [[AI-006-kirsty-looker-claude]]
