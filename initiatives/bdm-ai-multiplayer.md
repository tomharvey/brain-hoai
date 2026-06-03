---
title: BDM AI Multiplayer
created: 2026-06-03
updated: 2026-06-03
domain: ai-enablement
type: initiative
status: active
owner: Tom
tags: [bdm, sales, shared-brain, multiplayer, notion, hubspot, mcp]
---

# BDM AI Multiplayer

Give the BDM/sales team a shared, Claude-native brain — a structured knowledge graph spanning Notion (soft knowledge, conversations, signals) and HubSpot (deals, accounts) — accessible through a thin MCP that gates writes and federates queries. This is the first multiplayer AI deployment at Flock: a team operating out of a shared context, not individual silos.

Parent initiative: [[ai-capability-uplift]]

---

## Goal

A 4-person sales team with:
- A single place to read from and contribute to through Claude
- Clean, structured knowledge (accounts, people, opportunities, signals) with typed edges and controlled vocabularies
- Search that spans both Notion and HubSpot
- A write path that keeps the knowledge clean (lint-validated, gated)
- Telemetry from day one so the brain can improve itself

**Not a PoC.** This is production-grade from day one, because the team will trust it with real deal context.

---

## Anton's challenge

> Anton is the standing challenger for this initiative. Every decision — feature, hypothesis, scope change — must pass his test before it moves forward.

Anton's posture at the 2026-06-03 Prodtech demo: three parallel efforts running on conversion improvement, no coordination, no roadmap, no stack-ranked experiment list. His words: *"I've not been in a workshop to talk about it. I've not seen any roadmap. I've not seen an experiment list we can stack rank based on value. Let's start there."* His deeper frustration: initiatives get built, value is promised at 9–18 months, but no one can explain how it improves conversion *now*.

Anton is also Matt Lees's pragmatic grounding. Matt described it directly: *"Anton is always very crystal clear on what I should be doing — don't get lost in what the tools can do that might jeopardize the real objectives."* ([[2026-05-26-matt-lees-ai-catchup]]) Tom's read: *"this is the point at which you've just sharpened your tool away to nothing."* Matt is Flock's most capable AI user in distribution. Anton's check is what stopped him disappearing into tooling. The same check applies here.

### The Anton gate — run this against every design decision

1. **What is the OKR that counts?** Name the specific conversion metric this moves. Not "better context" — a decision made differently, a deal that closes or doesn't stall.
2. **Who benefits and how?** Two valid answers: (a) this makes what Matt does available to the whole team — the brain is the mechanism for spreading his practice, not an individual setup; (b) this is a genuinely team-level capability nobody has yet. One invalid answer: this adds sophistication to something that's already working well enough.
3. **Is this "more context" or "a better decision"?** Context doesn't convert deals; decisions do. The test: can you name the specific moment in the sales process where a BDM acts differently because of this? If not, it's context, not capability.
4. **Is this proactive or reactive?** Reactive (BDM asks, brain answers) is table stakes. The brain earns its existence by being proactive — surfacing things BDMs didn't know to ask.

---

## Conversion hypotheses

*Must be agreed with Adam and Oli before the workshop. These drive the acceptance tests and the 30/60/90-day evaluation frame.*

Candidate hypotheses (to be validated):
- *"A BDM who knows what a colleague discussed with a prospect last week will open the call in a different place — reducing recap time and moving faster to need/objection"* — team-level signal, individual setup can't produce this
- *"Surfacing 'ghost' accounts (warm signals, no recent contact across the team) will recover deals that would otherwise drop out of pipeline without anyone noticing"* — requires cross-BDM visibility
- *"When a new deal lands (e.g. Pegasus Couriers), proactively identifying 10 similar businesses in the target list will produce faster follow-on prospecting than waiting for the BDM to notice"* — Matt named this explicitly as the proactivity he wants ([[2026-05-26-matt-lees-ai-catchup]])
- *"BDMs who receive a daily brief before their first call will make fewer avoidable mistakes (wrong context, missed follow-up, duplicate outreach) than those who reconstruct context manually"*

Each hypothesis must pass the Anton gate: which decision does it change, in which moment, measurably?

---

## Proactivity as core differentiator

Matt identified proactivity as the specific thing he wants that his individual setup doesn't reliably deliver: *"for me, that more feels like proactivity — whether on an individual basis or on a team collective basis."* Example: *"if we've just picked up Pegasus Couriers, could it proactively notify me and identify 10 other businesses that fit that customer profile?"*

