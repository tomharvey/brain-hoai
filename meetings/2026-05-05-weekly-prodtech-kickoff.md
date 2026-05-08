---
title: Weekly Product + Tech Kickoff
created: 2026-05-05
updated: 2026-05-05
domain: operational-tooling
type: meeting
tags: [prodtech, kickoff, installments, career-product, mtas, anton-darren, pricing]
---

## Attendees

- Tom Harvey
- [[fergus|Fergus Doyle]]
- [[matt|Matt Price]]
- [[jordi|Jordi Pallares]]
- [[geran|Geran Butcher]]
- Product + Technology Leadership (prodtech-leads group)

## Key themes

### Career product launch — delayed

- Career product for admin cannot launch until MTA bugs are resolved first
- Main priority: fix MTA/vehicle-add flow to match previous product behaviour, then roll out career
- Timeline: speed-run MTAs for haulage/taxi customers first → then separate, considered conversation with Anton and Darren about career go-live

### Installments — platform support shipped, process still manual

- Geran and Sam shipped platform support for installments last week — system now tags deals with Admiral installments attached (previously manual scanning of underwriting-wins channel)
- **Process of executing installments is still heavily manual** — Jade Mounir brought a paper to SLT this morning detailing the backlog
- Jade's paper shows a "laundry list" of parameters causing operational problems
- Working plan: dedicate resource in Q3 to making installments first-class. Geran and Matt Price to do scoping homework and present Q3 picture with trade-offs
- Fergus: if installments is blocking a haulage deal, we'll swallow the manual cost — question now is scalability of the current process
- Three states: (1) today's manual process, (2) a more palatable interim version, (3) 3–5 year target state

### Anton/Darren acquisition team conflict

- Unresolved debate between Anton and Darren on acquisition team direction — blocking career product launch decision
- Matt Price to separate: career launch conversation needs Anton + Darren to agree first
- Specific deviations (e.g. changing deposit terms, adjusting first installment amount) are causing operational misery — these need to be documented as the "don't sell this" list, not just "don't deviate"

### ISB/development factors — broker remuneration

- HRI (a fleet/broker) has agreed a backdoor subsidy with Amazon involving an ISB
- Development factors and pricing implications not Q2 — but Adam pushing for something this quarter
- Matt Price to brief Fergus separately on the ISB conversation — context needed before it "happens by default"
- Career product changes on development factors: Matt to bring as a separate one-pager

### MTA failures — ongoing cleanup

- MTA invoicing issues from haulage release still being resolved by Sam
- Installments relaunch last week helped fix some; outstanding items still being addressed
- Target: back to baseline invoicing by end of this week

## Actions

- [ ] Geran + Matt Price: scoping homework on Q3 finance/installments — present trade-offs including what won't happen if we pull ahead finance work
- [ ] Matt Price: brief Fergus separately on ISB conversation and HRI/Amazon arrangement
- [ ] Matt Price: document specific operational deviations that cause downstream misery (the "don't sell this" list)
- [ ] Sam: resolve remaining haulage invoicing issues by end of week

## Notes

The installments situation has three distinct layers that need separate plans: the immediate operational pain (manual process), the tactical fix (more palatable interim), and the strategic solution (first-class platform support). Conflating them is causing confusion.

Full transcript: [[2026-05-05-weekly-prodtech-kickoff-transcript]]
