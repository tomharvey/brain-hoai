---
title: AI Philosophy — "How we use AI" section draft
created: 2026-07-10
updated: 2026-07-10
domain: ai-enablement
type: reference
status: completed
tags: [ai-philosophy, notion, draft]
---

# "How we use AI" — draft for Flock's AI Philosophy (Notion)

Draft response to the comment on section **3. AI literacy** of the Notion doc
([Flock's AI Philosophy](https://www.notion.so/flockcover/Flock-s-AI-Philosophy-31fe4b9152598016ba77cd546de59892?d=389e4b9152598062a2e6001c3f3afc16)):
*"can we add a section here which talks about **how** we use AI? Automation etc"* / *"And examples of each"*.

Designed to slot in directly under the existing section-3 bullet, keeping the
heading (and its comment anchor) and section numbering untouched. Related:
[[AI-116-publish-notion-ai-philosophy-guide]].

---

**POSTED 2026-07-10**: content published into the Notion page under §3 (anchor and numbering preserved) and replied in Rakhee's comment thread (offering to split into a standalone §4 if she prefers). Open questions 1 and 4 were shipped as-drafted: team-level attribution, closing line unchanged.

## Draft content

### How we use AI

A core part of that literacy is recognising which **mode of use** fits the job. AI use at Flock falls into four modes. Most people start with the first and grow into the others — each mode hands more of the *doing* to AI, while the human moves up to briefing, reviewing, and designing.

**Assistance — thinking and working with AI.** You stay in the loop throughout: AI drafts, analyses, researches, and challenges your thinking, and you shape the result turn by turn. This is where everyone starts, and it never stops being useful.

*Examples at Flock:*

- Finance connects Claude to Looker so dashboards come back as written insight — not just "we lost that deal" but *why* we lost it (payment terms, not price).
- Month-end reconciliation runs through Claude, which lists every discrepancy down to minute differences for a human to resolve.
- Underwriters build a one-off analysis or dashboard in minutes — work that used to take a day, or simply didn't get done.

**Automation — packaging repeatable work as skills.** When a task is well-defined and repeats, we turn it into a skill: a written-down procedure Claude runs the same way every time, with a human checking the output. If you do something weekly that follows the same steps, it is probably a skill waiting to be written. And when several automated steps start chaining together, you're ready for the next mode: handing over the whole thing.

*Examples at Flock:*

- Notice-of-Cancellation letters: a skill pulls the ticket and policy data from HubSpot, calculates the dates, and fills the Word template — built by the underwriting assistant team themselves.
- Credit control starts each day with an automatically generated, prioritised briefing from NetSuite data — two minutes instead of a morning in spreadsheets.
- The weekly Finance MI dashboard and the Flock O'Clock deck both assemble themselves from their source data and team submissions.

**Delegation — handing over whole tasks.** Instead of automating one step, you hand over an outcome — then review the result the way you would review a colleague's work. You own what ships.

*Examples at Flock:*

- Finance built an instalment calculator with Claude (code-reviewed by engineering, self-auditing on every run) that made monthly instalments on quarterly adjustments possible — something we previously had to decline.
- Operations breaks processes like renewals into slices and delegates them: the HubSpot deal is populated, folders are created, and the broker email is drafted — all reviewed before anything is sent.
- Engineers hand a ticket to an agent and review the draft pull request as they would from a mid-level hire.

**Orchestration — systems of agents with human governance.** Several agents working together on an ongoing job. The human's role shifts from doing the work to designing the system, setting its guardrails, and monitoring its quality.

*Examples at Flock:*

- Our enterprise prospecting engine: a team of coordinated agents that enrich fleets, find and verify contacts, and maintain an enterprise pipeline — built by a BDM, not an engineer, unlocking a strategy that manual effort could never scale to.
- The safety agent in our product learns from human corrections and runs with full observability and a suite of over a hundred automated evaluation tests.
- Shared team "brains" — like the BDM team's shared workspace that knows our brokers, accounts, and conversation history, and surfaces things proactively rather than waiting to be asked.

Two rules apply in every mode:

- **You own the output.** The two quiet failure modes are over-engineering (jumping straight to a polished output without iterating through a conversation) and fire-and-forget (accepting whatever comes back unexamined). Both produce worse outcomes than not using AI at all.
- **Deterministic where it matters.** AI is for judgment, drafting, and ideas. Numbers we report come from frozen, auditable queries and calculations — Claude surfaces the insight; the auditable system does the maths. When in doubt, ask it to cite its sources.

Literacy grows by moving through these modes — from a first win, to working with context, to fluency, delegation, and orchestration. We support every Flocker on that path with workshops, 1:1 pairing, and a shared library of skills.

---

## Working notes (not for Notion)

### Who each example refers to

| Example | Person / source |
|---|---|
| Looker → written insight | Kirsty Alexandre — [[AI-006-kirsty-looker-claude]] |
| Month-end reconciliation | Queency Gonsalves — finance workshop 2026-05-19 |
| Underwriter dashboards in minutes | Tom Rogers — [[2026-06-22-tom-rogers-ai-discovery]] |
| NOC letters skill | Shreya Chowta — [[AI-008-shreya-noc-followup]] |
| Credit-control briefing | Ivan Boix — [[AI-145-netsuite-data-pull-automation]] |
| Finance MI dashboard | David Pilley — [[AI-138-finance-mi-dashboard-google-drive]] |
| Flock O'Clock deck | Phoebe Woodman — [[AI-089-flock-oclock-automation-phoebe]] / [[AI-141-flock-oclock-slack-trial]] |
| Instalment calculator | Matt Dipre — [[AI-162-matt-dipre-calculator-productionise]] |
| Renewal slices | Emily Staton — [[AI-158-emily-renewal-automation-first-slice]] |
| Ticket → draft PR review | [[ai-native-engineering]] / [[AI-053-endorsements-e2e-automation-pilot]] |
| Enterprise prospecting engine | Matt Lees — [[AI-005-hubspot-enterprise-engine]] |
| Safety agent | Ishmael — [[safety-agent-memory]] |
| BDM shared brain | [[bdm-ai-multiplayer]] |

### Framing sources

- Modes ladder echoes the [[activation-pathway]] stages (delegation, orchestration) and the automation-vs-delegation distinction from [[2026-07-02-ed-tom-q3-operationalisation]].
- "You own the output" + the two failure modes: [[AI-099-ai-workshop-framing-intent-ownership]].
- "Deterministic where it matters": [[AI-121-deterministic-reporting-pricing]] (phrased without referencing the Admiral incident).

### Decisions made

- **Example weighting is deliberate** (Tom, 2026-07-10): lean on proven successes over team balance. Finance/UW-heavy examples are fine — Q3 focus is lifting finance and underwriting capability, so the examples double as "people like you are already doing this." No rebalancing toward People/pricing/claims for representation's sake.
- **Dated figures dropped** (Tom, 2026-07-10): removed the £294M pipeline value (April figure, since grown, no current number) — the action is the point of that example, not the £ value. Agent count also made vague ("a team of coordinated agents"). The "~110 evals" claim was already phrased as "over a hundred".

### Open questions before pushing to Notion

1. **Names or teams?** Currently team-level attribution. Naming people (with their OK) would land harder and reward the builders — peer demos are the proven activation trigger ([[AI-110-underwriting-ic-activation-jake-led]]).
2. **Subsection of 3, or its own numbered section?** Currently written to sit inside "3. AI literacy" so the comment anchor and numbering survive. Renumbering to a standalone "4. How we use AI" is an option if Rakhee prefers.
3. **Overlap with Rakhee's guide** ([[AI-116-publish-notion-ai-philosophy-guide]]) — tools list and "Moscard → month → share findings" loop deliberately not duplicated here.
4. Does the closing line overpromise ("1:1 pairing" capacity)?
