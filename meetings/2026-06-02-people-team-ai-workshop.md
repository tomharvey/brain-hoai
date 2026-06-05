---
title: People Team AI Workshop — Lunch & Learn
created: 2026-06-02
updated: 2026-06-02
domain: ai-enablement
type: meeting
tags: [ai-enablement, people-team, workshop, flock-oclock, notion, engagement-survey]
---

# People Team AI Workshop — Lunch & Learn

**Date:** 2026-06-02 13:00 GMT+2
**Attendees:** [[phoebe-woodman]], [[jordi]], [[mima]], [[rakhee]], [[eraaz-ali]], Tom Harvey
**Full transcript:** [[2026-06-02-people-team-ai-workshop-transcript]]

---

## Key themes

### Flock O'Clock automation
- Current process: entirely manual — copy template from Drive, update slides, assign segments to contributors
- Solution path: Flock Deck Builder skill (already exists in the org) + feed in template + Slack connector to notify contributors + Google Drive connector to save
- Key tip: use Opus 4.8 model instead of Sonnet 4.6 for better deck output; switch via model dropdown
- Phoebe will start with a simple chat-based workflow before formalising into a skill
- End goal: contributors get a Slack link to the deck and add their own segment using the skill — no manual emailing

### People team task management in Notion
- Current setup: team tracker with three pillars (Performance, Engagement, Operations), individual trackers per person, linked projects — feels clunky and overwhelming
- Proposed shift: interface with Notion through Claude rather than the Notion UI
  - Claude connected to Notion already for Phoebe, Rakhee, Eraaz
  - Morning prioritisation prompt: "what should I be working on today?"
  - Daily check-in: "I've done X, what's next?"
  - Over time, Claude learns your capacity, what you deprioritise, what BAU overrides
- Eraaz's pattern (most advanced): daily optimisation view built from calendar + Notion + email; runs on co:work 3x a day — proven model to follow
- Alternative: Asana migration discussed briefly but Claude connector exists for Asana too; the bottleneck is clarity on workflow, not the tool

### Engagement survey workflow automation
- Current quarterly process: HiBob setup → reminder comms to SLT/ELT → dashboard creation → results download (2 Excel files: anonymous responses + department heatmap) → company presentation → department presentations per team → 1:1s with department heads
- HiBob MCP exists (Eraaz + Rakhee have access); only covers employee data / time off / tasks — engagement survey results not yet in MCP scope → still needs Excel download for now
- Once Excel downloaded, Claude can auto-generate company and department presentations
- Rakhee can use voice prompt to describe the workflow and ask Claude to automate it

### Company-wide AI adoption
- Ed has mandated all teams use the Deck Builder skill for presentations; scrutinising decks
- Eraaz shared his daily brief prompt (originated from People team AI breakfast) — now evolved into a full optimisation view built over weeks of iteration
- AI Workshop confirmed: **Tuesday 16 June, 11:30 AM UK time** — note: 18th June is Flock O'Clock with Henry + drinks (write-off day)

---

## Actions

- [ ] Phoebe: test Flock O'Clock automation with Deck Builder skill + existing template — [[AI-089]]
- [ ] Rakhee: sidebar on Notion workflow pain points, then implement Claude-based task management — [[AI-090]]
- [ ] Rakhee: automate engagement survey workflow (voice-prompt the process to Claude, build skill) — ready for end-June survey — [[AI-091]]
- [ ] Tom: AI Workshop June 16 confirmed — confirm logistics and send invite — [[AI-092]]
