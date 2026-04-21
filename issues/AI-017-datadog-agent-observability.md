---
title: "Resolve DataDog LLM observability integration issues"
id: AI-017
created: 2026-04-17
updated: 2026-04-17
due: 2026-04-25
origin: "[[2026-04-17-ismael-catchup]]"
domain: engineering-workflows
type: issue
status: in-progress
priority: high
assignee: ismael
tags: [datadog, observability, safety-agent, agents]
---

## Description

DataDog LLM observability is integrated with the safety agent but has three blocking issues that prevent meaningful analysis:

1. **User info not surfacing**: user ID, email, policy ID passed via Vercel's observability grab function but not appearing in traces
2. **Input/output mapping empty**: traces show empty inputs/outputs at the top level (data visible when drilling into individual spans)
3. **Session grouping broken**: each question creates a new trace instead of grouping by conversation session

Emailed DataDog on Apr 14 with technical details (included Maria, account manager). No response after 3 days — unusual silence.

Additionally: need programmatic API/MCP access to DataDog data for automated conversation analysis. Web UI is insufficient.

## Acceptance criteria

- [ ] User ID, email, and policy ID visible in DataDog traces
- [ ] Input/output mapping populated at top level
- [ ] Sessions grouped by conversation
- [ ] Evaluate DataDog MCP for programmatic access
- [ ] If DataDog can't deliver, fall back to S3 session storage

## Links

- [[2026-04-17-ismael-catchup]]
- [[safety-agent-memory]]
- [[agent-framework]]
