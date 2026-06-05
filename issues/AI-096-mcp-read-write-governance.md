---
title: MCP read/write governance — define approach for core systems
created: 2026-06-04
updated: 2026-06-04
domain: engineering-workflows
type: issue
status: todo
priority: high
origin: "[[2026-06-04-fergus-weekly]]"
tags: [engineering-workflows, mcp, governance, hubspot, notion]
---

# MCP read/write governance — define approach for core systems

The distinction between read and write access through MCP connectors is not yet codified. As more staff connect to HubSpot, Notion, Granola etc. via standard Claude connectors, the risk of inadvertent writes or deletes grows.

**The problem:**
- Ivan accidentally deleted all content in a personal Notion page (low blast radius)
- Same pattern on HubSpot (e.g. Emily deleting 2000 tickets) would be catastrophic
- Non-engineers don't have a mental model of "staging vs production" — they are working directly in prod data
- No "oops, I deleted all our production data" recovery culture exists outside engineering

**What needs to be decided:**
1. Quick answer: can we prevent deletes from HubSpot entirely? Most delete use cases can be replaced with archiving or pipeline moves
2. Longer-term: unified approach to MCP read/write governance across core systems (HubSpot, Notion, Google Workspace) — possible routing via AWS MCP gateway or similar
3. Authentication propagation: once authed against an MCP proxy, how does the proxy authenticate downstream to HubSpot *as that person* (not as a shared service account)?

**Owner:** Tom Harvey + Fergus Doyle
**Context:** Fergus <> Tom Weekly, 2026-06-04; also referenced in HubSpot info stack table-top exercise discussion
