---
title: Ivan Boix
created: 2026-06-02
updated: 2026-06-02
type: person
role: Financial Analyst
team: Finance (reports to Anneliese Van Wijk)
tags: [finance, credit-control, netsuite, ai-user]
ai_activation_stage: 3
ai_activation_confidence: high
ai_activation_assessed: 2026-06-02
---

## Role

Financial Analyst — credit control focus. Reports to [[anneliese-vanwijk|Anneliese Van Wijk]]. Joined Flock June 2025.

## Team

Finance. Works alongside [[matt-dipre|Matt Dipré]] and [[queency-gonsalves|Queency Gonsalves]] under Anneliese.

## Working style notes

- Built his AI workflow before anyone told him to — "built the process first, then figured out how AI could help." Right order of operations.
- Running the same context-loaded credit control chat for 2 months and saving "hours of work" daily
- Has created a Claude skill for the daily prioritisation report
- Weekly carrier reporting (Admiral net debt position) — 1 minute vs previous manual process
- HubSpot connector available but prefers manual approach for nuanced chasing (different broker handling strategies)
- Some broker payment terms (Marsh, Lockton) live only in his head — no system capture yet
- Described by Tom as "the archetype for data-heavy finance use cases"

## AI Activation

**Stage**: 3 — Daily automated workflow with skill creation
**Confidence**: high
**Assessed**: 2026-06-02
**Evidence**: Daily credit control prioritisation system running 2+ months: NetSuite aging export → Claude → prioritised report with summary dashboard, top 5 actions, movement tracking, overdue vs. not-yet-due breakdown. Completed in ~5 minutes including export. Weekly Admiral carrier reporting (1 min). Has created a Claude skill for the daily report. Considering migration to Claude Co-Work for better session management.

**Not Stage 2**: Not just using a connected tool — built an autonomous daily workflow and created a reusable skill from it. Stage 2 is "I have context loaded"; Stage 3 is "I have a system that runs."
**Not Stage 4**: Single workflow, single domain. No multi-agent orchestration or delegation of whole business processes. Hasn't yet shared or scaled the workflow to teammates.
**To progress**: Encode the payment terms knowledge that lives in his head into a Claude skill/context file — that's the Stage 3→4 data foundation. Then extend the workflow to HubSpot chasing when broker-specific logic is captured. Kevin and Matt Dipré are natural cross-pollination partners (AI-050 context).
**Framework note**: Strong Stage 3 with high confidence. "Well ahead of the team" per Tom's post-call notes. The daily use case is a reference model for ops/finance activation.

## 1:1 Log

### 2026-05-13 — AI Discovery
- See: [[2026-05-13-ivan-ai-discovery]]
- Daily NetSuite → Claude prioritisation system: 2 months running, saves hours daily. Created a skill.
- Admiral weekly debt review: 1 min vs manual process
- HubSpot chasing: prefers manual due to broker nuance
- Payment terms: stored in memory, not system — flagged as a gap
- Suggested Claude Co-Work migration for better file management
- Tom: capture as finance team workshop case study
