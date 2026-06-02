---
title: Fix Looker daily authentication issue for ops team
id: AI-084
created: 2026-05-13
updated: 2026-05-13
domain: operational-tooling
type: issue
status: todo
priority: medium
assignee: Tom
origin: "[[2026-05-13-monthly-ops-ai-sync]]"
tags: [looker, auth, ops, tooling]
---

## Description

The ops team (monthly ops AI sync, 2026-05-13) flagged a recurring daily Looker authentication failure. Users are having to re-authenticate every day, which creates friction and disrupts workflows that depend on Looker data.

Investigate root cause and implement a fix.

## Acceptance criteria

- [ ] Root cause identified (token expiry? session config? SSO issue?)
- [ ] Fix implemented or escalated to the right team
- [ ] Confirmed that the team is no longer hitting the daily re-auth wall

## Notes

Matt Duprey is using Looker + Claude daily for operational reporting. The auth issue adds unnecessary friction to a workflow that's already delivering value.
