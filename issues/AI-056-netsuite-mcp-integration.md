---
title: "AI-056: NetSuite MCP integration for finance team"
created: 2026-05-19
updated: 2026-05-19
domain: ai-enablement
type: issue
status: todo
priority: high
due: 2026-05-20
origin: "[[2026-05-19-finance-team-ai-workshop]]"
tags: [finance, netsuite, mcp]
---

## Summary

Set up a NetSuite MCP integration on a finance team member's laptop to eliminate manual data exports (primarily Ivan's daily credit control report). Tom to attempt this in the office on 2026-05-20 with a volunteer from the finance team.

## Context

Ivan currently copies data manually from NetSuite into Claude daily for credit control prioritisation. A NetSuite MCP connector would make this data directly accessible to Claude, removing the manual copy-paste step. Similar to the Looker MCP already set up locally.

Ivan flagged this as a key improvement. Tom committed to attempting it during the London office visit.

## Acceptance criteria

- [ ] NetSuite MCP working on at least one finance team machine
- [ ] Ivan able to query NetSuite data directly without manual export
- [ ] Document setup process for broader rollout if successful

## Notes

- Finance team volunteer needed to dedicate ~20 min in the office tomorrow
- Ivan is the primary beneficiary but broader finance team may benefit
- Keep it local/machine-scoped initially (same model as Looker MCP)
