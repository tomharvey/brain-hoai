---
title: AI Roadmap — Board Draft
created: 2026-03-30
updated: 2026-04-14
domain: ai-enablement
type: reference
status: active
tags: [roadmap, board, strategy, pioneer]
---

# AI Roadmap — Draft for Pioneer Board (2026-04-20)

> Draft: 2026-04-14. Review with Fergus before board.

---

## Executive summary

AI adoption at Flock is not a future initiative — it is already happening, self-started by enthusiastic individuals across every department. The Head of AI role exists to align, govern, resource, and accelerate these efforts without killing the momentum that makes them valuable.

In three weeks of discovery across 21+ stakeholders spanning every department, three things have become clear:

1. **The ROI is already real.** An Enterprise Fleet Lead with no engineering background built 9 autonomous agents managing a £294M sales pipeline in 5 days, for $104/month. An underwriting assistant built a working Claude skill to automate cancellation notices — end-to-end in a single execution. The ops team designs new processes with AI in mind from day one.

2. **The cultural shift is underway.** In the words of one underwriting assistant: "We're relying more on Claude now than tech automation." Teams are bypassing traditional tooling requests and solving problems directly with AI. A financial analyst previously automated invoicing via Claude before a NetSuite update broke it — and now wants it back. This is powerful — and ungoverned.

3. **The constraint is structure, not enthusiasm.** There is no shortage of people building with AI. What's missing is: shared standards for skills and agents, a path from prototype to production, visibility across efforts, access and permissions (Looker, HubSpot AI integration), and the enterprise tooling to support the usage that's already outpacing our plan limits.

This roadmap covers what's already in flight, what comes next, and the strategic bets that will shape the next 24 months.

---

## AI capability spectrum

Discovery revealed four consistent cohorts across every non-underwriting team. Every department has a mix — the challenge is not converting sceptics but clearing the path for people who already want to move.

### 1. Builders (5–10% of staff)

Building agents, skills, and automations independently. Already productive. Often outpacing the infrastructure.

**Examples**: Matt Lees (9-agent sales pipeline), Shreya Chowta (NOC letter skill), Kirsty (Looker→Claude dashboards with AI-generated insights), Javier (Flock API MCP, HubSpot→Claude quoting PoC), Jonny Smith (Zapier+Looker automations self-built)

**What they need**: governance frameworks, production paths for prototypes, more tokens, freedom to experiment with air cover. Stop them from being punished for going fast.

**Plan**: formalise agent/skill standards, provide enterprise Claude seats, create a path from "works on my laptop" to production. The Enterprise Engine is the reference case — most sophisticated deployment in the company, running on one person's laptop with no backup.

### 2. Active users (~20–30% of staff)

Using AI daily for specific tasks — formatting, drafting, data lookups. Hitting access blockers or data quality issues. Know what they want but can't quite get there alone.

**Examples**: Matt Dipre (invoice automation broken by NetSuite, blocked on Looker access), Anna (renewals process mapped, HubSpot connected), Alex Dyball (ChatGPT for presentations, Looker analysis), Liam Thomson (Artlist for video, Lovable for decks)

**What they need**: access unblocked (Looker permissions, HubSpot AI integration), connectors set up, 1:1 guidance to level up from using AI for formatting to building reusable workflows. Often one conversation away from becoming builders.

**Plan**: systematic access audit (Looker, HubSpot AI, Claude seats), department-specific 1:1 pairing sessions, skill templates for common workflows. Target: move 50% of this group to builder status by end of Q3.

### 3. Interested but stuck (~30–40% of staff)

See the value, want to use AI, but lack confidence or haven't had the "aha moment." Often intimidated by setup or don't know how to frame their problem as a prompt.

