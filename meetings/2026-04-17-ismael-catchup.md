---
title: "Ismael — agent demo and dev tooling"
created: 2026-04-17
updated: 2026-04-17
domain: engineering-workflows
type: meeting
tags: [safety-agent, datadog, vercel, evals, dev-tooling, personal-os]
---

# Ismael — agent demo and dev tooling

## Attendees

- [[ishmael|Ismael Jebril]]
- Tom Harvey

## Key themes

### DataDog integration operational but incomplete

Full conversation tracking visible. Issues: user ID/email/policy ID not surfacing in traces, input/output mapping showing empty, session grouping broken (each question creates new trace). Emailed DataDog Apr 14, no response. Plan to chase.

### Agent migrated: Strands to Vercel

Both frontend and backend. Chris approved after seeing consistency and advancement. Vercel now considered the go-to TypeScript agent framework.

### PromptFoo evals in place

"Golden set" and "red team" datasets (50-60 tests each). Run manually, passing through compliance. Future: automate in CI/CD, but needs staging telemetry data.

### Skills implemented

File-based system covering claims, data accuracy, disconnected vehicles, fatigue, portal navigation. Get-skill tool reads file and injects into LLM context.

### Memory via Bedrock Agent Core

Three strategies: summarization, semantic, user preference. Loads at conversation start, saves at end. Extracts structured memories, not full conversations.

### Team adoption strong

Most tech team has written skills (everyone except Stefan). [[jacob-holland|Jacob]] built impressive automated documentation updates.

### ~90% AI-generated code

Ismael working almost entirely through Claude Code, terminal-based.

### Tom demoed personal OS vault

Ismael visibly interested. Discussion on what developer tooling equivalent looks like. Follow-up planned on dev tooling and personal knowledge management.

### S3 vs DataDog for conversation storage

Tom showed S3 session storage (nested JSON, reloadable chats, automated improvement suggestions). DataDog web UI insufficient for meaningful analysis — need programmatic API/MCP access.

## Actions

- [ ] **[[ishmael|Ismael]]**: Chase DataDog again on integration issues
- [ ] **[[ishmael|Ismael]]**: Investigate DataDog MCP for programmatic access to conversation data
- [ ] **[[ishmael|Ismael]]**: Commit PromptFoo test datasets (golden + red team)
- [ ] **Tom**: Attend next week's team session
- [ ] **Tom + [[ishmael|Ismael]]**: Follow-up on developer tooling / personal knowledge management

## Transcript

Full transcript: [[2026-04-17-ismael-catchup-transcript]]
