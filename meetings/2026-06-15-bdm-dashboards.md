---
title: BDM Dashboards — shared brain architecture + workshop prep
created: 2026-06-15
updated: 2026-06-15
domain: ai-enablement
type: meeting
tags: [bdm, shared-brain, cowork, workshop, google-drive]
---

# BDM Dashboards — shared brain architecture + workshop prep

**Date:** Mon 15 Jun 2026, 11:00  
**Attendees:** [[adam-smith]], [[ollie-crowe]], Tom Harvey

Full transcript: [[2026-06-15-bdm-dashboards-transcript]]

---

## Key themes

### Ollie's file structure architecture

Ollie walked through the BDM brain design he has running with his engineering team. Core architecture:

- **Google Drive file sync** — markdown file structure synced via Google Drive desktop client. Every BDM's machine stays in sync automatically.
- **Co:work as the interface** — team accesses the brain through co:work, not Notion.
- **Resolver file** — routes prompts to the right skill automatically. Team doesn't need to think about which prompt to use.
- **Scheduled syncs** — e.g. weekly Granola sync that filters to distribution-relevant meetings only.
- **Shared definitions** — dashboard templates and metric definitions stored in the brain to enforce consistency across Alex, Jake, and others who currently run separate misaligned dashboards.
- **Playbook input** — strategy (e.g. "focus on accelerator brokers") fed in to drive daily outputs.

This is a different architecture from the Notion-based Phase 1 design in `reference/shared-brain/cowork-implementation.md`. Tom hadn't yet tested Ollie's file structure (shared Friday Jun 13) — needs testing before Wednesday.

### Three roles

Adam immediately mapped use cases to roles:
- **Librarian** — auto-files Granola transcripts, updates HubSpot notes, updates broker data
- **Secretary** — plans next actions, surfaces work stack, runs the "J dashboard" view
- **Coach** — replicates manager-style guidance for difficult situations

### Identify → diagnose → act framework (Ollie)

- **Identify** — heavy AI, low team involvement
- **Diagnose** — back-and-forth with the tool
- **Act** — team uses AI to produce the output, then executes

Team is responsible for how they use outputs. Tom and Ollie here to support, not prescribe.

### Risk: over-building dashboards

Strong agreement on building only what you have pain for right now. Matt's 9-agent story as cautionary tale (to be used in tomorrow's workshop). Sophie example: risk that she spends so much time in the dashboard looking at data she never looked at before, and stops doing her day-to-day job.

> "95% of a fully-generated dashboard often goes unused and gets in the way." — Adam

### Anton's point

Anton's framing: the underlying dataset should be malleable so individuals can build their own views on top of it. Start narrow: agree **one metric** for v1 (e.g. dormant brokers or accelerator broker growth) rather than chasing everything.

### Scale context

2 BDMs plus Adam across 356 brokers, plus dormant offices on top. Not manageable without tooling. The goal in 2-3 months: team manages panel twice as efficiently with high contact points and prioritised action.

### Workshop Wednesday Jun 18

Goal: team installs the brain, experiments with building their own skills, co-creates the dashboard template with definitions. Tom and Ollie here to support use-case generation, not prescribe it.

New BDM starts 21 Jul — aim to have the system meaningful by then.

---

## Actions

- [ ] **Tom** — Test Ollie's shared file structure before Wednesday workshop
- [ ] **Tom** — Get Google Drive synced on BDM team computers ahead of session (send instructions)
- [ ] **Ollie** — Write straightforward setup instructions for the team
- [ ] **Wednesday goal** — Team installs brain, experiments with skills, co-creates dashboard template with metric definitions
