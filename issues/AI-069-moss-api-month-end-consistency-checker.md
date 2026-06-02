---
title: "AI-069: Build MOSS API month-end consistency checker skill"
created: 2026-06-01
updated: 2026-06-01
domain: operational-tooling
type: issue
status: in-progress
priority: high
due: 2026-06-02
origin: "[[2026-06-01-anneliese-thomas]]"
tags: [moss, api, finance, month-end, automation, skill]
---

# AI-069: Build MOSS API month-end consistency checker skill

## Context

[[anneliese-vanwijk|Anneliese]] wants to automate her month-end MOSS review. Currently this is a manual, time-consuming process. MOSS API keys have been generated (secret key + public key, held by Anneliese). Finance tech day is tomorrow — Tom committed to building this.

API docs: https://developers.getmoss.com/

## Requirements

1. **Invoice coding consistency** — identify cases where the same merchant/subscription has been coded to different categories or cost centres across months. Flag discrepancies.
2. **Recurring invoice detection** — build a pattern from 12+ months of history. Identify vendors that appear every month. Flag any that are missing in the current month.
3. **Unapproved recurring transactions** — identify recurring transactions not yet in approval status at month-end (potential accruals needed).
4. **Report output** — produce a clean, human-readable summary Anneliese can act on directly.

## Deliverable

A skill at `.claude/skills/moss-month-end/` containing:
- A Python script that connects to the MOSS API and runs the checks
- A skill markdown file describing how to use it and configure credentials
- Credentials via environment variables (`MOSS_API_SECRET_KEY`, `MOSS_API_PUBLIC_KEY`)

## Notes

- Access shared with Queency only (the two MOSS users on finance team)
- The pattern-detection approach relies on MOSS history (12+ months available)
- Should be distributable — other finance teams could use this with their own API keys
