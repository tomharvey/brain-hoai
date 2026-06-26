---
title: "NetSuite MCP — Tom / Ivan"
created: 2026-06-25
updated: 2026-06-25
domain: operational-tooling
type: meeting
tags: [finance, netsuite, mcp, automation, credit-control, dashboards]
---

## Attendees

- Ivan Boix (Finance, Flockcover)
- Tom Harvey

Full transcript: [[2026-06-25-netsuite-mcp-ivan-transcript]]

---

## Key themes

### Current workflow — daily priorities report

- Ivan downloads XLS from NetSuite manually each morning, drags it into an incoming folder
- Claude runs the daily priorities report from that data, nudges Ivan on Slack by 9:15 if data isn't in
- Admiral report runs on Thursdays, same manual download process
- Report output (Word file) covers:
  - Movements since previous day, payments, new items
  - Top 5 credit control actions by age and balance size
  - Full overdue list organised by priority
  - Balances over £10k with funding dates
  - Policies on installments, cancelled policies with CCI, smaller balances

### NetSuite MCP — automating the manual step

- Goal: remove Ivan's manual download and folder-drag step entirely
- Ivan tested an overdue invoices query (60+ days) — looked plausible
- Plan: point Claude at the incoming folder files, describe the current UI workflow, ask MCP to replicate the data pull automatically
- Tom suggested keeping the download step initially so Ivan can verify correctness, then remove it in a later iteration
- Model choice: switch to Opus 4 (not Sonnet 4.6) for this task given its complexity

### Broker payment behaviour dashboard

- Ivan built an HTML dashboard tracking broker payment behaviour from NetSuite CSV exports
  - Compares invoice due dates vs. actual payment dates
  - Calculates per-broker average lateness, broken down by month
  - Includes AI-generated summary and analysis of largest accounts
- Data pull for this could also be automated via MCP
- Still in progress, room for improvement noted

### End-to-end automation vision

- If data pull is fully automated, the whole report pipeline could run in the cloud unattended
  - Daily briefing sent to Ivan (or a Slack channel) even when he's on holiday
  - Team could pick it up without Ivan needing to be present
- Ivan has an existing Claude skill for the report; plan is to extend it with the new automated data step
- Potential future area: month-end automation (booking commission income journals and bad debt operations)

---

## Actions

- [ ] Ivan Boix: automate NetSuite data pull via MCP and update the daily report skill — remove manual download step; extend existing Claude skill to run end-to-end → [[AI-145]]
- [ ] Ivan Boix: catch up next week to review progress — demo how far he's got with the MCP automation
