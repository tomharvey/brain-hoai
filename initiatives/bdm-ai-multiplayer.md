---
title: BDM AI Multiplayer
created: 2026-06-03
updated: 2026-06-12
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

## Brain roles

The brain is not one thing. It can act under eight roles across four modes — not all of them in Phase 1, but all of them in scope for this initiative. The full-context substrate (the clean ontology + MCP) is what makes all eight possible.

See: `[[reference/roles.png]]` — full taxonomy diagram.

### Handle the work
| Role | What it means for BDMs | Phase |
|------|------------------------|-------|
| **Secretary** | Tracks commitments from Granola transcripts, flags missed follow-ups, manages outstanding actions across the team | 1 |
| **Librarian** | Answers "what do we know about Acme?" — federated search across Notion and HubSpot, single query surface | 1 |

### Make me better
| Role | What it means for BDMs | Phase |
|------|------------------------|-------|
| **Coach** | Surfaces patterns in what's working and not working, connects current deal to similar past deals, supports skill development. Francesco's performance coach pattern is prior art. | 2 |
| **Forecaster** | Predicts outcomes: ghost account detection (warm signals, no recent contact), conversion likelihood scoring, pipeline risk flags — before the BDM notices | 1 |

### Think with me
| Role | What it means for BDMs | Phase |
|------|------------------------|-------|
| **Strategy partner** | Synthesis mode — the brain integrates what it knows (account history, deal signals, team context) and helps a BDM arrive at a direction. Additive and collaborative. Pre-call brief is the clearest example: "I'm about to call Acme, what do I know and what should I lead with?" Architecturally: read + synthesise. | 1 |
| **Sparring partner** | Adversarial mode — the brain holds a position and pushes back. Challenges deal assumptions, stress-tests pricing reasoning, plays devil's advocate on proposals. Requires the brain to have formed a *view*, not just retrieved facts — meaning it needs to have absorbed enough context to have an informed opinion. Harder to do well. | 2 |

> **Strategy vs sparring:** strategy partner is *with* you (it adds to your thinking); sparring partner is *against* you (it tests your thinking). Both are "Think with me" modes, but the second requires more context depth and a brain confident enough to disagree. That's a Phase 2 capability.

Adam's pattern in practice: the Admiral paper work ([[2026-05-27-adam-ai-catchup]]) is strategy partner — three-stakeholder navigation, fed Granola transcripts + paper objectives, brain *"helped shape thinking and acted as council."* Tom's framing from that same conversation: *"as a coach, as a strategic partner and as a sort of secretary"* — this pattern emerged independently across Adam, Matt Lees, and Alex Dyball without prompting.

### Maintain + grow itself
| Role | What it means for BDMs | Phase |
|------|------------------------|-------|
| **Caretaker** | Enforces write-gate lint rules, flags stale records, keeps controlled vocabularies clean without the team having to police each other | 1 |
| **Apprentice** | Self-inspection using telemetry — learns what queries recur, what gaps keep appearing, suggests schema and vocabulary improvements. Requires Phase 1 usage data to fuel it. | 3 |

Phase 1 delivers: Librarian, Secretary, Forecaster, Strategy partner, Caretaker — the brain is immediately useful.
Phase 2 adds: Coach, Sparring partner — the brain starts making the team better, not just informed.
Phase 3: Apprentice — the brain improves itself.

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

### Delivery mechanism (open design gap)

Proactive outputs are not reactive — they require a scheduler. Each output type has a different trigger:

| Output | Trigger type | Cadence |
|--------|-------------|---------|
| Similar prospects | Event-triggered | New deal lands (HubSpot webhook?) |
| Ghost accounts | Scheduled | Daily |
| BDM collision | Scheduled | Every N hours |
| Broker pattern | Scheduled | Daily |
| Follow-up reminder | Scheduled + threshold | N days since Granola action logged |

