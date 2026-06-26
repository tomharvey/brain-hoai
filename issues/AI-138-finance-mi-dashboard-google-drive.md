---
title: "AI-138: Finance MI dashboard — Google Drive save step + daily schedule"
created: 2026-06-24
updated: 2026-06-24
domain: operational-tooling
type: issue
status: todo
priority: medium
origin: "[[2026-06-24-david-pilley-ai-discovery]]"
tags: [david-pilley, finance, mi-dashboard, google-drive]
---

David Pilley has built a Claude skill that generates the weekly Finance MI dashboard (three Looker explores, runs in under 10 minutes). The next step is adding a save step so the HTML output automatically saves into a shared Google Drive folder for distribution.

Second phase: schedule the skill to run daily (pull previous day's data). File naming: YYYY-MM-DD format for correct sorting. Archive structure: year/month folders + always overwrite "current" file at top level.

## Actions

- [ ] David Pilley: add save-to-Google-Drive step to the MI dashboard skill
- [ ] Test end-to-end: skill runs → HTML saves to shared folder → syncs to team Macs
- [ ] Set up daily schedule for the skill
- [ ] David Pilley: present workflow at next AI Breakfast
