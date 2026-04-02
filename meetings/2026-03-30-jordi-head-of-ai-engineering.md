---
title: "Tom <> Jordi: Head of AI x Engineering"
created: 2026-03-30
updated: 2026-03-30
domain: engineering-workflows
type: meeting
tags: [jordi, engineering, ai-strategy, coordination]
attendees:
  - "[[jordi|Jordi Pallares Roset]]"
---

## Context

First 1:1 since starting as Head of AI. Covering AI initiatives in engineering, Sam's CoP direction, coordination model between Tom and Jordi, and emerging themes.

## Notes

### Sam's AI Community of Practice

- Sam pitched an AI CoP, created a Slack channel, shared with [[mima|Mima]]
- Mima's feedback: "we're already doing this" — things moved fast since Sam's original pitch
- Jordi guiding Sam toward more focused goals for Q2
- Agreed direction: **evals** (the content, not the framework — e.g. what goes into prompt-foo, not prompt-foo itself) + **documentation for AI readability** (institutional knowledge that Chris hasn't covered)
- Sam struggles with execution on large undefined projects — start small, define measurable goals, expand scope after delivery
- Jordi has 1:1 with Sam Thursday to set Q2 goals
- Lunch & learn proposed: Sam presents his documentation learnings

### Engine Room ticket triage automation

- Jordi building a Lambda connected to PostHog + internal MCP to auto-triage Engine Room tickets (Linear bugs/data errors)
- Using Bedrock directly — no framework, just an MVP to validate feasibility
- Very early stage — ~2 hours of work so far
- [[mima|Mima]] identified specific use cases she thinks are easy to automate with existing data
- Not scalable yet — if validated, would move to proper framework (Chris/Ishmael's work)

### WhatsApp driver reporting bot

- [[ollie-crowe|Ollie Crowe]] built and deployed to render.com (Twilio, SQLite)
- Not customer-facing yet — crucial distinction
- Tom advised: test with 1-2 fleets via Ben, treat as experiment, don't put in front of more until validated
- If it works → engineering conversation about WhatsApp as a platform service + AI part into the kit
- Jordi confirmed in claims planning meeting it's "just a demo" — Ollie not expecting engineering resources yet

### Renewal automation (underwriting)

- Jordi working with [[anna|Anna]] to automate part of the renewal spreadsheet process
- **Blocker**: Google MCP requires local hosting — Jordi has to run it manually on calls with Anna
- Existing Claude Google connector only does Calendar; Drive connector is read-only (file list, not edit)
- Discussed workarounds: G Drive sync to local filesystem, G Scripts, questioning whether Google Sheets is the right platform
- Deeper issue: 3 different spreadsheets with different structures, Zapier workarounds connecting HubSpot — process itself may need rethinking
- Tom reviewing this tomorrow (2026-03-31)

### Skills deployment standards

- Matt asked Jordi about sharing a skill company-wide — Jordi's response: "who tested this?"
- Need to define: public vs private skills, testing/review standards before distribution
- Relates to [[skills-distribution]] initiative

### Coordination model

- Jordi's strategy: stay close to business side, ask about AI needs, discover opportunities
- Tom's role: resource for complex implementations, strategic coordination across teams
- No overlap — Jordi discovers, Tom supports and governs
- Tom's framing to everyone: "I'm not here to stop what you're doing or replace it. This role is about taking responsibility for the thing that no one's accountable for."
- Everyone enthusiastic — this is not a hard sell. Challenge is consolidation without killing momentum.

### Emerging: insights database

- Tom seeing a pattern: AI lets us get insight from data we never had time/ability to analyse
- Examples: CC data (Abs's tool), virtual imagery, HubSpot, PDFs, submissions
- Framing it as a 3-month horizon to build an "insights database"
- Distinct from the longer-term [[insight-layer]] strategic bet

### Other

- "Other Tom" interested in automating things — Jordi has catch-up in ~2 weeks
- Ollie's WhatsApp bot is an example of the spectrum: from private prompts → skills → deployed shadow prod-tech

## Decisions

- Sam to focus on evals + documentation for Q2 (not CoP leadership)
- Weekly 1:1 Tom <> Jordi on Fridays (Tom to send invite)
- Coordination model: Jordi discovers, Tom supports complex implementations

## Actions

- [ ] Tom: send Friday 1:1 calendar invite to Jordi
- [ ] Tom: review Google MCP hosting situation (2026-03-31)
- [ ] Jordi: set Sam's Q2 goals in Thursday 1:1
- [ ] Jordi: continue Engine Room triage MVP
- [ ] Ollie: test WhatsApp bot with 1-2 fleets via Ben

## Links

- Transcript: [[2026-03-30-jordi-head-of-ai-engineering|transcripts/2026-03-30-jordi-head-of-ai-engineering]]
- Related: [[agent-framework]], [[skills-distribution]], [[underwriting-assistance-ai]], [[insight-layer]], [[engine-room-triage-automation]]
