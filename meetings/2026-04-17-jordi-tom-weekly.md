---
title: Jordi <> Tom — Weekly
created: 2026-04-17
updated: 2026-04-17
domain: engineering-workflows
type: meeting
tags: [weekly, jordi, offsite, workshop, developer-os, alerts, datadog, self-healing]
---

## Attendees

- [[jordi|Jordi Pallares Roset]]
- Tom Harvey

## Key themes

### Workshop planning — strongly validated

Jordi aligned on the three-station rotation with hard outputs. Independently described almost exactly the three threads we've been developing:

1. **Surface insight** — "there's this pile of data that we're not getting the insight we should get out of it"
2. **Encode improvements** — the progression from prompt → skill → deterministic function. "Is this the prompt? Is it a skill? Is it a deterministic function that has a unit test on it?"
3. **Self-healing systems** — "how do we take that context to then feedback into the system... write a linear ticket to say fix this... even better is actually self-healing and it's changing its code"

Jordi naturally described the same methodology applying to multiple data sources — not just Jay, but telemetry, GitHub cadence, Linear tickets, Datadog alerts.

### Quality and ownership of AI output

Jordi raised a specific concern: receiving Notion docs that were clearly AI-generated and sent without review. "We have to review what the AI is producing. As part of this feedback loop... making sure that we as a human, we know what we are selling to another person."

This is distinct from evals (which test the product agent) — it's about the team's own AI-assisted work quality. The cargo-culting pattern Tom described (non-developers attempting refactoring) is the extreme version.

### Alerts workshop coordination

- Chris off next two weeks
- **AI workshop first, then alerts workshop** — deliberate sequencing so the mindset carries over
- Ishmael to demo Datadog AI monitoring (~10 mins in alerts session)
- Jordi will use AI to pre-group existing alerts into topics before the alerts workshop
- Goal: teams discuss services they own and monitoring they want → Jordi works on it
- Shared hope: after the AI workshop, people will naturally think "I'll just connect to CloudWatch/Datadog and ask Claude" instead of reading logs manually

### Tom confirmed Jay conversation data extracted

- Used Datadog API (not MCP) to download all Jay conversations during the Ishmael meeting
- Data is available for Station A4 pre-work
- Ishmael's Datadog UI confirmed as inadequate for browsing at scale

### Developer OS + future of engineering

- Same themes as Fergus/Geran/Rob conversations
- Individual vs team vs company augmentation still an open question
- Jordi's concern: cursor-in-the-cloud assignment was available on Linear for ages but nobody used it — is local-first philosophically different?
- Tom's point: "just running Claude in plan mode inside a repo doesn't feel like the end state — that feels like stage 2, we should be at stage 10 by now"

## Actions

- [ ] Tom: finalise 3-station workshop plan — share with Jordi and Fergus
- [ ] Ishmael: prepare 10-min Datadog AI monitoring demo for alerts session
- [ ] Jordi: pre-group alerts using AI before the alerts workshop
- [ ] Confirm schedule: AI workshop first, alerts second

## Notes

Jordi independently validated the three-thread model (insight → encode → self-healing) and noted it applies beyond Jay to any data source. His quality/ownership concern is a strong candidate for the third station or a thread woven through all three.

The alerts workshop sequencing after the AI workshop is deliberate and smart — the AI session should change how people approach the alerts discussion that follows.

Full transcript: [[2026-04-17-jordi-tom-weekly-transcript]]
