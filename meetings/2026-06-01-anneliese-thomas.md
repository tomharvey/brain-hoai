---
title: "Anneliese / Thomas — Claude setup & MOSS integration"
created: 2026-06-01
updated: 2026-06-01
domain: operational-tooling
type: meeting
tags: [finance, moss, api-integration, claude-setup, month-end, connectors]
---

# Anneliese / Thomas — Claude setup & MOSS integration

**Date**: 2026-06-01 11:45  
**Attendees**: [[tom-harvey]], [[anneliese-vanwijk]]

Full transcript: [[2026-06-01-anneliese-thomas-transcript]]

---

## Key themes

### Claude connector setup — finance tech day prep

Walked Anneliese through connecting Claude to the tools her team will use at the finance tech day tomorrow:

- **Notion** (Flock workspace)
- **Slack**
- **Granola** (for recording the tech day sessions themselves)
- **Looker** (for direct database queries — Anneliese keen on this)
- **Flock custom connector** (telemetry + platform data: renewals, policy queries)
- **Gmail, Google Drive, Google Calendar**
- HubSpot skipped — minimal usage for Anneliese

### MOSS integration — the primary goal

Anneliese's main AI ambition: automate month-end consistency checking in MOSS. Current process is time-consuming and error-prone.

Use cases:
1. **Invoice coding consistency** — same subscription coded to same category/cost centre every month. Staff sometimes vary (e.g. "platform costs" vs "subscriptions"), polluting budget data per cost centre.
2. **Recurring invoice pattern detection** — MOSS has 12+ months of history. Identify invoices that always appear; flag if missing. Primary case: contractor invoices (often late). "We should always have a TomVey invoice every month — if we don't, why?"
3. **Missing accruals** — invoices in-flight at month-end that need accruing but haven't been submitted yet.

MOSS API keys generated today (secret key + public key). API docs: https://developers.getmoss.com/  
Access to be shared with [[queency-gonsalves|Queency]] only (only two on the team who use MOSS).

Tom agreed to build the integration. See [[AI-069]].

### AI job security — finance team framing

Anneliese flagged that junior team members are nervous about displacement. Agreed framing:
- Claude handles **processes**; humans handle **analysis and decision-making**
- Job is to achieve the **outcome**, not perform the process
- Relevant given bonuses will be attached to outcomes in future

### Finance tech day (tomorrow, 2026-06-02)

- Dedicated AI time for the finance team — Anneliese leading
- Plan: start with everyone describing their job role (to Claude / to each other via Granola)
- Context: Anneliese herself noted "I don't even know what my job is" — framing job objectives first is the right anchor

---

## Actions

- [ ] **Tom** — Build MOSS API wrapper and month-end consistency checker skill → [[AI-069]]
- [ ] **Anneliese** — Lead finance tech day with job-role clarification exercise as opening
- [ ] **Anneliese** — Share MOSS API access with Queency only
