---
title: Anneliese / Thomas — AI discovery (May 11)
created: 2026-05-11
updated: 2026-05-11
domain: operational-tooling
type: meeting
tags: [operational-tooling, finance, cancellations, netsuite, ai-discovery]
---

# Anneliese / Thomas — AI discovery — May 11

**Attendees:** Tom Harvey, [[anneliese-vanwijk|Anneliese Vanwijk]]

Full transcript: [[2026-05-11-anneliese-ai-discovery-transcript]]

---

## Key themes

### Cancellations — deep dive on complexity
- Two-part process:
  1. Calculate GWP based on vehicles and time on risk (relatively straightforward; underwriting assistants handle)
  2. Invoicing reconciliation — the messy part
- Invoicing complications:
  - Zero → NetSuite transition created journal postings instead of proper invoices (now past 12-month window)
  - Invoicing structure evolved significantly; multiple legacy formats
  - Broker commission handled differently depending on payment method (GoCardless vs. BACS)
  - Old Admiral vs. New Admiral rules (pre/post October 2025): new Admiral uses month-based percentages instead of days on risk
- Volume: ~7 cancellations last month (mostly underwriters moving annual to LTA policies); will decrease post-Amazon season
- Exception handling often bigger than standard process

### Finance team AI usage
- Anneliese: uses Claude sporadically for data analysis, month-end commission posting; "too busy to have a proper play"
- Matt Dipré: heavily automated — built prompts for daily installment policy notifications, automated report generation from Looker, working on NetSuite invoice automation
- Matt wants NetSuite MCP integration → Tom flagged as potentially risky (write access, not just read)
- Ivan using Claude a lot for credit control (as confirmed separately)

### Snowflake data inconsistency
- Snowflake installments data inconsistent → manual workbook backup (Matt's system)
- Matt has a daily workbook that tells him which installment invoices to raise that morning

### Key insight: skills for recurring tasks
- Anneliese has recurring Claude chats that "know how to do things" — she just tells them "do it exactly like last time"
- Tom suggested: convert those chats to skills so any new chat can pick up the knowledge
- Anneliese receptive; plans to create the skill before next month's commission posting

### Data sources in use
- Looker (operational data)
- NetSuite (separately, no Looker integration)
- Platform/Retool (vehicle/GWP information)
- Excel/Sheets (calculations and reconciliation)

---

## Actions

- [ ] Anneliese: Create skills from existing recurring Claude chats before next month's commission posting
- [ ] Tom: Flag NetSuite MCP write-access risk to Matt Dipré (read-only is safe; full access is not) (→ AI-083)
- [ ] Tom: Link underwriting assistants with finance on cancellations process (cross-team automation)
