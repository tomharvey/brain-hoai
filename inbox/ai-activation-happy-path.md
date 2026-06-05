---
title: AI activation happy path — developer model and role variants
created: 2026-05-22
updated: 2026-05-22
domain: ai-enablement
type: inbox
status: ingested
tags: [activation, enablement, developer, draft]
---

# AI Activation: The Happy Path

*Rough draft — thinking piece, not polished doc.*

---

## The core problem

People ask one question, get a mediocre answer, and move on. They've treated the model like a search engine — one shot, assess, close. The answer was fine but not remarkable, so they don't go back. What they haven't discovered is that the quality ceiling isn't in the model — it's in the conversation. Activation is the moment that stops happening.

**Activation hypothesis:** A user crosses the threshold when they complete 3 useful tasks in a context-fuelled project. Oddly specific is the point — it forces concrete actions and rules out "I've tried it a few times."

---

## Developer happy path

### Stage 1 — First genuine win

The task needs to be real work, not a toy example. Best candidates for first wins:

- Explaining an unfamiliar codebase or PR ("what does this do?")
- Writing a test for a function they already wrote (low stakes, fast feedback loop)
- Debugging a gnarly error with full stack trace pasted in
- Drafting a commit message or PR description from a diff

What makes these work: they're bounded, the developer can verify the output immediately, and there's no ambiguity about whether it helped. The win is felt in minutes, not days.

What to avoid for Stage 1: open-ended architecture questions, greenfield design, anything where "good" is hard to define in under 10 minutes.

### Stage 2 — Context mastery

This is where most developers stall if they had a win at Stage 1. They got something useful and try to repeat it — but the next session starts from scratch. The model doesn't remember the codebase, the conventions, or why things are the way they are.

Context mastery means learning to front-load context before asking anything:

- A `CLAUDE.md` (or equivalent) in the repo root — conventions, architecture decisions, what to avoid
- Pasting relevant file sections, not just the error
- Opening a project in Claude Code rather than the chat window
- Understanding what "indexed" means (the model has seen the files) vs what needs to be explicitly quoted

The shift in mindset: the model is only as good as the context you give it. A mediocre prompt with rich context beats a polished prompt with none.

### Stage 3 — Conversational fluency

Single-shot thinking is the biggest limiting behaviour. The developer writes a prompt, reads the output, and either accepts it or closes the tab. They're not iterating.

Conversational fluency looks like:

- Pushing back: "That's not quite right — the constraint here is X, try again"
- Building on partial output: "Good, now apply the same approach to the other 3 endpoints"
- Using the model to check the model: "What are the failure modes of this approach?"
- Thinking out loud with the model before asking for output

The model becomes a thinking partner, not a code dispenser. This is the stage where developers start saying things like "I was talking to Claude about this..." — the agent is now part of their cognitive loop.

### Stage 4 — Delegation

The developer has developed enough fluency and verification skill to hand off meaningful units of work. Not one-liners — PR-sized chunks.

What this looks like:
- "Implement this issue. Here's the spec, here are the relevant files, here are the tests you need to pass."
- Reviewing the agent's output at the pull request level, not line-by-line
- Trusting the agent to make reasonable decisions about structure and naming, within stated constraints
- Catching and correcting errors efficiently because they understand the codebase well enough to spot them

The prerequisite for delegation is the ability to review. If a developer can't tell good output from bad, delegation means shipping bugs with extra steps.

### Stage 5 — Integration

AI is no longer a separate activity — it's part of the SDLC. The developer doesn't "go to Claude" the way they'd open a browser tab. It's already in the loop.

What integration looks like:

- Claude Code running in the terminal, aware of the working directory
- MCPs connecting the model to real systems: Linear, GitHub, Datadog, Slack
- Pre-commit hooks, CI commentary, PR review automation
- Custom skills that encode team conventions and run them on demand
- The model as the interface to internal tooling, not just external APIs

At this stage, the developer has stopped thinking about AI as a tool and started thinking about it as infrastructure.

---

## Developer activation definition

**A developer is activated when they can load meaningful context into a project, iterate through a non-trivial problem conversationally, and accurately review the output — without needing to one-shot or start from scratch each session.**

---

## Failure modes

### Stalling at Stage 1 — the "I've tried it" trap

They got a win. It was useful. They went back to their normal workflow. The win was a one-off, not a new default. Often happens when the first win was in a low-stakes context that doesn't connect to their daily work. The fix is not more demos — it's finding the task they do every day and showing them it works there too.

