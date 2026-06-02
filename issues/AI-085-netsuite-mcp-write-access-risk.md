---
title: Assess NetSuite MCP write-access risk and investigate safe read-only path
id: AI-085
created: 2026-05-11
updated: 2026-05-11
domain: operational-tooling
type: issue
status: todo
priority: high
assignee: Tom
origin: "[[2026-05-11-anneliese-ai-discovery]]"
tags: [netsuite, mcp, security, governance, finance]
---

## Description

Anneliese raised a concern during her AI discovery session: if a NetSuite MCP integration were connected to Claude, there's a risk that Claude could perform write operations (modify invoices, update records) without appropriate controls. NetSuite is the system of record for finance — erroneous writes could have significant downstream consequences.

Before any NetSuite MCP work proceeds, assess:
1. Does a NetSuite MCP connector exist, and what operations does it expose?
2. Can it be configured as read-only? If so, how?
3. What approval/confirmation gates would be needed for any write operations?
4. Who needs to sign off on the risk before connecting Claude to NetSuite?

## Acceptance criteria

- [ ] Assessment completed: what does a NetSuite MCP integration look like?
- [ ] Read-only path identified (or confirmed as not available)
- [ ] If write access is unavoidable, governance proposal drafted
- [ ] Jade or Matt Lees consulted before any connector goes live
- [ ] Clear recommendation: proceed (with safeguards) / don't proceed / defer

## Notes

Ivan's credit control workflow (daily NetSuite export → Claude analysis) is a great pattern precisely because it keeps Claude read-only: data is exported to a flat file, then processed. This should be the model for any NetSuite AI work unless there's a compelling case for live writes.

Anneliese is already thinking about this risk unprompted — a good sign that finance is becoming more AI-literate.
