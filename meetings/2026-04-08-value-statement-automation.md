---
title: "AI Workshop: Automating Value Statement"
created: 2026-04-08
updated: 2026-04-09
domain: operational-tooling
type: meeting
tags: [value-statement, tco, automation, hubspot, lovable, matt-lees, mima]
---

## Attendees

- [[mima|Jemima Pitceathly]]
- [[matt-lees|Matt Lees]]
- Tom Harvey (did not attend — summary via Granola)

## Context

Continuation of the Flock Value Statement / TCO automation work. Focus: how to automate the new business value document so it doesn't require Matt's involvement for every deal.

## Current process

- **Trigger**: HubSpot TCO ticket pipeline fires for all deals over £100K (trades and courier), new business and renewal
- **Workflow**: Matt downloads CCA (claims data) → drags into Lovable tool → auto-populates ~50% of fields (client name, broker, claims history) → manually fills remaining (rate vs market, rebate assumption ~8%, excess per claim, claims narrative)
- **Output**: three-bucket summary (insurance premium, claims & downtime, operational costs) with total projected saving and saving per vehicle
- **Time**: ~15–20 mins when data is present
- **Storage**: saved in submission folder and HubSpot, tracked via HubSpot document analytics (named viewer identity — reason PDFs chosen over Lovable URLs)
- **Renewal version** exists — uses actual client data, slightly more detailed than new business

## Core thesis

Flock's value proposition is **total cost of ownership (TCO)**, not just premium price. In a soft market where Flock isn't always cheapest, the document articulates: reduced fuel, service/maintenance costs, and a 10% claims reduction that cuts excess payments, self-repair costs, and vehicle downtime.

## Automation approach (new business first)

- **Goal**: remove Matt from the process entirely, not just reduce his time. Underwriters and BDMs get a document that appears automatically in the submission folder.
- **Preferred path**: generate output via **Claude + HubSpot MCP** rather than Lovable-to-PDF pipeline. Claude artifact quality has improved enough to potentially remove steps in the chain.
- **Trigger**: could fire automatically when a TCO ticket is created in HubSpot
- **Data**: CCA data already being extracted into Snowflake (Tom Harvey's prior work) — opportunity to pipe into TCO calculations without re-extracting
- **Automation target**: ~80% automated with a final human check. Manual review still needed for rate confirmation, multiple excess types, self-repair cases.
- **Not production-grade** — doesn't need to be
- **Renewal**: follow after new business — same automation logic, additional instructions to reference existing policy data

## Scope & output design

- Current output may be too detailed for everyday cases — consensus to **simplify for the majority**
- **Proposed**: headline metrics only (severity, frequency, etc.) with ability to drill down on request
- **Bespoke detailed decks** retained for large/complex risks (e.g. McQueen's-style)
- **Sub-£100K fleets**: no plan to extend this level of detail near-term; simplified headline messages could apply more broadly if they resonate

## Longer-term dependencies

- Getting **submissions data into the data lake** is a prerequisite for scaling this and other use cases — flagged as separate project

## Other options discussed

- **Self-service**: send assumptions to broker/client earlier in the journey so they input their own data — less emotive, more credible
- **HubSpot document tracking trade-off**: named viewer identity is the reason for PDFs; worth reconsidering if better automation requires a different format

## Actions

- [ ] Mima / team: assess best path forward for automation approach
- [ ] Matt Lees: share simplified Lovable document examples
- [ ] Determine which data points / output format to lock in before building — what's unlikely to change vs what will evolve through Q2

## Notes

- This is the second AI initiative where the preferred approach is **Claude + HubSpot MCP** replacing an intermediate tool (Lovable in this case, spreadsheets in others). Pattern is converging.
- The Snowflake CCA extraction (Tom's prior work) being reusable here is a good example of infrastructure paying off across use cases.
- Connects to [[insight-layer]] — submissions data into the data lake is a shared prerequisite.
