---
title: AI Activation Pathway
created: 2026-06-02
updated: 2026-06-02
type: reference
domain: ai-enablement
tags: [activation, enablement, framework, stages]
---

# AI Activation Pathway

The framework for understanding and measuring how individuals progress from treating AI as a search engine to operating as a director of agent systems. Applied company-wide; scored per-person in people files and aggregated in [[ai-activation-map]].

---

## Activation threshold

> A person crosses the activation threshold when they complete 3 useful tasks in a context-fuelled Claude project — without one-shotting or starting from scratch each session.

Oddly specific is intentional. It forces concrete actions and rules out "I've tried it a few times." The threshold is the same across roles; what counts as a "useful task" varies by context.

The **developer** variant: can load meaningful context into a project, iterate through a non-trivial problem conversationally, and accurately review the output.

The **ops/PM/sales** variant: AI becomes the first step in a new task — before going to a manager, a template folder, or a colleague.

---

## The stages

### Stage 0 — Search mode

Single prompt, read answer, done. No follow-up, no correction, no conversation. The output is often fine but unremarkable, so they don't go back. This is where most unactivated people sit.

### Stage 1 — It's a conversation

First realisation that pushing back, redirecting, and iterating produces qualitatively better output. The model is no longer a search engine.

**Activation threshold sits at the top of Stage 1.** Getting three genuinely useful wins — in a project with loaded context — is what marks the transition from "tried it" to activated.

Failure mode: the "I've tried it" trap. Got a win, it was useful, went back to their normal workflow. The win was a one-off, not a new default. Fix: find the task they do every single day and show them it works there.

### Stage 2 — Context and tools

Understanding that the model is only as useful as the context and tools it can access. Key milestones:
- Front-loading context before asking anything
- Dressing the model: `CLAUDE.md`, conventions, project structure (dev); strategy docs, customer notes, product principles (PM); process maps, role context (ops/sales)
- Giving the model access to real systems (MCP servers, files, APIs, schemas)

The conceptual shift: **you are not writing prompts, you are building an environment for an agent.**

Failure mode: context aversion. Keeps firing questions with no context loaded, gets mediocre results, quietly concludes the model isn't that good. The bottleneck is the user, not the model. Most common stall point. Symptom: "I tried it but the answers weren't relevant to our situation."

### Stage 3 — Conversational fluency

Single-shot thinking is the biggest limiting behaviour at this stage. The person generates output, reads it, and either accepts or closes the tab. Not iterating.

Fluency looks like:
- Pushing back: "That's not quite right — the constraint here is X, try again"
- Building on partial output
- Using the model to check the model: "What are the failure modes of this approach?"
- Thinking out loud with the model before asking for output

The model becomes a thinking partner. For developers, plan mode is the structural intervention: activate plan mode, then interrogate the plan — ideally in a sub-agent running async so you can continue reading while justifications come back.

Danger zone: one-shotting in confidence. Senior people push back; less experienced people (Rob pattern) take output at face value. The Stage 3 ceiling is quality — the output is fine but the person doesn't yet know how to push past "fine."

### Stage 4 — Delegation

Has developed enough fluency and review skill to hand off meaningful units of work. Not one-liners — PR-sized chunks for developers; whole workflows for ops; full campaign prep for sales.

What this looks like:
- Reviewing agent output at the whole-task level, not line-by-line
- Trusting the agent to make reasonable decisions within stated constraints
- Catching and correcting errors efficiently because they understand the domain well enough to spot them
- For developers: multiple sessions in parallel against different tickets; worktrees as the structural signal

**The prerequisite for delegation is the ability to review.** Delegating without review skill means shipping whatever the agent produces. That's the over-reliance-before-mastery failure mode.

Failure mode: burnout risk at Stage 4 if token time (the wait during agent execution) is mismanaged. Context-switching between five sessions is technically valid but cognitively unsustainable. No settled answer to the token time problem yet.

### Stage 5 — Extended orchestration

Current ceiling. The person is not doing the work — they are directing a system.

The psychological shift that unlocks this stage: **you are not an agent babysitter.** The engineering problems are real and novel:

- **Persuasion, not logic.** Traditional work is about expressing intent through output (code, documents, decisions). Agentic work is about getting an agent to adhere to your intent. The instrument is persuasion — what are the tools of persuasion?
- **The adherence spectrum.** From most to least constraining: deterministic function → integration test → unit test → strict system prompt → structured output schema → weak prompt. Knowing where to place each constraint is the judgment call.
- **Context quality as engineering.** The right question is not "does this context file read well?" — it's "does the agent adhere to it?" You cannot know if context is well-weighted by reading it. You know by observing agent behaviour. PromptFoo (or equivalent) for context unit tests: did this change improve or degrade adherence?
- **Human vs agent vs function.** Knowing when each is right, and how to compose them.

People who reach Stage 5 typically stop seeing it as babysitting and start finding the new problems genuinely interesting. Those who stall tend to be ones who haven't made the persuasion/logic reframe.

Stage 5 is the current defined ceiling. Ishmael is operating there; the frontier beyond Stage 5 is not yet characterised. He is the right person to help define what Stage 6 looks like.

