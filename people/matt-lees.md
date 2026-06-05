---
title: Matt Lees
created: 2026-04-02
updated: 2026-04-02
type: person
role: Enterprise Fleet Lead
team: Distribution (reports to Adam Smith)
tags: [distribution, enterprise, ai-advanced, lovable, skills, agents, apollo]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-02
---

## Role

Enterprise Fleet Lead

## Team

Distribution — reports to [[adam-smith|Adam Smith]]

## Relationship

Not yet spoken to directly. Context from Adam's discovery call, Slack thread (Mima/Jordi/Matt Price), and Notion documentation Matt produced.

## Working style notes

- Most advanced non-engineering AI user in the company — by a significant margin
- Proactive documenter — Loom walkthroughs, Notion process docs, technical reviews written unprompted
- Comfortable with Claude skills, MCP integrations (Looker, Gmail, Slack, Granola, Apollo, Google Drive), Lovable for document generation
- Graceful when pushed back — accepted Mima's and Jordi's governance positions without friction
- Recovering from Achilles rupture — working remotely, testing trips to office
- Adam groups him with Matt Price and Ollie Crowe as someone who needs freedom, not frameworks
- Writes detailed technical documentation that would pass engineering review

## Current AI work

### 1. TCO / Flock Value Statement documents

Client-facing value documents for new business and renewal opportunities:
- **Scope**: Courier & Trades risks over £100k premium
- **Pipeline**: HubSpot auto-generates TCO tickets when deals meet criteria
- **Process**: 12-step workflow — CCE upload → Lovable template → claims modelling → PDF export → HubSpot tracked link
- **Data sources**: HubSpot deals, G Drive CCE documents, claims listings, Lovable prototype
- Claude skill reviews client info via MCP, outputs Lovable prompt with all data
- Human-in-the-loop: CSM and UW sign off before client sees output
- New business template in use; renewal template still being finalised
- Full process documented in Notion + 3-part Loom series
- Working examples: Spectrum Comms, Beaz Logistics

**Status**: Moving toward automation. Mima and Matt discussed replacing Lovable pipeline with Claude + HubSpot MCP (2026-04-08). Target: ~80% automated, document appears in submission folder without Matt's involvement. Simplifying output for everyday cases — headline metrics only, bespoke decks retained for large risks. Snowflake CCA extraction (Tom's prior work) reusable. See [[2026-04-08-value-statement-automation]].

### 2. Enterprise Engine — autonomous agent pipeline

**This is the big one.** 9 scheduled autonomous agents running on Claude Cowork, managing a full enterprise sales pipeline:

- Pipeline: **64 accounts, £294M estimated premium** (was 18 accounts on 31 Mar)
- 22% reply rate on first outreach batch
- Runs on weekday schedules, all output to Matt's Slack DM — nothing posts to team channels
- Human-in-the-loop: agents create Gmail **drafts only** — Matt reviews and sends manually

**Agent chain:**

| Time | Agent | Purpose |
|------|-------|---------|
| 06:15 | Email-CRM Sync | Scan Gmail for replies/bounces/OOOs, update pipeline |
| 06:30 | Pipeline Validator | Score accounts by urgency/premium/completeness |
| 07:00 | Research & Enrichment | Apollo + web to verify emails, fill gaps (8-12 accounts/run) |
| 07:45 | Outreach Drafts | Personalised emails via approved template, 3-day follow-up rule |
| 08:00 | Daily Briefing | Summary of overnight outputs → Slack DM |
| 08:15 | Outreach Validator | Cross-ref contacts across Gmail, Slack, Granola, web |
| 17:00 | Pipeline Expansion | Apollo + web to discover 8-12 new accounts/day matching ICP |
| 17:30 | Action Plan Updater | Refresh MEDDPICC-scored account action plans |
| Fri 17:00 | Weekly Report | Funnel analysis, outreach metrics, wins/risks |

**MCP connectors**: Gmail, Slack, Granola, Apollo.io, Google Drive, Notion

