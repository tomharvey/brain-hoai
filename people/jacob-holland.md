---
title: Jacob Holland
created: 2026-04-21
updated: 2026-04-21
type: person
role: Data Engineer
team: Engineering — Retention / Safety
tags: [engineering, data, automation, ai-champion]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-18
---

## Role

Data Engineer

## Team

Engineering — Retention / Safety team (with Jemima, Ismael)

## Relationship

Met in group context at codifying context session (2026-04-21).

## Working style notes

- Built automated documentation update agents — runs on cron, impressive results
- Golden rules for DBT projects recorded in markdown files — Claude enforces standards
- Wiring Fergus's submission pipeline results into Iceberg table for querying
- Strong AI builder — most tech team members have written skills, Jacob among the most productive
- Comfortable with Claude Code from terminal (99% of usage)
- Skeptical of Notion MCP quality — prefers markdown + vector encoding for search

## AI Activation

**Stage**: 4 — Delegation
**Confidence**: high
**Assessed**: 2026-06-18
**Evidence**: Managing 2-3 parallel Claude Code processes as junior engineers — assigns discrete tasks, flips between screens, reviews at task level. "I just view them as really capable Juniors." Built automated documentation update agents on cron. Maintains golden rules for DBT projects in markdown that Claude enforces. Had to set a guardrail when an agent tried to push directly to main — meaning autonomous production pushes are a realistic failure mode he has addressed.

**Not Stage 3**: Not thinking with the model — directing multiple instances in parallel. Reviews at task level, not line-by-line.
**Not Stage 5**: Cron agents and DBT golden rules are personal/team-scoped. Has not yet described directing multi-agent systems with defined adherence metrics or building shared infrastructure others use.
**To progress**: Take the DBT golden rules pattern and make it the team standard. Add a conformance check loop and Slack notification when drift is detected — that tips into Stage 5 territory.
**Framework note**: Jun 2026 group therapy session provided direct verbatim Stage 4 evidence. The "capable Juniors" framing and guardrail anecdote are unambiguous.

## 1:1 Log

### 2026-04-21 — Codifying Context (group session)

- Shared golden rules pattern for DBT projects — markdown files in code repos
- Raised question: how do we share resources beyond local terminal usage?
- Automated documentation agents flagged as template for team-level shared context
- Could encode data extraction skills for wider team (Ismael, Kirsty, Ben)
- See: [[2026-04-21-codifying-context-retention-team]]
