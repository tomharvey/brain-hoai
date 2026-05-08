---
title: "Prep: CEO CATCHUP SESSION — AI Developments"
created: 2026-05-07
updated: 2026-05-07
domain: ai-enablement
type: meeting
tags: [ceo, ed, prep, catchup]
---

# Prep: CEO AI Catchup — Mon 11 May, 15:15

**Attendees**: Ed (CEO), Jordi, Ollie, Jemima, Tom
**Format**: Casual. No decks, no formal updates. Ed wants to see what's new.

---

## What Ed has asked for

> "Some time to chat about what's changed in AI at Flock since I've been away. Zero need for formal updates, presentations etc — keep it very casual. Would love to see what's new in the product (Jay!) and internally."

**Jay** will likely be covered by Jordi / product side. Tom's lane is **internally**.

---

## What has happened since Ed was away

### 1. ProdTech AI offsite session (22–23 Apr)

A 90-minute hands-on session with the full ProdTech team (~18 people). Three rotating stations, each working with real Flock data:

- **Station A (Jay)**: Ishmael + Mima analysed 200+ real Jay conversations for failure patterns, then designed a self-improving feedback loop
- **Station B (SDLC)**: Tom + Ollie — draft PRs generated from real Linear tickets, failure modes categorised, feedback loop designed
- **Station C (context quality)**: Matt Price + Liam — real tickets, Notion docs, external comms ranked and quality-checked; checklists produced

Key outcome: every group left with an actionable implementation plan. Format was: surface insight → encode fixes → self-heal. The same methodology applies everywhere.

### 2. Submissions pipeline — narrative reframed

Ollie's conversations with Antton and Curtis shifted the framing:

- **Old story**: extract better data → Milan's pricing models use it → conversion goes up
- **New story**: we're building the data substrate that enables three specific conversion bets:
  1. **Development factor** — Flock applies ~30% uplift to current-year claims that Curtis believes no competitor applies. If disprovable with data, that's a direct price lift at no loss-ratio cost.
  2. **Submission scoring** — incoming submissions scored by likelihood to convert, powered by the structured pipeline
  3. **Driver-data payload** — Milan's team, still on roadmap

Antton asked Ollie to come back with five ranked conversion bets grounded in data. **Ollie is in this meeting** — he'll have a view on where this sits.

### 3. AI-native engineering pilot underway

Javier is running a month-long pilot on the Acquisition AI squad. Local harness takes a Linear ticket, generates a draft PR, engineer reviews and teaches. Hypothesis: shifts engineers from mechanical coding to architectural thinking. Early, but live.

Parallel: Jordi has a vulnerability bot (Claude-based cron job) running on personal repos, about to move to Flock repos (platform). Side project, but real infra.

### 4. Capability uplift — past the discovery phase

20+ discovery conversations done across the company. Four cohorts mapped: builders, active users, stuck, observers. Moving from group workshops to **applied 1:1 pairing** — sit with someone on their actual work, not a demo. Finance (Kirsty's Looker→Claude MCP) is the flagship example.

Rate limits are becoming a real constraint. Matt Lees hit the cap. Enterprise deal is the next unlock.

### 5. Jay — internal angle

Jay instrumentation is in Datadog, not PostHog — Mima doesn't have visibility by default. Thumbs up/down feedback buttons exist but aren't wired up yet. Mima and Ishmael now have Datadog API access to fix this. The feedback loop from the offsite session (Station A) directly addresses this.

---

## Things Tom can show if asked

- **Roadmap visualisation** — pulled current initiative state into a visual now/next/later chart (live in vault)
- **Kirsty's Looker→Claude connection** — can describe or demo the MCP setup
- **The offsite format** — three stations, real data, self-improving methodology; can walk through it in 2 mins

---

## Likely questions from Ed

- *Where is Jay?* → Jordi/product side. Tom's view: instrumentation gap is the priority, not the product itself.
- *What's the biggest internal blocker?* → Rate limits + Claude Enterprise deal. Skills and MCPs are all Claude-ecosystem, so the enterprise deal is load-bearing.
- *Is AI adoption real or superficial?* → Discovery data shows real gradient. Finance and ops are ahead. Engineering is moving. The holdouts are structural (Anton/Darren deadlock, token cost anxiety).
- *What happened at the offsite?* → See above. Concrete artefacts at every station.

---

## Watch-outs

- Ollie is in the room and is **caught between conflicting SLT direction** (Anton vs Darren on pricing). Don't surface that tension in front of Ed — it needs a data-led resolution, not a politics conversation.
- Keep it light. Ed asked for casual. Resist the urge to over-structure.
- 45 minutes is short with 5 people — expect each person to get one thread, not a full debrief.

---

## Links

- [[reference/offsite-ai-session-draft]] — offsite session structure
- [[reference/ollie-conversion-bets-2026-04-27]] — conversion bets narrative
- [[domains/ai-initiative-roadmap]] — now/next/later
- [[meetings/2026-04-28-jordi-1-1]] — Jay instrumentation + SDLC pilot
- [[meetings/2026-05-05-matt-price-1-1]] — second brain, multiplayer, Ollie's doom loop
