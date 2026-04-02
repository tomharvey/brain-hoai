---
title: Anna Spriggs
created: 2026-03-27
updated: 2026-03-30
type: person
role: Senior Underwriting Assistant
team: Ops (reports to Emily Staton)
tags: [underwriting, ops, ai-user]
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
