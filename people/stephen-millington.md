---
title: Stephen Millington
created: 2026-04-21
updated: 2026-05-19
type: person
role: Data / Backend Engineer
team: Engineering — Retention / Safety (reports to Jemima)
tags: [engineering, databricks, data]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-05-26
---

## Role

Data/backend engineer on [[mima|Jemima]]'s retention team. Works in Databricks; builds data pipelines, monitoring systems, and alerting infrastructure.

## Team

Engineering — Retention / Safety team

## Relationship

First 1:1 on 2026-05-19. Was previously under the radar on AI usage (occasional ChatGPT); hit #2 on company token leaderboard in two weeks by building a Databricks monitoring system with Claude Code. Now on premium plan.

## Working style notes

- Self-described "vibe coder" — let AI handle implementation while focusing on what to build
- Still values notebooks for quick data exploration and to stay technically sharp
- Honest about feeling behind the curve on AI previously; building his way forward
- Concerned about becoming a "prompt babysitter" — wants to stay relevant through understanding systems, not just prompting
- Prefers Slack-first for alerting/triage workflow
- More interested in "why does our job exist in 2030" conversation than weekly AI breakfast format

## Work highlights

- **Databricks monitoring system**: AI-powered overnight monitoring of Databricks jobs. SQL queries → visual graph → Claude detects anomalies. Slack alerts with Acknowledge/Create ticket buttons. MCP server for sending alerts is team-agnostic. Linear integration for ticket creation. Uses Databricks Mosaic endpoint.
- System is non-deterministic (Claude decides what's anomalous) vs his previous deterministic code — a deliberate architectural choice.

## AI Activation
**Stage**: 4 — Multi-agent orchestration  
**Confidence**: high  
**Assessed**: 2026-05-26  
**Evidence**: Built Databricks monitoring system with Claude Code in ~2 weeks (SQL queries → Claude anomaly detection → Slack alerts with Acknowledge/Create ticket buttons → Linear integration); built team-agnostic MCP server for Slack alerting; deliberate non-deterministic vs deterministic architectural choice; went from occasional ChatGPT to #2 on company token leaderboard. Grappling with Stage 5 questions ("prompt babysitter" concern, relevance through systems understanding).

**Not Stage 3**: Built a complete multi-component pipeline from scratch, not just one-shot code generation. Made explicit architectural decisions about determinism. Built reusable infrastructure (the MCP server is team-agnostic) rather than a one-off tool. The scale and intentionality of the Databricks system is well past plan mode.  
**Not Stage 5**: The system is a single workflow, not orchestrated multi-agent work. No evidence of empirical context quality testing on his own systems (he knows PromptFoo from J evals but hasn't applied it to his own work). The "prompt babysitter" anxiety signals he's approaching Stage 5 questions but hasn't resolved them.  
**To progress**: Apply empirical context testing to his own systems — PromptFoo or equivalent. Does improving the prompt actually improve anomaly detection? That measurement step is the Stage 4→5 transition. Then expand from single-workflow builds to multi-workflow orchestration.

## 1:1 Log

### 2026-05-19 — AI catchup

- Demoed Databricks monitoring system
- Discussion about deterministic vs non-deterministic systems, staying relevant, vibe coding
- Demo scheduled for wider audience 2026-05-20
- See: [[2026-05-19-stephen-millington]]

### 2026-04-21 — Codifying Context (group session)

- Attended but limited individual input captured
- See: [[2026-04-21-codifying-context-retention-team]]
