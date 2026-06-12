---
title: "Performance Management: Francesco / Oli → Rakhee / Eraaz"
created: 2026-06-09
updated: 2026-06-09
domain: ai-enablement
type: meeting
tags: [performance-management, cowork, enablement, people-team]
---

# Performance Management: Francesco / Oli → Rakhee / Eraaz

**Date**: 2026-06-09
**Attendees**: [[ollie-crowe]], [[francesco-venerandi]], [[rakhee]], [[eraaz-ali]], Tom
**Transcript**: [[2026-06-09-performance-management-transcript]]

## Context

[[ollie-crowe]] and [[francesco-venerandi]] brought their AI-powered performance coach to [[rakhee]] and [[eraaz-ali]] — flagged to Tom first, then set up as an alignment check. The goal was not to propose a company rollout but to share the work, check for concerns, and see whether any elements could feed into the People team's ongoing performance revamp.

## What Francesco built

A co:work-based performance coaching system:

- **Onboarding**: captures role, manager, key stakeholders, promotion rubric. [[milan-chavda]] wrote Francesco's rubric with Darren's input — it's the foundation the whole system tracks against.
- **Weekly schedule**: scans Granola, Slack, email, Claude conversations → writes a Notion page summarising work done and linking each item to Francesco's promotion criteria
- **Pre-1:1 schedule**: detects 1:1s on calendar, generates a manager-ready summary of work since last session
- **Post-1:1 schedule**: ingests Granola transcript from the 1:1, extracts manager feedback, updates goals
- **Weekly performance coach**: Slack message with specific evidence-based feedback ("you presented X to Darren on Y date, a lead data scientist should lead more on decisions")
- Local storage in co:work files persists context over time; Notion pages as the living record

The system runs entirely in the background after ~10 min setup. Francesco's view: it's made his 1:1s with Milan structured and high-quality without either of them doing extra work.

## Key concerns raised

1. **People team already redesigning the process** — Rakhee and Eraaz are mid-way through a full revamp (6-monthly → quarterly cycle, new PGR process). Not public yet. Risk: building on top of a moving foundation.

2. **AI tooling gap across the company** — Not everyone uses the same tools (Granola, Notion, Linear etc). A system that depends on signal from those tools doesn't work for people who don't use them. Can't roll this out uniformly.

3. **Over-reliance risk** — Rakhee's concern: what if someone arrives at a PGR with an AI-generated achievements list and treats it as gospel? The human, behavioural, and values elements aren't captured by tool logs. "This doesn't tell us that."

4. **Complexity barrier** — The demo looked technically involved. Even if it "just runs," the setup diagram would put off most non-technical staff. Needs a much simpler entry point.

5. **Removing friction that creates learning** — Tom flagged: some friction in performance reflection is the point. Risk of bypassing the thinking process, not just the admin.

## Outcome

No company rollout. Outcome agreed:

- **Immediate takeaway**: strip it back to a single **copy-paste prompt** — something people can use after an AI breakfast to start doing performance coaching via Claude. Not the full system; just the core habit.
- Francesco to send the prompt to Rakhee and Eraaz
- Rakhee + Eraaz will test it themselves as guinea pigs, iterate, then consider embedding in the next PGR cycle communication
- Focus group idea mentioned: interested individuals (Tom, others) play with it and give feedback

## Actions

- [ ] [[francesco-venerandi]]: send copy-paste performance coach prompt to Rakhee + Eraaz
- [ ] [[rakhee]] + [[eraaz-ali]]: test the prompt, give feedback to Francesco
- [ ] Tom: consider whether activation data / coaching usage could surface to People team (privacy constraints acknowledged — noted as interesting future question, not a current action)

## Notes

- Milan's promotion rubric for Francesco is the clearest single example of a manager doing this well — the system works because there's something concrete to track against. Most people don't have this.
- Adam is doing something analogous for BDM coaching: querying Granola call transcripts for customer service feedback. A simpler, lower-stakes version of the same idea.
- The "bombastic version" problem: when something is shown at its most built-out, it reads as "Francesco's way" not "a way." Starting with a prompt inverts this — everyone customises from the same blank slate.
