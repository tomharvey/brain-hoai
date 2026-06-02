---
title: Define and document engineering AI target state
id: AI-054
created: 2026-05-18
updated: 2026-05-18
origin: "[[2026-05-18-dev-ai-practices]]"
domain: engineering-workflows
type: issue
status: todo
priority: high
assignee: jordi
tags: [target-state, engineering-environment, direction, team-communication]
---

## Description

Fergus's point from the Dev AI Practices session: "if we can describe the direction of travel and what good looks like in a target state, the team can chip away at it incrementally." Without a written target state, the team can't self-serve and the Head of AI ends up being the sole source of direction.

The target state document should cover:
- What does a typical engineering day look like in the target state?
- What is the Linear → PR flow and what does "reviewing like a mid-level hire" mean?
- What are the unbreakable principles/rules (front end: UI kit, components; back end: CQRS/hexagonal)?
- Where is the harness vs where is human judgment?
- What is the gold standard service that agents should replicate?

Jordi + Chris own this. Tom to prompt/facilitate. Should be a living document the whole team can read and contribute to.

## Acceptance criteria

- [ ] One-page target state written and shared with engineering team
- [ ] Covers: daily workflow, Linear→PR flow, unbreakable principles, gold standard service
- [ ] Team can use it to chip away incrementally without being told what to do next

## Links

- [[2026-05-18-dev-ai-practices]]
- [[ai-native-engineering]]
- [[platform-architecture-docs]]
