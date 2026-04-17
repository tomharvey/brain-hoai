---
title: Javier — AI-native engineering followup
created: 2026-04-16
updated: 2026-04-16
domain: engineering-workflows
type: meeting
tags: [javier, engineering, agents, developer-harness, claude-code, 2027, strategic]
---

# Javier — AI-native engineering followup

Follow-up to a cryptic Slack message from Tom. Went deep on what a "personal OS for a developer" would look like, and landed on Javier piloting a local harness around his current PoC for a month.

## Attendees

- [[javier|Javier Pallares]]
- Tom (me)

---

## Key themes

### Tom's personal OS as the reference pattern

- HoAI vault: people/, reference/, decisions/, initiatives/, meetings/ — markdown files + AI agent
- Example: *"who do I need to speak to in underwriting about their use of AI"* → mermaid org chart → list → calendar invites → Granola picks up transcript → person file updates with their opinions on AI
- Separately: Rosenfeld energy market project — different brain: Apollo, Outlook, PostHog, Linear. Drafts outbound emails, tracks responses, creates Linear issues from product usage patterns.
- Vault got big enough that keyword search stopped working → asked the agent to improve → added local SQLite vector encoding
- Local-first: everything runs on the laptop. Philosophical, not just technical.

### The developer OS question

> *"What is a personal OS in a developer space? The one I described is business-dev / PM / head-of-AI shaped. What does the developer version look like?"*

Tom's starting sketch:
- `CLAUDE.md` above the repos (Javier already has one per repo)
- Linear → cron job → draft PR on a named branch
- Developer starts from the PR, not the ticket
- Three outcomes per review:
  1. Bin it, restart
  2. Hand-edit directly
  3. **Teach the agent** why it was wrong → builds the harness

### "Better, not faster" — the philosophical core

- This is not about speed. Expectation: **Javier will be slower for some time** while teaching the agent.
- Encoded engineering practices → architectural decision logs populate themselves → code review becomes debate about decisions, not syntax.
- Javier endorsed: *"Better is a better overarching word for the end product."*
- Speed is a side effect that can be spent on robustness, research, test coverage, documentation — not velocity.

### Job-security concern (surfaced by Javier)

- *"I'm worried about that bit — what will happen with us once you get to that point?"*
- Tom's response: the engineer role doesn't end. Up-front ticket work ↔ back-end work to improve the harness ↔ architectural thinking ↔ "what engineering practices are we still missing that we now have time to build?"
- Javier's clarification later: the risk isn't the engineering team's capability, it's managing the **narrative** to leadership who might hear "AI codes now" and misread it.
- Tom: at Flock specifically, no one above the team has ever said "you need to move faster" — that trust buys the room to do this right. Rare.

### Local-first vs cloud agents

- Explicit contrast drawn with Cursor Cloud Agents
- *"This is a thing that runs on my laptop. If I'm off, it's off. I still own it."*
- Not a technical claim — a philosophical one about ownership, agency, and the shape of the tool

### New domain = ideal test ground

- Javier's current Acquisition AI PoC (HubSpot→Claude→Flock API quoting) is in a new domain for him
- Hypothesis: the harness helps you think about the **domain** rather than the **curly brackets**
- Which is very different from how a PM or an operator thinks about the domain
- Engineering mindset still exists and still matters — "now anyone can do it" is bullshit

### Meetings as engineering artefacts

- Javier: *"I can see a future where we sit down at a table, hit record, and by the time we leave the door, it's done."*
- Granola-as-context pattern: transcript + summary → feeds into repo artefacts (decisions, standards, open questions)

### References & reading

- **g-stacks.org** — CEO/PM/QE persona repo. Useful inspiration; implementation irrelevant. Worth skimming before starting the build.
- Tom to share his Claude Desktop advanced-research chats as seed context for the dev version

---

## Decisions

- Javier pilots. **Month of not coding** — starting from the current PoC repo.
- Harness pattern: local-first, `CLAUDE.md`-driven, Linear → draft PR, feedback loop as first-class.
- Scope tight: one repo, one developer, one PM (Ollie) in the loop.
- Productionisation (durability, tracking, sharing) is explicitly parked — revisit once Month 1 runs.
- New initiative tracked as [[ai-native-engineering]].

---

## Actions

- [ ] **Tom**: Share Claude Desktop advanced-research chats on dev workflow with Javier
- [ ] **Javier**: Review g-stacks.org for pattern inspiration (don't copy)
- [ ] **Javier**: Bootstrap the harness on the existing PoC repo
- [ ] **Javier**: Stand up the Linear → draft PR loop (1-day build)
- [ ] **Javier**: Begin the not-coding month; teach the agent via the feedback loop
- [ ] **Tom**: Loop in Ollie on ticket writing — handoff quality feeds harness quality
- [ ] **Tom**: Flag to Fergus as an engineering-workflows roadmap item; set "slow month" expectation

---

## Quotes worth keeping

> *"It's not letting the agent do the grunt work — it's teaching the agent how to do the work."* — Tom

> *"This is not about being faster. No one in this company or above is saying this team needs to move faster — which is incredibly rare."* — Tom

> *"I can see a future where we sit down at a table, hit record, and by the time we leave the door, it's done."* — Javier

> *"You in 2026, you know what the development workflow looks like. What does it look like a year or two down the line? And how do we engage with that today?"* — Tom

---

Full transcript: [[2026-04-16-javier-ai-native-engineering-transcript]]
