---
title: AI capability baseline — April 2026
created: 2026-04-13
updated: 2026-04-13
domain: ai-enablement
type: reference
tags: [capability, baseline, measurement, strategy]
---

## Purpose

Snapshot of AI capability across the company as of mid-April 2026, after 3 weeks of discovery (20+ conversations). Two uses:

1. **Measurement** — track progress against this baseline over time
2. **Strategy** — design department-specific uplift paths based on where each team actually is

## Maturity scale

| Level | Label | Description |
|-------|-------|-------------|
| 1 | **Unaware** | No usage, no exposure |
| 2 | **Exploring** | Tried tools, intermittent use, doesn't stick |
| 3 | **Daily user** | AI integrated into daily workflow |
| 4 | **Designing with AI** | New processes designed AI-first |
| 5 | **Building with AI** | Creating agents, skills, automation infrastructure |

---

## Department summaries

### Ops (Emily Staton's team) — Maturity: 4

**The reference model.** Daily AI usage across the entire team. Emily designs new processes with AI in mind from the start — this is the behaviour we want to replicate everywhere.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Emily | 4 | Claude, ChatGPT, Zapier | Process design, compliance checking, forecasting |
| Shreya | 5 | Claude, HubSpot MCP, Zapier | Built NOC letter generator skill independently |
| Anna | 3–4 | Claude, HubSpot MCP | Migrated ChatGPT→Claude, renewals process mapping |
| Fred | 2–3 | Claude | VRN extraction, document parsing. Early stage but receptive |

**What's working:**
- Zapier as automation backbone (transfer of agency fix, deviation tracking)
- Claude replacing ChatGPT based on evidence (better PDF handling)
- Shreya building skills without engineering support
- Cultural shift: "We're relying more on Claude now than tech automation"

**Gaps:**
- Fred's HubSpot not connected to Claude (quick win)
- Retool dependency blocks NOC steps 6-8
- Renewals flow has 3 spreadsheets that should be eliminated, not automated
- Zapier automations becoming load-bearing without engineering visibility

**Recommended intervention:** Document this team as the reference model. Help Fred connect HubSpot. Unblock renewals via Looker MCP cloud deployment (AI-010).

---

### Engineering — Maturity: 3 (with pockets of 5)

**Building foundations, not yet scaled.** Power users shipping value (Chris on architecture docs, Jordi on Engine Room triage, Ollie on WhatsApp bot). Main gaps are coordination, governance, and code quality feedback loops.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Chris Fothergill | 4 | Claude Code | Architecture documentation for AI consumption, skills from docs |
| Jordi | 4 | Bedrock, Lambda | Engine Room triage automation MVP |
| Abs | 5 | Claude | CC extraction tool (leaving soon — knowledge transfer risk) |
| Mima | 5 | Claude, PromptFoo | 111 eval test cases, `/create-test-cases` skill, deck builder |
| Ismael | 3–4 | Claude, Datadog | Safety agent with memory, observability integration |
| Javier | 4 | Claude, Flock API MCP | Acquisition AI vision, HubSpot→Claude→Flock API PoC |
| Ollie | 4–5 | Claude, Twilio | WhatsApp bot (1.5hrs to MVP), Co-Work workshop lead |
| Sam | 2–3 | Claude | AI governance/security PhD. Redirected from AI CoP to evals |

**What's working:**
- Eval testing framework (111 cases, stakeholder-friendly test creation)
- Architecture documentation for Claude consumption (Chris)
- Fast prototyping culture (Ollie: 1.5hrs to WhatsApp bot)
- No philosophical resistance to AI — scepticism is about execution, not the tool

