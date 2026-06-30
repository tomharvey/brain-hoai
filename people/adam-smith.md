---
title: Adam Smith
created: 2026-03-27
updated: 2026-06-30
type: person
role: Head of Distribution
team: Distribution
tags: [distribution, leadership, granola, hubspot, trading-pack, strategic-partner]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-30
---

## Role

Head of Distribution

## Team

Distribution — direct reports: Alex Dyball, Liam Thomson, Matthew Lees, Sophie Dodds (+ new hire incoming)

## Relationship

First spoke 2026-04-02. Positive, collaborative, wants structured support for his team.

## Working style notes

- Philosophy: "selfish with AI" — team should use AI as an efficiency tool, not spend time building models
- Wants a ready-made **toolkit** for the team (slide decks, broker prioritisation, data interrogation) rather than asking them to explore and build
- Distinguishes between advanced users (Matt, Ollie) who need freedom and the broader team (Sophie, Alex, new hire) who need structured tools
- All team using Granola on every meeting — shared folder as queryable broker knowledge base
- Kirsty integrated trading data into Looker via MCP — review packs can be auto-generated
- HubSpot clean-up project with Emily to enable richer broker data
- Thinks in terms of "fundamentals first, then free exploration on top"

## AI Activation

**Stage**: 4 — Delegation
**Confidence**: high
**Assessed**: 2026-06-30
**Evidence**: Built a Claude trading review project for SLT + trading team; runs scheduled inbox cleanup automation; uses Claude as strategic partner for complex stakeholder navigation (Admiral paper, leadership coaching via Granola transcripts). Independently developed AI-as-coach usage pattern. **Quality concern (Jun 11)**: Fergus reported that at a trading meeting, "almost on every slide, it was like those numbers don't look right" — the trading pack had data integrity issues presented to SLT. This is the "output ownership" failure mode: delegating without sufficient validation of the output. **Jun 15 update**: Built trading report pack skill in co:work. Built activity tracking dashboard for team performance (meetings, calls, face-to-face split). Using Granola transcripts for personal coaching/post-call analysis. Articulated clear AI team vision: librarian (data lookup), secretary (prioritization/scheduling), coach (personal development + sales playbook). Managing 356 broker accounts with 2.5 BDMs. New BDM starting Jul 21. Wants AI to help identify, diagnose, then let team take action.

**Not Stage 3**: Running scheduled automations and delegating whole workflows (inbox, trading pack, coaching). Well past fluency. Now building team-level tools (activity dashboard) and articulating product-level AI vision.
**Not Stage 5**: The Jun 11 data integrity failure shows he's not yet measuring or validating AI output systematically. He's delegating at scale but the quality assurance layer is missing. HubSpot data quality acknowledged as messy — validation infrastructure not yet in place.
**To progress**: Instrument the trading pack with validation queries — SQL persistence + Kirsty sign-off before presenting to SLT. The "output ownership" lesson is the most important one for Q3. Team toolkit consistency (2-3 common workflows everyone runs) is the bridge to Stage 5 — directing a system, not just delegating individual tasks.

## Broker segmentation (as of 2026-05-27)

Four tiers: **champion** (strong existing support) → **accelerator** (short-term potential, laser focus) → **potential** → **foundation**

Accelerator brokers have a Notion dashboard. Currently static PDF; Adam wants it live-updating.

## Current AI work (2026-05-27)

### Trading review project
- Claude Chat project (not Co-Work) shared with SLT and trading team
- Monthly trading pack: executive summary → pipeline by segment → conversion → broker performance (top 10 retail) → lost reasons → 30-day forecast
- Before: screenshots + manual RAG dots in PowerPoint. Estimated equivalent: 3 junior staff.
- Kirsty co-owns the project; verifying data sources when back from holiday → [[AI-065]]
- Pack "signed off" — next run is the consistency test
- Outstanding: pack consistency follow-up (occasional re-teaching needed)

### Inbox automation
- Scheduled task every couple of days: removes spam and OOOs from broker Flock inbox, keeps HubSpot tickets manageable

### AI as strategic/coaching partner
- Fed Granola transcripts + 1:1 feedback → Claude as leadership coach ("reviews past meetings, scores interactions, recommends prep for upcoming ones")
- Admiral paper: three-stakeholder navigation (internal Flock / personal objectives / Admiral). Recorded conversation with father (former haulage broker) on Granola → fed into the thread → AI verified against paper objectives
- Pattern: secretary → coach → strategic partner. Emerged independently, not prompted by Tom.

