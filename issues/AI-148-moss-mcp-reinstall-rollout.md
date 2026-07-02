---
title: Roll out new Moss MCP version to Jade, David Pilley, Christian
created: 2026-07-02
updated: 2026-07-02
domain: operational-tooling
type: issue
status: in-progress
priority: high
due: 2026-07-06
origin: "[[2026-06-29-moss-finance-rollout]]"
tags: [moss, mcp, finance]
---

# Roll out new Moss MCP version to Jade, David Pilley, Christian

**Owner:** [[kirsty|Kirsty Alexandre]]

Old Moss MCP installs (wrong auth headers, no rate-limit handling) caused 401s and month-end timeouts. Kirsty and Queency reinstalled live on the Jun 29 call; remaining machines: Jade, David Pilley, Christian. Each user needs their own API key (Moss caps at 5).

- David Pilley done 2026-06-30 with Tom (Python install was the blocker — see [[2026-06-30-david-pilley-moss-install]]).
- Queency to share her Claude chat with Tom to surface expense-type filtering issues.
- Expect Python-not-installed failures on non-developer machines (see [[AI-149-debug-anneliese-python-install]]).