**Open question (see Open decisions #7):** where do scheduled tasks run, and how does output reach BDMs — Slack DM, HubSpot task, or email? This is not in the Phase 1 spec and must be before build starts.

---

## Architecture (strawman)

**Phase 1 delivery: co:work implementation** — see `[[reference/shared-brain/cowork-implementation]]` for the full build sheet (scheduled tasks, Granola skill, notification logic, Caretaker loop, onboarding prompt, rollout plan). The thin-MCP architecture below remains the Phase 2 target.

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

Every interaction is logged with a `role` classification (inferred from intent) against the eight-role taxonomy. The observability layer evaluates responses against the expected role mode — a strategy-partner request that gets a librarian response is a failure, not a success. See `[[reference/shared-brain/strawman-observability-self-improvement]]` for the full capture schema, role-alignment rubric, and inspection patterns.

### MCP capability surface — open questions

How capabilities like "find similar prospects" or "ghost account detection" actually surface through the MCP is not yet resolved. The strawman specifies the MCP as a write gate and query federator, but not how richer, composed capabilities are exposed. Candidates:

- **One MCP tool per capability** — the MCP exposes discrete tools (e.g. `find_similar_prospects`, `detect_ghosts`) and Claude calls them directly. Simple, but bakes logic into the MCP and couples the tool surface to every capability change.
- **Fat skills loaded by an agent** — capabilities live as Claude-native skills that an agentic client loads on demand; the MCP is purely data access. This is how J works, but J's client is Claude Code + skills files. It's not clear this applies cleanly to a BDM using a web interface.
- **Resolvers** — named, composable query handlers inside the MCP that fan out across Notion + HubSpot and merge results. Likely the right concept for cross-store queries regardless of which capability pattern wins.

**Unresolved. See Open decisions #8.**

The deeper question underneath this (see Open decisions #9): is the MCP client agentic at all? If the BDM is just prompting Claude directly, the "skill surface" question is moot — Claude decides what to call based on the tool list. Answering #9 first narrows the answer to #8.

---

## Open decisions (gating Phase 1)

These must be resolved in the technical pre-workshop before the main team session:

1. **Identity / join keys** — domain (Account) + email (Person) as keys across Notion ↔ HubSpot. Highest unresolved risk.
2. **HubSpot graduation threshold** — what event promotes a prospect into a HubSpot deal? (team decides)
3. **Search: federate vs. AWS derived index** — ship federation v1; define the trigger to build the AWS index
4. **Thin MCP shape & hosting** — tool surface, hosting, auth, stateless design, bus-factor plan
5. **Controlled vocabularies** — stages, roles, statuses, angles (team owns these)
6. **Write workflow & gate strictness** — which rules block vs. warn
7. **Proactivity delivery mechanism** — where scheduled tasks run (Lambda? cron on the MCP server?), what triggers event-based tasks (HubSpot webhook?), and how output reaches BDMs (Slack DM? HubSpot task?). Must be resolved before Phase 1 build starts — proactivity without a delivery path is just a reactive query with a scheduler nobody checks.
8. **MCP capability surface** — how are richer capabilities (multi-step queries, composed outputs) exposed: discrete MCP tools, Claude-native skills loaded by an agent, named resolvers, or something else? Answering #9 first will constrain the answer here.
9. **Is the MCP client agentic?** — So far the design assumes a BDM prompts Claude, which calls MCP tools reactively. That is not an agent loop; it's a structured interface. Does Phase 1 need autonomous agent behaviour (plan → act → observe → continue) or is reactive tool-calling sufficient? Proactivity (scheduled tasks running without a BDM prompt) implies *some* agentic loop exists — but it may live in the scheduler, not in the client Claude instance. This distinction matters for architecture and for what the BDMs actually experience.

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

## Data architecture confirmed (2026-06-10)

From Adam's direct description:

- **FP&A / Looker ([[kirsty]])**: source of truth for trading numbers — converted deals, GWP, segment performance. Platform feeds HubSpot; FP&A cleanses it for reporting. *"Everyone should be singing off the same FP&A sheet."*
- **HubSpot**: activity and detail layer — lost reasons, broker submissions, contact-level data, phone call logs (aspirationally). Messy in practice; Brown & Brown has 60 child companies with contacts scattered across parent/child records.
- **Notion**: strategy and playbook only — accelerator dashboards, sales playbook, processes. Not a data store.

Implications for the brain:
- Forecaster role pulling conversion signals should reference FP&A data via Kirsty's Looker connection, not raw HubSpot numbers
- HubSpot is the right store for activity (who called whom, when) but needs cleaning first
- The HubSpot repair capability (Gmail + Granola → surface missing contacts) directly addresses the Brown & Brown problem Adam named

---

## Quick call logging gap (confirmed 2026-06-10)

A structural gap in the brain's data coverage: phone calls — quick check-ins, mobile callbacks — don't get logged anywhere. Adam confirmed this directly (*"I've got a callback straight after this. I won't log it."*).

The EOD voice wrap-up pattern was proposed and received well: after a call, open Granola and narrate a 2-minute summary. Adam: *"Perfect. Yeah, exactly that sort of stuff."*

**Design implication**: the EOD nudge scheduled task should explicitly prompt: *"Any phone calls today you want to just talk me through?"* — voice wrap-up as capture, `/granola` skill as processing. The skill currently assumes a transcript exists; this extends it to narrated summaries.

---

## Three coaching layers (confirmed 2026-06-10)

Adam sees coaching as three distinct things, not one:

1. **Personal development** (individual, private) — e.g. Sophie's concise communication coaching. *"She could use something like that really, really well."*
2. **Performance feedback** (post-meeting) — did you hit your objectives for this meeting? What could you have done better? Instant feedback on broker review sessions.
3. **Sales playbook coaching** (team-wide) — are you following the playbook? Connects individual session behaviour to the shared Notion strategy layer.

Maps directly to the Coach role (layers 1–2) and Sparring partner role (layer 3). The Sales Playbook Notion page is the grounding for team-wide coaching.

---

## Distribution → Underwriting signal flow (end-state vision)

Adam explicitly named the end-state: *"This broker's converting really well — we should tell underwriting so that on their priority dashboard, that can go up."*

[[jake-wood]]'s underwriting prioritisation dashboard is the destination for this signal. Currently these tools are isolated — distribution strategy doesn't feed underwriting priority. The shared context layer (Activity Log, account data) is what makes the link possible.

This is out of scope for Phase 1 but shapes the architecture: the Shared Activity Log should capture enough structure (broker, outcome, conversion signal) to eventually feed the underwriting prioritisation model.

---

## Toolkit framing (2026-06-10)

Adam's language for what the team needs: *"When you go into a broker review meeting, do this. When you want to understand your panel's performance, do this. How do we build really specific tools?"*

Not a second brain. Not a free-for-all. A **toolkit** — specific workflows for specific moments. The co:work scheduled tasks and skills are exactly this pattern: `/granola` after meetings, morning brief before the day, `/ghost-check` for panel diagnosis. The language to use with the team should match Adam's framing, not the "shared brain" language used internally.

---

## Status notes

- 2026-06-03: Initiative created. Strawman design set imported from `electron-1/pkm` PR #2 into `reference/shared-brain/`.
- 2026-06-03: Adam Smith confirmed onboard via Slack. Targets confirmed: qualified submissions, conversion, GWP. Tom and Oli to get tech foundations together before coming back with a structured proposal.
- 2026-06-04: Fergus briefed on the BDM brain design (Fergus weekly). He endorsed the company-wide vision: "everyone using Claude to interface with Notion should have it, regardless of whether they're building the team OS or contributing content." BDM-first is the right start; Flock-layer then BDM-layer distinction acknowledged. MCP read/write governance gap flagged as adjacent risk — same session. → [[2026-06-04-fergus-weekly]], [[AI-096]]
- 2026-06-09: Prep session with Oli Crowe. → [[2026-06-09-ollie-weekly]]
- 2026-06-10: Adam Smith 1:1 — BDM team AI. Adam confirmed: trading pack data integrity is urgent, HubSpot messiness (Brown & Brown), wants activity tracking dashboard, proactivity explicitly named, three coaching layers. New BDM joining July 21. Primary metric: qualified submissions. → [[2026-06-10-adam-thomas-bdm-team-ai]]
- 2026-06-10: **Phase 1 implementation scoped to co:work** — downscoped from thin MCP to co:work desktop app. Full build sheet: [[reference/shared-brain/cowork-implementation]]. Key decisions:
  - HubSpot is the ownership oracle (query company owner at write time, no manual table)
  - BDM Directory is the canonical roster (names, Slack handles, HubSpot owner IDs) — maintained by Adam
  - Granola skill with sales-specific template + BDM mention detection
  - 4 scheduled tasks: morning brief, pre-meeting brief, EOD nudge, Monday weekly pulse
  - Caretaker/Apprentice maintenance loop starts Week 1 via weekly pulse + Brain Health Log
  - Cross-BDM notification: HubSpot owner query → BDM Directory → Slack DM (show draft first)
- Next: ingest W22 meetings (Ollie, Matt Price, Rakhee AI Workshops, group therapy session 3), then set up co:work pilot with Matt Lees.
- 2026-06-11: BDM enablement session with Ollie. Key confirmations: co:work scheduled tasks are **client-side only** — the app must be open for them to run (Ollie has 123 runs; confirmed this is how Gary Tan's version works too, though Gary's is cloud-based — different infrastructure). Non-deterministic conversion definitions surfaced from HubSpot MCP queries — the same question returns different answers across runs; this is a data quality / prompt design issue to resolve before the brain is trusted for conversion analysis. Semantic/ontology MCP layer discussed: the right way to prevent sloppy prose is a validation layer with a controlled vocabulary of BDM-world first-class objects (brokers, conversations, accelerators), not just schema enforcement. → [[2026-06-11-ollie-tom-bdm-enablement]]
