---
title: PostHog/DOM log workflow analysis
created: 2026-03-27
updated: 2026-03-27
domain: operational-tooling
type: initiative
status: proposed
origin: proposed
owner: geran
tags: [posthog, analytics, workflow, ux-research]
---

## Summary

Use existing PostHog activity tracking and DOM event logs to understand operational workflows at scale, instead of relying on manual documentation or individual video recordings.

## Goal

AI-powered analysis of how people actually use internal tools — at scale, not one video at a time.

## Current state

- Geran conducting time/motion study with video recordings of underwriting assistants
- PostHog already tracking button clicks, input fields, DOM events
- Matt and Tom discussed: an AI reading 1,000 DOM logs gives averaged, robust answers vs one person watching a few videos
- New platform taking longer for quotes — this could diagnose why

## Dependencies

- PostHog data access and permissions
- Geran's time/motion study findings as a baseline
- Someone to build the analysis pipeline

## Risks

- Privacy concerns with recording/analysing employee workflows
- Treated as surveillance rather than improvement tool
- Data may not be granular enough to be useful

## Next actions

- [ ] Review what PostHog currently captures
- [ ] Assess feasibility of AI analysis of DOM event logs
- [ ] Connect with Geran on time/motion study findings

## Log

### 2026-03-27

- Idea emerged from Matt conversation (Mar 24)
- Geran's video study provides baseline comparison
