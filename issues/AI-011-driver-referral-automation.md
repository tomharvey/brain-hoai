---
title: "Automate driver referral process"
id: AI-011
created: 2026-04-09
updated: 2026-04-09
origin: "[[2026-04-08-fred-ai-discovery]]"
domain: operational-tooling
type: issue
status: backlog
priority: medium
assignee: tom
tags: [ops, driver-referrals, hubspot, automation, fred]
---

## Description

Driver referrals are a fully manual process: extract driver info from emails (license, DVLA summary, claims), input into a HubSpot template ("driver referral underwriter"), send to underwriters/Admiral. 10-20 per day, ~15 minutes each. No automation exists today.

## Current workflow

1. Driver referral arrives in Support inbox (HubSpot ticket)
2. Open email attachments (license, DVLA summary, claims info)
3. Create note in HubSpot, use `#driver referral underwriter` template
4. Manually copy data from email/attachments into template fields
5. Send to underwriter
6. Back-and-forth for missing information
7. Underwriter returns price → relay to broker

## Opportunity

- Structured input (email with standard attachments) → structured output (HubSpot template)
- Claude already proven better than ChatGPT at PDF/document extraction (Fred confirmed)
- HubSpot is both source and destination — no cross-system complexity
- Missing info detection could be automated (flag gaps before sending to underwriter)
- Potential time saving: 2.5–5 hours/day across the team

## Acceptance criteria

- [ ] Map the exact fields in the HubSpot driver referral template
- [ ] Prototype: Claude extracts driver info from sample email + attachments into template format
- [ ] Assess whether this can run as a Claude skill or needs a Zapier/automation trigger
- [ ] Get Fred and Emily's feedback on prototype

## Links

- [[2026-04-08-fred-ai-discovery]]
- [[fred-bush]]
- [[underwriting-assistance-ai]]
