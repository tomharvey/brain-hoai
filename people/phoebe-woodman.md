---
title: Phoebe Woodman
created: 2026-06-04
updated: 2026-06-04
domain: ai-enablement
type: person
tags: [people-team, hr, ai-enablement]
ai_activation_stage: 3
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-24
---

# Phoebe Woodman

**Role:** People Team (HR)
**Company:** Flockcover
**Email:** phoebe.woodman@flockcover.com

## Context

Member of the People team at Flock. Key focus on company communications, Flock O'Clock (all-hands), and people operations workflows.

- Owner of the Flock O'Clock deck creation process (currently manual — copy from template, update slides, assign segments)
- Exploring AI automation for Flock O'Clock: Deck Builder skill + Google Drive + Slack connectors
- Has the Flock Deck Builder skill available and connected to Google Drive and Slack
- Attended AI Lunch & Learn workshop (2026-06-02) with Rakhee and Eraaz

## AI Activation

**Stage**: 3 — Fluency
**Confidence**: medium
**Assessed**: 2026-06-24
**Evidence**: HTML slides for June fireside chat built entirely in Claude and deployed on Netlify ("I felt like I was getting really techy"). Daily task briefings via Alar. Uses Claude for design (flyers, posters), data manipulation and summarisation. Flock O'Clock automation fully designed: Slack-based contributor flow, Claude validates against Ed's comms playbook, deck rebuilds automatically on each submission. Discovered and began exploring Claude Design tab during Jun 24 session. Still uses ChatGPT occasionally for tone/phrasing.

**Not Stage 1**: Multiple demonstrated wins — Netlify HTML slides shipped, Alar daily briefings live, data manipulation at scale. No longer prospective.
**Not Stage 2**: Live tools running (Alar), artefacts shipped (Netlify slides), iterating on output quality. Past the context-and-tools stage.
**Not Stage 4**: Not yet delegating autonomously. Flock O'Clock automation is designed but the Slack trial (→ [[AI-141]]) has not yet run end-to-end.
**To progress**: Complete Flock O'Clock Slack trial. If contributors submit and deck rebuilds automatically, that's Stage 4 territory.

## Notes

- Working on reducing manual effort in Flock O'Clock: wants contributors to go directly to a shared deck rather than emailing content
- Has been asked by Ed to ensure all slide decks go through the Deck Builder skill

## 1:1 Log

### 2026-06-24 — AI Session (Flock O'Clock automation design)

- Walked through Flock O'Clock architecture: two-column spreadsheet, Slack channel with Claude tagging contributors, deck rebuild on each submission
- Claude validates contributor content against Ed's comms playbook — removes Phoebe as the bad guy for quality feedback
- Anthropic's new Claude-in-Slack feature enabled this design (released the night before)
- Skill holds template/format logic; data lives in the spreadsheet (mail-merge analogy)
- Trial planned: Tom + Rakhee + Eraaz playing contributors → [[AI-141]]
- HTML slides for fireside chat already deployed on Netlify — first real AI artefact shipped
- Discovered Claude Design tab (bottom left of app) during this call
- See: [[2026-06-24-ai-phoebe]]
