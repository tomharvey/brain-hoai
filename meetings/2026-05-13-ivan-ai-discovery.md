---
title: Tom <> Ivan: AI Discovery (May 13)
created: 2026-05-13
updated: 2026-05-13
domain: operational-tooling
type: meeting
tags: [operational-tooling, finance, credit-control, netsuite, ai-discovery]
---

# Tom <> Ivan: AI Discovery — May 13

**Attendees:** Tom Harvey, Ivan Boix (credit controller)

Full transcript: [[2026-05-13-ivan-ai-discovery-transcript]]

---

## Key themes

### Ivan's daily credit control prioritisation system
- Built comprehensive daily report from NetSuite aging data
- Process: export NetSuite aging report (5 minutes) → feed to Claude → get prioritised daily report
- Report features:
  - Summary dashboard: gross invoices, overdue amounts, payment comparisons
  - Top 5 immediate actions based on balance and due dates
  - Movement tracking vs. previous day
  - Key deadlines with funding date considerations
  - Separate sections for overdue vs. not-yet-due policies
  - Installment policies filtered out (unless direct debit fails)
- Running the same chat for 2 months; saving "hours of work" daily
- Has created a skill for this too

### Weekly carrier reporting
- **Admiral**: weekly debt review using refined NetSuite exports; net position view (RPs offset against invoices); 1 minute to generate vs. previous manual process
- **Acorn**: fewer risks — still manual

### HubSpot chasing — still manual
- Different account handlers per broker complicate automation
- Needs to balance strict vs. soft approach per case
- HubSpot connector available but Ivan prefers manual approach for nuanced chasing

### Payment terms — stored "in head" only
- Some brokers (Marsh, Lockton) have custom payment terms that affect overdue calculations
- Not captured in any system — purely in Ivan's memory

### Technical suggestions explored
- Migration to Claude Co-work (better file organisation vs. long chat history)
- Tom suggested: ask current chat to create a zip for migration
- Ivan to explore after call

### Finance team AI maturity observation
- Ivan is well ahead of the team: clear use case, solved a real daily problem
- Matt Dipré also doing things; Anneliese using it sporadically; Christian not yet reached
- Finance team overall: "too busy fighting fires to invest in optimisation"
- Ivan's approach: built the process first, then figured out how AI could help — right order of operations

---

## Actions

- [ ] Ivan: Explore Claude Co-work migration after call
- [ ] Tom: Organise team AI workshop (company-wide Co-work intro, then team-specific) (done — May 19)
- [ ] Tom: Capture Ivan as case study for finance team workshop
- [ ] Ivan: Investigate capturing broker payment terms in a system (rather than memory only)

---

## People without vault files
- Ivan Boix — credit controller; built an impressive daily credit control prioritisation system using Claude + NetSuite exports; joined Flock June 2025
