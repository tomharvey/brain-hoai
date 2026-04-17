---
title: ProdTech offsite — 90-min AI session
created: 2026-04-16
updated: 2026-04-17
domain: ai-enablement
type: reference
tags: [offsite, ai-session, prodtech, workshop]
---

> **v4 — 2026-04-17.** Final structure. To share with Fergus, then brief anchors individually before Wednesday.

## Context

90 minutes, Wed 22 Apr afternoon. Prodtech team + Liam Thomson (~18 people). Follows team time in the morning. Alerts workshop follows this session — deliberate sequencing so the AI mindset carries over.

## Format

Three stations. Three groups of ~6. Three rounds of 24 minutes. Every group visits every station. Each station progresses through three threads as groups rotate — by the final round, the station has advanced from raw exploration to a self-improving system.

Tom floats between stations. Each station has named anchor(s) who stay put, carry context between rounds, and guide the progression.

```
5 min     Intro — three threads, iterative model, what "hard output" means
72 min    3 rounds × 24 mins (groups rotate between stations)
6 min     Station report-outs (2 min each, final group presents)
7 min     Follow-on commitments + live demo (Claude building the plans)
─────
90 min
```

## Three threads running through every station

| Round | Thread | What happens |
|---|---|---|
| 1 | **Surface insight** | Use AI to find what's actually happening in real data. Validate the LLM's analysis. Add human judgment. |
| 2 | **Encode fixes** | For each problem found: what's the fix, and at what level? Prompt edit → skill → deterministic script → eval case → checklist. |
| 3 | **Self-healing** | Design the system that catches this automatically next time. Write an implementation plan specific enough for Claude to start building during the wrap-up. |

Each station arrives at Round 1 with **pre-work already done** — LLM analysis of real data. The room validates, deepens, and builds on top of that analysis. Nobody starts from a blank page.

---

## Station A4 — Jay: from conversations to self-healing agent

**Anchors**: Ishmael + Mima

**Domain**: Product → Customer. How does the agent that talks to fleet managers get better every week?

**Pre-work**: 200+ real Jay sessions already extracted via Datadog API (scrubbed of PII). Run LLM analysis before Wednesday: classify each conversation, flag factual errors, hallucinations, tone issues, tool failures, user confusion, missed opportunities. Rank by severity. Summarise trends. Select top 10-20 worst for human review.

| Round | Prompt | Artefact |
|---|---|---|
| 1 — Surface insight | "Here's what the LLM found across 200+ sessions. Here are the 5 worst conversations to read yourself. Do you agree with the LLM's assessment? What did it miss? What patterns do you see?" | Validated + amended trend list. Mistakes, style issues, data gaps, tool failures — categorised. |
| 2 — Encode fixes | "For each problem category: is the fix a prompt edit, a skill update, a new tool, a deterministic script, or an eval case? Use Mima's `/create-test-cases` skill if available. Be specific — write the actual change, not 'make it better.'" | Table: problem → fix type → specific change. Covers prompt tweaks through to deterministic tooling. |
| 3 — Self-healing | "How does this happen automatically next month? Every new session generates data. Design the pipeline: conversation → signal detection → categorisation → fix proposal → human review → deploy. Write it as a plan Claude can implement." | Actionable implementation plan → Claude starts building during wrap-up. |

