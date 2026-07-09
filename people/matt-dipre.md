---
title: Matt Dipre
created: 2026-04-14
updated: 2026-04-14
type: person
role: Financial Analyst
team: Finance (reports to Anneliene)
tags: [finance, invoicing, netsuite, snowflake, ai-user]
ai_activation_stage: 3
ai_activation_confidence: high
ai_activation_assessed: 2026-07-09
---

## Role

Financial Analyst

## Team

Finance — reports to Anneliene

## Relationship

First spoke 2026-04-14 (AI discovery round). Keen to experiment, already built a working invoice automation in Claude before access issues stopped him.

## Working style notes

- Uses Claude (Sonnet) as primary AI tool — hardly uses ChatGPT
- Previously automated full invoice + broker commission workflow via Claude + NetSuite browser automation — broken by NetSuite update (no dual-browser sessions)
- Currently uses Claude for Excel formatting (broker statements) and general time-saving
- Has a personal Google Sheet tracking installment policies with formulas
- Uses Geran's Snowflake Streamlit for policy lookups
- Daily routine: invoices + bank recs done by 11am, then projects
- Building a Google Sheets dashboard for invoice metrics (volume, on-time %, improvement)
- Blocked on Looker access (has account, no permissions) and HubSpot AI integration (needs admin approval)
- Good candidate for quick wins once access is unblocked
- Interested in recreating invoice automation as a reusable Claude skill

## AI Activation

**Stage**: 2 — Context and tools (access-blocked)
**Confidence**: medium
**Assessed**: 2026-06-02
**Evidence**: Previously built a complete invoice + broker commission automation workflow via Claude + NetSuite browser automation — broken by a NetSuite update. Currently using Claude for Excel formatting and general tasks. Actively building a metrics dashboard. Clear mental model of what he wants to rebuild. Blocked on Looker access and HubSpot AI integration.

**Not Stage 1**: Previously demonstrated Stage 3 capability (end-to-end workflow automation). Multiple current use cases.
**Not Stage 3**: Current practice is simpler than peak capability due to access blockers. The automation regression means day-to-day behaviour is Stage 2, even though his ceiling is higher.
**To progress**: Unblock Looker and HubSpot access. The invoice automation skill he wants to rebuild is a natural Stage 3 goal. He has the mental model — access is the constraint.
**Framework note**: Assessment reflects current state, not peak capability. Access blockers are the limiting factor. Once unblocked, likely to jump directly to Stage 3 rebuilding.

### Update 2026-07-09

**2→3 (blocked→builder again).** Calculator ~1 month in daily production: code-reviewed by Chris (one fix, correct since), per-run self-audits, quarterly-MTA capability ("made something that was never possible possible" — lets finance say yes to brokers), feature added live in an OKR session, "it's like my own personal engineer". Engineering adopting it as the basis for the OKR build. Access blockers bypassed via data lake (AI-014 obsolete). Source: [[2026-07-08-ai-finance-workshop]].

## 1:1 Log

### 2026-04-14 — AI Discovery

- See: [[2026-04-14-matt-dipre-ai-discovery]]
- Key blockers: Looker permissions, HubSpot AI access, NetSuite dual-session restriction
- Actions: resolve Looker with Kirsty/Geran, check Quincy's data source, investigate NetSuite data in Looker/Snowflake
- Encouraged to experiment with Claude HTML dashboards during project time
