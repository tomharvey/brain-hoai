---
title: Safety agent with memory
created: 2026-03-27
updated: 2026-04-17
domain: product-ai
type: initiative
status: active
origin: self-started
owner: ishmael
tags: [safety, agents, memory, learning]
---

## Summary

Ishmael is building a safety agent that learns from corrections over time via memory systems. Discussed as a pattern that could apply more broadly to underwriting and submissions.

## Goal

An agent that improves accuracy over time by remembering human corrections — applicable initially to safety scoring, potentially to submissions and underwriting.

## Current state

- Ismael has a working safety agent deployed on Vercel (migrated from Strands)
- Skills implemented via file-based system (claims, data accuracy, disconnected vehicles, fatigue, portal navigation)
- Memory integrated via Bedrock Agent Core (summarization, semantic, user preference strategies)
- DataDog integrated for LLM observability — issues pending (user info not surfacing, session grouping)
- PromptFoo evals: ~110 test cases (golden set + red team), running manually
- Production readiness: CI/CD automation planned, needs staging telemetry data

## Dependencies

- Memory architecture decisions
- Integration with existing safety scoring systems

## Risks

- Stays as a one-person side project without broader adoption
- Memory approach may not generalise across domains without design work

## Next actions

- [ ] Catch up with Ishmael on current state and architecture
- [ ] Assess applicability to submissions and underwriting
- [ ] Connect with Chris's thinking on deterministic tools with arguments

## Log

### 2026-03-27

- Referenced in Chris AI conversation as a pattern worth expanding

### 2026-04-17

- **Major progress**: agent migrated from Strands to Vercel (frontend + backend). Chris approved — Vercel now the go-to TypeScript agent framework.
- **DataDog integrated** for LLM observability — full conversation tracking. Issues: user ID/email/policy ID not surfacing in traces, input/output mapping showing empty, session grouping broken. Emailed DataDog Apr 14, no response.
- **Skills implemented**: file-based system covering claims, data accuracy, disconnected vehicles, fatigue, portal navigation. Get-skill tool reads file and injects instructions.
- **Memory via Bedrock Agent Core**: three strategies (summarization, semantic, user preference). Loads at conversation start, saves at end. Extracts structured memories, not full conversations.
- **PromptFoo evals**: "golden set" + "red team" datasets (~50-60 tests each). Running manually, passing through compliance. Future: automate in CI/CD (needs staging telemetry data).
- ~90% of Ismael's code is AI-generated via Claude Code
- **S3 vs DataDog debate**: DataDog for monitoring, S3 for programmatic access. Tom showed S3 session storage — reloadable chats, automated improvement suggestions. Need DataDog API/MCP for meaningful analysis.
- See [[2026-04-17-ismael-catchup]]
