---
title: Anna Spriggs
created: 2026-03-27
updated: 2026-03-30
type: person
role: Senior Underwriting Assistant
team: Ops (reports to Emily Staton)
tags: [underwriting, ops, ai-user]
ai_activation_stage: 3
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-18
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

**Stage**: 3 — Fluency
**Confidence**: medium
**Assessed**: 2026-06-18
**Evidence**: Process redesign thinking: "ideally we would just cut out all of these unnecessary steps rather than trying to automate each step." Independently migrated ChatGPT prompts to Claude after quality assessment. Experimented with Claude Computer Use for G Drive automation. At May 13 ops sync, identified systematic errors in the deal creator amount calculation and proposed a dual-logic fix (use provided rate when available, default to Fred's calculation otherwise). This is iterative, critical engagement with AI output.

**Not Stage 2**: Redesigning processes architecturally, critically evaluating AI output (systematic error identification), proposing multi-condition logic fixes, proactively exploring new capabilities. Past context-loading.
**Not Stage 4**: No evidence of delegating whole workflows end-to-end. G Drive Computer Use project was experimental as of April — unconfirmed if shipped.
**To progress**: N/A — departing 2026-07-10. Priority is knowledge transfer, not progression.
**Framework note**: Confidence medium because April transcript is a stub (meeting note only). May 13 ops sync contributions are the strongest direct evidence. Departing Jul 10 — focus on handover of renewals process knowledge and any AI workflows she has built.

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
