---
title: Define and publish blacklist of unsupported policy configurations
id: AI-083
created: 2026-05-21
updated: 2026-05-21
domain: operational-tooling
type: issue
status: todo
priority: high
assignee: Geran
origin: "[[2026-05-21-finops-prodtech-discussion]]"
tags: [finops, underwriting, policy, operations, governance]
---

## Description

The "don't sell things we can't support" approach hasn't worked because there's no explicit list of what can't be supported. Underwriters operate by intuition, so non-standard configurations get agreed with brokers and then cause operational fires downstream.

Create and publish a blacklist of policy configurations that Flock won't support — starting with the most common operational pain points.

Examples from the finops discussion:
- BACS payments (always GoCardless instead)
- Min/max premium overrides
- Certain rebate offset arrangements

## Acceptance criteria

- [ ] Draft blacklist created from Jade's document + Geran's operational knowledge
- [ ] Reviewed by Anton and Darren (they need to enforce it with underwriters)
- [ ] Communicated to underwriting team clearly — with examples
- [ ] Process defined for how new discoveries get added to the list
- [ ] Published in an accessible location (Notion or underwriting reference doc)

## Notes

Critical: this only works if Anton and Darren are willing to enforce it. The list should grow over time as new edge cases emerge. Design it to be updatable.
