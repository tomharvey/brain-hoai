---
title: Anna Spriggs
created: 2026-03-27
updated: 2026-03-30
type: person
role: Senior Underwriting Assistant
team: Ops (reports to Emily Staton)
tags: [underwriting, ops, ai-user]
ai_activation_stage: 2
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-02
---

## Role

Senior Underwriting Assistant

## Team

Ops — reports to [[emily|Emily Staton]]

## Relationship

<!-- to be confirmed -->

## Working style notes

- Experienced daily AI user — longest-tenured AI adopter on the ops team
- Successfully migrated ChatGPT prompts to Claude for vehicle resolution — found higher success rates
- Involved in renewals process (weekly manual work)
- Subject of Geran's time/motion study (video recorded doing day job)
- Emily recommends speaking to her for ground-level AI usage patterns

## AI Activation

**Stage**: 2 — Context and tools
**Confidence**: medium
**Assessed**: 2026-06-02
**Evidence**: Longest-tenured AI adopter on Emily's ops team. Daily user. Successfully migrated ChatGPT→Claude for vehicle resolution (found higher accuracy). Connected HubSpot to Claude "trivially easy." Experimenting with Computer Use for G Drive folder automation. Process redesign instinct: "ideally we would just cut out all of these unnecessary steps rather than trying to automate each step" — already thinking architecturally.

**Not Stage 1**: Multiple tools connected, cross-platform migration, multi-task usage — well past single-task wins.
**Not Stage 3**: Data from April 2026 (2+ months stale). The Computer Use experimentation and process redesign thinking are Stage 3 signals, but no confirmed Stage 3 patterns observed.
**To progress**: The G Drive Computer Use experiment is the right next step. If she's iterating on that and building conversational refinement into her workflow, she's likely already at Stage 3. Needs a fresh 1:1 to verify.
**Framework note**: Data is stale. Emily's team moves fast and Anna is the longest-tenured adopter. She may well be Stage 3 already — reassessment is a priority.

## 1:1 Log

### 2026-03-30 (via Jordi 1:1)

- Jordi working with Anna to automate part of the renewal spreadsheet process using Google MCP
- **Blocker**: Google MCP requires local hosting + Google Cloud auth — Jordi has to run prompts manually on calls with Anna
- Underlying process concern: 3 different spreadsheets with different structures, Zapier workarounds connecting HubSpot — process itself may need rethinking before automating
- Tom reviewing Google MCP hosting situation 2026-03-31

### 2026-04-02 — AI Discovery

- **Renewals process mapped**: Looker → PMT (download + add sheet) → Billy allocates underwriters → Anna copies to Renewals Tracker → Zapier creates HubSpot deals (6 weeks before renewal)
- Jordi's Google MCP work was automating step 3 (PMT → Renewals Tracker copy/paste)
- **Direction change**: eliminate spreadsheets entirely, go Looker → HubSpot direct. Google MCP hosting is now moot.
- **G Drive automation** is her next project — auto-create folders + drop broker submission docs per deal. Company name matching is the hard part. Experimenting with Claude Computer Use.
- Connected HubSpot to Claude via connectors panel — trivially easy (click connect, OAuth). Can walk Matt Lees through it.
- Vehicle resolution: ChatGPT → Claude migration complete, significantly more accurate (ChatGPT converted zeros to O's)
- "Ideally we would just cut out all of these unnecessary steps rather than trying to automate each step"
- Kirsty's Looker→Claude connection is the key enabler — Tom to investigate
