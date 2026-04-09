---
title: AI Roadmap — Board Draft
created: 2026-03-30
updated: 2026-04-03
domain: ai-enablement
type: reference
status: active
tags: [roadmap, board, strategy, pioneer]
---

# AI Roadmap — Draft for Pioneer Board (2026-04-20)

> Draft: 2026-04-03. Review with Fergus before board.

---

## Executive summary

AI adoption at Flock is not a future initiative — it is already happening, self-started by enthusiastic individuals across every department. The Head of AI role exists to align, govern, resource, and accelerate these efforts without killing the momentum that makes them valuable.

In two weeks of discovery across 10+ stakeholders, three things have become clear:

1. **The ROI is already real.** An Enterprise Fleet Lead with no engineering background built 9 autonomous agents managing a £294M sales pipeline in 5 days, for $104/month. An underwriting assistant connected HubSpot to Claude in 30 seconds and started automating cancellation notices the same afternoon. The ops team designs new processes with AI in mind from day one.

2. **The cultural shift is underway.** In the words of one underwriting assistant: "We're relying more on Claude now than tech automation." Teams are bypassing traditional tooling requests and solving problems directly with AI. This is powerful — and ungoverned.

3. **The constraint is structure, not enthusiasm.** There is no shortage of people building with AI. What's missing is: shared standards for skills and agents, a path from prototype to production, visibility across efforts, and the enterprise tooling to support the usage that's already outpacing our plan limits.

This roadmap covers what's already in flight, what comes next, and the strategic bets that will shape the next 24 months.

---

## Now (Q2 2026 — already in flight)

### Headline: Enterprise Engine

[[matt-lees|Matt Lees]] (Enterprise Fleet Lead, Distribution) built a fully autonomous sales pipeline using Claude Cowork:

- **9 scheduled agents** running daily — enrichment, outreach drafting, pipeline expansion, contact validation, weekly reporting
- **64 accounts, £294M estimated premium** — grew from 18 accounts in 3 days
- **22% reply rate** on first outreach batch
- **Cost: $104/month** (Apollo.io for contact enrichment) + existing Claude Team seat
- **Human-in-the-loop**: agents create Gmail drafts only, never send autonomously
- Admiral acquisition is the strategic accelerant — broker-friendly messaging, targeting 200+ vehicle fleets

This is not an efficiency play — enterprise prospecting was previously paused because manual outreach at scale created broker friction. The agents make an entirely different strategy viable.

Fergus reviewed and gave thumbs up (2026-04-02). Matt Lees already hit the Team plan rate limit — evidence that adoption is outpacing our tooling.

