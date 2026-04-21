---
title: Fergus Doyle
created: 2026-03-27
updated: 2026-04-20
type: person
role: Interim CPTO
team: Leadership
tags: [leadership, strategy]
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
