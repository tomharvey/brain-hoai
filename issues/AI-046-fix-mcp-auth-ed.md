---
title: Fix MCP auth for Ed — Slack, Notion, Telemetry requiring approval on every action
created: 2026-05-14
updated: 2026-05-14
domain: ai-enablement
type: issue
status: todo
priority: urgent
due: 2026-05-15
origin: "[[2026-05-14-ed-tom-121]]"
tags: [mcp, auth, ed, slack, notion, telemetry]
---

Ed has "dangerously skip permissions" enabled but is still being blocked on every MCP tool call for Slack and Notion. Telemetry MCP is also requiring approval but Ed is less concerned about that one.

Root cause likely: MCP server config requires explicit trust grants that aren't persisting between sessions, or the MCPs aren't in the trusted list.

Telemetry MCP also has known auth issues — old implementation, problems with how it's defined. Lower priority for Ed but worth a glow-up when addressing the others.

Actions:
- [ ] Check Ed's Claude Desktop MCP config — which servers are listed, which have trust settings
- [ ] Verify Slack and Notion MCPs are configured to allow auto-approval
- [ ] Investigate Telemetry MCP auth definition — flag for separate cleanup
