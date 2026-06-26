---
title: "AI discovery — David Pilley"
created: 2026-06-24
updated: 2026-06-24
domain: operational-tooling
type: meeting
tags: [david-pilley, finance, mi-dashboard, looker, html, dashboards]
---

## Attendees

- David Pilley (Finance Analyst)
- Tom Harvey

Full transcript: [[2026-06-24-david-pilley-ai-discovery-transcript]]

---

## Key themes

### Finance weekly MI dashboard — built and running

- David built a Claude skill to auto-generate the weekly MI report
- Three inputs: effective date, quarter OKRs, and month for lost renewals/new business
- Data from three Looker explores: Kirsty's FP&A explore, policy data platform, HubSpot
- Outputs: top policies, OKR tracking, new business/renewals breakdown, lost renewal buckets, connectivity data
- Skill is 99% fetch-and-layout — no significant calculations
- Runs in under 10 minutes
- Kevin Berg and Christian reviewing; Kevin wants more clickable elements and additional metrics

### Distribution options explored

- Current flow: save as HTML, manually send to Christian at ~9:30am
- Options tested in the call:
  - Google Drive Sync folder: HTML opens directly in Safari from desktop (tested live — works)
  - Slack file: opens in browser on desktop, but raw code on mobile
  - Notion page: discussed previously
- Recommended approach: add a step to the skill to save HTML into a shared Google Drive folder
- Agreed to get end-to-end working today (file drops into folder), then iterate the skill logic

### Scheduling and file management

- Plan: schedule the skill to run daily for the previous day
- Logic for renewals/new business: if in first 5 days of month, pull last month; otherwise pull current month — logic belongs in the skill, not the schedule
- File naming convention: YYYY-MM-DD (zero-padded) so files sort correctly
- Folder structure: archive by year/month; always overwrite a file named "current" at top level for quick access

### Submission mix and pricing analysis

- Separate dashboard David built for Christian and Tom
  - Tracks submission buckets, conversion rates, segment mix — YTD and current quarter views
  - One-page narrative summary with insights on where Flock may be losing ground
- Next step: add Milan's pricing model change data to the Claude folder to overlay pricing model updates on conversion rate graphs by segment

### Insight tracking as a feedback loop

- Key idea: AI-generated insights are inputs, not just outputs
  - Track how insights change week-over-week, not just underlying metrics
  - Flag when an insight is brand new vs. recurring (recurring = signal in itself)
  - Query which insights were acted on vs. ignored
- Francesco's customer transcript summaries became repetitive daily — better to surface delta and novelty
- Next week's insights should be informed by what was flagged last week

---

## Actions

- [ ] David Pilley: test HTML upload in Google Drive, add save step to skill → [[AI-138]]
- [ ] David Pilley: add Milan's pricing data to Claude folder, overlay on conversion rate graphs
- [ ] David Pilley: build insight delta tracking into daily dashboard
- [ ] David Pilley: present dashboard-sharing workflow at next AI Breakfast
