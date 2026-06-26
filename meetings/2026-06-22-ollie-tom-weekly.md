---
title: "Ollie / Tom — Weekly (AI / The New Frontier)"
created: 2026-06-22
updated: 2026-06-22
domain: engineering-workflows
type: meeting
tags: [ollie-crowe, engineering, submissions-mcp, claims-transcripts, acquisition-brain, broker-portal]
---

## Attendees

- [[ollie-crowe]] (Oliver Crowe, Technical PM)
- Tom Harvey

Full transcript: [[2026-06-22-ollie-tom-weekly-transcript]]

---

## Key themes

### Claims transcripts — major output

- Ollie ran Claude over ~1,128 claims transcripts via 10 sub-agents + a QA agent
  - First 600: just over an hour; next 528: 54 minutes
  - Output: comprehensive claims pain point brief
- Next step: bring findings into Five Sigma sessions; push for customer-centric view of claims vs replicating legacy TPA processes
- Five Sigma's live AI tool (triage, policy doc checking) needs investigation — who sets the rules, can it expose an API endpoint?

### Value selling OKR and sales AI support

- Q1 OKR (Matt Price + Matt Lees) largely stalled — only output is a portal checkbox showing if customer had a demo
- Sales team lacks customer context going into calls (e.g. current insurer, policy history)
- Lightweight BDM brain with an underwriting component suggested — minimal maintenance but high value
- Tom Rogers using AI more broadly than expected (LinkedIn research, Claude, Looker dashboards) — good source for sharing with wider team

### Submissions pipeline MCP

- Officially deprioritized from Q3 OKRs but tracked in Notion (item 27); end-of-week delivery expected (dbt work by Alex Dyball first, then bolt an MCP)
- Jacob confirmed: adding to existing Flock MCP is a small lift vs a separate MCP
- Two Flock MCPs exist: policy administration (platform DB) and data lake — submissions likely goes into data lake given Alex's dbt work
- V0 tool design: single "get claim submissions data" tool, pre-baked query, inputs: date range and/or insurer name
- Pricing team use case: "what has DCL been doing across their top 100 submissions?"
- Need to sketch a ticket with enough detail for an agent to execute before delivery

### Engineering AI practices — agent plans

- [[javier]] is storing agent plans and keeping agents on track with them — only engineer doing this consistently
- Plans could live in the acquisition brain for Ollie to review at PR time
- Rob still "finishing things off by hand" (his words) — unverified, could check PRs
- Plan-tracking as a new form of backlog refinement and retrospective input
- Tom to ping Javier about sharing plans in the acquisition brain

### Broker portal

- Ollie not satisfied with where it was left at end of last year; wants a polish pass
- PostHog metrics unreliable: confused by claims admin users and fleet users both hitting the policies page
- Plan: use Claude with Chrome to identify missing events and raise a ticket, then apply the same approach across all pages

### Context handoff between agent sessions

- Discussed markdown handover file updated as work progresses, picked up by next agent
- SQLite-based transcript indexing tool mentioned — Tom to find and share to avoid re-running full pipeline for new batches

---

## Actions

- [ ] [[ollie-crowe]]: sketch a ticket for the submissions MCP tool before delivery → [[AI-133]]
- [ ] [[ollie-crowe]]: use Claude and Chrome to fix PostHog event tracking on broker portal
- [ ] Tom: ping [[javier]] about storing agent plans in the acquisition brain
- [ ] Tom: find and share SQLite-based transcript indexing tool for claims batches
- [ ] [[ollie-crowe]]: run acquisition brain walkthrough in a team sync
