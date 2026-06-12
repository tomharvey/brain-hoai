---
title: "AI — Engineering Group Therapy (Chris / Sam / Alex)"
created: 2026-06-10
updated: 2026-06-10
domain: engineering-workflows
type: meeting
tags: [chris, sam, alex-smith, engineering, ai-culture, testing, coding-os, junior-engineers]
---

# AI — Engineering Group Therapy (Chris / Sam / Alex)

**Date:** 2026-06-10
**Attendees:** [[chris]], [[sam]], [[alex-smith]], Tom

_Note: this meeting was recorded as part of a single Granola session titled "Ai" (ID: c132142b). The session contained two back-to-back conversations; this is Meeting 1. Meeting 2 is [[2026-06-10-ai-strategy-geran]]._

Full transcript: [[2026-06-10-ai-engineering-group-therapy-transcript]]

---

## Key themes

### Cambrian explosion in tests — the blocker is gone

The constraint on writing tests has been removed. AI writes them faster including edge cases engineers wouldn't have thought of.

- **Chris**: front-end is now better tested than ever, and none are flaky.
- **Sam**: AI surfaces hard test cases he'd never have considered.
- **Alex (caveat)**: tests can be written to fit a logic bug if the AI misunderstood the requirements. Still requires the engineer to fully understand what's being built.

**Implication**: the expected test coverage baseline should rise — the old justifications for skipping tests are gone. This needs to be a team standard, not individual choice.

### How we enjoy the work — dopamine, satisfaction, identity

- **Sam**: enjoys it more now. Uses it as pairing with a senior engineer who challenges his thinking. Line-by-line interrogation of output (not blind acceptance). Not the "junior engineer" paradigm — senior engineer paradigm.
- **Chris**: loves it for config files, gnarly package errors, things that used to waste half a day. Slight loss of dopamine from not solving hard problems line by line. Reframing: architectural decisions for satisfaction, agents for the tasks you'd dislike.
- **Alex**: still writes parts he cares about by hand. Frames AI as extra team members. "It's just working with artificial people instead of actual people in your team."

### Junior engineer problem — the elephant in the room

Seniors fit AI naturally: offloading to a junior, pairing with a peer, getting help from a senior — all familiar. For a junior, writing slowly line by line *was* the job. That's changed dramatically.

Chris's frame: **need-to-know vs. want-to-know** will separate good engineers from the rest. Curiosity about how things work underneath is what makes the rounded engineer. Sam: engineers who go back to learn underlying principles (JS before React, Ruby before Rails) become the best ones. Same will apply to AI.

Historical parallel: when MVC frameworks arrived, seniors worried juniors would never learn "real" Ruby. Didn't pan out. Same pattern with C, assembly, and every abstraction layer since.

Alex: bad code is still bad code, regardless of who wrote it.

### Building the coding OS — next-generation codebases

Current codebases work well: AI follows patterns, uses type-gen and schema docs, understands architecture from examples. Blank-slate problem is harder.

**Proposed approach** (emerged from group):
- Feed it principles + respected third-party repos + your own codebase
- Generate a baseline style guide through iterative conversation (not step-by-step)
- Encode architectural rules in linters (folder-level constraints, etc.) for deterministic checking
- Reason about principles, not "how we've done it before" — it might produce better code

Tom: already doing this on personal repos — interrogating Claude file by file and directory by directory on its choices. The conversational work-tree checkout-of-main as an architectural review is the interesting emerging pattern. → [[AI-102]], [[AI-103]], [[AI-104]]

### Productivity pressure — no external pressure, internal pull

No one feels explicit external pressure to 10x. Internal pressure exists: when AI gives speed, the instinct is to grab the next ticket immediately. No measurable step-change in velocity since adopting LLMs (ELT perception may be that the team is slower, but quality has gone up — more tests, fewer issues). Tom's view: far more interesting definitions of "better" than "faster."

---

## Actions

- [ ] **Engineering team**: define what team-level AI coding standard looks like, building on linting/test conventions → [[AI-103]]
- [ ] **Chris + Tom**: build coding OS baseline — principles, respected repos, iterative LLM style guide → [[AI-104]]
- [ ] **Tom**: explore conversational architectural review pattern (checkout of main, surface codebase drift) → [[AI-102]]
- [ ] **Tom**: reshuffle groups and run another AI conversation in a few weeks