**Gaps:**
- AI-generated code quality in PRs (multiple review iterations, doesn't meet standards)
- Three independent groups on submissions — no coordination
- Skills governance undefined (public vs private, testing before distribution)
- Cursor adoption low among engineers (PMs using it more)
- Abs leaving — CC extraction knowledge transfer needed

**Recommended intervention:** Define skills governance standards (Jordi's concern). Address code quality via Chris's architecture docs → skills pipeline. Consolidate submissions work before Abs leaves.

---

### Product — Maturity: 4–5

**Most advanced team by breadth.** Running production agents (Matt Lees), building governance infrastructure (Mima), and shifting PM workflows to Cursor/Claude. Output quality is the main gap.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Matt Price | 3–4 | Cursor, Claude | PM IDE shift, process codification thinking |
| Mima | 5 | Claude, PromptFoo, Cursor | Eval testing, deck builder skill, test case creation |
| Matt Lees* | 5 | Claude + 6 MCPs | 9-agent Enterprise Engine, £294M pipeline |
| Ollie* | 4–5 | Claude, Twilio | WhatsApp bot, Co-Work workshop lead |

*Sits under Distribution but product-adjacent in AI maturity.

**What's working:**
- Enterprise Engine: non-technical PM built 9-agent pipeline in 5 days, 22% reply rate
- Eval framework: 111 test cases, red team/security coverage, stakeholder-accessible
- Deck builder skill: brand-consistent presentations from Claude
- PMs adopting VS Code forks for product work (significant behavioural shift)

**Gaps:**
- AI output quality: verbose, low signal-to-noise ("need agents to edit agent output")
- Value Statement automation paused pending product-market fit clarity
- Bus factor on Enterprise Engine (local JSON, no external sync)
- Cowork projects can't be shared between team members

**Recommended intervention:** Style guides to address output quality (Jemima working on this). Externalise Enterprise Engine data to HubSpot (in progress). Scale eval framework to other teams.

---

### Distribution (Adam Smith's team) — Maturity: 2 (with tier-3 outliers)

**Widest spectrum in the company.** Ranges from Sophie (needs a toolkit) to Matt Lees (built an enterprise agent system). Adam's thesis: "selfish with AI" — use it for efficiency, don't build models.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Sophie Dodds | 2 | Granola, Claude | Broker map project, switching from ChatGPT |
| Alex Dyball | 3 | ChatGPT (primary), Claude, Looker MCP | High-volume pragmatist, meeting self-scoring |
| Liam Thomson | 3 | ChatGPT, Claude, Lovable, Artlist | One-person marketing, AI as brainstorming partner |
| Matt Lees | 5 | Claude + 6 MCPs, Lovable, Apollo | Enterprise Engine (see Product section) |
| Ollie Crowe | 4–5 | Claude, Twilio | WhatsApp bot, workshop lead |

**What's working:**
- Granola as accidental CRM: broker knowledge now queryable across team
- Alex's high-volume pragmatism: 5+ daily interactions, AI is embedded
- Meeting self-scoring pattern (Alex): replicable across company
- Matt Lees as proof point for the board

**Gaps:**
- No standardised toolkit for the middle (Sophie, Alex, new hire)
- Workshop scheduling conflicts: broker meetings always win
- Mima's presentation skill: only 3 users despite multiple comms
- Scattered tooling: ChatGPT, Claude, Lovable, Artlist — no standard
- Sophie blocked by dying laptop (physical blocker)

**Recommended intervention:** Build distribution-specific toolkit with Adam (slide decks, broker prioritisation, data interrogation). Book team session with Kirsty for Looker MCP. Share Alex's meeting self-scoring as a replicable pattern.

---

### Finance — Maturity: 3 (with tier-5 outlier)

**Higher than expected.** Kirsty is a standout power user building capabilities that were previously impossible in standard BI tools. Rest of team trialling locally.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Kirsty Alexandre | 5 | Claude, Looker MCP | AI-generated financial insights, driver tree dashboard |
| Christian Nielsen | 2 | Claude (trialling) | CFO, exploring locally |
| Kevin Berg | 2 | Claude (trialling) | FP&A, exploring locally |
| David Pilley | 2 | Claude (trialling) | Financial planning, exploring locally |
| Jade Mounir | 2 | Claude | VP Finance, discovery done |

**What's working:**
- Kirsty's Looker→Claude MCP: AI-generated insights changing business decisions
- Fleet Evolution example: £600K lost deal — AI surfaced that customer chose AIG for payment terms, not price. Directly contradicts "we're priced too high" narrative.
- Trade segment insight: 57% of submissions, only 19% convert — actionable deprioritisation signal
- Review pack generation for distribution team
- ICP analysis in progress (data-driven vs Adam's assumptions)

**Gaps:**
- Cloud MCP deployment (AI-010) — Kirsty runs locally, can't scale to team
- Persistent insight problem: weekly insights become stale if not tracked
- Infrastructure support needed to move from prototype to production
- Rest of team at exploring stage — no defined pathway

**Recommended intervention:** Prioritise AI-010 (Looker MCP cloud deployment) — this unblocks Finance, Distribution review packs, and Renewals automation. Design a pathway from Kirsty's local setup to team-wide access.

---

### Underwriting — Maturity: Unknown (gap area)

**Critical discovery gap.** Ops-side underwriting assistance is covered (see Ops section). Core underwriting team — Darren, Billy, and underwriters — has not been engaged. Darren has "siloed AI work" (Chris flagged) but no visibility into what or how mature.

| Person | Level | Tools | Key capability |
|--------|-------|-------|----------------|
| Darren McCauley | Unknown | Unknown | CUO. Excited about driver-level risk. Own AI work in progress. |
| Billy | Unknown | Manual spreadsheets | Renewals allocation. Won't delegate. Needs HubSpot equivalent views. |

**What we know:**
- Strategic ambitions exist: driver-level risk management, personal lines quoting potential
- Paul O'Neill flagged: system doesn't capture data against Admiral delegated authority guardrails — can't measure compliance, therefore can't deploy agents
- No underwriter has attended AI Breakfast

**Gaps:**
- No discovery with core underwriting team
- Data capture infrastructure missing for compliance measurement
- Billy's allocation workflow undocumented — blocks renewals automation (AI-007)

**Recommended intervention:** Schedule discovery with Darren and Billy as priority. Understand Darren's existing AI work before it diverges further. Billy conversation needed anyway for AI-007.

---

## Cross-cutting blockers

Ranked by frequency across discovery conversations:

| Blocker | Departments affected | Impact |
|---------|---------------------|--------|
| **HubSpot data quality** | All | Contact staleness, name mismatches, missing loss reasons, inconsistent tagging. Single most repeated blocker. Affects every automation that touches customer data. |
| **Looker MCP cloud deployment (AI-010)** | Finance, Ops, Distribution | Kirsty's integration is local-only. Cloud deployment unblocks team-wide access, renewals automation, and review pack generation. |
| **Skills governance** | Engineering, Product | No standards for testing/review before company-wide sharing. Jordi blocks distribution without validation. |
| **AI output quality** | Product, Engineering | Verbose, low signal-to-noise. Multiple PR review iterations. Style guides and editing agents needed. |
| **Workshop scheduling** | Distribution | Broker meetings always win. Distribution team can't attend existing sessions. Needs alternative format. |
| **Retool dependencies** | Ops | Manual steps in workflows that can't be automated until Retool is addressed or replaced. |
| **Data capture gaps** | Underwriting | Can't deploy compliance agents without capturing the data compliance needs to measure. |

---

## Capability cohorts

Discovery revealed four distinct cohorts. Each needs a different intervention — one-size-fits-all won't work.

| Cohort | Description | Intervention | Graduation signal |
|--------|-------------|-------------|-------------------|
| **Observer** | Aware AI exists, haven't found their use case | 1:1 pairing, show don't tell | Uses AI daily without prompting |
| **Operator** | Using AI daily for existing tasks | Ready-made skills, tool standardisation | Redesigns a process rather than just using AI within an existing one |
| **Designer** | Redesigning processes with AI in mind | Process support, unblocking dependencies | Creates something others can use (skill, agent, workflow) |
| **Builder** | Creating agents, skills, infrastructure | Governance, scaling infra, freedom | Systems run in production with monitoring |

### Current distribution (April 2026)

| Cohort | People | Count |
|--------|--------|-------|
| **Observer** | Fred, Sophie, Christian, Kevin, David, Jade | 6 |
| **Operator** | Alex, Liam, Anna, Sam | 4 |
| **Designer** | Shreya, Emily, Jordi, Ismael, Javier, Matt Price | 6 |
| **Builder** | Matt Lees, Kirsty, Mima, Chris, Abs, Ollie | 6 |
| **Unknown** | Darren, Billy, Geran + rest of underwriting | 3+ |

**Movement is the metric.** Fred becoming an Operator matters more than Matt Lees becoming a better Builder. Track heads per cohort quarterly — success is people moving right.

### What each cohort needs

**Observers** need a first win. Pair them with someone one level up, connect their tools (e.g. HubSpot to Claude), and give them a task they already do manually. Don't explain what AI can do — show them on their own data.

**Operators** need standardisation. They're already using AI but with scattered tooling (ChatGPT here, Claude there, Lovable elsewhere). Give them ready-made skills, a standard tool, and replicable patterns (e.g. Alex's meeting self-scoring).

**Designers** need unblocking. They know what to build but hit infrastructure walls (cloud MCP, HubSpot data quality, Retool dependencies). Remove blockers and they'll move themselves.

**Builders** need governance and infrastructure. They're already shipping — the risk is ungoverned systems becoming load-bearing. Give them monitoring, testing frameworks, data structure alignment, and peer review.

---

## Strategic recommendations

### 1. Fix HubSpot data quality (foundation for everything)

Every department hits this wall. No automation scales on dirty data. This isn't an AI initiative — it's a data initiative that AI makes urgent. Coordinate Emily + Sophie's ongoing cleanup with engineering visibility.

### 2. Deploy Looker MCP to cloud (AI-010) — highest-leverage unblock

One infrastructure change unblocks: Finance team access, Distribution review packs, Renewals automation (AI-007), and broader analytics-via-AI adoption. This is the single highest-ROI technical task.

### 3. Design uplift tracks per cohort, not one programme

| Cohort | Format | Goal | Timeline |
|--------|--------|------|----------|
| **Observers** | 1:1 pairing + tool connection | First productive daily use | 1 week |
| **Operators** | Ready-made skills + standard tooling | Consistent, repeatable workflows | 2 weeks |
| **Designers** | Blocker removal + process workshops | One new AI-first process designed | 1 month |
| **Builders** | Governance framework + infra support | Production-grade with monitoring | Ongoing |

### 4. Discover underwriting (Darren + Billy)

Biggest gap in the baseline. Strategic value (driver-level risk, compliance measurement) but zero visibility. Schedule before board roadmap if possible.

### 5. Replicate Emily's monthly sync model

Ops team has a running AI/Automations sync that builds peer accountability and surfaces wins. Other departments should have equivalent forums — adapt format per team, don't impose Ops model wholesale.

### 6. Address the "saturation of the willing"

People who were going to attend AI Breakfast have attended. The persuadable middle (open but confused) needs different entry points: 1:1 pairing, department workshops, ready-made skills they can try immediately. The reluctant (no underwriter at AI Breakfast) need leadership air cover and peer examples.

---

## Measurement framework

Re-assess quarterly. Primary metric: **cohort movement** — people graduating to the next level.

### Cohort tracking

| Cohort | Apr 2026 | Jul 2026 (target) |
|--------|----------|-------------------|
| **Observer** | 6 | 2 (move 4 to Operator) |
| **Operator** | 4 | 6 (absorb from Observer, move 2 to Designer) |
| **Designer** | 6 | 7 |
| **Builder** | 6 | 7 |
| **Unknown** | 3+ | 0 (discover all) |

### Supporting metrics

| Metric | How to measure | Baseline (Apr 2026) |
|--------|---------------|---------------------|
| **Daily AI users** | Count of people using AI tools daily | ~15-18 of ~40+ staff |
| **Skills/agents built** | Count of working Claude skills/agents | 4 (NOC, deck builder, Enterprise Engine, WhatsApp bot) |
| **Processes redesigned** | Count of workflows redesigned AI-first | 2 (transfer of agency, NOC) |
| **Cross-cutting blockers resolved** | Track blockers list above | 0 of 7 resolved |
| **Departments with AI sync** | Monthly forums like Emily's | 1 (Ops) |

---

## Links

- [[ai-capability-uplift]] — parent initiative
- [[AI-013-ai-capability-baseline-report]] — tracking issue
- [[ai-roadmap-draft]] — board roadmap (due Apr 20)
