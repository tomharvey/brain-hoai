---
title: "Claude-native API endpoint — share and expand pattern"
created: 2026-06-12
updated: 2026-06-12
domain: engineering-workflows
type: issue
status: todo
priority: medium
origin: "[[2026-06-11-tom-jordi-weekly]]"
tags: []
---

Chris is building an API endpoint with no frontend — Claude is the sole consumer. This is a paradigm shift: design the interface for an AI, not a human. No UI, no pagination niceties, just structured data optimised for LLM consumption.

## Action

- Share the pattern with the wider engineering team via Spotlight or a short post
- Explore where else in the stack we could expose Claude-native endpoints (telemetry summaries, HubSpot read-only, underwriting data)
- Consider whether this should become a convention in the engineering playbook

## Context

Jordi surfaced this from Chris's work. The insight is that once you stop designing for humans, the interface gets simpler and the data model gets cleaner. Worth amplifying before it becomes invisible tribal knowledge.
