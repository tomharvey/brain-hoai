---
title: Philosophical AI Workshop — design notes
created: 2026-05-22
updated: 2026-05-22
type: reference
domain: ai-enablement
tags: [workshop, culture, systems-thinking, critical-thinking, token-time]
---

# Philosophical AI Workshop

A workshop format for people already using AI — not a capability primer, but a session about identity, judgment, and what the job actually is. Designed in conversation with Ollie Crowe 2026-05-20.

Two audiences, same core structure:
- **Engineering / technical** → [[ai-native-engineering]] initiative; emphasis on Mode 1/2, deterministic vs agentic, systems design
- **Non-technical / company-wide** → [[ai-capability-uplift]] initiative; emphasis on role identity, the K-curve, the spreadsheet analogy

---

## Core provocation

> "Your job was never to type things. Those were implementations of your job. What's the underlying function you actually serve?"

This is the thread that connects all four themes.

---

## Theme 1 — What is your job?

**Provocation:** The PM that AI is killing has been dead for 10 years. The engineer whose job is typing has been wrong about their job for longer than AI has existed. What's the underlying function?

**Evidence from Flock:**
- Javier's message: "the new gold is to keep context secret — that's how we keep our jobs." Tom's response: makes you a bottleneck holding the can for the shit work you're bored of. Never worked before AI, won't work now.
- Matt Price's blog post angle: PM who didn't think critically was never doing the job. The AI isn't killing a viable role.
- The spreadsheet moment (Matt Price): when spreadsheets went digital, the person filling in paper columns didn't disappear — cost of the task went to zero, so you could go infinitely wider and deeper. Same transition now.

**Key reframes:**
- "Your value is never your ability to turn that wheel" — make something of what comes out the other end
- The K-curve (Mark, ScreenCloud CEO): AI splits everyone onto upper or lower arm. Upper arm: using AI to go broader and deeper into the newly-novel. Lower arm: watching the commodity layer of their job disappear.

**Exercise:**
> *"If you were hiring yourself into this role today — with AI already at its current capability — what would the job description say? What would you not bother putting in it?"*

Strips away implementation bias. The gap between their current JD and this new one is exactly where AI is landing.

---

## Theme 2 — What do you do during token time?

The most honest question in the workshop. Nobody has a fully worked answer yet — that's the point.

**The mode gap (engineering framing):**
- Mode 1: you're in the loop — ask question, read response, ask question. You're the CPU.
- Mode 2: you're outside the loop — you set the objective, let it run, come back and judge. You're the architect.
- Token time only exists in Mode 2. If you're still in Mode 1, there's no token time — you're just a slower CPU than Claude.

**Honest answers collected so far:**
- Stephen Millington: "make another cup of tea" — and admitted he hasn't figured it out
- Tom: "I feel like I've got 20 arms" — the reframe that token time is parallel time, not dead time
- Chris (Dev AI Practices session): use it for systems thinking — but what does that mean concretely?

**Exercise:**
> *"Show me your calendar from yesterday. When was Claude running? What were you doing during those moments? What should you have been doing?"*

Follow-up: design the ideal token-time workflow. What would you do if you had a guaranteed 20-minute window while Claude worked on something hard?

---

## Theme 3 — How to retain critical thinking

**The Rob problem:** delegating without first knowing what you want. Open Claude, type problem, accept output. You've outsourced the thinking, not just the execution.

**The right pattern has two parts:**
1. **Before prompting**: articulate what "good" looks like. What would make you reject the output?
2. **After receiving**: can you explain *why* the output is right or wrong? If you can't, you can't validate it — and you've outsourced a judgment you don't understand.

**The citation principle** (from finance workshop): always ask Claude to cite sources and explain decisions. Does two things: creates friction against hallucination, and forces you to engage with the reasoning instead of accepting the answer. Kirsty's Looker field documentation on every slide. Kevin's reconciliation tabs. Same instinct.

**Fergus's framing:** "indexing for differential thinking, judgment — so we can guide agents to really good results." The skill isn't prompting. It's knowing what right looks like.

**Exercise:**
> *"Take a recent Claude output you used. What would a rigorous audit of it look like? At which decision points did you actually evaluate the reasoning, vs accept the answer?"*

Stronger version: give the output to someone else and ask them to find the weakest assumption. Can you defend it?

---

## Theme 4 — Expanding to systems thinking

The upper-arm skill. The question shifts from "how do I do this task?" to "how should this system work?"

**The three-layer question** (emerged from Stephen Millington's monitoring system):
> Where does the human sit? Where does the agent sit? Where does the deterministic function sit?

This is a new design skill. Most people haven't thought about it because they haven't built anything complex enough yet.

**Stephen's system as a worked example:**
- Deterministic: SQL query (always the same output)
- Non-deterministic / agentic: Claude evaluates the graph visually and decides what's anomalous
- Human: reads Slack alert, decides to acknowledge or raise a ticket

The interesting question isn't "should this step be AI or not?" — it's knowing which layer each decision belongs in.

**Wardley lens (Fergus almost invoked this):** What's been commoditised in your role? What was always novel but you were too busy to do? What's newly novel — things that weren't even possible before? The upper-arm people are flooding into that third category.

**Exercise:**
> *"Pick a workflow you own. Draw it as three layers: deterministic functions, agentic steps, human judgment points. Are those in the right places? Is any human judgment happening on something that should be deterministic? Is anything deterministic that should have flexibility?"*

---

## Suggested 60-minute session structure

| Time | Section |
|------|---------|
| 10 min | Opening: the spreadsheet moment — not about tools, about the abstraction layer shift |
| 10 min | Theme 1: What is your job? — pair discussion on the hiring exercise |
| 10 min | Theme 2: Token time — honest answers, no performance |
| 10 min | Theme 3: Critical thinking — audit exercise on a real recent output |
| 10 min | Theme 4: Systems thinking — three-layer drawing exercise |
| 10 min | Closing: each person writes one sentence: *"My job is actually to \_\_\_."* Read aloud. |

The closing exercise is the output. The range of answers is the most valuable thing that comes out of the room.

---

## Audience variations

**For engineers** (via [[ai-native-engineering]] initiative):
- Lead with Mode 1 vs Mode 2 — they feel this in their daily work
- The three-layer systems design exercise is the centrepiece
- "Employable in 2030" is the frame that landed best in Dev AI Practices (2026-05-18)

**For non-technical / mixed** (via [[ai-capability-uplift]]):
- Lead with the spreadsheet moment and K-curve
- Token time discussion is more abstract — keep it high-level
- The closing "my job is actually to \_\_\_" exercise is the most valuable moment

---

## Sources / evidence base

- [[2026-05-19-stephen-millington]] — token time, Mode 1/2, vibe coding, staying sharp
- [[2026-05-19-jordi-weekly]] — knowledge hoarding, systems thinking, scheduling forces output
- [[2026-05-19-matthew-price]] — spreadsheet analogy, K-curve, PM blog post
- [[2026-05-18-dev-ai-practices]] — critical thinking deficit (Rob), "employable in 2030", Fergus on judgment
- [[2026-05-20-ollie-tom-new-frontier]] — session where these ideas were first structured
