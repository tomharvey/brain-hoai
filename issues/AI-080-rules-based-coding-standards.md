---
title: Rules-based coding standards approach (individual rule files, skills from PRs)
id: AI-080
created: 2026-05-14
updated: 2026-05-14
domain: engineering-workflows
type: issue
status: todo
priority: medium
assignee: Tom
origin: "[[2026-05-14-rob-hubspot-pipeline]]"
tags: [engineering, standards, rules, pr-review, claude-code]
---

## Description

Rob's HubSpot ETL PR raised the question of how coding standards get communicated when someone (human or AI) writes code without full context on Flock's conventions. The proposed approach: a `rules/` folder in the repo where each file is a single discrete rule, written in plain English, linked to the PR comments that established it.

This allows:
- Claude Code to load relevant rules when generating code
- New engineers (and AI) to understand the reasoning behind each rule
- PR review to generate new rules when recurring patterns are spotted

## Acceptance criteria

- [ ] Proposal written up and shared with Rob / Jordi / Chris for feedback
- [ ] Decision on where `rules/` lives (per-repo vs shared repo)
- [ ] First 3–5 rules drafted based on the most common PR feedback patterns
- [ ] Claude Code CLAUDE.md updated to reference the rules folder
- [ ] Process documented: how does a PR comment become a rule?

## Notes

Rob arrived at this pattern independently while learning Flock coding conventions via Claude during the HubSpot pipeline work. The fact that an external contractor reached for this instinctively is a good signal that the need is real.

The rules should be terse and actionable — not a style guide, but opinionated defaults. e.g. "Use vitest, not jest" or "All API responses wrapped in Result<T, E>".
