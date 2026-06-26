---
title: "AI-145: Automate NetSuite data pull for daily credit control report"
created: 2026-06-25
updated: 2026-06-25
domain: operational-tooling
type: issue
status: todo
priority: medium
origin: "[[2026-06-25-netsuite-mcp-ivan]]"
tags: [finance, netsuite, mcp, automation, credit-control]
---

Ivan Boix currently downloads an XLS from NetSuite manually each morning and drags it into an incoming folder for Claude to process. The goal is to remove this manual step entirely using the NetSuite MCP.

If the data pull is fully automated, the whole daily report pipeline runs unattended — daily briefing could be sent to a Slack channel even when Ivan is on holiday.

## Actions

- [ ] Ivan Boix: extend existing Claude skill to automate the NetSuite data pull via MCP
- [ ] Test: verify MCP query returns same data as manual XLS download
- [ ] Remove manual download step once verified
- [ ] Ivan + Tom: catch up next week to review progress and demo