_Status: live, ungoverned. Needs: HubSpot integration, backup strategy (currently local JSON on Matt's laptop), production path._

### Engineering Workflows

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Platform architecture docs | Chris Fothergill | Active | Types done, architecture in progress. Foundation for AI-generated code meeting company standards. |
| AI-assisted code review | Chris Fothergill | Proposed | Claude in GitHub Actions for non-blocking PR review. Depends on arch docs maturity. |
| Skills distribution + governance | Tom Harvey | Active | Central repo exists, ungoverned. Matt Price asked to share a skill company-wide — Jordi's response: "who tested this?" Need public/private governance and testing standards before distribution. |
| Engine Room triage automation | Jordi Pallares Roset | Active (early) | Lambda + Bedrock MVP to auto-triage Linear bug tickets using PostHog + internal MCP. ~2 hours invested. Mima identified easy-to-automate use cases. |

### Operational Tooling

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Underwriting assistance AI | Emily Staton | Active | Renewals process mapped: 4 manual steps that should be 1. Direction is eliminate spreadsheets (Looker→HubSpot direct), not automate them. Kirsty's Looker→Claude connection is the key enabler. |
| NOC automation | Shreya Chowta | Active (early) | Cancellation notices when connectivity drops below 75%. Shreya iterating via Claude prompt + HubSpot connector — faster path than her original Zapier workflow design. |
| Submissions automation | TBD (Abs leaving) | Fragmented | Three groups working independently. Needs consolidation. Chat interface with human-in-the-loop is the emerging direction. CC parsing already faster via Claude prompt than the Retool version Abs built. |
| CC extraction handover | Abs Lamzini → TBD | Active | Abs departing. Tool is functional, needs knowledge transfer before last day. |

### Product AI

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Safety agent with memory | Ismael Jebril | Active | Agent that learns from corrections. Pattern could generalise to underwriting and submissions. |
| WhatsApp driver reporting | Ollie Crowe | Active (early) | Deployed to render.com (Twilio, SQLite). Not customer-facing. Testing with 1-2 fleets via Ben. If validated → WhatsApp becomes a platform service. |
| TCO value statement | Matt Lees | Paused | Client-facing renewal/new business docs via Claude skill + Lovable templates. 12-step process documented. Mima assessed as experimental — deprioritised pending Q2 OKR progress on simplifying value sales approach. |

### AI Enablement

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Claude standardisation | Tom Harvey | Active | Company split between Claude/ChatGPT. Skills, MCPs, plugins all Claude-ecosystem. Enterprise deal needed — rate limits already a constraint (Matt Lees hit cap at $69 of $150 individual limit). |
| Skills training programme | Tom Harvey | Active | Session 1 delivered (2026-03-27) to cross-functional group. Skills vocabulary established. |
| AI capability uplift | Tom Harvey | Active | Company-wide programme. Spectrum runs from Sophie Dodds (needs a ready-made toolkit) to Matt Lees (needs freedom + governance). Emily's ops team is the reference model. |
| AI governance framework | Tom Harvey | Parked | Risk scenarios identified by Sam (PhD researcher). Important, not urgent. Deferred to later Q2. Sam + Paul as co-owners when work begins. |

---

## Next (H2 2026 — concrete deliverables)

### Engineering Workflows

- **Agent framework** — move agents from side-of-desk prototypes to production assets. Token monitoring, standardised deployment, production standards. The Enterprise Engine is the reference implementation — most sophisticated agent deployment in the company, yet running on one person's laptop with no backup or monitoring.
- **Productionised MCP infrastructure** — Google MCP, HubSpot MCP, Looker MCP all being used ad-hoc. Need hosted, authenticated, shared connectors rather than individual setups.

### Operational Tooling

- **Renewals process simplification** — Looker→HubSpot direct flow, eliminating PMT and Renewals Tracker spreadsheets. Requires: Kirsty's Looker connection, new HubSpot views for Billy's allocation workflow, alignment with Adam + Emily's HubSpot clean-up project.
- **Process documentation programme** — codify what people do before automating. Start with top 3 workflows from ops discovery. The missing 20% is institutional knowledge that isn't in Notion.
- **PostHog/DOM workflow analysis** — use existing telemetry to understand operational workflows at scale instead of manual documentation. Complements Geran's time/motion study.

### Product AI

- **Insight layer (first use case)** — create queryable pathways across data pools that were previously unanalysable: CC data, virtual imagery, HubSpot, Granola meeting notes, broker submissions, PDFs. Adam's Granola-as-CRM and Matt Lees' Apollo-enriched pipeline both demonstrate the pattern. Needs a narrow first use case to anchor it.
- **AI as product interface** — the product toolkit is no longer just forms and buttons. Chat, visualisation, dynamic UI, agent-driven workflows. WhatsApp bot and safety agent are early signals.

### AI Enablement

- **AI governance framework** — company-wide guidelines, risk scenarios, response protocols. Business continuity workshop with Sam and Paul. Deferred from Q2 but needed before year-end.
- **Self-service AI capability** — move beyond "wow that's magic" to teams solving their own problems. Department-specific onboarding paths: distribution needs toolkits, engineering needs freedom, ops needs process support.
- **Claude enterprise deal** — rate limits, admin controls, usage analytics, ToS compliance. Already a constraint — not a future need.

---

## Later (2027+ — strategic bets, 24-month outlook)

### Big bets under discussion

1. **Disconnected fleets** — insurance for non-connected commercial fleets. Acquisition funnel or dedicated loss ratio play? Would require a dedicated squad.
2. **E-trading automation** — fully automated quoting. Challenge: brokers won't complete 16-page forms without incentives. AI could change the submission interface entirely.
3. **Driver-level risk management** — risk at driver level vs vehicle level. Personal lines quoting potential. Darren excited about the possibilities.

### Directional themes

- **Insights database** — company-wide, AI-queryable knowledge across all data pools (telemetry, CCs, virtual imagery, HubSpot, Granola, PDFs). The pattern is emerging in distribution (Granola + Looker MCP), underwriting (HubSpot + Zapier), and enterprise sales (Apollo + pipeline JSON). Consolidating these into a coherent data strategy is the 3-6 month horizon.
- **AI as product interface** — chat, visualisation, dynamic UI rather than CRUD forms. What Web 2.0 did with input fields, agents will do with conversations.
- **Agents that learn from corrections** — memory pattern from safety agent → underwriting → submissions. Self-improving systems, not static automation.
- **Business process documentation as institutional memory** — the missing prerequisite for reliable automation. "Load-bearing Google sheets" need to become queryable, governed knowledge.

---

## Resource implications

- **Head of AI (Tom Harvey)** — full-time from Q2 2026. Currently the only person with cross-company visibility of AI efforts. No direct reports.
- **No dedicated AI team** — all work happens through existing squads + cross-cutting enablement. This is sustainable for Q2 but may not scale.
- **Abs Lamzini departing** — submissions automation and CC extraction lose their pioneer. Knowledge transfer in progress.
- **Claude enterprise deal needed** — Team plan rate limits are already a constraint. Matt Lees hit his cap running the Enterprise Engine. Org is at 8% of overall spending but individual seat limits are fixed. Enterprise plan gives: higher limits, admin controls, usage analytics, ToS compliance.
- **Apollo.io** — $104/month for contact enrichment powering the Enterprise Engine. Budget approval needed.
- **The ROI equation** — Matt Lees built a £294M pipeline for $104/month with no engineering support. Shreya automated cancellation notices in an afternoon. Anna connected HubSpot to Claude in 30 seconds. The cost of not investing in AI infrastructure is measured in the opportunities these people can't pursue when they hit platform limits or governance gaps.

---

## Open questions

- Who leads submissions automation after Abs departs?
- What are the finance pain points? (Jade conversation rescheduled to 2026-04-07)
- Is there appetite/budget for a dedicated AI squad, or does this remain embedded in existing teams?
- How does the Enterprise Engine move from Matt's laptop to company infrastructure? (Agent framework question made concrete)
- What does Kirsty's Looker→Claude connection look like technically? (Key dependency for renewals and insight layer — meeting 2026-04-08)
- What governance is needed for autonomous agents that access email, CRM, and external APIs?

---

## Discovery log

| Date | Person | Role | Key insight |
|------|--------|------|-------------|
| 2026-03-24 | [[matt]] | Head of Product | PMs shifting to Cursor/Claude. AI output quality is the last mile problem. Codifying > automating. |
| 2026-03-25 | [[sam]] | Staff Engineer | "200mph with no guardrails." Governance framework needed. PhD resource. Redirected to evals + documentation for Q2. |
| 2026-03-25 | Eng group | Engineering drop-in | Skills vocabulary defined. Claude standardisation. WhatsApp demo. |
| 2026-03-26 | [[fergus]] | Interim CPTO | Board roadmap. Three strategic bets. Fertile ground: distribution, UW assistance, finance. |
| 2026-03-26 | [[abs]] | Engineer | Retool-replication culture. 10x better not 10x faster. Referrals = how to do it right. |
| 2026-03-27 | [[chris]] | Head of Architecture | 3 groups on submissions. Load-bearing sheets. Arch docs for Claude. |
| 2026-03-27 | Group | Skills AI session | Skills = context + procedure + references. Distribution is the gap. |
| 2026-03-30 | [[emily]] | Senior UW Ops Manager | Team uses AI daily. Zapier backbone. Claude preferred. Designs new processes with AI in mind. Monthly AI sync exists. Reference model for capability uplift. |
| 2026-03-30 | [[jordi]] | Head of Engineering | Coordination model agreed: Jordi discovers, Tom supports. Engine Room triage MVP. Skills need governance. Insights database = 3-month bet. Weekly 1:1 on Fridays. |
| 2026-04-02 | [[adam-smith]] | Head of Distribution | "Selfish with AI" — team needs ready-made toolkit, not exploration. Granola = accidental CRM. Kirsty's Looker MCP generating review packs. HubSpot thin on broker data — clean-up project with Emily. Semantic naming consistency prerequisite. |
| 2026-04-02 | [[matt-lees]] | Enterprise Fleet Lead | Enterprise Engine: 9 autonomous agents, £294M pipeline, $104/month. Built in 5 days. Fergus thumbs up. Admiral acquisition driving urgency. Hit Team plan rate limit. |
| 2026-04-02 | [[anna]] | Senior UW Assistant | Renewals process mapped (4 steps → should be 1). Direction: eliminate spreadsheets, Looker→HubSpot direct. G Drive folder automation next. HubSpot connected to Claude trivially. |
| 2026-04-02 | [[shreya-chowta]] | Underwriting Assistant | NOC automation via Claude + HubSpot. "Relying more on Claude than tech automation." CC parsing via Claude faster than Abs's Retool version. Submissions needs scoping into small goals. |
| 2026-04-07 | [[jade-mounir]] | VP of Finance | _Scheduled — to be filled_ |
| 2026-04-08 | [[kirsty]] | Senior Analytics Engineer | _Scheduled — Looker→Claude connection, key dependency_ |
