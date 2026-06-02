---
title: FinOps Discussion — ProdTech Next Steps (May 21)
created: 2026-05-21
updated: 2026-05-21
domain: operational-tooling
type: meeting
tags: [operational-tooling, finance, finops, automation, installments, stripe]
---

# FinOps Discussion — ProdTech Next Steps (May 21)

**Attendees:** [[jordi|Jordi Pallares]] (note creator), [[matt|Matt Price]], [[geran|Geran Butcher]], [[fergus|Fergus Doyle]], Tom Harvey, [[chris|Chris Fothergill]]

Full transcript: [[2026-05-21-finops-prodtech-discussion-transcript]]

---

## Key themes

### Finance team capacity crisis
- Jade's document highlights significant operational burden on finance
- 50/50 split on installment calculation accuracy: 50% correct, 50% require manual overrides (rebates, deposits, cancellations)
- Finance at 110% capacity — limiting ability to scale trading decisions
- Manual processes: broker statements, board rows, credit control

### Strategic direction
- Existing agreement between Darren, Christian (Leth Nielsen), and Chris on upfront commission structure
- Admiral installments program in motion but lacks programme management
- Focus: upfront payments and cost coverage mechanisms (not traditional installment collection)
- Key opportunity: insert into Admiral conversation to improve coordination

### Q3 priorities — decouple conversion from automation
- **Conversion uplift achievable without technical changes** — historical: 30–40% of book on installments during peak periods
- Can offer installments on taxi immediately after platform migration
- Conservative estimate: £2M GWP uplift potential
- Q3 approach: automation of broker-arranged finance processes (not installments themselves)

### Q3 automation targets (Jade's priority list)
1. Cancellations workflow
2. Rebates and return premiums
3. Voids processing
4. Broker statements
5. Board row automation
6. Recurring trading deviations (12 identified)
- Plus: blacklist of unsupported configurations (e.g. no BACS payments, GoCardless only)

### Technology considerations
- **Stripe premium finance**: emerging option — virtual bank accounts, transaction-level reconciliation
- Currently bleeding-edge with limited documentation; worth tracking
- Build vs. buy timeline: likely 2027–2028 for major overhaul
- H2 2026: tactical improvements only

### Resource constraints
- David on parental leave until September (100% return)
- Alex leaving the team
- Limited Q3 capacity requires careful prioritisation

---

## Actions

- [ ] Matt and Jordi: Meet with Jade (next Friday) to prioritise requirements, stack-rank automation targets (→ AI-079)
- [ ] Tom/Jordi: Develop cost-benefit analysis for finance team relief
- [ ] Explore Stripe integration timeline and capabilities (→ AI-080)
- [ ] Define blacklist of unsupported policy configurations (→ AI-081)
