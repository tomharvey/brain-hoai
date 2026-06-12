---
title: "AI Strategy — Tom + Geran"
created: 2026-06-10
updated: 2026-06-10
domain: ai-enablement
type: meeting
tags: [geran, ai-enablement, finance, underwriting-assistance, okrs, resourcing, data-access, bdm, operational-tooling]
---

# AI Strategy — Tom + Geran

**Date:** 2026-06-10
**Attendees:** [[geran]], Tom

_Note: this meeting was recorded as part of a single Granola session titled "Ai" (ID: c132142b). The session contained two back-to-back conversations; this is Meeting 2. Meeting 1 is [[2026-06-10-ai-engineering-group-therapy]]._

Full transcript: [[2026-06-10-ai-strategy-geran-transcript]]

---

## Key themes

### AI bubble and the finance lens

Geran frames AI from a finance perspective: when does Anthropic charge what it actually costs them, and can anyone afford that rate? Investment into LLM models vs. market cap doesn't add up. Usage pullback risk is real — companies are already seeing it.

[[javier]] (installments) is the clearest current example of trying to extract measurable ROI: higher engagement with AI vs. without it. Token cost return still unclear long-term.

### Skills vs. automation — the current stance is shifting

Company currently building capability in people first, not dropping automation on them. That is starting to shift over the next 6–8 months toward "give people the tools." Tom's view: deeply unconvinced that delivering a skill to someone (e.g. [[shreya-chowta]]) creates the output. Shreya building the skill with a capital S does. Large-scale AI automation dumped on people doesn't land — they need to be taken on a journey.

How many people have actually used the Members Presentation Skill vs. created presentations in the last two months? Under 10%.

### Finance team vs. Ops — brittle vs. resilient

- **Finance**: brittle, unintentionally operational, no cross-skilling. Macd (installments — see name flags) has pulled far ahead on AI capability; the rest of the team can only do a diminished version of the role when someone is off. Jay frames the problem as "the platform is bad" rather than surfacing the underlying team fragility.
- **Ops/EM team ([[emily]])**: can hot-swap. Emily can drop into quotes and support tickets. Built-in flex. Better positioned to absorb burning.
- Finance will crash at some point. Fergus's focus at SLT: underwriting assistance, finance, and the engineering team are all under rising temperature.

### Data access as the real unlock

Driver referral example: Claude could pull policy data, check referral limits, and process it, with the human clicking the final button. Requires endorsements and policy state on the new platform — limited to new policies for now.

Core blocker across all of this: data access and a coherent data model. "Fix the data" is what unlocks agentic enablement for operational teams. Platform migration is the precursor — most of this becomes viable in the 6–9 month view.

Chris exploring API endpoints (the Claude-native pattern: see [[AI-098]]). Not yet a priority, won't be fast.

### Resourcing — mechanics, architects, and the PM/engineer ratio

Geran's current posture: build Streamlit apps as a defensive shield — protecting engineers from context-switching until resourcing improves.

Industry hypothesis: ratio shifting from 1 PM to 3 engineers → 3 PMs to 1 engineer. Tom's pushback: engineers orchestrating 20 agents on 20 tickets in parallel is a fast track to burnout. Typing was never the bottleneck — clear direction from leadership is what's holding teams back.

**Mechanic analogy**: don't ask [[fred-bush]] to be a systems builder or architect — ask him to be a mechanic. Tom's role: teach the mechanic skills. Geran's role: define the system and help the team think about it. Together they unlock the operational teams to self-maintain.

Three buckets for unlocking operational teams:
1. Pull one engineer to build AI-enabling infrastructure (Chris on API endpoints — rare, slow)
2. Geran builds with AI (Streamlits, skills, workflows) — effectively 1PM to 3.5 engineers
3. Treat operational team (underwriting assistance, finance) as 0.25-engineer contributors — teach them to be mechanics, with Tom + Geran providing architectural and product support

### Underwriting assistance and BDM enablement

- BDMs: hundreds of leads, same task repeated, relationship-driven. [[rob]] and Tom Harvey working on submissions within the protect bubble. Ollie keen to spend time with BDMs on AI conversion tools. Tom keen too. Right for the librarian/secretary/coach model. → [[AI-101]], [[initiatives/bdm-ai-multiplayer]]
- Underwriting assistants: dozens of varied small tasks (cancellations, driver referrals, endorsements), each requiring different judgment. More agent-shaped but requires data access.
- [[emily]]'s team: more judgment-heavy than finance, less clearly mapped to automation. No equivalent of [[jade-mounir]]'s wish list for underwriting assistance yet. → [[AI-105]]

### OKRs and making AI enablement explicit

Q3 OKRs being agreed at SLT offsite; Q4 set provisionally. Geran wants AI's role made an explicit priority at SLT level — not just "figure it out on a whim." Platform migration is well-articulated; AI enablement layer is not.

Tom: will push to make this more concrete next quarter. Not a conversation yet had with Fergus or Ed. Fergus needs to be the person who tells [[emily]] and Anton that "yes, AI will fix this, but here is how" — not just the fairy-tale version. → [[AI-106]]

---

## Actions

- [ ] **Tom**: explore Claude-native API endpoint pattern with Chris; share Matt's endpoint in Flock Launches → [[AI-098]]
- [ ] **Geran + Tom**: identify and document underwriting assistance task inventory for AI suitability (equivalent to Jade's finance wish list) → [[AI-105]]
- [ ] **Tom**: shape SLT framing — AI enablement as explicit Q3/Q4 OKR priority, separate from platform migration → [[AI-106]]
- [ ] **Tom + Geran**: align on mechanic-enablement model for operational teams (underwriting assistance, finance)

---

## Name flags

- **Macd** — finance team, installments, pulled far ahead on AI capability. No people file. Confirm identity.
- **Anton** — appears in multiple meetings as a product/roadmap stakeholder. No people file. Confirm identity.
- **Christian** — male, Finance/SLT-adjacent, built HTML budget analysis co:work project post-Admiral close. Also flagged in [[2026-06-11-fergus-tom-weekly]]. No people file. Confirm identity.
