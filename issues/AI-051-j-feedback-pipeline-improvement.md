---
title: Improve J feedback transcript pipeline — persistent memory and broader scope
id: AI-051
created: 2026-05-18
updated: 2026-05-18
origin: "[[2026-05-18-product-team-context]]"
domain: product-ai
type: issue
status: todo
priority: medium
assignee: tom
tags: [jay, feedback, transcripts, self-healing, Francesco]
---

## Description

The J feedback pipeline (built by Francesco) currently takes a snapshot of the last week's calls and synthesises them. The team identified two problems:

1. **No persistent memory** — it treats known issues (e.g. claims servicing slowness) as novel every week, generating urgent-sounding noise the team ignores
2. **Narrow scope** — only reads J transcripts; misses Granola chats, HubSpot, PostHog, Datadog signals

The fix: give the pipeline context of what the team is already working on (OKRs, initiatives, roadmap) so it surfaces only novel, strategy-relevant insight. Also broaden the data sources it reads.

## Acceptance criteria

- [ ] Speak to Francesco about current pipeline architecture
- [ ] Add strategy/OKR context to the pipeline prompt (what's already known and being addressed)
- [ ] Extend data sources to include Granola transcripts, HubSpot, PostHog where relevant
- [ ] Output should be ≤200 words of novel insight, not a full weekly recap
- [ ] Test with one product drop-in as a standing agenda item

## Links

- [[2026-05-18-product-team-context]]
