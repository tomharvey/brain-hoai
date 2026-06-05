---
title: Ollie Crowe — BDM Brain design review (meeting prep)
created: 2026-06-04
updated: 2026-06-04
domain: ai-enablement
type: inbox
tags: [bdm, shared-brain, meeting-prep, ollie-crowe]
related: adam-bdm-brain-meeting-prep
---

# Ollie Crowe — BDM Brain design review

**Format:** 60 min, 1:1 — run this after the Adam meeting
**Goal:** Walk out with Ollie's challenges to the architecture and phase plan on the table, his PM role confirmed, and a shared view of what the BDM team actually uses day-to-day.

---

## What success looks like

Ollie has seen the full design and pushed back on at least two things. You have his honest read on HubSpot data quality and Notion adoption. He has confirmed (or renegotiated) his PM role through to launch. You've agreed the shape of the pre-workshop joint session.

Not success: Ollie has nodded along to a presentation he could have read in a doc.

---

## Opening (5 min)

Start with what Adam said.

> *"I spoke to Adam. He said [X — fill in from the Adam meeting]. That's the outcome we're building toward. I want to show you the full architecture and phase plan, and I want you to challenge both — particularly on what the BDM team actually uses day-to-day versus what we think they use."*

This frames Ollie correctly: not a passive audience for a design review, but a co-owner of whether the design is right.

---

## Questions to get answered

1. **What does Ollie already know?** Start by asking what he's across — don't re-explain things he already understands. There may be more shared context than expected given his conversion bets work.
2. **How clean is HubSpot data actually?** The identity/join key problem (Account domain + Person email as keys across Notion ↔ HubSpot) is the highest unresolved risk. Ollie is closer to this than the design docs assume. Push for a real answer, not "it's probably fine."
3. **Are BDMs actually in Notion daily?** The brain writes structured knowledge to Notion and assumes the team will read and contribute through it. If Notion is aspirational rather than actual, the architecture has a problem.
4. **Which conversion bet does he think this most directly moves?** He authored the conversion bets framing. He should be able to point at the specific one — if he can't, that's a signal.
5. **Does he have PM capacity for this?** Make this explicit. What else is he carrying? Is he the right PM, and if so, what does he need from Tom to make it work?
6. **What's his read on the BDM team's appetite for contributing to a shared system?** Not just using it — writing to it. That's a different ask.

---

## What to show

Show everything. Ollie can handle the full picture.

**The roles taxonomy** — use the eight-role framework. Ask him: which of these does he think the team will reach for first? Which will take the longest to earn trust?

**The three-plane architecture** — Source-of-truth (Notion + HubSpot), Control plane (thin MCP), Derived data (AWS). One diagram, five minutes. Ask: what's his instinct on the HubSpot integration path?

**The phase plan:**
- Phase 1: brain works (clean Notion DBs, thin MCP, HubSpot read, telemetry on)
- Phase 2: brain searches well (AWS derived index if federation isn't enough)
- Phase 3: brain improves itself (self-inspection, Apprentice role)

Ask him to challenge the sequencing. Is Phase 1 the right cut? Is there something that should be earlier or later?

**The open decisions register** — walk through the six unresolved items and ask which ones he has views on. Particularly: HubSpot graduation threshold (team decision), controlled vocabularies, write workflow strictness.

**The conversion hypotheses (Adam's version)** — present what Adam confirmed and ask Ollie to stress-test them against his conversion bets framing. Does each hypothesis trace to a specific bet?

---

## What to leave open (he should own or co-own these)

- Phase sequencing — he should pressure-test it, not just accept it
- Workshop agenda — this is co-owned; agree the shape in this meeting
- Tool stack validation — does "Claude + Notion + HubSpot + email/calendar" match what BDMs actually use? He's closer to this than the design docs
- HubSpot graduation threshold — team owns this but Ollie has a view
- His PM scope and what he needs from Tom

---

## The PM role conversation

Have this explicitly. The initiative needs a named PM from here to launch. Questions to put directly:

- *"Are you the PM on this?"*
- *"What do you need from me to make that work alongside your other bets?"*
- *"What decisions are yours to make, and what needs to come to me?"*

Don't leave this implicit. Ollie being "involved" is not the same as Ollie being the PM.

---

## What you're not deciding in this meeting

- The conversion hypotheses final wording — that's Adam's (already done before this call)
- BDM team pilot membership — Adam's call
- Workshop date and attendees — agree the shape here, confirm logistics in the joint meeting
