---
title: Explore Stripe premium finance integration timeline and maturity
id: AI-082
created: 2026-05-21
updated: 2026-05-21
domain: operational-tooling
type: issue
status: backlog
priority: medium
assignee: Geran
origin: "[[2026-05-21-finops-prodtech-discussion]]"
tags: [stripe, premium-finance, finops, build-vs-buy]
---

## Description

Stripe has launched (or is launching) a premium finance / insurance payment offering. If mature enough, this could provide significant infrastructure that Flock would otherwise need to build — particularly around broker reconciliation, installments, and payment collections.

Investigate:
- What exactly Stripe's premium finance product covers
- Timeline for general availability
- Whether Flock is eligible / a good fit
- What it would cost relative to build

## Acceptance criteria

- [ ] Initial investigation completed (what does Stripe actually offer here?)
- [ ] Compared against current build plan for finance automation
- [ ] Assessment: is this a viable Q3/Q4 play or more of a 2027 bet?
- [ ] Brief written for Fergus / Darren / Christian to inform vendor strategy

## Notes

The finops group's instinct: Stripe's more mature features (virtual bank accounts per broker, transaction-level reconciliation) could unlock demonstrable value even before their insurance-specific features are ready. The more exotic premium finance features might be 6–12 months away.

This doesn't block Q3 automation work — it runs in parallel. But the decision has implications for how much we invest in bespoke builds.
