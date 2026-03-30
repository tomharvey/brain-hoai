---
title: Platform architecture documentation
created: 2026-03-27
updated: 2026-03-27
domain: engineering-workflows
type: initiative
status: active
origin: self-started
owner: chris
tags: [architecture, documentation, skills, code-quality]
---

## Summary

Chris is documenting platform architecture and coding standards so Claude can write code that meets company standards out of the box. Currently, AI-generated code requires multiple review iterations for basic patterns.

## Goal

Claude Code works out of the box for platform services — knows where tests go, how services are built, what libraries to use, and what patterns to follow.

## Current state

- Types documentation sorted
- Architecture documentation in progress
- Planning to look at TanStack's approach to generating skills from npm libraries
- PR reviews currently the main feedback loop (expensive in reviewer time)
- AI-generated code quality is a growing problem across teams

## Dependencies

- Chris having headspace (recently came off heavy delivery)
- Existing documentation being up to date before distilling into skills

## Risks

- Documentation becomes stale if not maintained alongside code
- Skills without validated content lead to worse outcomes (flagged at skills session)

## Next actions

- [ ] Complete architecture documentation pass
- [ ] Research TanStack skill generation approach
- [ ] Boil documentation down into Claude skills
- [ ] Experiment with AI-assisted PR review via GitHub Actions

## Log

### 2026-03-27

- Chris discussed approach in 1:1 — types done, architecture next
- Also wants to try quote/adjustment screen abstraction as a big Claude Code task