**Depends on**: Ishmael + Tom completing the LLM pre-analysis by Tuesday. Mima available as co-anchor (she owns Jay's product direction + built `/create-test-cases`).

---

## Station B — Engineering: from tickets to self-improving harness

**Anchor**: Javier

**Domain**: Engineering → Code. What does the developer experience look like when the agent handles implementation and the engineer handles judgment?

**Pre-work**: Before Wednesday, generate a batch of draft PRs from real Linear tickets using Claude Code. Then run an LLM review: compare each draft PR to its source ticket. Categorise: what was missing from the ticket? What did the implementation get wrong? What would a reviewer flag?

| Round | Prompt | Artefact |
|---|---|---|
| 1 — Surface insight | "Here are draft PRs the agent produced from real tickets. Here's the LLM's analysis of common failures. Read a handful of raw examples. Do you agree? What categories of failure do you see across ticket definition, implementation, and code review?" | Categorised list of failure modes. Ticket gaps, implementation mistakes, review issues — each named. |
| 2 — Encode fixes | "For each failure category: is the fix a ticket template change, a CLAUDE.md update, a skill, a pre-flight check that runs before the agent starts coding, an automated review rule, or a Notion doc that needs to exist? Use the progression: prompt → skill → deterministic function. Write the specific change." | Table: failure → fix type → specific change. Same format as A4. |
| 3 — Self-healing | "When Javi corrects a draft PR next week, how does that correction persist? When a reviewer flags the same issue for the third time, how does that become an automated check? Design the feedback loop. Write the plan — Claude implements it during wrap-up." | Actionable implementation plan → second Claude instance starts building. |

**Depends on**: Generating the batch of draft PRs (Tom + Javi, Mon/Tue). Running the LLM review. Rob should be in Javi's group for at least one round — he's the week-2 engineer who'll live this pilot.

---

## Station C — Context that travels: quality in, quality out

**Anchors**: Ollie + Liam

**Domain**: PM ↔ Engineering ↔ External. The context that feeds everything — tickets, specs, docs, stakeholder comms. AI is making it easier to produce plausible-looking garbage. How do we make it easier to produce good work instead?

**Pre-work**: Pull real examples from the last month — Linear tickets (good and bad), Notion docs sent to stakeholders, press releases, broker comms, proposal docs. Include at least 2-3 that are clearly AI-generated slop. Include 2-3 that are polished (Liam's haulage press release, a well-written ticket). Anonymise if sensitive.

| Round | Prompt | Artefact |
|---|---|---|
| 1 — Surface insight | "Here are real artefacts from the last month — tickets, docs, external comms. Rank them: which ones gave the recipient what they needed? Which ones are filler? For the bad ones: what's missing, and what's present but useless? Be honest — some of these are from people in this room." | Annotated examples. Each marked: what worked / what didn't / what's AI filler. Common failure patterns named. |
| 2 — Encode fixes | "For each type of artefact (Linear ticket, Notion spec, stakeholder doc, external comm): what's the quality bar? Write a checklist — not a style guide, a checklist an AI can enforce. What MUST be there? What signals slop? Liam's workflow is the reference model: he never ships AI output directly — AI critiques his writing, not the other way around." | Quality checklists per artefact type. Concrete, enforceable, machine-readable. |
| 3 — Self-healing | "When a ticket is created, an agent checks it against the checklist before it hits engineering. When a doc is about to be sent externally, an agent flags what's missing. When slop gets through anyway, how does the system learn? Write the plan — Claude implements it during wrap-up." | Actionable implementation plan → third Claude instance starts building. |

**Depends on**: Pulling real examples (Tom, Mon/Tue). Ollie being willing to anchor the problem he's part of — frame it as "you're the person closest to this, you're the right person to fix it." Liam confirmed attending. Brief Ollie before Wednesday.

---

## Intro framing (5 min, Tom)

"This isn't a talk. There are no slides. You're going to three stations. At each one, you'll find real data from our own systems — Jay conversations, draft PRs from Linear tickets, docs and comms from the last month. An LLM has already done a first pass on all of it. Your job is to validate what the LLM found, deepen it with your own judgment, and then build something that makes the problem fix itself.

Three threads run through every station:
1. **Surface insight** — what is actually happening in our data?
2. **Encode fixes** — how do we turn that insight into a specific improvement?
3. **Self-healing** — how does the system catch this automatically next time?

Each group builds on what the previous group left. By the time the third group finishes, each station should have an implementation plan specific enough that Claude can start building it while we do the wrap-up. That's the bar."

## Wrap-up (13 min, Tom)

- 2 min per station: final group's anchor presents what the station produced across all three rounds (6 min total)
- Tom synthesises: "Three domains, one methodology. The pattern is the same everywhere — surface, encode, self-heal." (2 min)
- Live: open Claude Code, paste the three plans, start building. The room watches their 90 minutes of work turn into code. (3 min)
- Follow-on commitments: who owns each station's output going forward? (2 min)

## Pre-work checklist

| Task | Owner | By when |
|---|---|---|
| LLM analysis of 200+ Jay sessions — trends, failures, top 20 worst | Tom + Ishmael | Tue 21 Apr |
| Generate batch of draft PRs from real Linear tickets | Tom + Javi | Mon-Tue 21 Apr |
| LLM review of draft PRs vs source tickets | Tom | Tue 21 Apr |
| Pull real Linear tickets, Notion docs, external comms (good + bad) | Tom | Tue 21 Apr |
| Brief Ishmael on anchor role + station progression | Tom | Mon-Tue |
| Brief Javi on anchor role + station progression | Tom | Mon-Tue |
| Brief Ollie on anchor role + station progression | Tom | Mon-Tue (in person) |
| Brief Mima on co-anchor role for A4 | Tom | Mon-Tue |
| Brief Liam on co-anchor role for C | Tom | Mon-Tue |
| Confirm room layout supports 3 stations | Tom | Tue |
| Print/prepare station materials (conversations, PRs, docs) | Tom | Tue evening |

## People to brief before Wednesday

| Person | Role | Key message |
|---|---|---|
| **Fergus** | Awareness | "Here's the plan. Three stations, real data, hard outputs. You float like me." |
| **Ishmael** | Anchor A4 | "Bring the Jay conversation analysis. Mima co-anchors. Three rounds, each builds on the last." |
| **Mima** | Co-anchor A4 | "Your `/create-test-cases` skill is the tool for Round 2. You bridge product and engineering perspectives." |
| **Javi** | Anchor B | "This is your pilot in action. The draft PRs are the opening data. Three rounds to define the harness." |
| **Ollie** | Anchor C | "You own this problem — ticket quality, doc quality. Liam is your co-anchor with the external comms angle. Three rounds to build the quality enforcer." |
| **Liam** | Co-anchor C | "You're the reference model. Your workflow (AI critiques human writing, not the reverse) is what Round 2 defines as the standard." |
| **Rob** | Participant | "You'll be in the room for Station B — your week-2 perspective on what context was missing from tickets is exactly what Round 1 needs." |

## Group assignments (draft — Tom to finalise)

Aim for cross-functional mix in each group. Each group visits all 3 stations.

| Group | Suggested composition |
|---|---|
| **Group 1** | Mix of engineering + product + data |
| **Group 2** | Mix of engineering + product + data |
| **Group 3** | Mix of engineering + product + Liam |

Rob in the same rotation path as Station B Round 1 if possible. Liam in Station C Round 1 or 2 to set the reference model early.

## Risks

- **Pre-work is the make-or-break.** Without the LLM pre-analysis, Round 1 at every station is cold reading. Protect Mon-Tue for prep.
- **Ollie anchoring his own problem** could go defensive. Frame it as "you're closest to this, so you're the right person to fix it" not "we're calling you out."
- **24 minutes per round** is generous for the first round (reading + reacting) but may feel tight for Round 3 (designing a system). Anchors need to manage the clock — don't let Round 1 eat into Round 2.
- **Claude building during wrap-up** depends on wifi and laptop. Have a backup plan (screenshot the plans, commit to building them Thursday morning).
- **Alerts workshop follows** — Jordi is pre-grouping alerts with AI. The mindset from this session should carry directly into that one. Worth Tom saying explicitly in the wrap: "You've just spent 90 minutes surfacing insight, encoding fixes, and designing self-healing systems. Jordi's alerts session is the same methodology applied to operational data."

## Links

- [[2026-04-14-prodtech-leadership-heartbeat]] — original topic suggestions
- [[2026-04-16-fergus-tom-weekly]] — Fergus validated stations format, aligned on AI-native engineering
- [[2026-04-17-jordi-tom-weekly]] — Jordi validated three threads, raised quality concern, alerts workshop sequencing
- [[2026-04-17-rob-ai-discovery]] — Rob's perspective as week-1 engineer on the acquisition squad
- [[ai-native-engineering]] — Station B feeds directly into this initiative
- [[thin-harness-fat-skills]] — the "skill-improving-skills" pattern is the intellectual backbone of Round 3 at every station
