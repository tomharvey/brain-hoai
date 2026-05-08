---
title: "Chris Fothergill — platform AI harness + coding standards from PRs"
id: AI-031
created: 2026-05-07
updated: 2026-05-07
due: 2026-05-08
domain: engineering-workflows
type: issue
status: in-progress
priority: urgent
assignee: tom
tags: [chris-fothergill, architecture, coding-standards, pr-review, ai-harness, platform]
---

# Chris Fothergill — platform AI harness + coding standards from PRs

## Description

Two connected conversations to pick up with Chris:

### 1. Platform architecture docs for AI harnesses

Chris is working on architecture docs and skills to teach Claude the company's coding standards. Goal: make it possible for engineers to work on the core platform inside Claude Code / Cursor without producing code that doesn't fit. Need to understand: what's he built so far, what's blocking, and what he needs from Tom.

This is tracked as a Next project on the roadmap ("Platform architecture docs — Chris, size M").

### 2. Mine PR comments into a coding standards document

Chris flagged in March that AI-generated code is degrading PR quality — multiple review iterations needed. He proposed using PR reviews to teach agents. Concrete next step: mine Chris's PR review comments for recurring patterns and build a coding standards doc (or CLAUDE.md-style instructions) that agents consume at generation time.

These are two sides of the same coin: architecture docs make agents write better code upfront; PR comment patterns validate what "good" looks like from Chris's actual corrections.

## Why urgent

- AI-generated code quality is a live problem — engineers are shipping AI code now
- Chris is the person best placed to define "what good looks like" for the platform
- Feeds directly into the "AI code review in CI" Later project (which depends on architecture docs maturity)
- Last logged conversation was March 27 — overdue for a catchup

## Prep

- Review recent PRs Chris has commented on for recurring correction patterns
- Check what architecture docs / skills Chris has produced since March
- Understand his view on CLAUDE.md / cursor rules as a delivery mechanism

## Links

- [[chris]]
- [[ai-native-engineering]]