**Examples**: Sophie Dodds (needs a ready-made toolkit, not open-ended exploration), Fred Bush (biggest manual pain point identified but hasn't connected to Claude yet), several people across ops and distribution

**What they need**: 1:1 time on their actual use cases (not generic workshops), someone to sit with them for 15 minutes and get them from zero prompts to one prompt. Setup guidance — installing Claude, getting permissions — is a real barrier.

**Plan**: shift from group workshops to applied 1:1 tutorials. Pair each person with a builder from their department. Create "starter kits" per department — pre-built skills and connectors for common workflows. The confidence barrier is the gap, not capability.

### 4. Observers (~20–30% of staff)

Watching others, not yet engaged. May be waiting for permission, waiting to see results, or don't see how AI applies to their work.

**What they need**: exposure to peers solving real problems (not external demos), explicit permission to experiment, and visibility of time saved. AI breakfasts and demos help but need to become peer-led, not top-down.

**Plan**: peer-led showcases (Shreya demoing her NOC skill, Matt Lees demoing Enterprise Engine), visible metrics on adoption (users with >100 tokens, not total tokens), explicit "now is the time to play" messaging from leadership.

### Underwriters — a special case

Cultural inertia from decades of manual processes. However, appetite is growing — Billy approached Jordi unprompted wanting to "chat about AI." Current framing: "automate the stuff we give underwriter assistants." This can be reframed: if the UW assistants automate their routine work, what higher-value work can they take on?

**Plan**: attend underwriting team call (15 Apr), listen before proposing. Build on Billy's momentum. Don't push — create pull by demonstrating wins from adjacent teams (Shreya's NOC skill, Anna's renewals mapping).

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

_Status: live, ungoverned. HubSpot now connected (Emily completed setup 2026-04-07) — AI data goes on company records (not deal records). Pipeline data moving from local JSON to structured data. Still needs: production deployment path, backup strategy, monitoring._

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
| NOC automation | Shreya Chowta | Active — working skill | Built a working Claude skill ("NOC letter generator") that runs end-to-end: find tickets → get company/deal info → parse ticket → calculate dates → fill Word template → save .docx. Remaining blockers: client addresses in Retool (not HubSpot), downloads folder permissions. Demoing at Wed AI/Automations sync. |
| Submissions automation | TBD (Abs leaving) | Fragmented | Three groups working independently. Needs consolidation. Chat interface with human-in-the-loop is the emerging direction. CC parsing already faster via Claude prompt than the Retool version Abs built. |
| CC extraction handover | Abs Lamzini → TBD | Active | Abs departing. Tool is functional, needs knowledge transfer before last day. |

### Product AI

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Safety agent with memory | Ismael Jebril | Active | Agent that learns from corrections. Pattern could generalise to underwriting and submissions. |
| WhatsApp driver reporting | Ollie Crowe | Active (early) | Deployed to render.com (Twilio, SQLite). Not customer-facing. Testing with 1-2 fleets via Ben. If validated → WhatsApp becomes a platform service. |
| TCO value statement | Matt Lees | Paused | Client-facing renewal/new business docs via Claude skill + Lovable templates. 12-step process documented. Mima assessed as experimental — deprioritised pending Q2 OKR progress on simplifying value sales approach. |

### Product AI (additional)

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Safety product naming ("Jay") | James | Active | Sentiment analysis of customer Granola transcripts showed "AI" scares customers. J chosen for personal, approachable feel (bird theme → Flock). 4 starter prompts to reduce friction. Validating with Antoine + customers. |
| Acquisition AI — HubSpot→Claude→Flock API quoting | Javier | PoC (2-week target) | "Surface everywhere" strategy. Chris already built a Flock policy management MCP. PoC target: automated quoting from HubSpot submission through to Flock API. ~Due Apr 24. |

### AI Enablement

| Initiative | Owner | Status | Key detail |
|-----------|-------|--------|------------|
| Claude standardisation | Tom Harvey | Active | Company split between Claude/ChatGPT. Skills, MCPs, plugins all Claude-ecosystem. Enterprise deal needed — rate limits already a constraint (Matt Lees hit cap at $69 of $150 individual limit). |
| Skills training programme | Tom Harvey | Active | Session 1 delivered (2026-03-27). Shifting from group workshops to applied 1:1 tutorials on real use cases — workshops build familiarity but 1:1 pairing breaks the confidence barrier. |
| AI capability uplift | Tom Harvey | Active | Company-wide programme. Four cohorts identified (see capability spectrum above). Emily's ops team is the reference model. Baseline report in progress. |
| AI governance framework | Tom Harvey | Parked | Risk scenarios identified by Sam (PhD researcher). Paul O'Neill flagged compliance measurement gap — can't govern what you don't measure (meeting attendance, regulation readership, referral tracking). Deferred to later Q2. Sam + Paul as co-owners when work begins. |
| Compliance measurement gap | Paul O'Neill / Tom | Identified | Paul's thesis: can't deploy agents responsibly if underlying compliance data isn't captured. Underwriting referrals, policy readership, meeting attendance — none systematically measured. Exploring Google Calendar integration for participation data. |

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

- **AI governance framework** — company-wide guidelines, risk scenarios, response protocols. Business continuity workshop with Sam and Paul. Deferred from Q2 but needed before year-end. Paul's compliance measurement gap is a prerequisite.
- **Self-service AI capability** — move beyond "wow that's magic" to teams solving their own problems. Four cohorts need four different interventions (see capability spectrum). Department-specific starter kits, 1:1 pairing, peer-led showcases.
- **Claude enterprise deal** — rate limits, admin controls, usage analytics, ToS compliance. Already a constraint — not a future need.
- **Access and permissions audit** — Looker permissions, HubSpot AI integration, Claude seats. Multiple people blocked by access rather than capability (Matt Dipre, Sophie Dodds, others). Quick wins hiding behind admin tasks.

### Cross-cutting: the "last mile" interpretation problem

A pattern flagged independently by Matt Price, Kirsty, and Ollie Crowe: LLMs generate numbers and charts, but nobody does the interpretation. Dashboards ship without context. Reports land with data but no "so what." Kirsty's approach — AI-generated paragraph summaries alongside the numbers — is the right pattern. This isn't an AI problem; it's a culture problem that AI makes more visible. Every AI-generated report should include a plain-language interpretation. This needs to become a standard, not a nice-to-have.

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
- **Access blockers as hidden cost** — multiple people blocked by permissions, not capability. Matt Dipre can't access Looker dashboards. Sophie Dodds doesn't have HubSpot AI integration. These are admin tasks masquerading as technical problems — quick wins hiding in plain sight.
- **The ROI equation** — Matt Lees built a £294M pipeline for $104/month with no engineering support. Shreya built a working NOC automation skill in a single session. Matt Dipre previously automated invoicing end-to-end before a NetSuite update broke it. The cost of not investing in AI infrastructure is measured in the opportunities these people can't pursue when they hit platform limits, access blockers, or governance gaps.

---

## Open questions

- Who leads submissions automation after Abs departs? (Three groups working independently — needs consolidation)
- What are the finance pain points? (Jade conversation still to be scheduled. Matt Dipre discovery reveals: invoice automation broken by NetSuite update, data scattered across Snowflake/Google Sheets/Quincy's backup sheet, Looker access blocked)
- Is there appetite/budget for a dedicated AI squad, or does this remain embedded in existing teams?
- ~~How does the Enterprise Engine move from Matt's laptop to company infrastructure?~~ → HubSpot now connected. Remaining: production deployment, monitoring, backup. Agent framework is the generalised solution.
- ~~What does Kirsty's Looker→Claude connection look like technically?~~ → Answered. Decision 004 made: Looker MCP server selected. Next: cloud deployment with `use_client_oauth` (AI-010).
- What governance is needed for autonomous agents that access email, CRM, and external APIs?
- How much to invest in HubSpot improvements given Pioneer's potential Salesforce migration via Five Sigma? (Raised by Matt Price, 2026-04-14)
- CRM data quality: company-wide blocker. Who owns the clean-up? How do we stop "data isn't perfect" from being an excuse to not adopt AI?

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
| 2026-03-30 | [[emily]] | Senior UW Ops Manager | Team uses AI daily. Zapier backbone. Claude preferred. Designs new processes with AI in mind. Reference model for capability uplift. |
| 2026-03-30 | [[jordi]] | Head of Engineering | Coordination model agreed: Jordi discovers, Tom supports. Engine Room triage MVP. Skills need governance. |
| 2026-04-02 | [[adam-smith]] | Head of Distribution | "Selfish with AI" — team needs ready-made toolkit, not exploration. HubSpot thin on broker data. |
| 2026-04-02 | [[matt-lees]] | Enterprise Fleet Lead | Enterprise Engine: 9 agents, £294M pipeline, $104/month. Hit Team plan rate limit. |
| 2026-04-02 | [[anna]] | Senior UW Assistant | Renewals process: 4 manual steps → should be 1. Eliminate spreadsheets, not automate them. |
| 2026-04-02 | [[shreya-chowta]] | Underwriting Assistant | "Relying more on Claude than tech automation." NOC automation faster via Claude than Zapier. |
| 2026-04-07 | [[matt-lees]] | Enterprise Fleet Lead | HubSpot connected. AI data on company records. Moving from local JSON to structured data. |
| 2026-04-08 | [[fred-bush]] | Underwriting Assistant | Driver referrals are biggest manual gap: 10-20/day at ~15min each, fully manual. |
| 2026-04-09 | [[kirsty]] | Senior Analytics Engineer | AI-generated paragraph insights solve "users see numbers but don't interpret" problem. Looker MCP key enabler. |
| 2026-04-10 | [[paul]] | Head of Risk & Compliance | Compliance measurement gap: can't deploy agents if underlying data isn't captured. |
| 2026-04-10 | [[alex-dyball]] | Distribution | Pragmatic ChatGPT+Claude user. Meeting self-scoring pattern. Renewal nudge blocked by data quality. |
| 2026-04-10 | [[jonny-smith]] | Connectivity Ops Manager | MCP telemetry needs domain-specific data quality filters (GPS fix thresholds) before customer-facing AI. |
| 2026-04-10 | [[javier]] | Engineer | Acquisition AI: "surface everywhere" strategy. Flock API MCP exists (Chris built it). 2-week quoting PoC. |
| 2026-04-10 | [[liam-thomson]] | Marketing Manager | One-person marketing team. Flock ranks first for "connected fleet insurance" in AI search. |
| 2026-04-10 | [[mima]] | Product Manager | AI adoption segmentation model. Personal OS in VS Code. Style guides for communication. |
| 2026-04-13 | [[sophie-dodds]] | Broker Distribution Mgr | HubSpot cleanup is year-long effort. Needs ready-made tools, not open-ended exploration. |
| 2026-04-14 | [[matt-dipre]] | Financial Analyst | Invoice automation broken by NetSuite update. Blocked on Looker + HubSpot AI access. Keen builder stuck behind permissions. |
| 2026-04-14 | [[matt]] | Head of Product | Three adoption cohorts confirmed. "Last mile" metrics interpretation problem. Acquisition/expansion boundary unclear. |
| — | [[jade-mounir]] | VP of Finance | _Not yet scheduled_ |