**Cost**: ~910K tokens/day (~25-30M tokens/month). Apollo Growth plan $104/month. All within existing Claude Team plan.

**Account action plans**: MEDDPICC-scored, auto-updated daily, stored as HTML cards + JSON in Google Drive.

**Data security**: Local JSON file, no external sync. Gmail read + draft only. Agents run under Matt's Cowork session only. Open question for Fergus on storage approach as pipeline scales past 100 accounts.

**Matt's recommendation**: Current agent approach covers 90% of workflow. API integration only needed for real-time enrichment during calls and bulk segment discovery.

## Context: enterprise prospecting strategy

- Joined Flock Aug 2024 with mandate to accelerate direct sales — early activity manual/AI-assisted
- Direct outreach at scale created friction with broker relationships → paused as part of 2025 strategy rethink
- Focus shifted to Flock Value/TCO project — enterprise prospecting had less attention in recent months
- **Revised strategy**: build awareness with senior stakeholders at large fleet operators ahead of the submission process
- **Admiral acquisition** is the accelerant — goal is to maximise that moment by getting in front of decision-makers
- Core objective: get large fleet operators proactively directing their broker to include Flock at submission
- All direct messaging broker-friendly — positioning Flock as a specialist worth asking their broker about
- On large risks, Flock is often either not established with the relevant national broker, or that broker has no incentive/awareness to bring Flock in
- The agents automate the churn (contact finding, email verification, research, prioritisation) so Matt can focus on direct presentations
- "Have an agent surface the high-value activities each week, so I can just action them"
- **Not yet connected to HubSpot** — pipeline entirely in local JSON. Biggest gap and easiest governance win.
- Self-describes as "a layman" — he's not, but powerful framing for the capability uplift story

## Current state (2026-05-26)

**Major strategic shift since April:**
- TCO value docs: now only for deals >£500k on request (was all deals meeting threshold). Strategic change led by Adam and Tom.
- Enterprise prospecting email automation: **abandoned**. Single-digit response rates despite compelling Admiral story. Pivoted to phone calls as primary outreach.
- AI role: now "chief of staff" — daily briefs, accountability coaching, task prioritisation. Claude Co-Work project with full role context.
- Target list: **600 companies** (was 64 in April). Refreshed periodically. Prioritisation: renewal timing, telematics investments, fleet size 500–2,000 vehicles.
- £2M deal example: Claude built a layman's model of excess options + connectivity requirements → Matt challenged underwriting/pricing from an informed position.
- Wants automated Granola ingestion from Google Calendar → [[AI-063]]
- Distribution second brain: saw the value, asked the right question ("what's the team use case?"). Not yet clear.
- Adam's read: Matt has a tendency to over-engineer. Told him directly to start basic.
- Underwriters reluctant to document in HubSpot — flagged as cross-team adoption challenge.

## AI Activation

**Stage**: 4 — Multi-agent orchestration (non-engineering ceiling)
**Confidence**: high
**Assessed**: 2026-06-02
**Evidence**: 9 scheduled autonomous agents managing a full enterprise sales pipeline (600 companies, MEDDPICC scoring, £2M deal decision support). MCP connectors: Gmail, Slack, Granola, Apollo, Google Drive, Notion. CoWork "chief of staff" project for daily briefs, coaching, and task prioritisation. Built and adapted the Enterprise Engine based on what actually works (abandoned email automation, pivoted to phone + AI prep). Adam's read: has a tendency to over-engineer — told him directly to start basic.

**Not Stage 3**: Scheduling, coordination, and autonomous operation across 9 agents is well past conversational fluency. The pipeline runs without his involvement — that's delegation at scale.
**Not Stage 5**: No evidence of adherence measurement or context quality testing. Adam's note (over-engineers) suggests he hasn't yet hit the meta-level thinking of Stage 5 — he's building prolifically but not measuring whether the builds adhere correctly.
**To progress**: Apply empirical context testing to the Enterprise Engine — does changing the prompt actually improve agent output quality, or does it just feel better? That measurement step is the Stage 4→5 transition. Moving from "it works" to "I know why it works."
**Framework note**: Highest Stage 4 outside the engineering team. The coaching/chief-of-staff use case is the clearest "secretary → strategic partner" progression in the company. The 9-agent pipeline is an impressive build; the over-engineering tendency is the thing that keeps it at Stage 4.

