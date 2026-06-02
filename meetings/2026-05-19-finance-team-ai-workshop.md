---
title: Finance Team AI Workshop
created: 2026-05-19
updated: 2026-05-19
domain: ai-enablement
type: meeting
tags: [finance, workshop, excel, netsuite, automation]
---

## Attendees

- [[kirsty|Kirsty Alexandre]]
- [[queency-gonsalves|Queency Gonsalves]]
- Kevin (finance — no people file)
- Ivan (finance, credit control — no people file)
- [[shreya-chowta|Shreya Chowta]] (joining towards end, underwriting assistants)

Full transcript: [[2026-05-19-finance-team-ai-workshop-transcript]]

## Key themes

### What people are already doing

- **Kevin** (Excel): No longer writes formulas manually — uses Claude Excel plugin via voice dictation. Built a skill that enforces auditable formulas (XLOOKUP over nested IFs), reconciliation checks, and a master error-tracking tab. Also used Claude Code to generate hundreds of Word docs for a share options project without hitting the "press continue" interruption.
- **Queency**: Pastes Moss transaction totals into Claude to validate reimbursement calculations. Initially cross-checked manually; now trusts results for simple arithmetic.
- **Kirsty**: Transformed a broken pod metrics Google Sheet in one afternoon. Uploaded existing sheet, extracted metrics, connected Looker data, populated ~70% automatically. Added documentation of Looker filters/fields used per metric. Now a reusable skill for quarterly updates.
- **Ivan** (credit control): Daily report that takes aging invoice data, prioritises by balance/aging, excludes direct debit policies, adds proactive funding checks for new business. Saves hours per day. Also built a broker payment behaviour dashboard (avg days late per broker).

### Process automation opportunities identified

- **NetSuite MCP** — could eliminate Ivan's manual data exports. Tom to attempt setup in the office tomorrow with a volunteer.
- **Installment management** — 25% of book on installments, ~20 manual entries per month at month-end. No visibility into upcoming installments. Opportunity for automated Slack notifications.
- **Credit control emails** — standardised broker outreach templates, HubSpot integration, automated past-due notifications.

### Principles that emerged

- Start by describing the current process to Claude ("can you help with this?"), not by assuming limitations
- Ask Claude to cite sources and explain decisions — makes output auditable, builds confidence in meetings
- Excel plugin superior to Google Sheets for serious work; use Excel, upload back to Sheets for collaboration
- Dependency risk raised: what if Claude goes down? Mitigation: where possible, have Claude produce the logic (formula, script) rather than staying in the loop for every run

## Actions

- [ ] **Tom**: Set up NetSuite MCP integration in the office tomorrow (2026-05-20) — volunteer from finance team needed
- [ ] **Finance team**: Each person describes one daily process to Claude this week and reports back with automation ideas
- [ ] **Kirsty**: Share finance AI use cases list from startup CFO group
- [ ] **Tom**: Weekly check-in with finance team to review progress

## Notes

- Kevin flagged dependency risk: "if Claude goes down for a day, productivity collapses." Good forcing function to production-ise outputs (export to HTML/Excel) rather than running Claude every time.
- Ivan's credit control report took ~1 week of iteration — but now saves hours daily. The investment pays back very quickly.
- Google Sheets has no equivalent to the Claude Excel plugin. Team consensus: use Excel for anything serious, share back to Sheets for collaboration.
- Highest Claude token user in the company appears to be someone named Christian (not in this meeting) — finance team context.
