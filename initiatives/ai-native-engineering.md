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

## Activation definition

> A developer is activated when they can load meaningful context into a project, iterate through a non-trivial problem conversationally, and accurately review the output — without needing to one-shot or start from scratch each session.

## Activation pathway

The journey from zero to full activation has identifiable stages. Engineers move through these at different speeds; the failure modes cluster at specific transitions.

### Stage 0 — Google Search mode
Single prompt, read answer, done. No follow-up, no correction, no conversation. This is where most non-activated developers sit. The output is often fine but unremarkable, so they don't go back.

### Stage 1 — It's a conversation
First realisation that pushing back, redirecting, and iterating produces qualitatively better output. The model is no longer a search engine. Engineers at this stage are still in a chat window.

### Stage 2 — Context and tools
Moving from chat window to Claude Code in a repo. Understanding that the model is only as useful as the context and tools it can access. Key milestones:
- Dressing the model: `CLAUDE.md`, conventions, project structure
- Giving access to data (files, APIs, schemas)
- Giving access to tools (MCP servers, shell, Linear)

The conceptual shift: **you are not writing prompts, you are building an environment for an agent.**

### Stage 3 — Plan mode and plan interrogation
Claude Code in a repo, one-shotting is the default here — and the danger zone. Senior engineers push back; junior engineers (Rob pattern) take the output at face value.

Plan mode is the first structural milestone:
- Activate plan mode before execution
- Don't just *read* the plan — *interrogate* it
- Ask questions of the plan faster than the agent can justify itself: run interrogation in a sub-agent so you can continue reading while justifications come back async
- Reconcile justifications at the end

This introduces multi-agent thinking at a small scale: one agent doing, one agent explaining.

### Stage 4 — Multi-agent orchestration
Moving from a single Claude Code instance to multiple coordinated agents:
- Multiple sessions running in parallel against different Linear tickets
- Worktrees as the structural signal — multiple items checked out simultaneously
- Orchestrating agents across repos: front-end and back-end at the same time

This is where the "10 arms" feeling first appears. It is also where **burnout risk emerges** if token time is mismanaged. Context-switching between five sessions against five tickets is technically valid but cognitively unsustainable.

**Token time — open problem.** No settled answer yet. Observed behaviours:
- Making tea (low cognitive load, disengaged)
- Switching to another session (compounds context-switching load)
- Systems thinking, planning ahead (aspirational but hard to sustain)

The Admiral Business data point: a team of five engineers mostly operating at this level. Output is high but burnout is real. The PM↔EM interaction has changed — agents need to be fed far more tickets, creating a product management bottleneck.

### Stage 5 — Extended orchestration and the engineering problems of the new paradigm
Current ceiling: 4+ hours of sustained multi-agent, multi-worktree orchestration. At this point, the engineer is not writing code — they are directing a system.

The psychological shift that unlocks this stage: **you are not an agent babysitter**. The engineering problems are real and novel:

- **Persuasion, not logic.** Traditional engineering is about expressing intent through functions and logic. Agentic engineering is about getting an agent to adhere to your intent. The instrument is persuasion. What are the tools of persuasion?
- **The adherence spectrum.** From most to least constraining: deterministic function → integration test → unit test → strict system prompt → structured output schema → weak prompt. Knowing where to place each constraint is the engineering judgment call.
- **Human vs agent vs function.** Knowing when each is right, and how to compose them in a workflow.
- **MCP servers as the integration layer.** Moving beyond prompts into first-class tool access.
- **Context quality as engineering.** The right question is not "does this markdown file read well?" — it's "does the agent adhere to it?" You cannot know if a context file is well-weighted by reading it. You know by observing agent behaviour.
  - Tool: PromptFoo (or equivalent) for context unit tests — does this change improve or degrade agent performance?
  - Rob pattern failure: reading the document and guessing at weighting, rather than measuring adherence empirically

Engineers who reach Stage 5 typically stop seeing it as babysitting and start finding the engineering problems genuinely interesting. The ones who stall tend to be the ones who haven't made the persuasion/logic reframe.

## Framework observations (from first scoring pass)

Applying the pathway to 12 people across engineering, product, ops, finance, and leadership surfaced the following gaps and edge cases. These should be resolved before rolling the framework out to all staff.

**1. Conceptual model ≠ activation stage (Ed, Matt)**  
Both have sophisticated conceptual understanding of Stage 4/5 but practical experience that lags significantly. The framework scores behaviour, not understanding. This is correct but counterintuitive — the CEO scores lower than some junior engineers. This should be stated explicitly so scores aren't read as capability rankings.

**2. Confidence is a first-class concern, not a footnote (Fergus)**  
A low-confidence Stage 3 could easily be Stage 2 or Stage 4. Currently confidence is a qualifier on the map but isn't prominent enough in the person file. A low-confidence assessment is an instruction to gather more data before acting on the score.

**3. Prior experience from other contexts doesn't transfer (Rob)**  
Rob's sub-agent experience at Boxfish gives conceptual awareness but hasn't translated into practice at Flock. The framework should stage current practice in the current context, not historical peaks elsewhere.

**4. Stage 1 may need splitting (Queency)**  
"Has one working use case and trusts it" is meaningfully different from "using AI regularly across multiple tasks." The Stage 1→2 transition definition may need sharpening, or Stage 1 needs sub-stages (1a: first genuine win; 1b: multiple use cases, starting to explore).

**5. Stage 5 needs a frontier description (Ishmael)**  
Stage 5 is currently the ceiling with no description of what comes next. Ishmael is operating there and the right person to help define Stage 6 or the frontier of Stage 5.

**6. Role title is not a reliable pathway indicator (Ollie)**  
Ollie is a TPM who follows the dev pathway more than the PM pathway. Role title shouldn't determine which activation pathway applies — actual behaviour should.

**7. Non-dev Stage 5 needs sharper definition (Emily)**  
The ops Stage 5 equivalent ("process design and automation decisions") is less precise than the dev equivalent. Emily's situation is a good worked example to develop the ops Stage 5 definition from.

**8. Product domain vs personal practice (Jemima)**  
Jemima runs PromptFoo evals and builds skills — Stage 5 behaviour — but in service of a product she manages, not her own personal practice. "Building AI infrastructure for a product" may need to be tracked separately from "personal activation stage."

**9. Data freshness (Javier)**  
Assessment from April may no longer be accurate. The framework needs a "last verified" concept — an assessment decays in reliability over time, especially for people moving fast.

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