### Context aversion

They skip Stage 2 entirely. They keep firing questions at the model with no context loaded, getting mediocre results, and quietly concluding the model isn't that good. They don't realise the bottleneck is them. This is the most common stall point. Symptoms: "I tried it but the answers weren't relevant to our codebase." Fixing it requires showing them the before/after of the same prompt with and without context.

### Over-reliance before mastery

They reach Stage 4 behaviourally (delegating work) without going through Stage 3 (developing the ability to review output). This is the Rob problem: they don't yet know what good looks like, so they can't catch errors. Result: bugs shipped, trust broken, reversion. The model's output quality isn't the failure — the absence of a verification layer is. Fix: slow down delegation until review confidence is genuine.

### Tool switching

They use Claude for a week, switch to Copilot, try Cursor, go back to ChatGPT. Every tool restart means starting the context and conversational muscle memory from scratch. Depth compounds. Breadth doesn't. The goal is one tool, used deeply enough to develop instincts — then expand. The instincts transfer even if the interface doesn't.

---

## Applicability to other roles

The developer path is the reference model because the feedback loop is tight and the output is verifiable. Other roles have longer feedback cycles and fuzzier success criteria, which changes what activation looks like and how you get there.

---

### Product Manager

**Stage 1 — first win:**
Drafting a spec, user story set, or competitive teardown from a half-formed brief. The PM already has a mental model of what they want; the model externalises and structures it faster than they can type. Other strong candidates: summarising a long thread of Slack/Jira commentary into a decision log, or turning meeting notes into a structured brief.

**Activation definition:** A PM is activated when they use the model as the first draft of their thinking — and find that the edit-to-completion time is shorter than writing from scratch.

**Key difference from dev path:** There's no equivalent of "run the tests." Output quality is harder to verify — a beautifully structured PRD can still be strategically wrong. This makes Stage 3 (conversational fluency) more important earlier: the PM needs to argue with the output, not just accept it. Context mastery also looks different — it's loaded from strategy docs, customer interviews, and product principles, not a codebase.

**Risk:** PMs are especially vulnerable to polished-but-wrong output. The activation risk isn't that they won't use it — it's that they over-trust it.

---

### Operations

**Stage 1 — first win:**
Writing or improving a process document. Ops staff usually have tacit knowledge of how something works; the model can turn a verbal explanation into a structured SOP in one pass. Other strong candidates: drafting an email escalation, analysing a small data export, summarising a support ticket backlog.

**Activation definition:** An ops team member is activated when AI becomes the first step in any new task — before going to a manager, a colleague, or a template folder.

**Key difference from dev path:** Ops teams often have the shortest path to activation because the tasks are discrete and the wins are immediately legible ("this would have taken me an hour"). The failure mode is the opposite of the developer's: ops users often get to Stage 3 quickly but never build toward Stage 4 because they don't think of their work as "delegatable." The step they need help with is realising that whole workflows — not just single tasks — can be handed off.

**Note:** Emily's team at Flock is already at Stage 4–5 and is the reference model for the rest of the company.

---

### Sales

**Stage 1 — first win:**
Personalising an outreach email with context from a prospect's LinkedIn, recent news, or shared connection. This is fast, immediately useful, and the improvement over a generic template is obvious. Other strong candidates: prep for a discovery call (what do we know about this account?), post-call summary from notes, objection handling prep.

**Activation definition:** A salesperson is activated when they use AI to research and personalise before every significant customer interaction — not as a writing tool, but as a preparation layer.

**Key difference from dev path:** Sales activation is less about depth and more about habit. The individual tasks are simpler but the volume is high. The win isn't one transformative output — it's 15 minutes saved on every call prep, multiplied by 20 calls a week. Context mastery for a salesperson means maintaining a CRM-connected project with the account's history, stakeholders, and notes — so that each interaction starts informed. The risk is treating the model as a writing assistant only, and missing the research and synthesis capability that compounds over time.

---

## Cross-cutting observation

Every role has a version of the context aversion failure mode. Developers don't load the codebase. PMs don't load the product strategy. Ops staff don't explain the process. Salespeople don't brief the account context. In all cases, the output is disappointing, and the user blames the model.

The activation curriculum — whatever form it takes — needs to make "front-load context first" the first lesson, not an advanced technique.
