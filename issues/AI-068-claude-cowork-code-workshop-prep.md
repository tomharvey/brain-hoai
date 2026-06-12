---
title: "Company-wide workshop prep: Claude / Cowork / Claude Code"
id: AI-068
created: 2026-05-29
updated: 2026-06-12
domain: ai-enablement
type: issue
status: in-progress
priority: high
assignee: Tom
due: 2026-06-16
tags: [workshop, enablement, claude, cowork]
---

## Description

90-minute company-wide workshop on when and how to use Claude, Cowork, and Claude Code. Booked: **Tue 16 June, 11:30, in-person + remote**.

Core mental model:
- **Claude** — thinking partner. Conversational, exploratory, one-off tasks.
- **Cowork** — virtual employee. Scheduled autonomous agents, runs without you. Where your context lives.
- **Claude Code** — building partner. File-aware, long-running, lives in the terminal (signposted as next step only, not demoed).

Key insight to land: friction comes from routing work to the wrong tool — and both failure modes (over-engineering and fire-and-forget) happen before the tool is even opened.

---

## Structure and timings

| Block | Time | Duration | Owner |
|-------|------|----------|-------|
| Framing | 0:00–0:25 | 25 min | Tom + plants |
| Demo | 0:25–0:35 | 10 min | Matt Lees |
| Activity setup | 0:35–0:40 | 5 min | Tom |
| CoWorking pairs | 0:40–1:05 | 25 min | Pairs |
| Debrief | 1:05–1:15 | 10 min | Tom |
| Wrap | 1:15–1:30 | 15 min | Tom + Kevin |

**Why 25 not 30 for framing:** four live plant stories at 60 seconds each plus five framing sections is 30+ min in practice. Tighten to 25 and protect the activity — that's where the commitment happens.

**Why 40 not 35 for activity:** pairs need time to get past the surface answer on the intent question. 25 min working + 10 min debrief is the minimum viable version.

---

## Framing block talk track (25 min)

### Slide title-statements (Rule 04/05 from [[flock-communication-playbook]])

Reading these in order tells the whole argument:

1. *Frustration with AI is a routing problem, not a model problem*
2. *Both failure modes happen before you open the tool*
3. *Version zero should be a conversation, not a dashboard*
4. *Ops people need many narrow projects; sales people need one deep one*
5. *A project is where your context lives — the more you put in, the better it gets*

---

### Section 1 — The routing problem (3 min) · Tom

Open with the frustration, not the tools:

> "Most of you have tried Claude. A lot of you got a mediocre answer, put it down, and moved on. That's not because the tools are bad."

Introduce the three tools as answers to intent questions, not as products:
- Claude → think through a problem, one-off task
- Co:work → AI that knows you and your work, runs without you
- Claude Code → building something that lives in files (signpost only)

---

### Section 2 — Two failure modes / intent first (5 min) · Tom + Matt (60 sec)