This is the structural advantage a shared brain has over individual setups: it has the full picture (all BDM activity, all pipeline signals, all Granola transcripts) without any individual BDM having to maintain it. Tight schedules (check every N hours) feel like proactivity when the brain surfaces something before the BDM noticed it.

Proactive outputs the brain should aim to deliver:
- New deal landed → 10 similar prospects surfaced automatically
- Prospect goes quiet → flag to owning BDM before they notice
- Two BDMs independently approaching same account → surface the collision
- Broker signal appearing across multiple accounts → surface as emerging pattern
- BDM hasn't followed up on an action from a Granola transcript → reminder before the window closes

---

## Architecture (strawman)

Three planes — see `[[reference/shared-brain/README]]` for full design set:

| Plane | What | Tools |
|-------|------|-------|
| Source-of-truth + UX | Knowledge graph + deal data | Notion, HubSpot |
| Control plane | Single front door — federated queries, write gate, telemetry | Thin MCP |
| Derived data + compute | Telemetry, search index | AWS (CloudWatch, S3/Athena, OpenSearch) |

Phased delivery:
- **Phase 1** — brain works: clean Notion DBs + thin MCP (federated search) + HubSpot read-through + telemetry capture
- **Phase 2** — brain searches well: AWS derived index (OpenSearch + Bedrock) if federation isn't enough
- **Phase 3** — brain improves itself: self-inspection + improvement suggestions once usage data exists

---

## Open decisions (gating Phase 1)

These must be resolved in the technical pre-workshop before the main team session:

1. **Identity / join keys** — domain (Account) + email (Person) as keys across Notion ↔ HubSpot. Highest unresolved risk.
2. **HubSpot graduation threshold** — what event promotes a prospect into a HubSpot deal? (team decides)
3. **Search: federate vs. AWS derived index** — ship federation v1; define the trigger to build the AWS index
4. **Thin MCP shape & hosting** — tool surface, hosting, auth, stateless design, bus-factor plan
5. **Controlled vocabularies** — stages, roles, statuses, angles (team owns these)
6. **Write workflow & gate strictness** — which rules block vs. warn

---

## Workplan

### Step 1 — Prep with Oli Crowe
Align on scope, BDM team context, and what Oli needs from this. Oli as TPM is the bridge between the technical design and the team. Agree the pre-workshop agenda.

### Step 2 — Technical pre-workshop (~2h, Tom + Oli)
Resolve the plumbing before the team's time is spent on it. Produce:
- Clean object-model diagram for the team to react to
- Strawman vocab lists (printed, ready to challenge)
- 2–3 real messy Notion records for the migration exercise
- One-pager: decided / recommend / needs-the-group

### Step 3 — Stand up the strawman
Before the main workshop, get a working skeleton in place:
- Notion databases scaffolded to the schema
- Thin MCP running with federated search
- CloudWatch telemetry capture on

### Step 4 — Main workshop with BDM team (~3.5h)
See [[reference/shared-brain/strawman-workshop-plan]] for full facilitation plan. Key outputs: validated object model, locked vocabularies, ranked query list (acceptance tests), agreed write workflow, HubSpot graduation rule, migration plan.

### Step 5 — Build out
Post-workshop: fold decisions back into strawman docs, run migration, go live.

---

## Related

- [[ai-capability-uplift]] — parent initiative
- [[AI-072]] — BDM team workshop (due 2026-06-13)
- [[reference/shared-brain/README]] — full design set (strawman)
- [[ollie-crowe]] — TPM, key collaborator
- [[matt-lees]] — highest Stage 4 in distribution, reference model
- [[adam-smith]] — BDM team

---

## Team targets (from Adam, 2026-06-03)

The shared brain needs to tie into these:
- **Qualified submissions** — primary leading indicator
- **Conversion** — core target
- **GWP** — ultimate measure

Adam also flagged **"ghosts and accelerators"** as more granular leading indicators within the team — things that predict or inhibit conversion. Worth surfacing explicitly in the workshop vocabulary exercise.

Adam's framing: *"an AI manager/coach to shape thinking, broker strategies, actions, feedback."* This is close to the performance coach pattern Francesco has already built — worth showing as prior art.

---

## Status notes

- 2026-06-03: Initiative created. Strawman design set imported from `electron-1/pkm` PR #2 into `reference/shared-brain/`.
- 2026-06-03: Adam Smith confirmed onboard via Slack. Targets confirmed: qualified submissions, conversion, GWP. Tom and Oli to get tech foundations together before coming back with a structured proposal.
- Next: book prep session with Oli Crowe.
