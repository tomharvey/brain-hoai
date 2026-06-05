---
title: Francesco Venerandi
created: 2026-05-19
updated: 2026-05-19
type: person
role: Senior Data Scientist
team: Pricing (reports to Milan Chavda)
tags: [pricing, data-science, ai-enablement]
ai_activation_stage: 4
ai_activation_confidence: high
ai_activation_assessed: 2026-06-02
---

## Role

Senior Data Scientist on [[milan-chavda|Milan Chavda]]'s pricing team. Works on pricing model feature discovery, telemetry analysis, and AI tooling.

## Relationship

First direct 1:1 catchup 2026-05-19 (had been on holiday in Mexico). Previously referenced in multiple meetings. Strong candidate for collaboration on pricing automation and transcript infrastructure.

## Working style notes

- Builds things off-the-side on top of his regular work (performance coach built in off-time)
- Frustrated by pricing work being consistently deprioritised despite strong AI interest
- Wants to move from "using AI to build things" to "building AI systems" — aspirational technical direction
- Thoughtful about the architecture: prefers saving the pricing JSON at source rather than reconstructing it from Postgres
- Planning a 2-day hackathon with [[javier|Javier]] to accelerate pricing automation

## Work highlights

- **Performance coach** (with [[ollie-crowe|Ollie]]): MCP-based career coaching system using Granola, Slack, Notion, GCal. Three modes: weekly progress tracking vs promotion criteria, 1:1 prep/follow-up, weekly coaching. Code on GitHub.
- **Triangle analysis skill**: built independently (with parallel work by [[milan-chavda|Milan]]) — example of skills fragmentation in pricing team
- **J feedback pipeline**: Granola-based transcript synthesis service for the product team — currently outputs weekly summaries but lacks persistent memory of known context (see [[AI-051]])
- **Ben weekly transcript summaries**: earlier work that hit the "same thing every week" insight fatigue problem

## AI Activation

**Stage**: 4 — Multi-agent orchestration
**Confidence**: high
**Assessed**: 2026-06-02
**Evidence**: Built MCP-based performance coach system (Granola + Slack + Notion + GCal, three operating modes: weekly progress tracking, 1:1 prep/follow-up, weekly coaching). Built J feedback pipeline (Granola transcript synthesis service). Triangle analysis skill (built independently, parallel to Milan's). Planning 2-day pricing automation hackathon with Javier. "Wants to move from 'using AI to build things' to 'building AI systems'" — explicitly naming the Stage 4→5 transition.

**Not Stage 3**: The performance coach is a multi-MCP orchestration system with three distinct modes — this is architectural thinking and multi-component integration, not single-domain tool use.
**Not Stage 5**: No evidence yet of adherence measurement or empirical context quality testing on his own systems. Frustration about pricing work being deprioritised suggests he hasn't had space to apply Stage 5 meta-thinking to production systems.
**To progress**: The hackathon with Javier is the right vehicle. Stage 4→5 starts with measuring whether the context he writes actually produces better agent behaviour — PromptFoo or equivalent applied to his own pipelines, not just J.
**Framework note**: Strong Stage 4, closest to Stage 5 among non-engineering non-Ishmael staff. The "building AI systems" aspiration is exactly the Stage 5 orientation. The pricing deprioritisation is the main constraint.

## 1:1 Log

### 2026-05-19 — AI catchup

- Returned from Mexico holiday
- Demoed performance coach system
- Discussed pricing data extraction bottleneck and hackathon plan
- See: [[2026-05-19-francesco-ai-catchup]]

### Prior references (no direct 1:1)

- 2026-05-11: [[2026-05-11-milan-ai-discovery]] — Milan discussing Francesco's work and the skills fragmentation issue
- 2026-05-08: [[2026-05-08-fergus-tom-weekly]] — transcript service referenced
- 2026-04-16: [[2026-04-16-fergus-tom-weekly]] — telemetry/feature discovery pipeline with Darren and Michael
