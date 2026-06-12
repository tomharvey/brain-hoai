---
title: "Fergus <> Tom: Weekly"
created: 2026-06-11
updated: 2026-06-11
domain: ai-enablement
type: meeting
tags: [fergus, ai-workshop, cowork-artifacts, christian-unresolved, data-integrity, ollie-crowe, geran]
---

# Fergus <> Tom: Weekly

**Date:** 2026-06-11
**Attendees:** [[fergus]], Tom

Full transcript: [[2026-06-11-fergus-tom-weekly-transcript]]

---

## Key themes

### Two AI failure modes — both rooted in excitement about the artifact

**1. Over-engineering**: jumping straight to hi-fi. Ollie and [[geran]] both identified as falling into this — building full dashboards from a single prompt. "When I see so many widgets in version zero, 95% of that is bullshit."

**2. Fire-and-forget**: not owning the output. Adam's trading deck — bad numbers throughout. Same root cause: excitement about what the tool produced rather than clarity on what problem was being solved.

Fergus noted the engineering team is further ahead on this. Code reviews are a real forcing function. Sam treats the model as a senior peer and interrogates every line. The rest of the org doesn't have that equivalent accountability mechanism.

Proposed frame for the next workshop: two bookends — **be clear about the intent upfront** and **own the quality of what gets produced**. These are teachable skills, not tool mechanics. → [[AI-099]]

### Christian's co:work budget artifact — collaboration and shareability problem

_Note: "Christian" is unresolved — a male Finance/SLT-adjacent person who built a co:work project producing an HTML budget analysis post-Admiral acquisition (showing commitments vs. actuals). No people file — confirm identity._

The artifact was presented to SLT and shared around. The problem: co:work projects on local machines aren't shareable; artifact is aggregate, not the underlying data. [[geran]] and Thom Rogers ([[tom-rogers]]) want to drill into the numbers but can't.

**Right structure**: data layer (CSV/spreadsheet) + view layer (HTML or Looker dashboard), kept separate. The data layer can be shared independently; the view layer is a derivative. This is the opinionated artifact convention that needs to become standard across co:work outputs. → [[AI-101]]

Engineering has an untested pattern: Claude interrogates Looker and builds the dashboard directly. Worth testing.

### BDM use case framing confirmed

BDM: context coach persona (librarian, secretary, coach, strategic partner). Pre-call: surface who to talk to and what to cover. Post-call: flag communication gaps against personal development feedback goals (authority, TCO messaging). Adam deliberately had BDMs build separately first; now moving toward sharing — this is the natural sequence.

Underwriting and finance are **more agent-shaped than coach-shaped**: tasks are operational and repeatable, uplift comes from doing the work not coaching through it.

### Engineering team conversation — worth broadcasting

Chris and Alex framed AI as an engineering challenge more than a productivity shortcut. Sam was the first senior engineer Tom has heard say explicitly: "I use it as a senior engineer, not as a junior." Tom's Spotlight slot every two weeks is the vehicle. Missed last one. → [[AI-100]]

---

## Actions

- [ ] **Tom**: frame next AI workshop around intent and output ownership, not tool mechanics → [[AI-099]]
- [ ] **Tom**: feed engineering AI conversation into Spotlight or broadcast format → [[AI-100]]
- [ ] **Tom + Fergus**: establish opinionated co:work artifact convention: data layer + view layer, shareable by default → [[AI-101]]

## Name flags

- **Christian** — male, Finance/SLT-adjacent, built HTML budget analysis co:work project post-Admiral close. No people file. Confirm identity.
