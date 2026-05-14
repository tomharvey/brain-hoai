---
title: "AI-040: Ship renewal risk dashboard to Ben and Daisy"
created: 2026-05-12
updated: 2026-05-12
type: issue
status: todo
priority: high
domain: product-ai
origin: "[[2026-05-12-matt-price-1-1]]"
tags: [retention, engagement, looker, posthog, hubspot]
---

# AI-040: Ship renewal risk dashboard to Ben and Daisy

Matt built an engagement analysis model joining 11 months PostHog data + Looker users table + HubSpot renewals. Defines daily/weekly/monthly active tiers per user per policy, mapped to renewal outcomes.

Fergus wants a radiator showing upcoming renewals with declining engagement as a churn risk signal. Matt has a publishable script and wants to get it into Ben and Daisy's hands for testing.

Methodology caveats to resolve: summer holiday gaps, February short-month DAU threshold.

Longer term: Matt wants to prove "engagement has causal uplift on retention" as the basis for hypothesis-led roadmaps.
