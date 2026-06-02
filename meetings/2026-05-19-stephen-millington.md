---
title: Stephen Millington — AI catchup
created: 2026-05-19
updated: 2026-05-19
domain: engineering-workflows
type: meeting
tags: [engineering, databricks, monitoring, agents, vibe-coding]
---

## Attendees

- [[stephen-millington|Stephen Millington]]

Full transcript: [[2026-05-19-stephen-millington-transcript]]

## Key themes

### What Stephen built: Databricks job monitoring system

Stephen has built an AI-powered monitoring system for Databricks jobs — the #2 token usage spike on the company leaderboard came from building this.

- Queries Databricks system tables for job runtime costs and performance metrics
- Instead of coding deterministic anomaly detection, passes the graph to Claude visually — "I can see the ones that are concerning to me straight away"
- Runs overnight, sends alerts to Slack with context about spikes/trends
- Built a Slack app with interactive buttons: **Acknowledge** (logs human review, no ticket) and **Create ticket** (auto-generates Linear ticket with full context)
- MCP server component allows any team to send alerts via text prompt — not retention-specific
- Instructions stored in MD files for easy updates; context builds up over time to reduce false positives
- Uses Databricks Mosaic endpoint (not direct Anthropic API) — worth noting for infrastructure alignment
- Minimal deterministic code (just SQL queries); rest is prompt-based
- Single main prompt: "You are monitoring the health of a data book job estate"

Demo tomorrow (2026-05-20). Questions to resolve: authentication, proper deployment vs current hacky state, whether other teams want to use it.

### Engineering philosophy discussion

- Stephen self-describes as learning "vibe coding" — letting AI handle implementation
- Still uses notebooks for quick data exploration and to "stay sharp"; wants to combine VS Code + Databricks notebook via cluster connection
- Discussion of staying relevant: "if my job becomes babysitting a prompt, I'll find something else to do"
- Key insight from Tom: **our jobs were never to type things** — the struggle of coding was the fun, but there are new shapes of problems now
- Good framing on deterministic vs non-deterministic: Stephen's monitoring system is now non-deterministic where his previous code was — and that's fine for this use case, but requires different thinking about validation
- Tom's synthesis: knowing **where** to use the non-deterministic system, where to use deterministic functions, and where the human sits in the loop is the new core engineering skill
- Raised concern about junior/entry-level engineers: Stephen spoke to a student about it and didn't know what to tell her

### Proposed: new AI workshop format

Both Tom and Jordi (separately) surfaced that an engineering-specific regular forum is needed — focused on **"how do we stay relevant and what is our job now"** rather than demo showcases. Stephen was explicit: he'd engage with that more than the weekly AI breakfast.

## Actions

- [ ] **Stephen**: Demo Databricks monitoring system to stakeholders tomorrow (2026-05-20)
- [ ] **Tom + Stephen**: Evaluate whether monitoring system can be generalised for other teams
- [ ] **Stephen**: Investigate VS Code + Databricks cluster connection for notebook-equivalent workflow in Claude Code

## Notes

- The Slack → Linear ticket integration Stephen built is a great pattern: low-cost to make agentic (auto-suggest fix), high-value, low-risk of harmful mistakes.
- Stephen confirmed Jordi ran a monitoring review session with his team yesterday — that's what prompted Stephen to demo his system.
- "gerund" in transcript = [[geran]] (Granola mishear).
- "giardi's alerting thing" in transcript = Jordi's alerting session.
