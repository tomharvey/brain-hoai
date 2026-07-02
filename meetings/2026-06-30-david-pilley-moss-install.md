---
title: David Pilley — Moss MCP install
created: 2026-06-30
updated: 2026-07-02
domain: operational-tooling
type: meeting
tags: [moss, mcp, finance, install]
---

# David Pilley — Moss MCP install

**Attendees:** [[david-pilley|David Pilley]], Tom

Full transcript: [[2026-06-30-david-pilley-moss-install-transcript]]

## Key themes

- Follow-up from [[2026-06-29-moss-finance-rollout]] — David's machine had the old partial install from Kirsty, and the update had failed.
- Root cause: no Python installed (same non-developer-machine class of problem as Anneliese). Installed Python 3.13, ran shell-profile update and certificates commands, then `bash install.sh` completed.
- Cleaned up the broken Moss entry in his Claude desktop config, pasted the correct command/args, relaunched.
- Live test query ("show me the five most recent expenses in Moss") worked; David confirmed the server visible in Claude settings.
- Context: David is doing Looker data-reconciliation work day-to-day; needed guiding through every terminal step (dock, TextEdit, cd, command history).

## Actions
- [ ] David — validate Moss end-to-end with real expense queries in daily use