## 1:1 Log

### 2026-04-02 (Slack)

- Enterprise Engine is new capability, not time saved — prospecting was paused because manual approach didn't work
- Admiral acquisition timing driving the push
- Flock Value Statement work (with Mima/Jordi) is separate — about sales materials, not pipeline management
- Mima: further automation on value statements pending, subject to Q2 OKR progress on simplifying value sales approach

### 2026-04-08 — Value Statement automation workshop (with Mima, Tom absent)

- Discussed replacing Lovable pipeline with Claude + HubSpot MCP for new business value docs
- Goal: remove Matt from process entirely — document appears automatically in submission folder
- Could trigger automatically on TCO ticket creation. Snowflake CCA data (Tom's prior work) reusable.
- Target: ~80% automated with human check. Simplify output to headline metrics for everyday cases.
- Renewal to follow with same logic. Sub-£100K fleets: no near-term extension.
- Longer-term: submissions data into data lake is a prerequisite for scaling.
- See [[2026-04-08-value-statement-automation]]

### 2026-04-02 (call with Fergus + Tom)

- Fergus gave thumbs up — keep going, keep Antton in the loop
- Previous direct outreach created broker friction — brokers saw it as a threat, clients wanted cheaper direct rates. Paused and restarted with broker-led message: "introduce your broker, don't bypass them"
- Target: 200+ vehicle fleets. Sweet spot avoids mega-fleets that self-insure. 6-9 month sales cycle ahead of renewal.
- Admiral acquisition driving urgency — using it in subject lines
- Apollo self-identified email bounce-backs and suggested its own integration — agent improved itself
- HubSpot connector is next priority — store enriched data on company records, not deal records
- Must back up Cowork files to Google Drive — laptop loss is the main risk today
- Tom: 15 mins next week to review front end, share tips (PDF via Claude instead of Lovable, email templates, backup habits)

### 2026-04-07 — Enterprise Engine Review 002

- **HubSpot connected this morning** (Emily got it sorted). Read-only initially, will test write permissions incrementally
- Confirmed direction: AI data goes on **company records**, not deal records (resolves AI-005)
- Matt to align with Emily and Adam on data structure
- Pipeline scheduling issue: tasks trigger on first login when laptop's asleep. Needs sleep mode disabled.
- Pre-loaded target fleet list from a 12-month-old manual exercise — skips business search step, accelerates enrichment
- Phasing: ~2 weeks max on enrichment, then pause and focus on churn of existing contacts
- Reconsidering Lovable front-end — Claude already surfacing next 10 actions conversationally. May shift to HubSpot dashboard if data lives there.
- Adam interested in replicating the agent workflow for broker contacts — pending HubSpot proof
- Discussed Claude best practices: push files over memory, end-of-session encoding ritual, explain the *why* with priorities

### 2026-05-26 — AI Catchup

- TCO value docs narrowed to >£500k on request. Email pipeline abandoned (single-digit response rates). Pivoted to phone calls + AI chief of staff.
- 600 target companies; cherry-picked by renewal timing, telematics signals, fleet size 500–2,000
- Claude Co-Work project: daily briefs, accountability coaching, task prioritisation
- £2M deal: layman's model of excess options built by Claude → challenged underwriting/pricing
- Distribution second brain concept raised; team-level use case unresolved
- Wants Granola auto-ingestion from Google Calendar as a scheduled task → [[AI-063]]
- Underwriters reluctant to document in HubSpot — flagged as adoption gap
- Tom's note: tool-sharpening risk now spreads company-wide. Anton's pragmatic grounding is valuable.
- Adam's read (2026-05-27): Matt over-engineers. Told him directly to start basic.
- See [[2026-05-26-matt-lees-ai-catchup]]
