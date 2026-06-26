---
title: "AI Group Therapy — Ishmael, Javier, Chris"
created: 2026-06-24
updated: 2026-06-24
domain: engineering-workflows
type: meeting
tags: [ishmael, javier, chris, engineering, plans, specs, testing, disaster-recovery]
---

## Attendees

- [[ishmael]] (Ismael Jebril, Principal Engineer)
- [[javier]] (Javier Arranz, Engineer)
- [[chris]] (Chris Fothergill, Head of Architecture)
- Tom Harvey

Full transcript: [[2026-06-24-ai-group-therapy-transcript]]

---

## Key themes

### Claude in Slack — connector setup

- Claude added to the retention channel; configure link allows custom prompts per channel
- Connectors (Linear, GitHub) currently authenticated as Thomas — needs a dedicated Claude user so actions appear as Claude in Linear, not the individual engineer
- Available integrations: Linear, GitHub, Google Calendar, Gmail, Stripe
- Custom/MCP connectors (Datadog) not yet working reliably

### Plan files — value, staleness, and spec-driven development

- Usage varies: Javier stores plans + uses them to keep agents on track; Ismael's plans go unused after the fact; Tom uses more structured spec workflow
- Tom's spec format: test plan, smoke test checklist, PR deviation log, architectural decision extraction
  - Specs checked into GitHub; queried through Claude rather than read directly
  - At PR time, second artifact captures deviations from original spec
- Key tension: plans get stale fast; verbose agent-generated plans aren't human-readable
  - Javier: would rather write a concise plan himself than clean up an agent's
  - Ismael: the evolution of a plan (how decisions changed mid-build) is more valuable than the final file
- Chris's framing: plan files map to existing SDLC artifacts
  - Ticket = requirements; inline comments = deviations; PR description = solution + rationale
  - Plans could automate and improve PR descriptions and deviation logging
  - Not all code is agent-written, so plans-folder-only doesn't fit the whole team yet
- Ask agents for concise, structured plans rather than open-ended "plan this"

### Testing standards

- Chris: writing significantly more tests now, just by asking agents to test what they write
- Ismael: not embedding testing in plans yet, but open to it
- Tom: including a test plan in specs forces better code structure + requirement traceability
  - Can also be done ad hoc ("what tests am I missing?") without full spec adoption
- Principles (write tests, document decisions) stay the same; AI makes some easier and some worse if not explicitly enforced

### AI resilience and disaster recovery

- Recent Anthropic/OpenAI outages prompted discussion
- Options: local/open-source models on Mac Mini (~£10k, less than monthly Anthropic spend, but only ~4 engineers); AWS with Nvidia GPUs (more scalable, DevOps overhead)
- Consensus: hackathon-style DR experiment on AWS (spin up instance, install a model, expose an OpenAI-compatible endpoint)
- Bedrock as fallback option: top-tier privacy and pricing but Claude Desktop doesn't work through it; potential chat interface on top of a Bedrock API endpoint

---

## Actions

- [ ] Run a DR experiment: spin up AWS with Nvidia, expose local model endpoint → [[AI-140]]
- [ ] [[ishmael]]: embed test planning into agent workflows
- [ ] All: explore asking agents for concise, structured plans rather than open-ended planning
- [ ] Tom: check if anything is wired to Bedrock as a fallback
