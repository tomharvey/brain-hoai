---
title: Fergus Doyle
created: 2026-03-27
updated: 2026-04-20
type: person
role: Interim CPTO
team: Leadership
tags: [leadership, strategy]
ai_activation_stage: 4
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-25
---

## Role

Interim CPTO (Chief Product & Technology Officer)

## Team

Leadership

## Relationship

Reports-to. Tom reports directly to Fergus. They worked together years ago at another startup and have worked together at least one other company.

## Working style notes

- Strategic thinker, comfortable with ambiguity
- Thinks about board-level concerns (roadmap, 24-month outlook)
- Pragmatic about re-teaming friction — expects people to "come out the other end"

## AI Activation

**Stage**: 4 — Delegation
**Confidence**: medium
**Assessed**: 2026-06-25
**Evidence**: Built a ledger service prototype overnight with Claude — never written a line of code in this codebase, ~80% of the way there with some architectural repointing needed. Gave Claude the full installments OKR doc + Jordi's MVP requirements → working service output. Used Claude to prototype and validate the OAuth refresh token auth flow as a background task (ran for an hour, found and implemented the abuse prevention feature in one change). Champions the self-healing loop and harness architecture concepts as central engineering strategy. "I can't understand why people aren't just doing the same sort of discovery effort."

**Not Stage 3**: This is agentic delegation — giving Claude an entire codebase context + requirements doc and getting a working service back overnight. Not conversational fluency.
**Not Stage 5**: Not yet running instrumented feedback loops or measuring model adherence at team level. The harness he's championing would be Stage 5 if built and instrumented.
**To progress**: Lead the two-day installments hack session (→ Jordi + Joanne + Geran + Javier). Drive the Ishmael harness pitch (→ [[AI-140]]). Both would turn his personal practice into team practice.

## 1:1 Log

### 2026-03-26

- OKR session outcomes — balanced delivery vs commercial targets
- Re-teaming: Alex concerned about change, Ishmael nervous about portal workload
- AI initiative rollout — announce at flock o'clock, start individual conversations next week
- Board meeting Apr 20 — needs AI roadmap (H2 2026 + 24-month)
- Three strategic bets: disconnected fleets, e-trading automation, driver-level risk
- Fertile grounds for AI: distribution, underwriting assistance, finance

### 2026-04-02 — Matt Lees Enterprise Engine review

- **Pre-call** (Slack to Tom/Jordi/Mima): initial reaction was "overengineered solution to the problem" and "might struggle with ownership/maintainability in its proposed state". Matt had asked for API keys; Fergus gave a cautious answer and wanted a call first.
- Fergus wanted to join for two reasons: (1) understand what Matt's trying to achieve, (2) optics — didn't want to seem unwilling to help after the bureaucratic API key response
- **Post-call**: shifted to thumbs up. Wants Antton kept in the loop. Comfortable with current security posture at this stage.
- Happy for Tom to run point — doesn't feel need to be involved beyond this conversation
- Enterprise Engine could be the board story — most concrete AI ROI example

### 2026-04-20 — Weekly Product + Tech Kickoff

- Jay staging: PR ready with Opus 4.7 upgrade, need volunteers by Wednesday lunchtime
- KR2 kickoff with Adam, Tom, Darren, Johnny — trading evolution, connectivity challenges
- Haulage fact find needed ASAP — Liam doesn't have current version
- BDM model opinions emerging — potential shift to GWP model for done deals
- OKR3 authority framework: Emily leading, Darren/Andrew co-owning
- David Stephens session Wednesday — Darren/Milan presenting power-up workstreams, Fergus monitoring

### 2026-04-20 — Submission Processing Pipeline

- Led walkthrough of 9,000-submission pipeline (~£40 total, ~50p/submission)
- Three S3 bucket architecture: raw docs → OCR/JSON intermediary → final partitioned
- Jacob wiring into Iceberg table. Only 6/9,000 too long for context window.
- Data source decision needed: HubSpot tickets vs Google Drive
- Integration opportunity with Javier's document classification work
- See: [[2026-04-20-submission-processing-pipeline]]

### 2026-06-25 — Weekly

- Frustration with Geran's "six months of work" framing for installments — built ledger service prototype overnight with Claude, never having written production code in this codebase
- Proposed two-day hack session: Joanne + Geran + Javier + Jordi + Fergus to surface what's actually hard
- Engineering culture concern: team frozen, not shipping at pace; "have we lost our ability to ship?"
- Proposed making building the harness Ishmael's explicit job for a month
- Claude spend: ~£5-6k/month; agreed to formalise as a production policy → [[AI-142]]
- Bedrock fallback: Tom to check what's wired → [[AI-143]]
- See: [[2026-06-25-fergus-tom-weekly]]
