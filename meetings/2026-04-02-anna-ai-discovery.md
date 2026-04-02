---
title: "Tom <> Anna: AI Discovery"
created: 2026-04-02
updated: 2026-04-02
domain: operational-tooling
type: meeting
tags: [anna, underwriting, renewals, hubspot, looker, gdrive]
attendees:
  - "[[anna|Anna Spriggs]]"
---

## Context

Discovery call with Anna (Senior Underwriting Assistant, reports to Emily). Focus on the renewals process, the spreadsheet problem Jordi flagged, and Anna's current AI usage. Key outcome: the spreadsheets should be eliminated, not automated.

## Notes

### Renewals process — now mapped

Four-step process, each step currently manual or semi-automated:

1. **Looker → PMT**: Anna downloads upcoming renewals from Looker, adds as a sheet on the Portfolio Monitoring Tool (PMT) spreadsheet
2. **PMT → Billy allocates**: Billy reviews and assigns each renewal to an underwriter (based on segment and broker relationships). Billy won't delegate this — Anna has asked.
3. **PMT → Renewals Tracker**: Anna copies relevant columns from PMT into the Renewals Tracker spreadsheet. **This is the step Jordi was automating** with Google MCP.
4. **Renewals Tracker → HubSpot**: Zapier reads a date column (6 weeks before renewal date) → auto-creates a pre-renewal ticket and deal template in HubSpot

Underwriters also use PMT for ongoing monitoring: RAG status, notes, progress tracking.

### Key insight: eliminate the spreadsheets, don't automate them

- Anna: "Ideally we would just cut out all of these unnecessary steps rather than trying to automate each step"
- The real question: **can we go straight from Looker → HubSpot?**
- This would cut out the PMT and Renewals Tracker entirely
- Would require: Billy doing allocation in HubSpot (new views needed), and Kirsty's Looker→Claude connection to understand feasibility
- Anna had a renewal pipeline in HubSpot previously — could be revived
- Jordi's Google MCP work becomes unnecessary if the spreadsheets go away

### G Drive automation — Anna's next project

- Goal: auto-create Google Drive folders and drop broker submission documents for each new deal
- Documents auto-attach to HubSpot deals but also need to be in separate G Drive folders for underwriters
- Caveats: no duplicate folders; same company from prior year = subfolder, not new folder
- Company name matching is a known problem (Ltd vs Limited vs trading names)
- Anna has experimented with Claude Computer Use ("it literally takes over your laptop — so cool")
- Tom suggested: if G Drive desktop sync is installed, Claude could create folders locally instead of needing a G Drive API

### HubSpot already connected to Claude

- Anna connected it via the connectors panel — just clicked connect, authorised via HubSpot OAuth
- Trivially easy — can walk Matt Lees through it
- This unblocks Matt Lees' Enterprise Engine HubSpot integration

### Kirsty's Looker connection

- Kirsty has connected Looker to Claude and produced visualisations (demoed at 4 o'clock session)
- Tom needs to speak to Kirsty to understand how this was done
- If Looker→Claude works, Looker→HubSpot direct flow may be feasible

### Vehicle resolution migration

- Moved VRN extraction from ChatGPT to Claude
- Claude significantly more accurate — ChatGPT randomly converted zeros to O's
- Prompt quality also improved with help from the team

## Decisions

- Direction: eliminate PMT and Renewals Tracker in favour of Looker→HubSpot direct flow
- Google MCP hosting is no longer the priority — solving the wrong problem if spreadsheets go away
- Tom to investigate Kirsty's Looker→Claude connection as the key enabler

## Actions

- [ ] Tom: speak to Kirsty to understand Looker→Claude connection
- [ ] Tom: explore Looker→HubSpot direct flow (cutting out PMT and Renewals Tracker)
- [ ] Tom: if viable, assess what changes Billy's allocation workflow needs (PMT→HubSpot views)
- [ ] Tom: help Matt Lees connect HubSpot to Claude (Anna can walk through if needed)
- [ ] Tom: follow up with Anna on G Drive folder automation progress
- [ ] Anna: continue building G Drive automation workflow in Claude
- [ ] Anna: flag other manual processes that could be retired (not just automated)

## Links

- Transcript: [[2026-04-02-anna-ai-discovery|transcripts/2026-04-02-anna-ai-discovery]]
- Related: [[underwriting-assistance-ai]], [[insight-layer]], [[process-documentation]]
- Prep: `inbox/anna-call-prep.md`
