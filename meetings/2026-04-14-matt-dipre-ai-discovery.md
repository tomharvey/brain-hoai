---
title: Matt Dipre — AI Discovery
created: 2026-04-14
updated: 2026-04-14
domain: ai-enablement
type: meeting
tags: [discovery, finance, invoicing, netsuite, snowflake, looker, hubspot]
---

## Attendees

- [[matt-dipre|Matt Dipre]]
- Tom Harvey

## Key themes

### Current AI usage

- Uses Claude (Sonnet) — performance jumped significantly after recent update
- Previously automated invoice creation and broker commissions via Claude + NetSuite in browser
- **NetSuite update broke this** — can no longer have two accounts open across browsers, so the entire invoice workflow is now manual again
- Still uses Claude for Excel formatting (broker statements) and general time-saving tasks

### Invoice workflow (installments)

Daily process, done by ~11am alongside bank recs:

1. Check personal Google Sheet (list of installment policies with formulas for due dates)
2. Look up policy in Snowflake Streamlit (built by [[geran|Jaren]]) for amounts due
3. Cross-check against [[quincy|Quincy's]] backup sheet (unclear data source — Retool? Snowflake?)
4. Create invoice in NetSuite by copying/modifying previous month's
5. Download PDF → HubSpot → email to broker → copy email link back to NetSuite for tracking

Lots of room for human error. Automation previously worked for one invoice before hitting token limits.

### Access blockers

- **Looker**: has an account but no permissions to create or view dashboards. Needs granular permissions from [[kirsty|Kirsty]]
- **HubSpot AI integration**: needs admin approval — [[emily|Emily]] may be handling for others
- Both blockers preventing him from experimenting further

### Opportunities discussed

- **Dashboard in Claude**: currently building a manual Google Sheets dashboard (invoice volume, on-time %, improvement over time). Could generate this via Claude from HubSpot/Snowflake/Looker data instead
- **Resurrect invoice automation**: first run was arduous (teaching + doing), but could be turned into a reusable skill. Needs more tokens allocated
- **Looker + Claude**: once access is sorted, can use Kirsty's Looker connector to pull data directly
- Encouraged to experiment during project time — make HTML dashboards, play with visualisations

## Actions

- [ ] Get Matt Dipre Looker access — resolve permissions with Kirsty and Jaren — Tom
- [ ] Check with Quincy on her backup sheet data source — Tom
- [ ] Investigate NetSuite data availability in Looker/Snowflake — Tom
- [ ] Get HubSpot AI permissions sorted — check with Emily — Tom/Matt Dipre
- [ ] Experiment with Claude dashboard generation during project time — Matt Dipre
- [ ] Once access sorted: revisit automated invoice workflow as a Claude skill — Tom/Matt Dipre

## Notes

Matt is keen but blocked on access. Good candidate for quick wins once Looker and HubSpot permissions are resolved. The invoice automation he previously built proves capability — just needs to be formalised as a skill and given enough tokens.

Full transcript: [[2026-04-14-matt-dipre-ai-discovery-transcript]]
