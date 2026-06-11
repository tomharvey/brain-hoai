---
title: Adam / Thomas — BDM Team AI
created: 2026-06-10
updated: 2026-06-10
domain: ai-enablement
type: meeting
tags: [distribution, bdm, hubspot, trading-pack, broker-pulse, toolkit, coaching, ai-enablement]
---

# Adam / Thomas — BDM Team AI

**Date:** 2026-06-10
**Attendees:** [[adam-smith]], Tom
**Full transcript:** [[2026-06-10-adam-thomas-bdm-team-ai-transcript]]

---

## Attendees

- [[adam-smith]] — Head of Distribution
- Tom

---

## Key themes

### 1. Trading pack data integrity — urgent

Adam's Claude trading pack (co:work, uses FP&A data, validates from HubSpot) is producing
data discrepancies. He just came out of a monthly trading meeting with SLT where the pack
was used and errors were noticed. Flo suggested linking up with Tom.

The pack currently runs as a co:work skill, iterates through co:work's self-amending skill
pattern. Adam plans to feed the transcript of the discrepancy discussion back into co:work
to diagnose and update the skill.

Tom's suggested fix: **store sample SQL queries inside the skill.** The skill should generate
and save the queries it uses; on subsequent runs, those queries are the default (99.9%
repeatability). Then share those queries with [[kirsty]] for validation — she's the FP&A
source of truth and can confirm whether the queries are pulling the right data.

A tripartite combination: Adam's prompt/skill → Tom reviewing the prompt engineering →
Kirsty validating the underlying queries.

**Action:** Adam to share the skill + transcript of the discrepancy call. Tom to review
prompts and suggest SQL query persistence. → [[AI-097]]

---

### 2. Team toolkit vision — from individual exploration to shared workflows

Multiple isolated individual tools exist across the trading/distribution team:
- Adam: monthly trading pack, inbox automation, coaching via transcripts
- [[ollie-crowe]]: broker pulse check (diagnostic across the panel)
- [[jake-wood]]: underwriting prioritisation dashboard
- [[alex-dyball]]: account-level work
- [[sophie-dodds]]: individual setup

Adam's diagnosis: *"What I'd love is — can we start to get 2–3 things that are common
workflows or problems or query states across the team where we can build something
consistently, giving everyone the same learning and information."*

His end-state: one consistent model that feeds signals both ways — distribution strategy
informs underwriting priority, underwriting data feeds distribution diagnosis. Can't get
there while tools are isolated.

His near-term ask is explicit: **when you go into a broker review meeting, do this. When
you want to understand your panel's performance, do this.** A toolkit, not a free-for-all.

**This is the BDM brain framing.** The shared context layer (Activity Log, account data)
and the scheduled tasks (morning brief, pre-meeting brief) are the answer to this. The
broker pulse becomes an input into the shared Forecaster role rather than a one-person
dashboard.

---

### 3. Activity tracking dashboard (Adam built over the weekend)

Adam showed a prototype activity dashboard tracking performance across the BDM team:
- Meetings per BDM: face-to-face vs online vs calls
- Split by broker tier (champion / accelerator / potential / foundation)
- Index score per BDM combining activity dimensions
- Goal: drive performance behaviour through visibility — who's doing what, against targets

Data source: HubSpot + calendar. Calendar-driven logic: event with a non-Google-Meet
location → assumed face-to-face (accurate in practice).

Problem: phone calls don't get logged anywhere (see below). He wants the team using
HubSpot more to log telephone calls, but doesn't want a double-entry burden.

---

### 4. HubSpot — messy, but it's still the CRM source of truth

Adam's honest assessment: *"HubSpot's messy. There's no way about it."*

Specific problem illustrated: Brown & Brown. ~60 child companies at parent level, contacts
at parent rather than individual office level. If a new BDM wants the contact for
Brown & Brown Birmingham, it could be in one of many places — or only in Adam's head.

Data architecture clarified:
- **FP&A (Kirsty/Looker)**: source of truth for trading numbers — converted deals, GWP,
  segment data. Platform feeds HubSpot; FP&A cleanses it into definitive reporting.
- **HubSpot**: layer above FP&A for activity detail — lost reasons, broker submissions,
  contact-level data, quick-call logs (aspirationally).
- **Notion**: strategy and playbook. Accelerator broker dashboards. Not a data store.

Contact data can often be inferred from the inbox — Gmail as the fallback for finding
who you've actually spoken to at a broker.

Directly relevant to the BDM brain: the HubSpot repair pattern (using Gmail + Granola
to surface missing contacts and stale records) addresses a real and named pain.

---

### 5. Quick call logging gap

Adam's team has good Granola adoption for structured meetings and Google Meets. Quick
phone calls — check-ins on a deal, callbacks on the mobile — get nothing logged.

Tom raised the EOD voice wrap-up pattern: after a quick call, pick up Granola and
talk to it like a dictaphone. Adam's response: *"Perfect. Yeah, exactly that sort of stuff."*

This is a gap in the BDM brain design: the `/granola` skill assumes a transcript exists.
For quick calls, it doesn't. The EOD nudge should explicitly prompt: *"Any phone calls
today you want to just talk me through?"* — voice wrap-up as the capture mechanism,
/granola as the processing step.

---

### 6. Three coaching layers

Adam uses Claude as a coaching tool himself. He also sees three distinct coaching layers
for the team:

1. **Personal development** — individual, private. E.g. Sophie working on concise
   communication style. *"She could use something like that really, really well."*
2. **Performance feedback** — post-meeting: did you hit your objectives? What could
   you have done better? *"Instant feedback"* on a review meeting.
3. **Sales playbook coaching** — team-wide. Are you following the playbook? Connects
   individual session behaviour to the shared Notion strategy layer.

This maps directly to the Coach and Sparring partner roles in the brain. The sales playbook
Notion page is the shared grounding for layer 3.

---

### 7. New BDM joining 21 July

Third BDM joining 21 July. Adam wants to use this as an AI-first onboarding moment:
*"Two things we can give her on day one to make her work really efficiently, get up to
speed faster than at any other company."* Tom flagged this as an experiment for the
co:work onboarding flow. → [[AI-095]] (London visit / onboarding planning)

---

## Actions

- [ ] Adam to share trading pack skill + discrepancy transcript with Tom → [[AI-097]]
- [ ] Tom: review prompts, suggest SQL query persistence pattern, set up Kirsty validation
- [ ] Tom + Adam + [[ollie-crowe]]: tripartite session (next week or week after) → [[AI-072]]
- [ ] Tom: shape / attend trading team AI session (next week — overlap with [[AI-072]])
- [ ] Tom: plan July 21 BDM onboarding around co:work setup → [[AI-095]]

---

## Cross-references

- [[bdm-ai-multiplayer]] — this meeting directly informs Phase 1 scope
- [[AI-072]] — BDM workshop (due Jun 13)
- [[AI-097]] — trading pack data integrity
- [[AI-095]] — London visit / new BDM onboarding
- [[ollie-crowe]] — broker pulse owner; tripartite session needed
- [[kirsty]] — FP&A validation for trading pack queries
- [[jake-wood]] — underwriting prioritisation dashboard (referenced as prior art)
