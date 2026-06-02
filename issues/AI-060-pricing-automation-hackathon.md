---
title: "AI-060: Schedule Francesco + Javier pricing automation hackathon"
created: 2026-05-19
updated: 2026-05-19
domain: ai-enablement
type: issue
status: todo
priority: medium
origin: "[[2026-05-19-francesco-ai-catchup]]"
tags: [francesco, javier, pricing, hackathon, feature-discovery]
---

## Summary

[[francesco-venerandi|Francesco]] and [[javier|Javier]] plan a 2-day in-office hackathon to accelerate pricing automation work. Needs scheduling. Goal: unblock the pricing data extraction problem and prototype AI-driven feature discovery.

## Context

The pricing team has two long-running blockers:
1. **Pricing model inputs not saved** — the JSON sent to the pricing service is constructed from 20–30 tables but never persisted. Francesco and Ollie are working with Ollie's team to fix this properly, but Tom suggested an alternative: use Claude Code to find where the JSON is assembled in the repo and write a script to also save it. Could be done in a day.
2. **Feature discovery bottleneck** — once data is accessible, the vision is an AI system that autonomously discovers candidate features from telemetry data and runs them through the GLM. This is the "building AI" work Francesco wants to do.

The hackathon is the forcing function to get both done.

## Actions

- [ ] **Francesco + Javier**: Agree dates for 2-day hackathon
- [ ] **Francesco**: Research pricing data extraction requirements this week (pre-hackathon)
- [ ] **Tom**: Optionally support with architectural direction on the feature discovery agent design

## Notes

- Tom's framing: this isn't just faster — it's a million-times-a-day capability. The bottleneck shifts from Francesco's time to compute cost.
- Francesco is nervous about touching live pricing infra — the hackathon approach (with Javier present) addresses this.
- See also the broader feature discovery initiative conversation from 2026-04-16: [[2026-04-16-fergus-tom-weekly]]
