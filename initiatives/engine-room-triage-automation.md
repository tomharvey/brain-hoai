---
title: Engine Room triage automation
created: 2026-03-30
updated: 2026-03-30
domain: engineering-workflows
type: initiative
status: active
origin: self-started
owner: jordi
tags: [engine-room, linear, triage, automation, lambda, bedrock]
---

## Summary

Automate the initial triage of Engine Room tickets (bugs and small data errors tracked in Linear) using AI. When a ticket is created, a webhook calls a Lambda that uses PostHog data and internal MCP to suggest a resolution or initial diagnosis.

## Goal

Reduce the time engineers spend on initial triage of Engine Room tickets. Many of these follow repeatable patterns where the data needed for diagnosis already exists in PostHog and internal tools.

## Current state

- Jordi built an early MVP (~2 hours of work) connecting:
  - Webhook on Engine Room ticket creation → Lambda → Bedrock (direct, no framework)
  - PostHog MCP + internal MCP as data sources
- Very early stage — validating whether the approach works at all
- [[mima|Mima]] identified specific use cases she thinks are easy to automate because the data is already in PostHog + internal MCP
- Not scalable — using raw Bedrock calls without any framework

## Dependencies

- PostHog data quality and coverage for Engine Room ticket types
- Internal MCP access
- If validated: [[agent-framework]] for production deployment path (Chris/Ishmael's work)

## Risks

- Engine Room tickets may be too varied for automated triage to be useful
- Without framework, the Lambda becomes unmaintainable if scope grows
- Could create noise if suggestions are wrong — needs accuracy threshold before expanding

## Next actions

- [ ] Jordi: validate MVP — does it produce useful triage suggestions?
- [ ] Identify the specific "easy" use cases Mima flagged
- [ ] If validated: plan migration to proper framework

## Log

### 2026-03-30

- Learned about this from Jordi in 1:1
- Very early — ~2 hours invested, Lambda + Bedrock + PostHog/internal MCP
- Mima sees easy wins; Jordi focused on proving it works first
