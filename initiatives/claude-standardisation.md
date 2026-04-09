---
title: Claude standardisation
created: 2026-03-27
updated: 2026-03-27
domain: ai-enablement
type: initiative
status: active
origin: directed
owner: tom
tags: [claude, tooling, enterprise]
---

## Summary

Standardise the company on Claude as the primary AI tool. Currently split between Claude and ChatGPT users. Skills development creates a barrier for ChatGPT users that needs resolving.

## Goal

Claude as the default AI tool across all departments. Enterprise deal in place. ChatGPT usage migrated or deprecated.

## Current state

- Company split between Claude and ChatGPT users
- Skills, MCPs, and plugins all Claude-ecosystem
- Enterprise deal negotiation potential (ToS concerns driving urgency)
- Engineering drop-in recommended standardising on Claude

## Dependencies

- Enterprise deal negotiation with Anthropic
- Migration path for ChatGPT users
- Claude desktop installed company-wide

## Risks

- ChatGPT users resist switching
- Enterprise pricing unclear
- ToS concerns if not on enterprise plan
- **Team plan rate limits are now a proven constraint** — Matt Lees hit the cap on Apr 2 running 9 agents (~910K tokens/day, ~25-30M tokens/month). No way to adjust per-seat limits on Team plan. Resets are fixed-cycle. This will get worse as more people build agent workflows.

## Next actions

- [ ] Install Claude desktop company-wide
- [ ] Evaluate ChatGPT removal and migration path
- [ ] Negotiate enterprise deal — rate limits now a concrete argument
- [ ] Evaluate Claude API as overflow for heavy agent users ($130/month Sonnet estimate from Matt Lees)

## Log

### 2026-03-27

- Discussed at engineering drop-in (Mar 25)
- Recommendation to standardise on Claude for tool development

### 2026-04-02

- Matt Lees hit Team plan rate limit — "out of extra usage, resets Apr 6 11am". Running 9 scheduled agents on Enterprise Engine (~910K tokens/day). $69 MTD of $150 individual limit.
- Org is only at 8% of overall monthly spending limit — plenty of budget headroom.
- **Quick fix: raise Matt's individual per-seat spending limit** in the admin console. No plan upgrade needed — just increase from $150 to $300-500.
- Longer-term options still valid: Enterprise plan (higher limits + admin controls), Claude API (pay-per-token, no caps).
- Short-term recommendation: Matt pauses expansion/enrichment agents until reset, keeps core pipeline running leaner
- Medium-term: API key for heavy agent users as overflow. Matt estimated ~$130/month on Sonnet.
- Long-term: Enterprise deal resolves this — higher limits, usage analytics, admin controls
- This is the strongest evidence yet for accelerating the enterprise deal negotiation
