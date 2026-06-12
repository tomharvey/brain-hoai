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

90-minute company-wide workshop on when and how to use Claude, co:work, and Claude Code. Booked: **Tue 16 June, 11:30, in-person + remote**.

Core mental model:
- **Claude** — thinking partner. Conversational, exploratory, one-off tasks.
- **Co:work** — virtual employee. Where your context lives. Runs without you.
- **Claude Code** — building partner. File-aware, long-running (signposted only).

Key insight: friction comes from routing work to the wrong tool — and both failure modes (over-engineering, fire-and-forget) happen before the tool is opened.

**No live demo.** Stories only. A well-told story outlasts a live agent run.

---

## Structure and timings

| Time | Block | Duration | Owner |
|------|-------|----------|-------|
| 0:00–0:30 | Framing | 30 min | Tom + plants |
| 0:30–0:35 | Activity setup | 5 min | Tom |
| 0:35–1:05 | CoWorking pairs | 30 min | Pairs |
| 1:05–1:15 | Debrief | 10 min | Tom |
| 1:15–1:30 | Wrap | 15 min | Tom + Kevin |

**Why no demo:** Matt's role is the cautionary tale — showing his 9-agent pipeline right after saying "don't over-build" contradicts the message. The activity is the hands-on moment. Stories land harder and last longer than watching an agent run. Freed 10 minutes goes into pairs working time.

---

## Framing block talk track (30 min)

### Five slide title-statements

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

Introduce the three tools as answers to intent questions:
- Claude → think through a problem, one-off task
- Co:work → AI that knows you and your work, runs without you
- Claude Code → building something that lives in files (next level, not today)

---

### Section 2 — Two failure modes / intent first (7 min) · Tom + Matt (3–4 min)

**Tom frames the failure modes (2 min):**
- **Fire and forget**: one question, meh answer, close the tab. The AI didn't know enough about you or the problem to help.
- **Over-engineering**: build nine agents before you know if one works.

Both happen before the tool is opened. The fix is one sentence written before you touch anything: *What am I trying to produce, and why?*

**Matt's story (3–4 min) — Beginning / Middle / End:**
- *Beginning:* 600-company pipeline. No way to track it properly. Clear problem, real intent.
- *Middle:* Built nine agents. MEDDPICC scoring. Automated alerts. Kept adding. Realised nobody was checking the adherence outputs — including him.
- *End:* "I went too far before I'd validated the first thing. The bit that's actually working now is [specific simple thing]. If I started again, I'd build that one thing first, use it for a month, and ask whether I needed anything else."

Self-deprecating, honest, gets a laugh. The most credible person in the room admitting he over-built.

---

### Section 3 — Incremental building (5 min) · Tom + Ivan (2 min)

**Ivan's story (2 min) — Beginning / Middle / End:**
- *Beginning:* Every morning, exported a CSV from NetSuite and manually worked out who to chase. Same task, every day, starting from zero every time.
- *Middle:* Started with a conversation — just pasted the CSV in and asked. Got the prioritisation. Moved it into a Claude project so the context was already there. Then moved it to co:work so it ran without him.
- *End:* Two minutes a day. Still running two months later. Hasn't needed to touch it.

**Tom's line:** He didn't build a dashboard. Version zero was a conversation. The dashboard is never version zero.

---

### Section 4 — Narrow vs broad / project scope (6 min) · Tom + Shreya (2 min) + Adam (2 min)

This answers the question the room is silently asking: *how big is my project supposed to be?*

**Shreya's story (2 min) — Beginning / Middle / End:**
- *Beginning:* Processing the same type of document repeatedly. Manual every time. No memory between uses.
- *Middle:* Built one skill to handle it. Got it right. New document type came up — built another. Didn't add it to the first one.
- *End:* The team now has a small library. Each does one thing. Each does it the same way every time. None of them complicated. All of them working.

**Adam's story (2 min) — Beginning / Middle / End:**
- *Beginning:* Showing up to broker conversations without the full picture — what had been said, what had been promised, what mattered to that person.
- *Middle:* Built one project that carries the relationship context. Loads it before calls. Adds to it after.
- *End:* "The AI briefs me now. I show up better in every conversation. It doesn't expire when a call ends — it gets richer."

**Tom's contrast (2 min):**
> "Same question — how big is my project? Two completely different right answers. Shreya's world is a set of repeatable tasks: one project per task, focused, shareable. Adam's world is a set of ongoing relationships: one project that grows with them. The answer is: it depends which one you are."

Pre-question for the activity: *Are you Shreya or Adam?*

---

### Section 5 — Context over prompting (4 min) · Tom

> "The unlock isn't a better prompt. It's a better context layer. Most people rewrite the prompt when they get a bad answer. The real fix is better context."

Co:work is not a smarter chat window. It's where your context accumulates — who you are, what matters, what the AI needs to know to be permanently useful.

**The skill → project moment (one sentence):**
> "When you find yourself explaining the same things to every skill you build, that explanation belongs in a project — not the skill."

---

### Bridge to activity (1 min) · Tom

> "You're about to build your version zero. Not a dashboard — the conversation you'd have first."

---

## Activity setup (5 min) · Tom

Four questions — write answers before opening co:work:

**Pre-question:** Are you Shreya or Adam? Ops/task → narrow projects. Sales/relationship → one broad project.

1. **What's your intent?** One sentence. If you can't write it in one sentence, split it first.
2. **What context does the AI need?** Files, notes, processes, people — list what it needs to know.
3. **What's the smallest version zero?** One thing. The conversation you'd have first.
4. **Sanity check:** Is this one intent or three? Pick one. Come back to the others next week.

