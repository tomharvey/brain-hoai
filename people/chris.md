---
title: Chris Fothergill
created: 2026-03-27
updated: 2026-03-27
type: person
role: Head of Architecture
team: Engineering
email: chris@flockcover.com
tags: [engineering, architecture, code-quality]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-24
---

## Role

Head of Architecture

## Team

Engineering

## Relationship

Peer

## Working style notes

- Deeply practical — focused on code quality, documentation, and maintainability
- Concerned about AI-generated code quality degrading PR standards
- Working on architecture docs and skills to teach Claude company coding standards
- Interested in using AI for large refactoring tasks (quote vs adjustment screen abstraction)
- Can still write code faster than Claude in some cases

## AI Activation

**Stage**: 4 — Delegation
**Confidence**: high
**Assessed**: 2026-06-24
**Evidence**: Jun 24 Group Therapy confirmed: "writing significantly more tests now, just by asking agents to test what they write." Engaged with spec-driven development — PR descriptions as spec artifacts, deviation logs, architectural decision extraction. Framed plans as mapping to existing SDLC artifacts (ticket = requirements; inline comments = deviations; PR description = solution + rationale). Jun 10 group therapy: delegating tasks to background agents. May 8 coding standards: multi-layer context hierarchy design (principles → service architecture → libraries → services) for team-wide AI use.

**Not Stage 3**: Delegating tasks to background agents, designing the architecture of AI systems for the whole team. Past conversational fluency.
**Not Stage 5**: Not yet measuring adherence or directing multi-agent systems with feedback loops. The style guide development cycle would be Stage 5 if instrumented with conformance checks.
**To progress**: Encode the style guide development cycle — take repos + principles, generate exemplar output, use as the standard agents are measured against. Add conformance checking → Stage 5.

## 1:1 Log

### 2026-03-27

- Three groups tackling submissions independently — needs coordination
- Risk of "load bearing Google sheets" from side-of-desk automations
- AI-generated code quality is a growing problem — multiple PR review iterations
- Proposed: use PR reviews to teach agents, build docs from corrections
- Wants to try Claude on quote/customer adjustment abstraction — run for weeks on a terminal
- Looking at TanStack's approach to skill generation from npm libraries

### 2026-06-24 — AI Group Therapy

- Plans discussion: framed plan files as mapping to existing SDLC artifacts (ticket = requirements, inline comments = deviations, PR description = solution + rationale)
- Writing significantly more tests now — "just by asking agents to test what they write"
- Engaged with spec-driven development approach; PR descriptions as architectural records
- Endorsed DR hackathon concept on AWS with Nvidia → [[AI-140]]
- Discussed self-healing loop with Fergus — harness building as Ishmael's explicit remit
- See: [[2026-06-24-ai-group-therapy]]
