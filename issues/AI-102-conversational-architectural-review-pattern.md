---
title: "Conversational architectural review pattern — document and share"
created: 2026-06-12
updated: 2026-06-12
domain: engineering-workflows
type: issue
status: todo
priority: medium
origin: "[[2026-06-10-ai-engineering-group-therapy]]"
tags: []
---

The engineering team has discovered that long conversational threads with Claude produce better architectural decisions than point-in-time code review. The model builds context over the conversation and can challenge assumptions in ways a one-shot prompt cannot.

## Action

- Document the pattern: what makes a good conversational architectural review (length, priming, iteration style)
- Share with Jordi and the broader team as a practice to adopt
- Consider whether this maps to existing SDLC gates (design review, RFC process)

## Context

Surfaced in AI engineering group therapy. The insight is that the value isn't in a single answer — it's in the accumulation of context across a conversation. This is different from "use AI for code review."
