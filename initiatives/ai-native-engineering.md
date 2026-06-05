---
title: AI-native engineering — developer harness pilot
created: 2026-04-16
updated: 2026-06-02
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

## Activation pathway

The Stage 0–5 activation framework originated here but is now company-wide. Canonical definitions, role-specific variants, failure modes, and scoring conventions live in [[activation-pathway]]. The company-wide rollout is tracked in [[ai-activation]].

For this initiative, the relevant activation context is: engineers in the pilot (Javier, Rob) are the concrete test cases for what Stage 3→4→5 progression looks like in practice. Observations from the pilot feed back into the framework.

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

### 2026-05-20 — Philosophical AI workshop design (with Ollie)

- Developed a structured workshop format for engineers on the philosophical dimensions of AI adoption. Designed in conversation with [[ollie-crowe]].
- Engineering-specific angle: Mode 1 vs Mode 2 as the central frame. Most engineers are still Mode 1 (ask→wait→repeat). The target is Mode 2 (sit outside the loop, guide and repoint).
- Token time as the honest question nobody has fully answered — Stephen's "make another cup of tea", Tom's "20 arms" reframe. Token time is parallel time, not dead time.
- Three-layer systems design exercise as the centrepiece: deterministic functions / agentic steps / human judgment points. Stephen's Databricks monitoring system is the worked example.
- "Employable in 2030" is the frame that lands best with this audience.
- See: [[philosophical-ai-workshop]]

### 2026-05-21 — Office conversations: developer journey mapping

Cross-team conversations in the office surfaced a detailed picture of the activation pathway from zero to current ceiling. Key threads:

- **The one-shot trap** is the primary failure mode at Stage 3. Rob's pattern (takes output at face value) vs senior engineer pattern (pushes back) is the most visible divergence in the team right now. Plan mode is the structural intervention — it forces a review step before execution. Interrogating the plan via sub-agent while continuing to read is the advanced form.
- **Token time remains unsolved.** Most engineers at Stage 4 are context-switching between multiple sessions, which works but compounds cognitive load. Worktrees are a useful signal that someone is at multi-agent scale. No clean answer to what to do during token time — systems thinking is the aspiration, but not what's actually happening.
- **Admiral Business data point**: team of five, mostly at Stage 4–5. High output but real burnout. The PM bottleneck has emerged — agents consume tickets faster than PMs can produce them. This is a structural consequence of activation, not a dysfunction.
- **The engineering identity reframe is the unlock for Stage 5.** Engineers who make it past the "agent babysitter" framing find the new problems genuinely interesting. Those who don't make that reframe tend to stall. The new engineering challenges: adherence spectrum (deterministic function → weak prompt), persuasion as the instrument of intent, human vs agent vs function composition decisions.
- **Context quality measurement.** Rob's instinct to read the markdown and guess at weighting is wrong — you don't know until you watch the agent. PromptFoo as a candidate tool for context unit tests: did this change improve or degrade adherence?
- **Current activation ceiling**: 4+ hours of sustained multi-agent, multi-worktree orchestration across front-end and back-end repos simultaneously.

### 2026-05-18 — Dev AI Practices session — Fergus, Jordi, Chris, Ishmael, David

- Fergus endorsed the direction: harness engineering is the lesser risk vs not building one. CICD analogy used — treat it as a technology initiative on the priority stack.
- Key insight surfaced: two fundamentally different AI use modes. Most engineers are in Mode 1 (ask → wait → repeat). Target is Mode 2 (sit outside the loop, guide and repoint).
- Endorsements process agreed as first isolated end-to-end workflow pilot ([[AI-053]]).
- Jordi + Chris to write engineering target state document ([[AI-054]]).
- Rob needs targeted critical-thinking scaffolding — different support from Chris/Ishmael ([[AI-055]]).
- Job security concern named explicitly by Tom. Room accepted the framing: lean into novel skills, recognise what's being commoditised.

### 2026-04-28 — Engineering AI adoption snapshot + pair prompting

- **Jordi 1:1 — team AI adoption read**:
  - Ishmael: most AI-native, likely not handcrafting code. Was on Sonnet not Opus — upgraded to 4.7.
  - Harvey: using Claude Code, frustrated with frontend detail quality. Candidate for "pair prompt" session with Ollie.
  - Rob: improving, likely enthusiastic for SDLC-of-the-future conversation.
  - Jacob: uses AI as a harness, unclear if generating code.
  - Sami (new hire): flagged by Jordi as not very AI-driven. 30-day goal set: AI is part of workflow, not a side project.
  - Ollie: getting beaten up by Anton on direction, sees SDLC exploration as a distraction.
- **Pair prompting concept**: Tom proposed Ollie + Harvey sit together and prompt their way to a solution live. Jordi enthusiastic ("worst thing is they learn"). → AI-023
- **Jemima + Ishmael working pattern**: shifted from PRD→handoff→done to close back-and-forth partnership. Sharing files (DB structure, frontend code) to refine requirements together. Tom flagged John Cutler's co-prompting article as relevant.
- **Jordi side project**: Claude-based cron job running in cloud that checks repo vulnerabilities and auto-raises PRs. Already running on personal repos, wants to apply to Flock platform repo. Tom's parallel: consolidate Dependabot PRs into single reviewed PR.
- See [[2026-04-28-jordi-1-1]], [[2026-04-28-jemima-1-1]]
