---
title: "Tom <> Milan: AI Discovery"
created: 2026-05-11
updated: 2026-05-11
domain: ai-enablement
type: meeting
tags: [ai-discovery, pricing, shared-skills, google-drive, cowork]
---

# Tom <> Milan: AI Discovery

**Date**: 2026-05-11 11:00
**Attendees**: [[tom-harvey]], [[milan-chavda]]

Full transcript: [[2026-05-11-milan-ai-discovery-transcript]]

---

## Key themes

### Team AI readiness

- Pricing team is pro-AI and keen to do more — held a whiteboard session ~1-2 months ago mapping all pricing activities and identifying AI automation opportunities
- Milan prioritising headspace for [[javier]] (Harvey in transcript) and Francesco by keeping their days light — [[javier]] attended AI breakfast last Friday and has been exploring agent capabilities
- Milan himself is in the "too busy to save time" camp — using Claude Cowork for ad hoc analysis (e.g. Admiral data request report), and using AI for analytical tasks similar to how Darren works
- Team is mostly single-player; Darren's AI usage is entirely opaque to the team

### Skills fragmentation — the classic pattern

- Francesco built a triangle analysis skill; Milan built a similar actuarial analysis skill — independently, with overlap
- Realised they need one consolidated skill per component and a single place to store them
- Attempted GitHub → failed (not GitHub-comfortable); switched to Google Drive shared folder → worked but got cluttered with AI output files

### Google Drive is the right path

- Tom's recommendation: lean into Google Drive (not GitHub)
  - The team already has Google Drive File Stream and an established pricing folder structure
  - Git version control overhead not worth the gain for a non-engineering team
  - Fix for file clutter: put a `claude.md` at the top level instructing the agent to write outputs to an `outputs/` subfolder
  - Google Drive has versioning — not as first-class as Git but sufficient
- Key insight: shared team Google Drive folder + AI working inside it = a second brain for the whole team. Not a calendar/notes brain — a data analysis brain.
- Milan's existing folder structure (`insurance/pricing/`) already has all the material; just needs AI context layer on top

### Shared context and the AI personal OS link

- Milan attended the AI breakfast personal OS session — hadn't connected it to their own Google Drive setup
- Tom's framing: "you've already got a team shared folder with years of context. Drop an AI in the middle of it and it becomes a second brain for the team — doing data analysis, not just taking meeting notes"
- Milan's setup (cowork pointed at pricing folder) is essentially this already — just needs structure and instruction layer

### Next steps

- Francesco back next week — schedule a follow-up team workshop with Tom invited
- Tom to announce the co-work workshop this week
- Milan to send Tom the pricing whiteboard (identified top automation targets, claims triangle building was the headline one)

---

## Actions

- [ ] **Milan**: Send Tom the pricing team AI whiteboard notes
- [ ] **Tom**: Announce co-work workshop this week
- [ ] **Tom + Milan**: Schedule follow-up pricing team AI session (invite Tom) — wait for Francesco to return next week
- [ ] **Milan**: Add a `claude.md` to the shared pricing Google Drive folder with output-folder instruction to keep workspace clean
