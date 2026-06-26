---
title: "Fergus <> Tom: Weekly"
created: 2026-06-25
updated: 2026-06-25
domain: engineering-workflows
type: meeting
tags: [fergus, installments, geran, engineering, bedrock, claude-spend, self-healing-loop, jordi]
---

## Attendees

- [[fergus]] (Fergus Doyle, CTO)
- Tom Harvey

Full transcript: [[2026-06-25-fergus-tom-weekly-transcript]]

---

## Key themes

### Finance installments — frustration with slow progress

- Geran's "six months of work" framing seen as completely wrong
  - Real problem: underwriters don't document policy configuration, not implementation cost
  - Parallel workstream needed: get underwriters documenting everything on every policy
- Fergus built a ledger service prototype with Claude overnight — not fully event-sourced, needed some architectural repointing, but ~80% there
  - Never written a line of code in this codebase; the team's hesitation baffling
- Finance may just build it themselves before the argument is resolved
- Proposal: get Joanne (contractor, onboarding next Friday), Geran, Javier, Jordi, and Fergus in a room for two days of hacking
  - Goal: surface what's actually hard vs. what's assumed to be hard
  - Gantt chart approach (flexible payment days as a phase) rejected: "that's a prompt, not a project"

### Engineering culture and the self-healing loop

- Team appears frozen, not shipping at pace
- Root concern: have we lost the ability to ship, or has the culture regressed?
  - Haulage migration cited as counterexample where Chris executed well with a clear vision
  - Current problem: no one has a clear picture of what's being built, so execution stalls
- PR quality low on AI-generated output, but no harness, no evaluation framework exists yet
  - Wrong question: "how do we handle PR load?" vs. "how do we make the output better?"
  - Bottleneck is PR review, not PR generation
- Proposal: make building the harness Ishmael's explicit job for a month
  - True signal is not volume of PRs but whether a self-healing loop is running
  - "Tending the garden rather than going to the shop to buy a melon every day"
- Architectural tenets questioned: portal pages slow to load, mid-policy migration still a multi-month fear
  - If truly event-sourced, replaying history to hydrate a new persistence layer should be trivial
  - If it can't be replayed, the event-sourced structure isn't delivering what it promised

### Claude spend, reliability, and Bedrock fallback

- Current spend: ~£5–6k/month; some users consistently hitting limits and need premium seats
- Framing: equivalent to a junior engineer; clearly net positive
- Action: formalise as a production system with a proper policy, not a "giant experiment"
- Reliability concern: Claude went down for ~3 hours, blocked meaningful work
  - Bedrock tested as fallback but not fully wired up; Tom to check
  - Bedrock offers top-tier privacy and pricing but Claude Desktop doesn't work through it
  - Potential option: chat interface on top of a Bedrock API endpoint

---

## Actions

- [ ] Tom: formalise Claude spend as a production policy — move away from treating as experiment; review seat levels and set usage guidelines → [[AI-142]]
- [ ] Tom: verify Bedrock wiring as a fallback — check and test what was connected → [[AI-143]]
- [ ] [[fergus]]: pitch Ishmael on owning the harness for a month — frame as building a self-healing loop, not hitting a PR volume target
- [ ] [[fergus]]: propose two-day installments hack session to [[jordi]] — get Joanne, Geran, Javier, and Chris in a room to surface what's actually hard
