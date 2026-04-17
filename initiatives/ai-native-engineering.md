---
title: AI-native engineering — developer harness pilot
created: 2026-04-16
updated: 2026-04-16
domain: engineering-workflows
type: initiative
status: active
origin: directed
owner: Javier Pallares (build) / Tom Harvey (sponsor)
tags: [engineering, agents, claude-code, linear, pull-requests, 2027, strategic]
---

## Summary

Build and pilot a local-first developer harness — a "personal OS for developers" — that turns Linear tickets into draft pull requests, learns engineering practices from developer feedback, and surfaces architectural decisions as first-class artefacts. The harness is the vehicle; the real question is *what does a software engineer look like in 2027?* and how do we start engaging with that today.

## Goal

Answer two linked questions through doing, not theorising:

1. **Tactical**: Can a local agent, given a Linear ticket + `CLAUDE.md` + a repo, produce a draft PR good enough that the engineer's job becomes reviewing, correcting, and *teaching the agent* — not writing code manually?
2. **Strategic**: Does this shift engineers from mechanical coding to architectural thinking, domain modelling, and decision-making? If so, what does the engineering practice look like a year or two out?

Frame: **better, not faster.** 10x better, more robust, more tested, more documented — not 10x faster.

## Current state

- Javier agreed to pilot, starting from his current Acquisition AI PoC (HubSpot→Claude→Flock API quoting, ~due Apr 24) as the minimal-scoped testing ground
- Javier already has a `CLAUDE.md` at the repo level — a foundation exists
- Tom has a working reference implementation in this vault (HoAI personal OS) and a separate developer-adjacent project (Rosenfeld energy market data) to draw on
- Local-first, SQLite vector-encoded personal OS pattern validated in Tom's Flock vault
- Conceptual parallel: `g-stacks.org` (CEO/PM/QE personas) — useful as reference, not a template

## Hypothesis

> A harness around a developer — Linear integration, draft PR automation, decision logs, coding-standard capture, feedback loop — lets them think about the **domain** rather than the **curly brackets**. The speed that comes out of that is incidental; the engineering quality is the point.

Corollary: engineering practices that were previously **implicit** get surfaced and made explicit through the act of correcting the agent. Architectural decision records fill themselves in. Code review shifts from syntax-level debate to architecture-level debate.

## The experiment

### Month 1 — Javier stops coding
- Linear → cron job → draft PR on a named branch
- Javier reviews, either:
  - rejects and restarts
  - hand-edits the PR directly
  - **teaches the agent** why the approach was wrong, updating the harness
- At end of each piece of work: what got wrong? how do we do it better next time? → feedback captured into the harness (standards, patterns, anti-patterns)

### What emerges organically (hypothesised)
- Architectural decision logs (auto-populated from each PR)
- Coding standards made explicit
- "Give me PRs for both approaches" becomes a tool — real exploration of alternatives, not mental modelling
- Meetings-as-context (Granola) feeding the harness the *why* behind tickets

## Scope

**In scope:**
- Local-first harness on Javier's laptop (philosophical choice — "if I'm off, it's off")
- Claude Code / Claude Desktop ecosystem
- One repo, one developer, one PM (Ollie)
- Include Ollie in the loop — how he writes tickets affects harness quality

**Out of scope (for now):**
- Cloud-hosted agents (explicitly different from Cursor Cloud Agents)
- Team-wide rollout
- Cross-repo agent coordination (may emerge later)

## Dependencies

- Javier's existing Acquisition AI PoC as the sandbox
- Ollie's willingness to iterate on ticket writing
- Claude Code stability / rate limits (tied to [[claude-standardisation]])
- Meeting context capture (Granola pattern, already proven in Tom's vault)

## Risks

- **Productionisation question** (raised by Javier): once the harness works on laptop, how do we make it durable, tracked, shared? No answer yet — deliberately parked.
- **Job-security anxiety** (raised by Javier): if we encode engineering practices well enough that an AI can apply them, what happens to engineers? Reframe to sell internally: this makes **better** engineers, not replaced engineers. But the narrative will need active management — particularly with non-engineering leadership who may read "10x faster" into any AI-for-eng story.
- **Month-one regression**: Javier will likely be *slower* while teaching the agent. This is the expected cost. Needs to be set up front with Fergus, Jordi, and the wider team so "slow for a month" isn't mistaken for failure.
- **Scope creep** into an abstract 2027 vision that never ships. Kept honest by the concrete ticket→PR loop as the forcing function.

## Strategic fit

- Feeds the Head of AI pitch milestone: *"Prodtech team deliver agentic systems as naturally as non-agentic. They prefer the iteration speed and insight agentic services deliver."* (Days 61–90)
- Candidate for the board roadmap (AI-001) under Engineering Workflows — sits alongside the [[agent-framework]] and [[ai-code-review]] initiatives
- Directly engages Fergus's strategic bet on pace — the answer to "how does a small team deliver at scale" is partly this
- Complements the [[insight-layer]] initiative: insight-as-data (for the business) ↔ decisions-as-data (for engineering)

## Next actions

- [ ] **Tom**: Share Claude conversations (advanced research chats) that shaped the HoAI vault — Javier to use as seed context
- [ ] **Javier**: Review `g-stacks.org` for pattern inspiration — adapt, don't copy
- [ ] **Javier**: Bootstrap prompt in Claude Code to scaffold the developer harness on top of his existing repo + `CLAUDE.md`
- [ ] **Javier**: Stand up the Linear → draft PR loop (scoped as a 1-day build)
- [ ] **Javier**: Begin month of not-coding; capture the feedback loop in decision logs / standards files
- [ ] **Tom**: Loop Ollie in — ticket-writing iteration is part of the harness quality
- [ ] **Tom**: Flag to Fergus as an engineering-workflows initiative for the roadmap — explicitly set the "slow month" expectation up front

## Log

### 2026-04-17 — Rob Grice discovery call

- Rob is week 1 on the acquisition squad. Already connected HubSpot MCP and is exploring the submissions pipeline.
- Strong AI user — Claude as primary tool, previous sub-agent experience across 9 repos at Boxfish.
- Shown Tom's personal OS vault — visibly engaged with the concept.
- Doesn't currently encode lessons from AI mistakes ("I just work around it") — exactly the habit this pilot aims to change.
- Ollie was discussed but not on the call. Rob has heard the pilot concept; Ollie has not — needs separate briefing before Station B at the offsite.
- Rob's former colleague at Boxfish had a working Jira→GitHub→OpenClaw pipeline — prior art for the Linear→draft PR loop.
- Key risk: Rob is week 1. The "slow month" for the pilot overlaps with his ramp-up. Could amplify or compound the slowness. Mitigated by: greenfield problem, no legacy habits, Javi as the experienced lead.

### 2026-04-16 — kickoff conversation

- Concept discussed with Javier after a cryptic Slack message from Tom
- Javier interested, expressed concern about job security — addressed directly with "better not faster" framing
- Javier already running a `CLAUDE.md` at repo root — foundation exists
- Current HubSpot→Claude→Flock API quoting PoC chosen as the sandbox (already scoped, due ~Apr 24, minimal blast radius)
- Agreement: **not coding for a month** as the forcing constraint
- Tom to share his Claude Desktop advanced-research chats as seed material
- Christian quote referenced: *"How did we have such velocity in such a small team?"* — the team's trust + pace is the context this experiment sits inside. The point is to compound that capacity, not to replace the team.
- Javier's closing framing: *"A future where we sit down at a table, hit record, and by the time we leave the door it's done"* — context-capture as primary engineering artefact

Full meeting note: [[2026-04-16-javier-ai-native-engineering]]