---

## Role-specific notes

### Developer

Feedback loop is tight and output is verifiable. The developer pathway is the reference model — other roles adapt from it.

Strong Stage 1 candidates: explaining an unfamiliar codebase, writing a test for code they already wrote, debugging with full stack trace, drafting a PR description from a diff.

Stage 2 context = `CLAUDE.md`, architecture docs, conventions.

Stage 4 prerequisite = review confidence. If a developer can't tell good output from bad, delegation means shipping bugs with extra steps.

### Product Manager

Output quality is harder to verify — a beautifully structured PRD can still be strategically wrong. This makes Stage 3 (conversational fluency, arguing with output) more critical, earlier than in the dev path.

Strong Stage 1 candidates: drafting a spec from a half-formed brief, turning a Slack/Jira thread into a decision log, structuring meeting notes into a brief.

Activation definition: a PM is activated when they use the model as the first draft of their thinking — and find that edit-to-completion time is shorter than writing from scratch.

Stage 2 context = strategy docs, customer interviews, OKRs, product principles.

Risk: PMs are especially vulnerable to polished-but-wrong output. The activation risk isn't that they won't use it — it's that they over-trust it.

### Operations

Shortest path to activation because tasks are discrete and wins are immediately legible ("this would have taken me an hour").

Strong Stage 1 candidates: turning a verbal process explanation into a structured SOP, drafting an email escalation, summarising a support ticket backlog.

Activation definition: AI becomes the first step in any new task — before going to a manager, a colleague, or a template folder.

Failure mode: ops users often reach Stage 3 quickly but never progress to Stage 4 because they don't think of whole workflows as "delegatable." That's the unlock.

Reference model: Emily's team. Daily AI usage, process-first thinking, Zapier automation pipelines, monthly AI/Automations sync. This is what Stage 4 ops looks like in practice.

### Sales / Distribution

Activation is less about depth and more about habit. Individual tasks are simpler but volume is high — 15 minutes saved on every call prep, multiplied by 20 calls a week.

Strong Stage 1 candidates: personalising outreach from a prospect's context, post-call summary from notes, discovery call prep ("what do we know about this account?").

Activation definition: a salesperson is activated when they use AI to research and personalise before every significant customer interaction — not as a writing tool, but as a preparation layer.

Stage 2 context = CRM-connected project with account history, stakeholders, and notes.

Risk: treating the model as a writing assistant only, and missing the research and synthesis capability that compounds.

---

## Framework refinements (from first scoring pass)

Issues surfaced when applying the pathway to ~13 people across engineering, product, ops, finance, and leadership. These should be resolved before rolling the framework out to all staff.

**1. Conceptual model ≠ activation stage (Ed, Matt)**
Both have sophisticated conceptual understanding of Stage 4/5 but practical experience that lags significantly. The framework scores behaviour, not understanding. This is correct but counterintuitive — the CEO scores lower than some junior engineers. This should be stated explicitly so scores aren't read as capability rankings.

**2. Confidence is a first-class concern (Fergus)**
A low-confidence Stage 3 could easily be Stage 2 or Stage 4. Currently confidence is a qualifier but isn't prominent enough. A low-confidence assessment is an instruction to gather more data before acting on the score.

**3. Prior experience from other contexts doesn't transfer (Rob)**
Sub-agent experience at a previous company gives conceptual awareness but hasn't translated into current practice. The framework stages current practice in the current context, not historical peaks.

**4. Stage 1 may need splitting (Queency)**
"Has one working use case and trusts it" is meaningfully different from "uses AI regularly across multiple tasks." The Stage 1→2 definition may need sharpening, or Stage 1 needs sub-stages (1a: first genuine win; 1b: multiple use cases, starting to explore).

**5. Stage 5 needs a frontier description (Ishmael)**
Stage 5 is the current ceiling with no description of what comes next. Ishmael is the right person to help define Stage 6 or the frontier of Stage 5.

**6. Role title is not a reliable pathway indicator (Ollie)**
A TPM who builds things follows the dev pathway more than the PM pathway. Actual behaviour should determine which pathway applies, not job title.

**7. Non-dev Stage 5 needs sharper definition (Emily)**
The ops Stage 5 equivalent is less precise than the dev equivalent. Emily's situation is the worked example to develop it from: making explicit the decision framework she applies intuitively — when does a task go to an agent vs a human? how does she know when an automation has degraded?

**8. Product domain vs personal practice (Mima)**
Building AI infrastructure for a product (PromptFoo evals, skills) is Stage 5 behaviour — but in service of a product she manages, not her own personal workflow. These may need to be tracked separately.

**9. Data freshness**
An assessment decays in reliability over time, especially for people moving fast. The framework needs a "last verified" concept separate from "last assessed." Medium confidence + stale data = could be wrong in either direction.

---

## Scoring convention

In people files, activation stage is recorded in frontmatter:

```yaml
ai_activation_stage: 3
ai_activation_confidence: high | medium | low
ai_activation_assessed: YYYY-MM-DD
```

And a full `## AI Activation` section gives evidence, not-stage reasoning, and progression next steps.

The aggregate view is maintained in [[ai-activation-map]].
