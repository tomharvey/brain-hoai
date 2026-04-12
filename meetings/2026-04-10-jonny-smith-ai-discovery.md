---
title: Jonny Smith — AI Discovery
created: 2026-04-10
updated: 2026-04-10
domain: operational-tooling
type: meeting
tags: [discovery, connectivity, telematics, data-quality, hubspot]
---

# Jonny Smith — AI Discovery

Discovery call with Jonny Smith (Connectivity Operations Manager, reports to Mollie). Team of one, embedded across ops teams. Deep telematics domain expertise (7 years). Pragmatic user hitting data quality barriers.

## Attendees

- Jonny Smith
- Tom (me)

---

## Current AI usage

### Tools
- **ChatGPT** — primary tool, used heavily when building Zapier workflows (~70% accurate, points in right direction, supplements with Google/YouTube/forums)
- **Claude** — basic usage
- **Granola** — meeting notes
- **MCP (telemetry)** — testing for data quality analysis, but hitting limitations

### Approach
Hybrid: ChatGPT for generic direction → forums/tutorials for specifics. Doesn't treat AI as verbatim source — uses it as a compass.

---

## MCP / telemetry data quality issue

### The GPS fix problem
- Customer reported 190mph speed reading — MCP confirmed it
- Jonny knew to check GPS fix — it was 3 (too low, need 5+ for accuracy)
- MCP doesn't understand GPS fix as a data quality indicator — it treats all data points as valid
- The portal was also showing 190mph — not filtering low GPS fix data points
- **Root cause**: 1Hz data from Nano devices not being filtered for low GPS fix, causing false high-speed alerts
- Tech team (Steve) aware, fix in progress after Jonny's escalation

### Key insight
The MCP needs **education on telematics domain knowledge** — specifically which parameters indicate data quality (GPS fix thresholds, satellite count, etc). Without this, it will confidently give wrong answers to customers.

Jonny's take: *"I've worked in telematics longer than AI has"* — for him personally, diagnosing without AI is faster. But for scaling to customer self-service, the AI needs to be right.

### Implication for customer-facing AI
If we put an AI agent in the portal for customers, it must understand data quality indicators. Telling a customer "your vehicle did 190mph" when the GPS fix is 3 would be a credibility disaster.

---

## Day-to-day operations

### Role
- Team of one, latches onto other teams
- Works closely with Ben and Daisy on scheduled customer calls
- Handles: connectivity troubleshooting, device installation/allocation issues, API credential setup, platform discrepancies (Geotab vs Flock portal calculations)
- Escalation path: customer → Matrix ticket → Jonny if technical → broker escalation if unresponsive → cancellation process

### Zapier automation (self-built)
Jonny has built significant automation in Zapier:
- **Connectivity monitoring**: triggers when fleet drops below 75% connected
- **Looker → HubSpot integration**: starts from Looker database, uses deal IDs to cross-reference HubSpot (avoids name matching entirely — solved the company name mismatch problem by using record IDs)
- **Automated ticket creation** for overdue telematics forms (14-day trigger)
- **Follow-up scheduling**: sets dates for when he's actually in the office

### Connectivity diagnosis vision
Jonny wants customers to self-diagnose connectivity issues. The data already exists in Looker (Kirsty built a calculation) to determine why a vehicle shows disconnected:
- No data for reg → API issue or Matrix issue
- Device sent but no data → not installed
- No device allocated → no reg-to-device mapping

My advice: don't frame this as AI — just show the answer next to the vehicle in the portal. Steve might build it in a morning. Keep it simple.

### Coverage when on holiday
- Zapier automations run themselves
- Manual follow-ups scheduled around his in-office days
- Emily's team handles inbound emails/tickets
- Training Emily's team in coming weeks to do more (e.g. updating registrations via new Matrix web app)
- New Flock-branded web app for reg updates going out to brokers via Liam's newsletter

---

## HubSpot data quality — the recurring theme

Jonny's biggest barrier to further automation:

**Deal owner/contact problem**: Primary contact on a HubSpot deal is the sales contact who wrote the policy. But BAU contact is often someone different at the same brokerage. Nobody updates the primary contact after the deal is done. Result: automated emails go to wrong person.

- Can find deal IDs, company IDs with 100% success
- Contact is wrong ~some% of the time
- Email thread history shows the real contact has changed, but the deal record doesn't reflect it
- No one's job to maintain this
- Potential AI use case: infer correct contact from email thread activity

This is the same HubSpot data quality problem surfacing across Matt, Kirsty, Alex, Oli, and now Jonny.

---

## Assessment

Jonny is a **capable self-starter** who's built real automation without engineering support. His Zapier + Looker integration is genuinely clever (using deal IDs to bridge the Looker/HubSpot name mismatch). Main blockers are data quality, not AI capability.

Two things to follow up on:
1. **MCP telemetry education** — GPS fix thresholds and data quality parameters need to be baked into the MCP's context
2. **HubSpot contact freshness** — a cross-company problem that keeps surfacing. Worth exploring whether email thread analysis could auto-update primary contacts.

---

## Actions

- [ ] **Tom**: Feed GPS fix / data quality context into telemetry MCP (or flag to whoever maintains it)
- [ ] **Tom**: Raise HubSpot contact freshness as a cross-company data quality issue — now surfaced by Jonny, Matt, Alex, and others
- [ ] **Jonny**: Continue training Emily's team on connectivity ops for coverage

---

Full transcript: [[2026-04-10-jonny-smith-ai-discovery-transcript]]
