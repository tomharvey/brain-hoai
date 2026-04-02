---
title: TCO / Flock Value Statement — New Business Process
created: 2026-04-02
updated: 2026-04-02
domain: operational-tooling
type: reference
author: matt-lees
tags: [tco, value-statement, lovable, hubspot, distribution, enterprise]
---

## Source

Designed by [[matt-lees|Matt Lees]]. Converted from Notion export on 2026-04-02. This documents the new business process only — renewal process is separate and still being finalised. Current status: Mima assessed as experimental, not product-market fit yet. Deprioritised pending Q2 OKR progress on simplifying value sales approach.

## Overview

TCO (Total Cost of Ownership) value statement documents support new business and renewal opportunities.

- Scoped to **Courier and Trades risks only** — Taxi and SDH excluded (policyholder doesn't pay all operational costs)
- Minimum threshold: **risks over £100k premium**
- Two separate documents: New Business (documented here) and Renewal (separate process)

## Loom walkthrough videos

| Part | What's covered |
|------|---------------|
| Part 1 | Steps 1–7: Ticket identification through claims frequency modelling |
| Part 2 | Steps 8–10: Premium inputs, operational costs and output review |
| Part 3 | Steps 11–12: PDF export and HubSpot distribution |

## Step-by-step process

### Step 1 — Ticket identification

- Every deal on the normal trading pipeline is automatically screened
- If criteria met (Courier/Trades + over £100k), a ticket is auto-generated in the TCO Ticket Pipeline in HubSpot
- Lands in "Identified for TCO" column

### Step 2 — Open ticket and locate underlying deal

- Open TCO ticket — displays headline stats, broker details, link to underlying deal
- Navigate to deal page for key inputs (fleet size, indicative rates, excess level, etc.)

### Step 3 — Access G Drive folder

- Navigate to the deal's G Drive folder
- Key documents: CCE (Claims Experience document), Claims Listings

### Step 4 — Open Lovable and create new document

- Go to the Lovable prototype to create client-facing documents
- Internal Lovable project contains underlying codebase/model — do not share externally
- Click gear icon → "Create New Document" → loads blank template

### Step 5 — Upload CCE document

- Drag CCE into Lovable document panel
- Lovable auto-extracts: client name, claims experience by year
- Click "Apply Data" → document auto-populates

### Step 6 — Input broker details

- Manually enter broker name (dual-branding)
- Confirm/enter risk inception month

### Step 7 — Enter projected savings inputs (manual)

| Field | Source |
|-------|--------|
| Fleet size | Underlying deal page |
| Vehicle years | Most recent CCE |
| Premium per vehicle (Flock rate) | Indicative rate on deal page |
| Market premium per vehicle | Competitor insight if known; otherwise match Flock rate |
| Flock rebate % | Default 8% — adjust as appropriate |
| Excess per claim | Auto-pulled from CCE — verify against quoted excess on deal page |

### Step 8 — Review and annotate claims history

**Most important step.** Claims history is the credibility foundation of the entire document.

- **8a — Verify claims data**: cross-reference against CCE from G Drive, check vehicle years
- **8b — Apply colour coding**: 🟢 improving (frequency trending down), 🟡 flat/mixed, 🔴 deteriorating (frequency trending up)
- **8c — Write contextual commentary**: tailored to client trajectory. Honest about challenges, positioned around Flock's levers (telematics, early reporting, driver behaviour). Avoid overstating projections.
- **8d — Configure claims modelling assumptions**: repair cost per claim, fault ratio (default 75%), vehicle off-road duration, cost per day off road, self-repair % (e.g. 25%), early reporting benefit

### Step 9 — Configure operational cost assumptions

- Fuel, tyres, service & maintenance
- Defaults to be agreed — manual override per deal

### Step 10 — Review the output

- Auto-calculated projected savings across three buckets: insurance premium (inc rebate), claims & downtime costs, operational costs
- Output: total projected saving, saving per vehicle, with/without Flock comparison
- Full appendix with underlying data and assumptions

### Step 11 — Export as PDF

- Browser print → Save as PDF
- Layout optimised for print but may produce blank pages — delete manually
- Naming: `[Client Name] - Flock Value Statement`

### Step 12 — Upload to HubSpot Documents

- Upload PDF to HubSpot Documents
- Create unique shareable link (prompts recipient for email → enables engagement tracking)
- Send to broker via HubSpot email template or embed in outbound email with underwriter
- Tracking: opens, viewing sessions, scroll depth

## Planned improvements

- Per-vehicle/fleet inputs currently manual — automation from deal page planned
- Segment-specific claims defaults to be agreed
- Alternative distribution via unique Lovable URL (instead of PDF) being explored
- Renewal process documented separately

## Links

- [[matt-lees]]
- [[2026-04-02-matt-lees-enterprise-engine]]
