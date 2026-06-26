---
title: "AI discovery — Matt Lees"
created: 2026-06-24
updated: 2026-06-24
domain: ai-enablement
type: meeting
tags: [matt-lees, distribution, enterprise, chief-of-staff, bdm-brain, dashboards]
---

## Attendees

- [[matt-lees]] (Matthew Lees, Enterprise Fleet Lead)
- Tom Harvey

Full transcript: [[2026-06-24-matt-lees-ai-discovery-transcript]]

---

## Key themes

### Chief of Staff folder → team Brain

- All deal context currently in markdown files inside the Chief of Staff folder
- Goal: build an Enterprise prospecting pipeline tool accessible to Adam, with a dashboard and HubSpot push (like Jake's setup)
- Decision: move Chief of Staff folder into the team Brain space
  - No sensitive content blocking this (strategic notes about colleagues: keep in personal space)
  - Use Claude to migrate and reorganise into a sensible folder structure

### Working across two folders in Claude

- Workaround: click "work in folder" and select both folders rather than a single project
- Add global instructions in Claude settings defining each folder's purpose
  - e.g. "This folder is personal, this one is shared with the team. Make good decisions about where to save output."
- Matthew to experiment with this setup

### Apollo integration for prospecting

- Currently doing manual web search in Claude, then manually searching Prospero for contacts
- Apollo not returning results for Matthew
- Tom has been using Apollo via Claude Code — wrote a tool against the Apollo API directly; could potentially ship a shared tool for the BDM team
- LinkedIn access remains a blocker: can't access meaningfully without Chrome extension (risks account bans)

### Claude Desktop issues

- Getting VM errors; also blocking slide deck updates
- Suggested fixes: turn off memory and connector discovery in Settings; fully uninstall (including VM) and reinstall
- Update available: Matthew to install alongside settings change

### HTML dashboards and artifact sharing

- David Pilley has skills that generate HTML dashboards and needs a place to save them
- Proposal: create a Dashboards folder in Google Drive (with sync enabled)
  - Skills save artifacts directly into the folder; syncs to everyone's Mac
- Matthew's immediate use case: surface BDM pipeline status as an artifact-style dashboard for the wider team

---

## Actions

- [ ] [[matt-lees]]: move Chief of Staff folder into team Brain space; use Claude to reorganise
- [ ] [[matt-lees]]: set up dual-folder working with global instructions in Claude settings
- [ ] [[matt-lees]]: fix Claude Desktop by disabling memory, installing update, reinstalling if needed
- [ ] Tom: create shared Dashboards folder in Google Drive for HTML artifacts → [[AI-139]]
