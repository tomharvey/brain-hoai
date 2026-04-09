---
title: "Matt Lees: Enterprise Engine Review 002"
created: 2026-04-07
updated: 2026-04-07
domain: operational-tooling
type: meeting
tags: [matt-lees, enterprise-engine, hubspot, agents, distribution]
attendees:
  - "[[matt-lees|Matt Lees]]"
---

## Context

Second call with Matt Lees on the Enterprise Engine. 15 min review covering pipeline status post-weekend, HubSpot integration progress, dashboard direction, and Claude best practices. Follow-up to the Thursday call with Fergus.

## Notes

### Pipeline status

- **Scheduling issue**: scheduled tasks trigger on first login when laptop is asleep, not at the set time. Needs sleep mode disabled or scheduling tweaked.
- **Pre-loaded target list**: Matt fed Claude a list of target fleets from a manual exercise 12 months ago, skipping the business search step. Goes straight to contact enrichment for known targets.
  - Tom's input: don't recalculate things that don't change day-to-day. Faster and more reliable, separate concern from token optimisation.
- **Phasing**: once ~80% of target market is mapped, pause enrichment and focus on churning existing contacts. Estimated 2 weeks max for the mapping phase.

### HubSpot integration — live

- **Emily got HubSpot connected this morning** — was the enabler
- Initial prompt: read-only, validate previous client comms, surface key headlines, check contact details on daily schedule. Working as expected.
- **Read-only for now** — will test write permissions incrementally
  - First test: create a company record update for emails sent
- **Data structure question**: Matt's instinct is to attach AI-generated data to **company records**, not deal records (underwriting team works on deal properties — don't want overlap with BAU)
- Matt to align with [[emily|Emily]] and [[adam-smith|Adam]] on where data lives
- **This resolves AI-005** — Matt is doing the assessment himself, in dialogue with Emily and Adam who own the HubSpot clean-up

### Dashboard / front-end direction

- Lovable front-end paused since Thu/Fri — Matt revisiting this afternoon
- **Reconsidering its purpose**: Claude is already surfacing next 10 actions conversationally — may reduce need for separate front-end
- If HubSpot holds contact/engagement data, a HubSpot dashboard may be simpler
- Could still build custom visualisation on top, pulling from HubSpot + other sources
- Tom to ask Kirsty tomorrow how Looker fits with HubSpot data

### Claude best practices (discussed)

- **Push Claude to write files** rather than rely on memory — more transparent, easier to audit
- **End-of-session ritual**: ask Claude to encode priorities and context as files for next session
  - "What's the best file structure to remember this prioritisation? Encode this as instructions for yourself."
- **Explain the why** when giving priorities — e.g. "maximum outreach right now, don't chase 3-day-old emails"
- **Backup**: Cowork files live locally on laptop. Tom to send link to Google Drive for Desktop sync — Cowork folder syncs to Drive automatically, two-way backup.

### Adjacent opportunity

- **Adam interested in replicating** the agent workflow for broker contacts
- Tom: prove HubSpot interaction first with the Enterprise Engine, then duplicate the pattern

## Decisions

- HubSpot data goes on **company records**, not deal records (avoids underwriting team overlap)
- Matt to lead the conversation with Emily and Adam on data structure
- Front-end dashboard direction: shift toward HubSpot-native if data lives there

## Actions

- [ ] Matt: fix scheduled task / disable sleep mode so pipeline runs at correct time
- [ ] Matt: test HubSpot write permissions — create company record update for sent emails
- [ ] Matt: speak with Emily and Adam to agree HubSpot data structure (company vs deal)
- [ ] Matt: back up Cowork files to Google Drive (2x per week)
- [ ] Matt: set up Google Drive for Desktop to sync Cowork folder automatically
- [ ] Matt: resume Lovable front-end testing this afternoon with JSON files
- [ ] Matt: explore replicating agent workflow for Adam (broker contacts) — pending HubSpot proof
- [ ] Tom: speak with Kirsty tomorrow — clarify how Looker integrates with HubSpot data
- [ ] Tom: send Matt link to install Google Drive for Desktop

## Links

- Previous call: [[2026-04-02-matt-lees-enterprise-engine]]
- Related: [[agent-framework]], [[matt-lees]], [[AI-005-hubspot-enterprise-engine]]
