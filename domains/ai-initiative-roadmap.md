---
title: AI initiative roadmap
created: 2026-04-22
updated: 2026-04-22
domain: ai-enablement
type: reference
status: active
tags: [roadmap, strategy, now-next-later]
---

# AI Initiative Roadmap

9-month horizon. Stages represent commitment, not time. Reviewed quarterly by SLT, tied to OKRs.

> Follows the ProdTech Now/Next/Later framework — see [[ProdTech Roadmaps Q2 2026.pdf]].

---

## NOW — Resourced or in progress

### AI capability uplift

**Outcome**: Every department designs processes with AI independently. Emily's ops team is the reference model — replicate it.

- **Owner**: Tom Harvey
- **Domain**: ai-enablement
- **Key detail**: Discovery round complete (20+ conversations). Four capability cohorts identified (builders, active users, stuck, observers). Shifting from group workshops to applied 1:1 pairing on real use cases. Department-specific starter kits in design.
- **Vault**: [[ai-capability-uplift]]

### AI-native engineering

**Outcome**: Engineers shift from mechanical coding to architectural thinking. AI generates draft PRs from tickets; humans review and teach.

- **Owner**: Javier Pallares (build) / Tom Harvey (sponsor)
- **Domain**: engineering-workflows
- **Key detail**: Month-long pilot on Acquisition AI PoC. Local-first harness turning Linear tickets into draft PRs. Hypothesis: AI teaching shifts engineers from mechanical coding to architectural thinking.
- **Vault**: [[ai-native-engineering]]

### Operational AI automation

**Outcome**: Ops team eliminates manual workflows that cost hours/day — NOC letters, submissions, renewals, driver referrals.

- **Owner**: Emily Staton (ops) / Tom Harvey (cross-cutting)
- **Domain**: operational-tooling
- **Key detail**: Multiple active workstreams. Shreya's NOC skill working end-to-end. Submissions fragmented across three groups — needs consolidation. Renewals process mapped (4 manual steps that should be 1). Kirsty's Looker→Claude connection is the key enabler.
- **Vault**: [[underwriting-assistance-ai]], [[submissions-automation]], [[cc-extraction-handover]]

### Claude standardisation

**Outcome**: One AI platform, company-wide. Enterprise deal, shared seats, rate limits unblocked. Foundation for everything else.

- **Owner**: Tom Harvey
- **Domain**: ai-enablement
- **Key detail**: Company split between Claude/ChatGPT. Skills, MCPs, plugins all Claude-ecosystem. Enterprise deal needed — rate limits already a constraint (Matt Lees hit cap). Skills repo exists but ungoverned.
- **Vault**: [[claude-standardisation]], [[skills-distribution]]

---

## NEXT — Clear need, know how we'd measure success

### AI governance framework

**Outcome**: Registry of all AI tools/skills/agents. Eval suite for quality. Sprawl prevention ("check before you build").

- **Owner**: Tom Harvey + Sam (risk) + Paul O'Neill (compliance)
- **Domain**: ai-enablement
- **Why not now**: Deferred to later Q2. Needs compliance measurement baseline first (Paul's thesis: can't govern what you don't measure). Sam redirected to evals + documentation for Q2.
- **Vault**: [[ai-governance-framework]]

### Productionised agent framework

**Outcome**: Agents move from laptops to production infrastructure with monitoring, deployment standards, and backup. Enterprise Engine is the reference case.

- **Owner**: Tom Harvey + Chris Fothergill + Jordi Pallares Roset
- **Domain**: engineering-workflows
- **Why not now**: Architecture docs (Chris) are a prerequisite. Token monitoring and infra decisions not yet made. Need to agree where agent services sit with Chris/Jordi.
- **Vault**: [[agent-framework]]

### Insight layer

**Outcome**: Queryable AI across data pools — CCs, telemetry, HubSpot, Granola, broker submissions. Company treats insight as naturally as telemetry.

- **Owner**: TBD (Matt Price, Kirsty, Tom Harvey in discussion)
- **Domain**: product-ai
- **Why not now**: No narrow first use case anchored. Cloud MCP deployment needed first. Kirsty's Looker+AI paragraphs is the proof point but hasn't been generalised.
- **Vault**: [[insight-layer]]

---

## LATER — Candidates for prioritisation

### AI as product interface

Chat, visualisation, agent-driven workflows replace CRUD forms. WhatsApp bot and safety agent are early signals. What Web 2.0 did with input fields, agents will do with conversations.

- **Domain**: product-ai
- **Vault**: [[whatsapp-driver-reporting]], [[safety-agent-memory]]

### Process documentation at scale

"Load-bearing Google Sheets" need to become governed knowledge before reliable automation is possible. PostHog/DOM analysis (Geran) could shortcut manual documentation.

- **Domain**: operational-tooling
- **Vault**: [[process-documentation]], [[posthog-workflow-analysis]]

### Self-improving agents

Memory pattern from safety agent generalises to underwriting and submissions. Corrections make agents better, not just faster. Ishmael's work is the reference implementation.

- **Domain**: product-ai
- **Vault**: [[safety-agent-memory]]

### Disconnected fleets

Insurance for non-connected commercial fleets. Acquisition funnel or dedicated loss ratio play — would require a dedicated squad.

- **Domain**: product-ai

### E-trading automation

Fully automated quoting. AI could replace the 16-page broker form with a conversation. Challenge: brokers won't complete forms without incentives.

- **Domain**: product-ai
