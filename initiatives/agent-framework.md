---
title: Productionised agent framework
created: 2026-03-30
updated: 2026-03-30
domain: engineering-workflows
type: initiative
status: active
origin: directed
owner: tom
tags: [agents, framework, platform, token-monitoring, production]
---

## Summary

Move agents from side-of-desk prototypes to core platform assets. Includes token cost monitoring, standardised agent deployment as part of platform-services, and a framework that makes building agentic systems as natural as building non-agentic ones.

## Goal

Prodtech team deploys agentic systems as naturally as non-agentic. Agents are monitored, costed, and treated as production services — not experiments.

## Current state

- Tom built initial frameworks before the Head of AI role:
  - Token cost monitoring framework
  - Framework for deploying agents as core parts of platform-services
- Unclear whether these are live, adopted, or still PoC
- Chris working on architecture documentation and skills — related but focused on code standards, not agent deployment
- MCP server work kick-started by Tom as PoC, teams picked it up — "now needs a framework for feedback and a vision for where it goes"
- WhatsApp driver reporting bot ([[ollie-crowe|Ollie Crowe]]): deployed to render.com (Twilio, SQLite), not customer-facing. Testing with 1-2 fleets via Ben. If validated → WhatsApp becomes a platform service, AI part goes into the kit

## Dependencies

- [[platform-architecture-docs]] — Chris's work on standards feeds into how agents get built
- [[skills-distribution]] — skills are the knowledge layer agents consume
- Clarity on where agent services live in the platform (infrastructure decision)
- [[ai-governance-framework]] — eval suite and observability are the testing/monitoring layer for production agents

## Risks

- Agents proliferate without monitoring — token costs spiral
- No production standards = fragile agents that break and erode trust
- Engineering team busy with OKR delivery — agent framework seen as "nice to have"

## Next actions

- [ ] Audit current state of token monitoring and agent deployment frameworks — are they live?
- [ ] Discuss with Chris and Jordi where agent services sit in the platform architecture
- [ ] Define minimum viable production standard for an agent (monitoring, error handling, cost tracking)
- [ ] Identify one existing agent to move through the framework as a reference implementation
- [ ] Connect Datadog observability work (Ismael) to agent monitoring requirements — per-tool traces, latency, token costs
- [ ] Evaluate S3 agent output storage as part of production agent standard (compliance + analytics)

## Log

### 2026-03-30

- Created from pitch document review
- Tom built initial frameworks pre-role — status unclear
- MCP server work picked up by teams but needs vision for next step
- WhatsApp bot (Ollie Crowe) updated: deployed render.com, testing with fleets next, pathway to platform service if validated
- Engine Room triage automation tracked separately as [[engine-room-triage-automation]] — not part of this initiative yet
- **Matt Lees' Enterprise Engine (2026-04-02)**: 9 autonomous agents on Claude Cowork managing a £294M enterprise sales pipeline. Most sophisticated agent deployment in the company — running entirely on a Team plan under one person's session. Raises questions about production standards, token monitoring, and what happens when this needs to scale or transfer. This is the strongest argument yet for a proper agent framework.
  - Key insight: this is **new capability, not efficiency** — enterprise prospecting was paused because manual outreach at scale wasn't viable. The agents make a different strategy possible.
  - Cowork projects cannot be shared between team members — bus factor of 1, tied to Matt's laptop
  - **Not connected to HubSpot yet** — pipeline in local JSON only. HubSpot integration is the obvious next step and would address visibility/governance
  - Admiral acquisition is the strategic accelerant — timing matters
  - **Fergus gave thumbs up (2026-04-02)** — keep going, keep Antton in the loop
  - Next step: HubSpot connector for enriched company data (company records, not deal records)
  - Matt to back up Cowork files to Google Drive as interim risk mitigation
  - Tom: 15 mins with Matt next week to review front end and share tips
  - Apollo agent self-improved — identified email bounce-backs and suggested its own integration
  - Full technical review: [[enterprise-engine-technical-review]]
  - **2026-04-07**: HubSpot connected (Emily got it working). Read-only initially. AI data going on company records (not deal records — avoids underwriting overlap). Matt aligning with Emily and Adam on structure. Adam interested in replicating the pattern for broker contacts. Lovable front-end may give way to HubSpot dashboard if data lives there.

### 2026-04-08

- Eval testing regroup (Mima-led, Tom absent). The eval/testing layer that production agents need is being built:
  - 111 PromptFoo test cases (red team, golden dataset, plugins) — run on-demand before major agent changes
  - `/create-test-cases` skill for stakeholders to contribute test requirements
  - Ismael connecting agent framework to **Datadog** — per-tool traces, outputs, latency. Demo with Datadog architect Fri/Mon.
  - **S3 storage** for all agent outputs under investigation — organised by user/policy for security, compliance, analytics
  - Auth/user-isolation testing scoped for Playwright (separate from PromptFoo)
  - Longer-term: agents analysing stored conversations for higher-level insights
  - See [[2026-04-08-eval-testing-regroup]]