*Facilitator note:* The most common failure is writing a paragraph for question 1. Send them back. One sentence.

Remote: breakout rooms for pairs. 30 min working time.

---

## Debrief (10 min) · Tom

Call on 2–3 pairs to share their intent sentence and version zero.

Use the pivot from [[flock-communication-playbook]] if questions go abstract: *"Can I tell you a story?"* — redirect to Shreya, Adam, Ivan, or Matt.

Watch for over-ambitious version zeros ("a full dashboard for my team"). Reframe: *"What's the conversation you'd have first?"*

---

## Wrap (15 min) · Tom + Kevin

**Commitments (5 min):** Each person writes one thing they'll do this week. Not "explore co:work" — a specific intent and a version zero.

**Common gotchas (5 min):**
- AI keeps starting from zero → context isn't loaded; it belongs in the project
- Got a bad answer → before rewriting the prompt, improve the context
- Project doing too many things → split it; one intent per project
- Built something, don't know how to maintain it → that's next week's problem; ship version zero first

**Claude Code signpost — Kevin (3 min):**
Kevin tells the Claude → co:work → Code arc honestly, including the friction. *"The next level for those who want it."* No demo, no pressure.

**Close (2 min):** Workshop is the start, not the event. The install link is in the calendar invite.

---

## Plant story briefs

Story structure per [[flock-communication-playbook]]: **Beginning** (real problem) → **Middle** (how it was solved) → **End** (results and meaning). Each story should be speakable in the time shown — no slides needed.

---

### Matt Lees — 3–4 min · Framing block

**Brief to send:**

> Matt — I'd love you to tell your story at the workshop on Tuesday. No slides, just the honest version.
>
> **Beginning:** You had a real pipeline problem. 600 companies to track, no good way to do it. Clear intent.
>
> **Middle:** You built nine agents. Went further and further. Realised at some point that nobody was checking the adherence outputs — including you.
>
> **End:** What you'd do differently. The one or two things that are actually working now, and why. "I went too far before I'd validated the first thing."
>
> You're the most credible person in the room to say this — because you're also the most capable. That's what makes it land. 3–4 minutes, honest, self-deprecating. You'll get a laugh.

---

### Ivan Boix — 2 min · Framing block

**Brief to send:**

> Ivan — I'd love you to share your credit control story at the workshop on Tuesday. Two minutes, no slides.
>
> **Beginning:** Every morning, NetSuite CSV, manually working out who to chase. Same task every day, starting from zero.
>
> **Middle:** You started with a conversation — just pasted the CSV in. Then built a project around it. Then moved it to co:work.
>
> **End:** It runs in two minutes now. Two months in, still working, you haven't touched it.
>
> The key line: "Version zero was just a conversation." That's the thing I want the room to hear.

---

### Shreya / UWA team member — 2 min · Framing block

**Brief to send:**

> [Name] — I'd love you to share how the ops team has been building AI tools, at the workshop on Tuesday. Two minutes, no slides.
>
> **Beginning:** Processing the same document type repeatedly, manually, every time.
>
> **Middle:** Built one skill to handle it. Got it working. New type came up — built another one, didn't add it to the first.
>
> **End:** The team now has a small library of tools. Each does one thing. None of them complicated. All of them working.
>
> The key line: "We didn't build one big thing — we built several small ones." That's exactly what I want the room to hear from someone who's done it.

---

### Adam Smith — 2 min · Framing block

**Brief to send:**

> Adam — I'd love you to share your broker relationship story at the workshop on Tuesday. Two minutes, no slides.
>
> **Beginning:** Showing up to broker conversations without the full picture — what had been said, what had been promised, what mattered to that person.
>
> **Middle:** Built one project that carries that context. Loads it before calls, adds to it after.
>
> **End:** "The AI briefs me now. I show up better in every conversation. It doesn't expire when a call ends."
>
> You're the sales-side answer to the ops story. Opposite shape, same principle: one clear intent, context that compounds.

---

### Kevin Berg — 3 min · Wrap

**Brief to send:**

> Kevin — I'd like you to close the workshop with an honest version of your journey from Claude to co:work to Claude Code. Three minutes, no slides.
>
> **Beginning:** Started using Claude for queries and analysis. Got value.
>
> **Middle:** Moved to co:work to build something that ran without you. Then wanted to go further — tried Claude Code.
>
> **End:** Honest about the friction at each step and what you got from pushing through. Not a pitch — the real version. "The next level for those who want it."
>
> The point isn't to sell Claude Code. It's to show there's a progression and it's achievable — from someone who's done it.

---

## Acceptance criteria

- [ ] Slide deck built (5 slides, title-statement format)
- [ ] Matt Lees briefed — confirm 3–4 min story
- [ ] Ivan Boix briefed — confirm 2 min story
- [ ] Shreya / UWA team member briefed — confirm 2 min story
- [ ] Adam Smith briefed — confirm 2 min story
- [ ] Kevin Berg briefed — confirm 3 min wrap story
- [ ] Activity prompt printed / shared for remote
- [ ] Calendar invite sent with co:work install link

## Notes

- Slack invite sent 2026-06-03
- Activation framework kept backstage — routing framing only for general audience
- Claude Code is a signpost only — no demo, no pressure
- Hybrid: in-person + remote. Breakout rooms needed for pairs activity
- Story structure: Beginning / Middle / End per [[flock-communication-playbook]]
- One point per slide, titles as statements, less content than you think
