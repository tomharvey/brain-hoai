---
title: AI-assisted code review
created: 2026-03-27
updated: 2026-03-27
domain: engineering-workflows
type: initiative
status: proposed
origin: proposed
owner: chris
tags: [code-review, github-actions, quality, automation]
---

## Summary

Use Claude in GitHub Actions to review PRs against company coding standards. Catches issues before human reviewers spend time on them. Complements the platform architecture documentation initiative.

## Goal

Reduce reviewer burden by catching standard violations (test placement, patterns, style) automatically. Non-blocking PR comments, not gatekeeping.

## Current state

- Not started — discussed in Chris AI conversation
- Chris spending significant review time on AI-generated code that doesn't meet standards
- Performance testing already running on PRs (42-second automated tests, non-blocking comments for 30%+ degradation)
- Pattern exists to build on

## Dependencies

- Platform architecture documentation (initiative) — needs standards documented before they can be enforced
- GitHub Actions infrastructure
- Claude API access in CI

## Risks

- AI reviewer gives bad advice, undermining trust
- Becomes annoying noise if not well-calibrated

## Next actions

- [ ] Wait for architecture docs to mature
- [ ] Prototype with one repo using existing performance test pattern
- [ ] Non-blocking comments only — advisory, not gatekeeping

## Log

### 2026-03-27

- Chris discussed in 1:1 — sees it as natural extension of documentation work
