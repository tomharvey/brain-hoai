---
title: "Scope submissions automation into small achievable goals"
id: AI-009
created: 2026-04-02
updated: 2026-04-28
due: 2026-04-14
origin: "[[2026-04-02-shreya-ai-discovery]]"
domain: operational-tooling
type: issue
status: todo
priority: medium
assignee: tom
tags: [submissions, automation, shreya, fergus]
---

## Description

Submissions/new business logging is entirely manual and flagged by multiple people (Shreya, Fergus, Tom) as a major automation opportunity. It's too large to tackle as one project — needs to be broken into small, achievable goals across dedicated meetings with Shreya and likely Fergus.

## Acceptance criteria

- [ ] Schedule dedicated meeting(s) with Shreya (and Fergus if needed) to scope the work
- [ ] Break into discrete, achievable milestones
- [ ] Identify first milestone that can be delivered quickly

## Notes

- Three groups were already working on submissions independently (flagged in Chris's meeting, week 1)
- Abs's CC extraction tool is part of this — handover needed before Abs leaves
- Haulage portal Claude prompt (CC→CSV) reportedly faster than Abs's Retool version
- Human-in-the-loop chat interface was the emerging direction from earlier conversations
- This is tracked as a separate initiative: [[submissions-automation]]
- **2026-04-28**: Ollie's conversion bet reframing ([[ollie-conversion-bets-2026-04-27]]) changes the scoping context. Pipeline now framed as substrate for three bets (development factor, submission scoring, driver data). Scoping should account for these downstream consumers, not just operational efficiency.
- **2026-04-28**: Matt Price aligned on data substrate framing. Key gap: "build the data substrate first" message hasn't reached Ollie. Matt's steer: log opportunities in Linear as slices of the same underlying work. Also: instrumentation gap — no PostHog equivalent for submissions, unclear where feedback data lives. Tom to follow up with Ollie. See [[2026-04-28-matt-price-1-1]].

## Links

- [[2026-04-02-shreya-ai-discovery]]
- [[submissions-automation]]
- [[shreya-chowta]]
