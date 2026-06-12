---
title: AI Adoption Frameworks
created: 2026-06-12
updated: 2026-06-12
domain: ai-enablement
type: reference
tags: [frameworks, enablement, adoption, strategy]
---

# AI Adoption Frameworks

Three complementary lenses for understanding how people and teams grow with AI. The [[activation-pathway]] describes individual skill progression. These frameworks describe *type of use*, *relationship model*, and *target capability* — and together they shape how we design programmes, tools, and interventions.

---

## 1. Team role taxonomy

How a team uses AI — what job the AI is doing for them. Based on the BDM brain work but applicable across all departments.

| Role | What it means |
|------|---------------|
| **Librarian** | Retrieves and synthesises information the team already holds — across CRM, meeting notes, documents. "What do we know about this account?" |
| **Secretary** | Handles workflow and administrative tasks — follow-up tracking, meeting summaries, CRM hygiene, action capture |
| **Coach** | Improves individual capability — post-meeting feedback, preparation, pattern recognition on what's working |
| **Forecaster** | Predicts outcomes before the human notices — ghost accounts, conversion likelihood, pipeline risk |
| **Strategy partner** | Helps think through decisions — pre-call briefing, synthesis of context into a direction |
| **Sparring partner** | Pushes back on decisions — adversarial mode, challenges assumptions, stress-tests reasoning |
| **Caretaker** | Keeps the team's knowledge clean — enforces structure, flags stale records, maintains controlled vocabularies |
| **Apprentice** | Self-improves from usage — learns what queries recur, surfaces gaps, suggests schema improvements |

Most teams start at Librarian/Secretary. The higher roles (Coach, Strategy partner, Sparring partner) require more context depth and a stronger team-level knowledge layer.

**Key implication for programme design:** don't pitch Coach to a team that hasn't got Librarian working yet. Sequence matters.

---

## 2. Utility vs companion

Not what the AI does, but the *type of context* the AI is carrying — and therefore the type of value it delivers.

Both modes are context-dependent. The difference is *what kind* of context.

### Utility
The AI carries **task context** — step by step, in the moment. The document you're editing, the data you're analysing, the problem you're solving right now. Context is loaded for the task and discarded when it's done. The AI's usefulness is proportional to how well you've described the immediate job.

Most people operate here. Most enablement programmes teach people to be better at utility use — clearer task context, more specific questions. It's valuable and it's where most people start.

### Companion
The AI carries **people context** — who someone is, relationship history, what matters to them, what's been said and promised, how they communicate. This context persists and compounds. The AI doesn't just help you complete a task; it helps you show up well in a relationship.

Companion mode is what the BDM brain delivers. The AI knows your brokers, your accounts, your team's conversation history. You show up to a call having been briefed not on the task but on the person and the relationship state.

**The key distinction:** utility context is about the work; companion context is about the people. Both require investment to build, but companion context is relational infrastructure — it doesn't expire when the task ends.

### Where each model fits

This maps directly onto how different teams create value:

**Sales and distribution → companion model.** People are the sharp end of delivery. What a BDM does is fundamentally relational — the quality of the conversation, the depth of broker knowledge, the ability to build trust. The AI's job is to carry the people context so the human can show up more fully in the relationship itself. The AI doesn't replace the relational work; it creates the conditions for better relational work.

**Operations and finance → agent/process model.** People define the processes; agents are at the core of executing them. The human role shifts from doing to designing and governing. The sharp end of delivery is increasingly automated — Emily's team (Zapier pipelines, scheduled tasks, automated reports) is the reference model. The people are upstream of delivery, not in the loop of it.

**Underwriting** sits closer to the ops/process model at the task level — work is operational and repeatable, and uplift comes from doing not coaching (Fergus, 2026-06-11). But there's a relational layer at the broker/account level that has companion characteristics. Likely splits internally: front-of-house underwriting (broker relationships) benefits from companion context; back-of-house underwriting (risk assessment, processing) benefits from agent automation.

**Key implication for programme design:** a sales workshop and an ops workshop should be designed for fundamentally different outcomes. Sales: how to build and maintain relationship context so the AI can carry it into every interaction. Ops: how to define processes clearly enough that an agent can execute them reliably, and how to govern what agents produce.

---

## 3. Implementer path vs systems thinker path

The activation framework describes where someone is. This framework describes where they're *trying to get to* — and there are two valid destinations for non-engineering roles.

### Systems thinker path
Stage 4–5 in the activation framework. Designs agent architectures, orchestrates multi-agent systems, thinks about adherence and context as engineering problems. High ceiling, hard to reach.

Appropriate target for: engineers, technical PMs, power users who are already at Stage 3–4 and pushing further.

### Implementer path
A more accessible target. Can build and maintain a tool that someone else designed — a co:work project, a Claude skill, a scheduled task. Configures, customises, and keeps it healthy. Doesn't require understanding the underlying architecture; requires understanding the *interface*.

Appropriate target for: PMs, ops, sales, distribution, finance — anyone in a role where the output is work product rather than software.

**Why this matters:** the implementer path is achievable in weeks, not months. It's the correct learning target for the majority of the company. The systems thinker path is the correct target for a minority.

**The mechanic analogy** (from conversations with Geran, 2026-06-10): don't ask Fred to be a systems architect — make him a mechanic. Tom teaches mechanics, Geran (or Fergus, or Jordi) defines the system. The mechanic doesn't need to understand the engine design to change the oil.

### How PMs and non-technical teams increase engineering capacity

A PM who becomes an implementer can build and iterate on tools without consuming engineering resource. The same applies to ops, sales, and distribution teams. The model:

1. Tom (or an engineer) designs and builds the initial system
2. Tom teaches the team to use and maintain it (implementer skills: configure, update content, customise outputs, diagnose simple failures)
3. The team maintains their own instance — it diverges from the template as they embed their own domain knowledge
4. Engineering resource is freed for systems work that genuinely requires it

This is the scaling model for AI adoption. It's more sustainable than Tom as the centre of excellence, and it's more achievable than expecting everyone to become a systems thinker.

**Key implication for workshop design:** the target output of a workshop is not "everyone can prompt well" — it's "everyone can maintain a tool." The curriculum shifts from prompting technique to: how do I update my context file, how do I adjust a scheduled task, how do I know when my skill is degrading.

---

## How the three frameworks relate

The activation pathway tells you *where someone is*.

The utility/companion distinction tells you *how they're working* — and flags whether their infrastructure is limiting their ceiling.

The team role taxonomy tells you *what the AI is doing for the team* — and gives a sequence for what to build next.

The implementer/systems-thinker distinction tells you *what they're aiming for* — and calibrates the right programme for each cohort.

Together: a BDM at Stage 2 activation, working in utility mode (task context only), with a team at Librarian stage — has a clear and achievable next step: build companion-mode relationship context, get the team to Secretary, and learn to maintain it. An ops person at the same activation stage has a different next step: identify one repeatable process and design it for agent execution.

Same activation stage, same role taxonomy position — completely different interventions, because the models of value creation are different.

---

## Relationship to other frameworks

- [[activation-pathway]] — the individual skill progression framework; these sit alongside it
- [[thin-harness-fat-skills]] — the implementer path is the "fat skills" side of that model
- [[bdm-ai-multiplayer]] — the BDM brain role taxonomy is the worked example of the team role framework in practice
