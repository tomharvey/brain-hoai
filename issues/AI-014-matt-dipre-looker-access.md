---
title: "Get Matt Dipre Looker access and permissions"
id: AI-014
created: 2026-04-14
updated: 2026-04-14
due: 2026-04-18
origin: "[[2026-04-14-matt-dipre-ai-discovery]]"
domain: ai-enablement
type: issue
status: cancelled
priority: medium
assignee: tom
tags: [looker, access, matt-dipre, kirsty]
---

## Description

Matt Dipre has a Looker account but no permissions to create or view dashboards. This is blocking him from experimenting with data and the Looker-Claude connector. Likely a common issue across the company — others have hit the same wall.

## Acceptance criteria

- [ ] Speak to Kirsty and Geran about granting Matt granular Looker permissions
- [ ] Confirm whether there's a license constraint or just permissions
- [ ] Matt can create and view dashboards in Looker

## Notes

- Matt is a financial analyst — needs access to invoice/NetSuite-related data at minimum
- Also check: is NetSuite data available in Looker/Snowflake? Would unlock invoice automation path
- While at it, check Quincy's backup sheet data source (Retool? Snowflake?)

## Links

- [[matt-dipre]]
- [[kirsty]]
- [[2026-04-14-matt-dipre-ai-discovery]]

**Closed 2026-07-09 — obsolete.** Matt bypassed the access problem: pulls straight from the data lake (Geran-enabled), has a Looker MCP, and "doesn't really use that as much anymore". Superseded by his calculator pipeline (AI-162).
