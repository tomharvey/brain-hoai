---
title: Ismael Jebril
created: 2026-03-27
updated: 2026-04-21
type: person
role: Engineering Manager
team: Engineering
tags: [engineering, management, portal, claims]
ai_activation_stage: 5
ai_activation_confidence: high
ai_activation_assessed: 2026-05-26
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
**Stage**: 5 — Extended orchestration  
**Confidence**: high  
**Assessed**: 2026-05-26  
**Evidence**: ~90% AI-generated code via Claude Code; PromptFoo evals with golden/red-team datasets (~50–60 tests each); DataDog LLM observability (full conversation tracking); Bedrock Agent Core memory (summarization, semantic, user preference strategies); switched agent framework from Strands to Vercel; deliberate non-deterministic vs deterministic architectural choices. Operating at the current engineering ceiling.

**Not Stage 4**: Multi-agent orchestration is table stakes for Ishmael — he's past that. He's building production observability infrastructure, running empirical evals against his own systems, and designing memory architectures. He's measuring and improving agent behaviour, not just directing it.  
**At the current ceiling**: Stage 5 is the defined top of the framework. The questions he's actively grappling with — adherence measurement, memory strategy, agent framework selection — are frontier problems with no settled answers. What comes next isn't yet characterised.  
**To progress**: Framework doesn't define beyond Stage 5. Likely frontier: multi-model orchestration, self-improving context loops, organisational-scale agent coordination. Ishmael is the right person to help define what Stage 6 looks like.  
**Framework note**: Stage 5 needs a description of what the frontier looks like from the inside — what are the open problems, what does progression look like when there's no defined next stage?

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

