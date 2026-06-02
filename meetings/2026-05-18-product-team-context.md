---
title: Product Team Context — Multiplayer AI
created: 2026-05-18
updated: 2026-05-18
domain: ai-enablement
type: meeting
tags: [multiplayer, shared-context, second-brain, product-team, ai-enablement, granola, transcript-repository]
---

## Attendees

- [[tom-harvey|Tom Harvey]]
- [[matt|Matt Price]]
- [[geran|Geran Butcher]]
- [[ollie-crowe|Ollie Crowe]]
- [[mima|Jemima Pitceathly]]

## Key themes

### The multiplayer hypothesis

Tom framed the session: everyone has built single-player AI harnesses, but the product team — who think about strategic priorities, OKRs, and stakeholder communication every day — has a natural multiplayer use case. The question: can shared team context produce value that individual second brains can't?

### AI slop — but who's the reader?

Matt surfaced the problem: the team is generating more AI content than ever, but towards different outcomes, without a clear direction. Tom's reframe: if AI is the consumer of this content, "slop" is fine — the AI reads it, not humans. The real problem is when that content needs to radiate outward to stakeholders (Emily, Ben, [[jonny-smith|Jonny]], Darren) in human-readable form, which requires a different output discipline.

### Shared strategy context gap

The team's individual second brains have deep context on their own domain but almost none on each other's. Matt added Anton's town hall company strategy slides, two-year view initiatives, and the SLT Notion roadmap to his context — and noted this is a shared asset the whole team should have. Underlying structural problem: Flock tends to restart OKRs from scratch each quarter, which makes it easy to rebuild priorities but hard to accumulate institutional memory.

### Cross-pollination blind spots

Ollie's acquisition discovery conversations with Lawrence and claims team members are gold for Geran's work, and vice versa. Mima's J transcript data is valuable to everyone. But each person prompts their own silo. The multiplayer value: when prompting the same bank of data individually, what are the blind spots? What's being missed in the Venn diagram gaps? That's where multiplayer wins.

### Product feedback pipeline needs rebuilding for the AI era

The cost of analysing transcripts is now effectively zero. Mima's self-healing approach — synthesising J pilot data (PostHog, Datadog, customer emails) into a launch decision in one prompt — demonstrated what's possible. But the existing J feedback channel (Francesco-built process) outputs urgent-sounding context that the team skims past because it lacks persistent memory of what's already known (e.g. claims servicing is being insourced — stop flagging it as novel). The rebuild direction: give the pipeline context of what the team is working on, so it surfaces only novel insight.

### Granola Enterprise API — company-wide transcripts

Mentioned as a likely route to accessing raw Granola transcripts programmatically across the company, rather than relying on individual note-taker access. Would enable a shared transcript repository. Tom flagged this as a running theme across multiple conversations.

### Sneaker-netting as the first step

Before building shared infrastructure, just share markdown files directly. Matt's GitHub repos (persona context, lines of business) already exist. Ollie added broker content. The immediate action is getting these files into each other's second brains.

## Actions

- [ ] Tom: speak to Francesco about improving the J feedback transcript pipeline — scope it for company-wide use and persistent memory of known context
- [ ] Tom: explore Granola Enterprise API for a company-wide transcript repository
- [ ] All PMs: identify 1–2 use cases that help join up the team (not localised ones) — bring to product drop-in this week
- [ ] Matt: share strategy context markdown files (Anton's town hall slides, two-year view, SLT roadmap) across the team
- [ ] Mima: share J self-healing approach/skill with the broader product team

## Notes

The clearest multiplayer win identified: a shared post-processing layer that routes relevant conversations to the right person without them having to ask. E.g. Ollie meets Lawrence → system flags it to Geran because it overlaps his work. The prerequisite is shared OKR/roadmap context so the routing has something to route *against*.

Unresolved name flags: **Francesco** (J feedback pipeline builder — no people file), **Christian** (mentioned in passing as approving expenditure — no people file), **Lawrence** (Ollie's claims contact — no people file).

Anton has no people file yet — recurring SLT figure across many meeting notes.

Full transcript: [[2026-05-18-product-team-context-transcript]]
