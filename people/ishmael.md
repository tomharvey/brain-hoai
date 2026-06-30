---
title: Ismael Jebril
created: 2026-03-27
updated: 2026-06-30
type: person
role: Engineering Manager
team: Engineering
tags: [engineering, management, portal, claims]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-30
---

## Role

Engineering Manager

## Team

Engineering

## Relationship

<!-- to be confirmed -->

## Working style notes

- Very hands-on as an EM
- Nervous about portal workload distribution in re-teaming
- Defensive about team changes initially ("don't fix what ain't broken") but comes around
- Concerned about claims integration maintenance (problematic until end of year)
- Working on safety agent with memory
- Switched safety agent from Strands to Vercel — now the go-to TypeScript framework
- ~90% AI-generated code via Claude Code
- Integrated DataDog for LLM observability
- Memory via Bedrock Agent Core

## AI Activation
**Stage**: 4 — Delegation
**Confidence**: high
**Assessed**: 2026-06-30
**Evidence**: Works from Segovia — just laptop + terminal, no external screen. Uses tmux-style workflows. Runs multiple agents in parallel writing PRs he reviews. Built submission pipeline rapidly with AI. ~90% AI-generated code via Claude Code. Admits "not learning that much" and "no craft." Feels expectations are higher with AI. Work seeps into evenings (sending prompts at 5pm, checking at 8pm). Doesn't feel job security fear. Calendar is a bottleneck (interviews, management duties). Previously built PromptFoo evals, DataDog LLM observability, Bedrock Agent Core memory.

**Not Stage 3**: Running multiple parallel agents generating PRs, reviewing at task level. Well past building individual tools — operating as a manager of AI workers.
**Not Stage 5**: Jun 2026 evidence shows strong delegation but the observability/eval infrastructure from May is product-specific (safety agent), not yet generalised across the team or directing multi-agent systems with adherence metrics at organisational scale. Previous Stage 5 assessment was premature — the evals and observability are impressive but scoped to his own domain.
**To progress**: Generalise the observability and eval patterns beyond the safety agent. Help define team-level standards for AI-generated code quality. His experience with PromptFoo and DataDog makes him the natural owner of shared AI quality infrastructure.
**Historical note**: Downgraded from Stage 5 (May 26) to Stage 4 (Jun 30). Earlier assessment over-weighted the sophistication of his safety agent infrastructure. Stage 5 requires directing multi-agent systems with validation/observability at an organisational level — Ishmael's work is impressive but still personally/product-scoped.
**Framework note**: The "no craft" concern and evening work seepage are Stage 4 existential questions — what does engineering become when you manage AI workers rather than write code?

## 1:1 Log

### 2026-04-17 — Agent demo and dev tooling

- Integrated DataDog for LLM observability — full conversation tracking, but issues: user ID/email/policy ID not surfacing, input/output mapping empty, session grouping broken
- Emailed DataDog Apr 14, no response — chasing
- Switched safety agent from Strands to Vercel (frontend + backend) — Chris approved
- PromptFoo evals: "golden set" + "red team" datasets (~50-60 tests each), running manually, passing through compliance
- Skills: file-based system (claims, data accuracy, disconnected vehicles, fatigue, portal navigation)
- Memory: Bedrock Agent Core (summarization, semantic, user preference strategies)
- ~90% of code AI-generated via Claude Code, terminal-based
- Tom showed personal OS vault — Ismael interested in developer tooling follow-up
- See: [[2026-04-17-ismael-catchup]]

### 2026-04-21 — Codifying Context (group session)

- Primarily needs technical context, skeptical about broader company context value for daily dev work
- Agreed shared skills (Granola→Linear, code reviews) are the clear first win
- GitHub vs Notion debate — prefers practical solutions over tooling debates
- See: [[2026-04-21-codifying-context-retention-team]]

### 2026-06-30 — June transcript synthesis

- Works from Segovia, Spain — just laptop + terminal, no external screen
- Uses tmux-style workflows — multiple agents in parallel writing PRs he reviews
- Built submission pipeline rapidly with AI
- Admits "not learning that much" and "no craft" — existential concern about what engineering becomes
- Feels expectations are higher with AI — more output expected
- Work seeps into evenings (sends prompts at 5pm, checks at 8pm)
- Doesn't feel job security fear
- Calendar is a bottleneck — interviews, management duties competing with coding time
- Stage reassessed: 5 → 4. Impressive tooling but scoped to personal/product domain, not yet organisational

