---
title: Monthly Operations Automation & AI Sync (May 13)
created: 2026-05-13
updated: 2026-05-13
domain: operational-tooling
type: meeting
tags: [operational-tooling, operations, hubspot, driver-referral, automation]
---

# Monthly Operations Automation & AI Sync — May 13

**Attendees:** Tom Harvey, [[shreya-chowta|Shreya Chowta]], [[emily|Emily Staton]], [[anna|Anna Spriggs]], [[fred-bush|Fred Bush]]

Full transcript: [[2026-05-13-monthly-ops-ai-sync-transcript]]

---

## Key themes

### Shreya's new business deal creator
- Reads broker emails and presentations from HubSpot tickets; auto-populates deal fields in HubSpot
- Creates new deals or links tickets to existing ones
- Accuracy: ~50–60%; takes 20–25 minutes for 15 tickets
- Known issues: amount calculations wrong (rate logic differs between Shreya and Fred); company names occasionally truncated
- Improvement paths:
  - Dual logic: use provided rate when available, default to Fred's calculation method otherwise
  - Add sub-broker identification (wholesale vs retail)
  - Try Claude Chrome extension for process training: records exact user steps, saves as skill

### Emily and Fred's driver referral skill
- Auto-populates all ticket fields from 15+ data sources (Looker, platform, multiple systems)
- Generates detailed rationale citing specific matrix criteria
- Standardises ticket naming conventions
- Team gaining authority to process all referrals internally (no underwriting approval needed)
- Known issue: Emily's version can't download attachments despite using the same prompts as Shreya's
- Current workaround: manually download attachments first, then run the skill

### AI driving better data structure
- Created new HubSpot properties for information previously stored only in notes
- Enables proper reporting and filtering
- Reduces duplicate data entry

### Deal allocation monitoring
- Emily built automated underwriter workload tracking via Slack: prevents uneven risk distribution

### Cross-team integration — cancellations as a case study
- Ops team sees cancellations as the worst process at Flock: spans ops, underwriting, finance
- Emily meeting with Anneliese and Curtis on Friday about cancellation calculation discrepancies (£22k variance found)
- AI could help: read policy doc, identify cancellation terms, work out GWP, generate correct invoice amounts

### Looker authentication issue
- Looker connection requires daily reconnect; breaks the driver referral skill when not connected
- Action needed

---

## Actions

- [ ] Tom: Organise Finance and Underwriting AI workshops (done — May 19)
- [ ] Emily: Meeting with Anneliese and Curtis on cancellation calculations (done — May 16)
- [ ] Tom: Explore resolving Looker daily authentication issue (→ AI-082)
- [ ] Emily: Try Claude Chrome extension for deal creator process training