**Tom frames the failure modes (Fergus's framing):**

- **Fire and forget**: ask one question, get a meh answer, close the tab. The AI didn't know enough to do anything useful.
- **Over-engineering**: build nine agents before you know if one works.

Both failures happen before the tool is opened. The fix: write one sentence before you open anything. *What am I trying to produce, and why?*

**Matt tells the over-engineering story on himself (60 sec):**
Nine agents, complex pipeline, MEDDPICC scoring. The question he's now asking: is anyone actually using it? "I went too far. Here's what I'd do differently."

Self-deprecating, honest, gets a laugh. Sets up the incremental point.

---

### Section 3 — Incremental building (5 min) · Tom + Ivan (60 sec)

**Ivan's story (60 sec):** Three visible steps, non-technical person:
1. ChatGPT conversation — just talking through the problem
2. Loaded the NetSuite CSV into a Claude project — same conversation, now it knew his data
3. Moved to co:work — runs every morning without him

> "He didn't build a dashboard. Version zero was a conversation. It took two months to get to step three. It now runs in two minutes a day."

**Tom's line:** Don't jump to hi-fi. The dashboard is not version zero. The conversation is.

---

### Section 4 — Narrow vs broad / project scope (5 min) · Tom + Shreya (60 sec) + Adam (60 sec)

This answers the question the room is silently asking: *how big is my project supposed to be?*

**Shreya / UWA team (60 sec):** The ops team hasn't built one big project. They've built several small ones — each does one thing, each does it the same way every time. One handles this document type, one handles that process. When a new problem came up, they built a new project. The result is a small library of tools the whole team uses.

**Adam (60 sec):** His project is a different shape. One project, one world — his brokers, his conversations, his relationships. It doesn't expire when a task is done. It gets richer every time he talks to someone. The AI knows who matters to him, what's been said, what's been promised.

**Tom's contrast line:**
> "Same question — how big is my project? Two completely different right answers. If your work is a set of repeatable tasks: build a set of focused projects. If your work is a set of ongoing relationships: build one project that grows with them. The answer is: it depends which one you are."

**The self-sorting question** (plant ahead of the activity):
> "Are you Shreya or Adam? That's the first question before you open co:work."

---

### Section 5 — Context over prompting (4 min) · Tom

> "The unlock isn't a better prompt. It's a better context layer. Most people try to write a better prompt when they get a bad answer. The real fix is better context."

Co:work is not a smarter chat window. It's where your context accumulates. A `claude.md` that says who you are and what matters. Files the AI can read. The more you put in, the more permanently useful it becomes.

**The skill → project moment** (one sentence only — expand in activity briefing if needed):
> "When you find yourself explaining the same things to every skill you build — that's the moment to put it in a project instead."

---

### Bridge to demo (2 min) · Tom → Matt

> "Matt's going to show you what this looks like when it's actually running — and he's going to be honest about where he went too far."

---

## Demo (10 min) · Matt Lees

Matt shows a live scheduled agent. Honest framing: what's working, what he'd simplify. Not a polished pitch — a real thing in use.

Briefing note for Matt: 10 min hard limit. Show one agent running, explain the intent behind it, land the "I'd build fewer, simpler things now" reflection. No need to prepare slides.

---

## Activity setup (5 min) · Tom

Brief the room before pairs form. Four questions — in order, write them down before opening co:work:

**Pre-question:** Are you Shreya or Adam? (ops/task → narrow; sales/relationship → broad)

1. **What's your intent?** One sentence. If you can't write it in one sentence, you have scope creep before you've started.
2. **What context does the AI need?** List the files, notes, processes, people. What does it need to know to be useful?
3. **What's the smallest version zero?** One thing. Not a dashboard. What's the conversation you'd have first?
4. **Sanity check:** Is this one intent or three? If three, pick one and come back to the others.

Facilitator note: the most common failure in the activity is people writing a paragraph for question 1. Send them back. One sentence.

Remote: breakout rooms for pairs. 25 min working time.

---

## Debrief (10 min) · Tom

Call on 2–3 pairs to share their intent sentence and version zero. Use the communication playbook pivot if questions go abstract: *"Can I tell you a story?"* — redirect to Shreya, Adam, or Ivan.

Watch for: over-ambitious version zeros ("a full dashboard for my team"). Reframe live: *"What's the conversation you'd have first?"*

---

## Wrap (15 min) · Tom + Kevin

**Commitments (5 min):** Each person writes one thing they'll do this week. Not "explore co:work" — a specific intent and a version zero. Collect or share in the room.

**Common gotchas (5 min):**
- The AI keeps starting from zero → your context isn't loaded; it belongs in the project
- I got a bad answer → before you rewrite the prompt, improve the context
- My project is doing too many things → split it; one intent per project
- I built something and now I don't know how to maintain it → that's next week's problem; ship the version zero first

**Claude Code signpost — Kevin (3 min):**
Kevin tells the Claude → co:work → Code arc honestly, including the friction. Frame: *"The next level for those who want it."* No demo, no pressure.

**Close (2 min):** Workshop is the start, not the event. The install link is in the calendar invite. The people who used these stories today are in this room — ask them.

---

## Plants — confirmed list and briefing notes

| Person | Role | Story | Block | Format |
|--------|------|-------|-------|--------|
| [[matt-lees]] | Over-engineering cautionary tale + demo owner | "I built nine agents. I'd build one now." | Framing + Demo | 60 sec story + 10 min demo |
| [[ivan-boix]] | Incremental build — step by step | ChatGPT → project → co:work, 3 steps, 2 months | Framing | 60 sec |
| Shreya / UWA team | Many narrow projects — ops model | "We didn't build one big thing. We built several small ones." | Framing | 60 sec |
| [[adam-smith]] | One broad companion — sales model | "One project. My brokers. Gets richer every conversation." | Framing | 60 sec |
| [[kevin-berg]] | Code signpost — honest arc | Claude → co:work → Code, including friction | Wrap | 3 min |

**Briefing message to send Monday:** ~3–4 min story, no slides needed, framing angle noted above, confirm availability for 11:30 Tue.

---

## Acceptance criteria

- [ ] Slide deck built (5 slides, title-statement format per [[flock-communication-playbook]])
- [ ] Matt Lees confirmed for demo
- [ ] All plants briefed (message Monday)
- [ ] Activity prompt printed / shared for remote
- [ ] Calendar invite sent with co:work install link
- [ ] Facilitator run-sheet (this doc serves as the basis)

## Notes

- Slack invite sent 2026-06-03
- Activation framework kept backstage — use routing framing only for general audience
- Claude Code is a signpost only: "the next level for those who want it" — no demo
- Hybrid: in-person + remote. Breakout rooms needed for CoWorking pairs
- Communication principles: one point per slide, titles as statements, less content than you think, stories beat claims — see [[flock-communication-playbook]]
