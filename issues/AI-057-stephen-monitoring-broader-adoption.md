---
title: "AI-057: Evaluate Stephen's Databricks monitoring system for broader adoption"
created: 2026-05-19
updated: 2026-05-19
domain: engineering-workflows
type: issue
status: todo
priority: medium
due: 2026-05-23
origin: "[[2026-05-19-stephen-millington]]"
tags: [engineering, databricks, monitoring, stephen, mcp]
---

## Summary

[[stephen-millington|Stephen Millington]] has built an AI-powered Databricks job monitoring system with Slack alerting and Linear ticket creation. Demo scheduled for 2026-05-20. Evaluate whether it can be generalised for other teams and what's needed to make it production-ready.

## Context

The system:
- Queries Databricks system tables for job costs and performance
- Passes data visually to Claude for anomaly detection (no coded algorithm)
- Sends Slack alerts with Acknowledge/Create ticket buttons
- MCP server component is team-agnostic — could be plugged in anywhere
- Currently uses Databricks Mosaic endpoint (not direct Anthropic API)
- Hacky deployment; needs proper auth and infrastructure work

Stephen noted nothing about the Slack messaging layer is retention-specific — it's a general alerting infrastructure that any team could use.

## Actions

- [ ] Attend/review demo on 2026-05-20
- [ ] Determine which teams would benefit from the Slack alerting MCP
- [ ] Assess auth and deployment requirements for production use
- [ ] Consider redirecting to AWS/AI gateway endpoint rather than Mosaic
- [ ] Evaluate adding agentic fix-suggestion to Linear ticket creation

## Notes

- [[jacob-holland|Jacob]] had an infrastructure conversation with Tom same morning — worth aligning
- Deterministic vs non-deterministic tradeoff is worth documenting as a pattern for other teams
