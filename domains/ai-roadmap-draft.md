---
title: AI Roadmap — Board Draft
created: 2026-03-30
updated: 2026-03-30
domain: ai-enablement
type: reference
status: active
tags: [roadmap, board, strategy, pioneer]
---

# AI Roadmap — Draft for Pioneer Board (2026-04-20)

> Draft due: 2026-04-03. Review with Fergus at Thursday weekly (2026-04-02).

## Context

The Head of AI role exists because AI initiatives already exist across the company — self-started by enthusiastic individuals, without accountability to targets. The role aligns, governs, resources, and accelerates these efforts.

This roadmap covers the four AI domains, informed by discovery conversations with 10+ stakeholders across engineering, product, operations, distribution, finance, and underwriting during w/c 2026-03-24 and 2026-03-30.

---

## Now (Q2 2026 — already in flight)

### Engineering Workflows

- **Platform architecture documentation** — [[chris]] building arch docs + skills so Claude writes code to company standards. Types done, architecture in progress. _Owner: Chris Fothergill._
- **AI-assisted code review** — proposed extension of arch docs into GitHub Actions. Non-blocking PR comments. _Owner: Chris Fothergill. Depends on: arch docs._
- **Skills distribution** — central repo exists, Tom taking ownership. Contribution guidelines, catalogue, cross-team visibility. _Owner: Tom Harvey._

### Operational Tooling

- **Submissions automation** — three groups working independently. Needs consolidation post-discovery. Chat interface with human-in-the-loop is the emerging direction. _Owner: TBD (Abs leaving). Status: fragmented._
- **CC extraction handover** — Abs's tool, technical deep-dive in progress. Must transfer before departure. _Owner: Abs Lamzini → TBD._
- **Underwriting assistance AI** — third-party vendor rejected. In-house approach preferred. Emily conversation today. _Owner: TBD._

### Product AI

- **Safety agent with memory** — Ishmael building an agent that learns from corrections. Pattern could generalise. _Owner: Ismael Jebril._
- **WhatsApp driver reporting** — proof of concept (Anthropic API + Twilio). Paused/broken. _Owner: TBD._

### AI Enablement

- **Claude standardisation** — company split between Claude/ChatGPT. Recommendation to standardise. Enterprise deal needed. _Owner: Tom Harvey._
- **Skills training programme** — Session 1 delivered (2026-03-27). Dev and non-dev audience. _Owner: Tom Harvey._
- **AI governance framework** — risk scenarios identified, no framework yet. Sam + Paul as co-owners when work begins. _Owner: Tom Harvey. Status: parked, important not urgent._

---

## Next (H2 2026 — concrete deliverables)

### Engineering Workflows

-
-

### Operational Tooling

- **Process documentation programme** — codify what people do before automating. Start with top 3 workflows from ops/finance discovery.
- **PostHog/DOM workflow analysis** — use existing telemetry to understand workflows at scale instead of manual documentation.
-

### Product AI

-
-

### AI Enablement

- **AI governance framework** — company-wide guidelines, risk scenarios, response protocols. Business continuity workshop.
- **Self-service AI capability** — move beyond "wow that's magic" to teams solving their own problems with AI tools.
-

---

## Later (2027+ — strategic bets, 24-month outlook)

### Big bets under discussion (from Fergus)

1. **Disconnected fleets** — insurance for non-connected commercial fleets. Acquisition funnel or dedicated loss ratio play? Would require dedicated squad.
2. **E-trading automation** — fully automated quoting. Challenge: brokers won't complete 16-page forms without incentives.
3. **Driver-level risk management** — risk at driver level vs vehicle level. Personal lines quoting potential. Darren excited.

### Directional themes

- AI as a product interface (chat, visualisation, dynamic UI) rather than CRUD forms
- Business process documentation as company-wide institutional memory
- Agents that learn from human corrections (memory pattern from safety → underwriting → submissions)
-

---

## Resource implications

- Head of AI (Tom) — full-time from Q2 2026, through end of year
- Abs Lamzini departing — submissions automation loses its pioneer
- No dedicated AI team — work happens through existing squads + cross-cutting enablement
- Claude enterprise deal needed for company-wide standardisation
-

---

## Open questions

- Who leads submissions after Abs?
- What does distribution actually need from AI? (Adam conversation 2026-03-31)
- How much of the underwriting assistance workflow is fixable with process change vs AI? (Emily conversation today)
- What are the finance pain points beyond "fin-ops V2"? (Jade conversation today)
- Is there appetite/budget for a dedicated AI squad or does this remain embedded in existing teams?
-

---

## Discovery log

| Date | Person | Role | Key insight |
|------|--------|------|-------------|
| 2026-03-24 | [[matt]] | Head of Product | PMs shifting to Cursor/Claude. AI output quality is the last mile problem. Codifying > automating. |
| 2026-03-25 | [[sam]] | Staff Engineer | "200mph with no guardrails." Governance framework needed. PhD resource. |
| 2026-03-25 | Eng group | Engineering drop-in | Skills vocabulary defined. Claude standardisation. WhatsApp demo. |
| 2026-03-26 | [[fergus]] | Interim CPTO | Board roadmap. Three strategic bets. Fertile ground: distribution, UW assistance, finance. |
| 2026-03-26 | [[abs]] | Engineer | Retool-replication culture. 10x better not 10x faster. Referrals = how to do it right. |
| 2026-03-27 | [[chris]] | Head of Architecture | 3 groups on submissions. Load-bearing sheets. Arch docs for Claude. |
| 2026-03-27 | Group | Skills AI session | Skills = context + procedure + references. Distribution is the gap. |
| 2026-03-30 | [[emily]] | Senior UW Ops Manager | _Today — to be filled_ |
| 2026-03-30 | [[jade-mounir]] | VP of Finance | _Today — to be filled_ |
| 2026-03-30 | [[jordy]] | Head of Engineering | _Today — to be filled_ |
| 2026-03-31 | [[adam-smith]] | Head of Distribution | _Tomorrow — to be filled_ |