## Working style notes (updated)

- Philosophy: "selfish with AI" — team should use AI as an efficiency tool, not spend time building models
- His read on Matt Lees: "tendency to start with the most complicated, scalable solution possible." Told Matt directly to start basic.
- Wants to build structures for the team to move into, rather than asking each person to build from scratch
- "Be incredibly selfish with what you want from AI" — his message to the team
- Thinks in terms of "fundamentals first, then free exploration on top"
- Attends AI Breakfast — coming to co-work + scheduling workshop

## 1:1 Log

### 2026-06-15 — BDM Dashboards

- Built trading report pack skill in co:work session
- Activity tracking dashboard: BDM activity index (meetings, calls, face-to-face split) for team performance visibility
- Using Granola transcripts for personal coaching and post-call analysis
- Wants team to share best practices — sees need for consistent toolkit across BDMs
- Articulated three-role AI vision: librarian (data lookup), secretary (prioritization/scheduling), coach (personal development + sales playbook)
- Managing 356 broker accounts with 2.5 BDMs — scale demands AI leverage
- New BDM starting Jul 21 — wants AI-first onboarding
- Wants AI to help identify and diagnose issues, then let team take action (not full automation)
- Using broker pulse concepts for prioritization
- HubSpot data quality acknowledged as messy — Brown & Brown complexity persists

### 2026-06-10 — BDM Team AI

- Trading pack data integrity issue: discrepancies in June SLT pack. Adam to share skill + discrepancy transcript; Tom to review prompts and suggest SQL query persistence pattern; Kirsty to validate queries → [[AI-097]]
- Team toolkit vision: wants 2–3 common workflows everyone runs consistently, not more individual exploration. Ollie's broker pulse, Jake's UW dashboard, EOD activity briefs, quarterly review packs are the candidates.
- Activity dashboard built over weekend: BDM activity index (meetings, face-to-face, calls) by broker tier. Calendar-sourced (non-Google-Meet location = face-to-face). Wants team logging phone calls in HubSpot but without double-entry burden.
- HubSpot architecture confirmed: FP&A/Looker (Kirsty) = trading number source of truth. HubSpot = activity detail layer. Notion = strategy/playbook only. HubSpot is genuinely messy — Brown & Brown has 60 child companies with scattered contacts.
- Quick call gap: won't log a mobile callback. EOD Granola voice wrap-up was well received.
- Three coaching layers: (1) personal development / communication style, (2) post-meeting performance feedback, (3) sales playbook alignment (team-wide).
- End-state: distribution broker performance signals feed into Jake's underwriting priority dashboard. Can't get there while tools are isolated.
- New BDM joining 21 July — wants AI-first onboarding; Tom flagged as co:work onboarding experiment → [[AI-095]]
- Tripartite session needed: Tom + Adam + Ollie before team session → [[AI-072]]
- See [[2026-06-10-adam-thomas-bdm-team-ai]]

### 2026-05-27 — AI Catchup
- Trading review project live and shared with SLT trading team — "amazing" quality
- AI-as-coach usage confirmed (independently, same as Matt Lees and Alex Dyball)
- Accelerator broker dashboard: wants live-updating Notion page (Kirsty + scheduled task)
- Matt Lees assessment: over-engineers, needs guardrails not capability uplift
- Tom flagged secretary→coach→strategic partner pattern for Rakhee
- AI Breakfast attendance confirmed
- See [[2026-05-27-adam-ai-catchup]]

### 2026-04-02 — AI Discovery
- Distribution = ~300 brokers, some with 50+ UK offices, high-touch account management
- Team already using Granola (shared folder), ChatGPT/Claude for data interrogation, Kirsty's Looker MCP
- Wants distribution-specific AI toolkit: slide production, broker prioritisation, data interrogation skills
- Granola as accidental CRM — solves decades-old problem of salespeople not filling in Salesforce
- HubSpot thin on broker account data — joint project with Emily to clean up
- Ideal pipeline: Granola → HubSpot → Claude via MCP
- Semantic/naming consistency across systems is a prerequisite
- Tom to act as bridge between advanced users and broader team
