---
title: "Ollie / Tom — BDM Enablement"
created: 2026-06-11
updated: 2026-06-11
domain: ai-enablement
type: meeting
tags: [ollie-crowe, bdm-brain, acquisition-brain, cowork, scheduling, architecture]
---

# Ollie / Tom — BDM Enablement

**Date:** 2026-06-11
**Attendees:** [[ollie-crowe]], Tom

Full transcript: [[2026-06-11-ollie-tom-bdm-enablement-transcript]]

---

## Key themes

### BDM brain vs. acquisition/underwriting brain — separate by design

Ollie raised whether the acquisition brain and BDM brain should combine. Tom's view: keep separate. The BDM use case is a **librarian / secretary / coach** — superpower the relationship and the person. Underwriting assistance and finance are **agent-shaped** — do as much of the task as possible with minimal human interaction. Mixing them now risks blurring both. Underwriters are not ready anyway (BDMs are far ahead).

Corollary: the product-PM framing maps naturally here. Ollie acts as PM to the BDMs-as-engineers. Tom brings architectural and technical support. Together they raise BDMs to "mechanic" level — not system builders, but able to maintain and extend their own tools.

### Acquisition brain status

Rob and Tom Harvey have access. Tom Harvey has added technical documentation. The brain is structured with a Google Drive–synced folder shared with the team, skills including an onboarding skill, and the pattern should evolve over time. Alex (engineering) had laptop issues slowing adoption; structure is there but real usage needs to start.

### Resolver / routing architecture

Ollie described his pattern: an `agents.md` file drives actions, a `resolver.md` routes queries to the right skill. This resolver is how the agent decides when to go to Granola, HubSpot, Looker, etc. Tom confirmed this maps to his own MCP tool routing approach. Strong resolvers are the prerequisite for the brain to be reliable. This should be built into the BDM brain — not left to the BDM to construct.

### Scheduling: co:work is client-side

Ollie confirmed co:work scheduled tasks are **client-side** only — the app must be open. His HubSpot label classifier runs every 30 mins and has done 123 runs. Gary Tan's version is cloud-based (different infrastructure). This is the key gap for fully automated scheduled tasks — needs either a cloud scheduler fallback or acceptance that tasks run when the app is open. Tom noted he's written his own idempotent scheduler on his machine as a workaround.

**Design implication**: This confirms the architectural decision in `decisions/005-bdm-brain-scheduling-architecture.md`. Server-side scheduling assumption needs validation. Fallback (n8n / GitHub Actions) may be needed sooner than expected.

### Session-close hooks in co:work

Tom raised: can a session-close trigger an automated self-improvement review in co:work? Unknown — to test. If yes: the `/session-close` skill becomes automatic. If no: prompting the BDM to run it manually is the fallback (which is the current design).

### Voice narration for phone calls

Confirmed again (first raised with Adam, Jun 10). End-of-day prompt: "did you have any phone calls you want to narrate?" BDMs are good with Granola but quick phone calls are missed. The brain should prompt for these. → Already in EOD nudge design.

### Workshop framing

For Monday: start with a simple diagram showing roles (librarian, secretary, coach, strategic partner) made BDM-specific. Don't present finished products — present examples. The goal is to capture Adam's imagination and let the team bounce off each other. Matt Lees needs guardrails more than capability; Sophie/Alex need a ready-made framework. The "resolver + skills" structure is what to build in the workshop, not polished outputs.

---

## Actions

- [ ] **Tom + Ollie**: share Google Drive with proposed BDM brain structure (Ollie to send) before Monday
- [ ] **Tom**: test whether co:work session-close hooks fire automatically at end of a session
- [ ] **Tom + Ollie + Adam**: align Monday on architecture, then run team session Wednesday
- [ ] **Tom**: validate server-side scheduling assumption with a simple test (5-min Slack task, app closed) — see `decisions/005`
