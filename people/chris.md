---
title: Chris Fothergill
created: 2026-03-27
updated: 2026-06-30
type: person
role: Head of Architecture
team: Engineering
email: chris@flockcover.com
tags: [engineering, architecture, code-quality]
ai_activation_stage: 3
ai_activation_confidence: high
ai_activation_assessed: 2026-06-30
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

**Stage**: 3 — Tool building
**Confidence**: high
**Assessed**: 2026-06-30
**Evidence**: Built API endpoint specifically for Claude (policy admin MCP server) — AI-specific infrastructure. Further along on AI than colleagues give him credit for. Interested in architectural patterns for AI integration. Strong on code review — doesn't skip PRs. Raised point about team-level vs individual AI adoption. Concerned about quality/testing. Principles-focused: "principles haven't changed, but processes need to support them." Previously: multi-layer context hierarchy design (principles -> service architecture -> libraries -> services), spec-driven development, writing more tests via agents.

**Not Stage 2**: Building AI-specific infrastructure (MCP server), designing architectural patterns for AI integration. Well past connecting existing tools.
**Not Stage 4**: The MCP server and architectural thinking are impressive tool-building, but Chris's approach is deliberate and principles-first. He's building the infrastructure for delegation rather than routinely delegating. Previous Stage 4 assessment over-weighted the background agent delegation; his primary mode is architectural design and quality enforcement.
**To progress**: Use the MCP server and coding principles as the foundation for a delegation workflow. Once the infrastructure is in place and trusted, shift from building the system to directing it. The conformance checking idea is the natural bridge.
**Historical note**: Downgraded from Stage 4 (Jun 24) to Stage 3 (Jun 30). Chris is building sophisticated AI infrastructure but his operating mode is architect/builder, not delegator. The quality concern and principles focus are strengths that keep him building robust foundations before delegating.

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

### 2026-06-30 — June transcript synthesis

- Built API endpoint specifically for Claude — policy admin MCP server
- Further along on AI than colleagues give him credit for
- Interested in architectural patterns for AI integration
- Strong on code review — doesn't skip PRs
- Raised point about team-level vs individual AI adoption
- Concerned about quality/testing — principles-focused: "principles haven't changed, but processes need to support them"
- Stage reassessed: 4 → 3. Sophisticated tool builder and architect, but operating mode is building infrastructure for delegation rather than routinely delegating
