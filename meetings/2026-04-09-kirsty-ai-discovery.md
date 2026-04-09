---
title: Kirsty AI Discovery
created: 2026-04-09
updated: 2026-04-09
domain: operational-tooling
type: meeting
tags: [kirsty, looker, claude, mcp, insight, renewals, data-architecture]
---

## Attendees

- [[kirsty|Kirsty Alexandre]] — Senior Analytics Engineer (Finance)
- Tom (me)

## Key themes

### Looker→Claude connection (MCP confirmed)

- Claude talks to Looker via MCP, set up on Kirsty's local machine
- Several finance people trialling locally: Christian, Kevin, David
- Multiple business users have reached out wanting access
- **Production need**: get MCP deployed on cloud infrastructure (same pattern as data lake MCP) — Tom has the required access keys
- Once deployed, users could access via browser extension — no local setup needed
- Bi-directional: can query data AND build reports/dashboards in Looker

### Tree diagram visualisation

- Kirsty drew a financial model wireframe on paper (drivers → top-line numbers)
- Photographed it and asked Claude to build dashboard using Looker data
- Output is HTML — currently hardcoded numbers, but could be:
  - Quick route: regenerate HTML daily, save to Google Drive
  - Proper route: hit Looker API for live data
- This type of visualisation (tree/funnel with driver relationships) is impossible in standard BI tools
- Shows which drivers users can influence to change top-line numbers

### AI-generated insights — the breakthrough

- Claude writes paragraph-form insights from the dashboard data
- Solves the perennial BI problem: users see numbers but don't interpret them
- Example: "Recoverable losses Q4: £1.7M despite competitive pricing"
  - LCH deal: £1.1M loss
  - Fleet Evolution: £600K loss — chose AIG for **interest-free payment terms**, not price
  - This directly challenges the "we're priced too high" narrative from underwriters
- Trade segment: 57% of submissions but only 19% win rate — stop concentrating on trade
- Anton and Adam already want to use this for performance tracking

### Strategic data architecture discussion

- Tom framed a multi-layered knowledge system:
  1. Highly structured data (Looker — current)
  2. Semi-structured data (less tightly modelled)
  3. Unstructured with flow (submission PDFs)
  4. Completely unstructured (user feedback, insights)
- The insight text Kirsty generates is itself a **new corpus of data** — not ephemeral
- Challenge: how to make insights persistent, self-referencing, and buildable
  - Needs human-in-the-loop for priority setting and feedback
  - Insight fatigue problem (cf. Francesco's Ben weekly — "it tells you the same stuff")
  - Solution: system that knows what it told you, what's been actioned, what's new
- **Timeline**: Q2 experiment, Q3-Q4 productionise

### Ideal customer profile analysis

- Tom suggested asking Claude to determine the narrowest ICP from 5 years of data
- Compare data-driven profile vs Adam's assumptions
- Track how profile has changed over time
- Removes opinion/bias from customer targeting decisions
- Kirsty to test this

### Looker explores structure

- Explores are curated data models for specific audiences:
  - **FPNA**: actuals, budgets, targets, 25 key metrics (finance-focused)
  - **HubSpot data**: includes logic corrections for human data entry errors (e.g. stage-skipping)
  - **Platform v1 vs v2** data separation
- Every table and field is labelled with descriptions — Claude can self-navigate
- Pointing Claude at the right explore improves answer quality

### Renewals workflow (briefly covered)

- Kirsty was unaware the team uses Zapier to push spreadsheet data back into HubSpot
- Confirmed MCP approach is viable for Looker→HubSpot direct integration
- Tom to pick up and explore further with Anna and Billy

## Actions

- [ ] **Tom**: Deploy Looker MCP on cloud infrastructure (has access keys) — critical enabler
- [ ] **Kirsty**: Share Notion page about Looker setup
- [ ] **Kirsty**: Share HTML dashboard file
- [ ] **Kirsty**: Test Claude ICP analysis vs Adam's assumptions
- [ ] **Tom**: Explore renewals Looker→HubSpot direct flow (report back to Anna)

## Notes

- This call resolves AI-006 — Kirsty's setup is understood
- AI-007 (renewals Looker→HubSpot) confirmed viable, needs scoping
- New issue needed: cloud MCP deployment for Looker
- Kirsty is a key ally — technically capable, enthusiastic, already delivering value. Needs infrastructure support, not direction.

Full transcript: [[2026-04-09-kirsty-ai-discovery-transcript]]
