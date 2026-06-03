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

## Conversion hypothesis requirement

> **Anton's signal (2026-06-03 Prodtech demo):** Three parallel efforts are running on conversion improvement with no coordination, no roadmap, no stack-ranked experiment list. His explicit frustration: initiatives get built, value is promised at 9–18 months, but no one can explain how it improves conversion *now*. The BDM brain must not be that project.

**This initiative must ship a named set of conversion hypotheses before or alongside the main workshop.** Not "this will help BDMs close more deals" — specific, testable statements:

- *"BDMs who can instantly surface a prospect's last 3 touchpoints before a call will have higher conversion on that call"*
- *"Surfacing 'ghost' accounts (warm signals, no recent contact) will recover deals that would otherwise drop out of pipeline"*
- *"Reducing time-to-context at the start of a call reduces the time BDMs spend recapping and increases time on needs/objections"*

These hypotheses should:
1. Be agreed with Adam and Oli before the workshop
2. Drive the acceptance tests (Step 4 workshop query list)
3. Be the frame against which the brain is evaluated at 30/60/90 days post-launch

**The question to answer at every design decision:** *"Which conversion hypothesis does this serve?"* If the answer is "none of them", it's out of scope.

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
