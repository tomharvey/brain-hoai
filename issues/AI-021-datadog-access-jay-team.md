---
title: "Datadog access for Jay team (Mima + Ishmael)"
id: AI-021
created: 2026-04-28
updated: 2026-04-28
domain: product-ai
type: issue
status: done
priority: high
assignee: tom
due: 2026-04-30
origin: "[[2026-04-28-jordi-1-1]]"
tags: [datadog, jay, observability, access]
---

## Description

Jay's usage data surfaces in Datadog, not PostHog. Neither [[mima]] nor [[ishmael]] currently have Datadog API access. This blocks the feedback loop that made driver claims and referrals successful — the "bonnet open" pattern where the team watches real usage daily and iterates.

Without this, Jay launches and nobody has instrumentation to learn from real users.

## Acceptance criteria

- [ ] Mima has Datadog API access and knows how to query Jay conversation data
- [ ] Ishmael has Datadog API access
- [ ] Both have a habit/skill for checking Jay usage regularly

## Notes

- Tom already has the API keys and export script (packaged in `outbox/datadog-chat-export.zip` for Jemima)
- Same gap exists for Geran's submissions work — unclear where that instrumentation data lives
- Raised independently in both the Matt Price and Jordi 1:1s on 2026-04-28

## Links

- [[2026-04-28-matt-price-1-1]]
- [[2026-04-28-jordi-1-1]]
- [[2026-04-28-jemima-1-1]]
