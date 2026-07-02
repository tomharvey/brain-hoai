---
title: Moss MCP — finance rollout check-in
created: 2026-06-29
updated: 2026-07-02
domain: operational-tooling
type: meeting
tags: [moss, mcp, finance, rollout]
---

# Moss MCP — finance rollout check-in

**Attendees:** [[kirsty|Kirsty Alexandre]], [[anneliese-vanwijk|Anneliese Vanwijk]], [[queency-gonsalves|Queency Gonsalves]], [[rob|Rob Grice]], Tom

Full transcript: [[2026-06-29-moss-finance-rollout-transcript]]

## Key themes

### Install state was worse than reported
- Moss MCP nominally "installed on 5 machines" (Christian, David Pilley, Queency, Kirsty, Anneliese, Jade) — but Queency and Anneliese were on outdated versions and Kirsty's was misconfigured. Kirsty had installed the old version on David's and Anneliese's machines assuming version didn't matter.
- Kirsty owned the miss directly: "I grossly underestimated what needed to be done here... I didn't actually understand the context of where all the issues were."
- Root causes in the old connector: wrong authentication headers and no API rate-limit handling (month-end report queries timing out). New version (`server.py`) fixes both and can fetch Christian's invoice files.

### API keys
- Users sharing API keys → 401 auth failures and MCP timeouts. Moss caps at 5 keys total. Each user needs their own.

### Live reinstalls
- Kirsty and Queency reinstalled successfully on the call from the new zip in #tech-finance.
- Anneliese blocked by a Python installation error (non-developer machine setup — same class of problem expected on Jade's and David's machines). Error log sent to Tom via Slack.

### Usage reality check
- Queency has not yet queried Moss data via Claude in real work — she feeds downloaded files in manually for approvals. Expense-type filtering (card transactions vs invoices vs reimbursements) not working correctly for her.
- Kirsty successfully querying expenses; asked to understand what's actually in the connector — wants the technical walkthrough.
- Kirsty asked whether NetSuite is connected to Claude → pointed to [[geran|Geran]].

## Actions
- [ ] Kirsty — install new Moss MCP version on Jade's, David Pilley's, and Christian's machines → [[AI-148-moss-mcp-reinstall-rollout]]
- [ ] Tom — debug Anneliese's Python installation error (log in Slack) → [[AI-149-debug-anneliese-python-install]]
- [ ] Queency — share Claude chat with Tom to surface expense-type query issues
- [ ] All — ping Tom directly when hitting Moss data query issues
