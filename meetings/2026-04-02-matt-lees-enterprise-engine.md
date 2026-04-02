---
title: "Matt Lees: Enterprise Engine + Distribution AI"
created: 2026-04-02
updated: 2026-04-02
domain: operational-tooling
type: meeting
tags: [matt-lees, fergus, enterprise-engine, agents, distribution, lovable, apollo]
attendees:
  - "[[matt-lees|Matt Lees]]"
  - "[[fergus|Fergus Doyle]]"
---

## Context

First call with Matt Lees. Fergus joined. Two topics: the TCO Value Statement (client-facing docs via Claude + Lovable) and the Enterprise Engine (9 autonomous agents managing a £294M sales pipeline). The Engine dominated the conversation.

**Pre-call context** (Slack — Fergus to Tom/Jordi/Mima): Fergus's initial reaction was "overengineered solution... might struggle with ownership/maintainability." Matt had asked for Claude API keys; Fergus gave a cautious answer and wanted a call first. Fergus wanted to join to understand the ambition and for optics (not wanting to seem unhelpful). Post-call: shifted to thumbs up. Happy for Tom to run point going forward.

## Notes

### Enterprise Engine — what Matt built

- 9 autonomous agents on Claude Cowork managing the full enterprise sales pipeline
- **64 accounts, £294M estimated premium** (was 18 accounts 3 days ago)
- Morning chain: email sync → pipeline scoring → Apollo enrichment → outreach drafts → daily briefing → contact validation
- Afternoon: pipeline expansion (8-12 new accounts/day) + MEDDPICC action plan updates
- 22% reply rate on first outreach batch
- Cost: $104/month (Apollo) + existing Team plan seat
- Built in ~5 days with no engineering support
- Human-in-the-loop: Gmail drafts only, Slack DMs only, never sends autonomously
- Apollo self-identified email bounce-backs and suggested its own integration — agent improved itself

### Why enterprise prospecting was paused and restarted

- Previous direct outreach created friction with broker relationships — brokers saw Flock going direct as a threat, clients wanted cheaper direct rates
- Message got diluted, approach got messy → paused
- Restarted with clearer broker-led message: "introduce your broker, don't bypass them"
- Target: fleet operators proactively pushing their broker to consider Flock at renewal
- **Admiral acquisition driving urgency** — subject lines referencing "what Admiral's move into commercial fleet might mean for your business"
- Target fleet size: **200+ vehicles** — sweet spot avoids mega-fleets (10k-100k) that self-insure with high excesses
- Typical sales cycle: 6-9 months ahead of renewal

### TCO Value Statement (smaller topic)

- Client-facing renewal/new business docs via Claude skill + Lovable templates
- 12-step process documented in Notion + Loom
- Mima: experimental, not product-market fit — deprioritised pending Q2 OKR progress on simplifying value sales approach
- Matt keeping local for now

### Concerns raised

- Cowork projects cannot be shared — bus factor of 1, tied to Matt's laptop
- No cloud sync, no backup of pipeline JSON
- ~25-30M tokens/month — Team plan rate limits a risk at scale
- Apollo ($104/month) — procurement/security awareness needed
- Gmail read + draft access — infosec implications
- 9 autonomous agents with no monitoring/alerting if one fails
- No path to team access without moving to proper infrastructure

## Decisions

- Thumbs up from Fergus — keep going, keep Antton in the loop
- HubSpot connector is the next priority — store enriched company data on company records (not deal records)
- Matt to back up Cowork project files to Google Drive regularly
- Tom to grab 15 mins with Matt next week to review front end and share tips

## Actions

- [ ] Matt Lees: confirm call was a thumbs up with Antton, share progress updates
- [ ] Matt Lees: explore HubSpot connector for enriched company data storage
- [ ] Matt Lees: back up Cowork project files to Google Drive — laptop loss is the main risk
- [ ] Matt Lees: maintain manual oversight on outbound emails given scale/value of targets
- [ ] Tom: book 15 mins with Matt Lees next week — review front end, share tips (PDF generation via Claude instead of Lovable, template-based email paragraphs, agent file backup)
- [ ] Tom: assess HubSpot architecture for storing enriched fleet data — confirm low impact on existing deal records
- [ ] Tom: position Enterprise Engine in board roadmap as reference implementation

## Links

- Transcript: too large to embed (50KB) — source: [Granola](https://notes.granola.ai/d/285387d3-6be0-4079-ae84-391df5b27162)
- Related: [[agent-framework]], [[skills-distribution]], [[ai-capability-uplift]], [[insight-layer]]
- Technical review: [[enterprise-engine-technical-review]]
- TCO process: [[tco-value-statement-process]]
