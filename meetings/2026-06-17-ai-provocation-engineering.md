---
title: AI Provocation — Engineering Team Practice
created: 2026-06-17
updated: 2026-06-17
domain: engineering-workflows
type: meeting
tags: [engineering, ai-adoption, team-practice, submissions, fergus, jordi, provocation]
---

# AI Provocation — Engineering Team Practice

**Date:** Tue 17 Jun 2026, 12:00
**Attendees:** [[jordi]], [[fergus]], Tom Harvey

Full transcript: [[2026-06-17-ai-provocation-engineering-transcript]]

---

## Key themes

### Individual progress is real; team-level practice hasn't moved

~50/50 split in engineering: half actively not writing code (using AI), half still constrained by old habits. Individuals have moved significantly in the last three months. But shared norms, style guides, and team collaboration on AI practices have not changed.

**Chris is further along and more open than given credit for.** The rest of the team similarly willing. The Sam/Chris/[[aleks-yanova|Aleks]] group gravitating toward automated tests, architectural design logs. Key insight from Chris: "the principles haven't changed, but the tools have" — processes need to move 10x faster to match AI's pace.

[[ishmael]] most naturally adaptive (Telemetry pipeline experience shaped this). [[javier|Rob]] and [[javier]] more hesitant to swap out frameworks or push architectural changes.

Engineers not sharing what they've built — not hiding it, just not broadcasting it. **This is a leadership gap, not a senior/junior engineer gap.** Leadership (Chris, Tom, Jordi, Fergus) should be modeling the art of the possible.

### Submissions pipeline concern

Four people, two months, not in production yet. Q3 approaching with no clear space for progressive delivery. No clear "version zero" milestone defined; priorities shift in conversation, creating drift.

Fergus offered to drop in and unblock — would likely solve "get something end-to-end and running" but not the deeper team practice problem. Still probably worth doing.

### Cross-team AI tooling gap

Acquisition team unlikely to self-identify blockers and swap out tools the way the J team does. [[ishmael]] shipped AI Kit for them but didn't socialize it — respecting their OKRs and delivery pressure. Risk: they won't reach for it when they need it.

Engineering decisions made in J (e.g. ISDA, agentic tooling choices) not being shared across teams. Non-J engineers not involved in those discussions or reasoning.

Data team ([[jacob-holland|Jacob]]) workflow different enough that it's tempting to exclude — but would be unfair.

### Three concrete levers for team-level change

All require whole-team buy-in:
1. **Corpus of style guide rules** — currently not expressed in a way AI can consume
2. **Architectural design logs** — history of decisions and rationale
3. **Spec-driven development** — acknowledged as controversial, but useful as a forcing conversation

Gentle nudging has moved individuals but not the team. Question: how hard to push vs wait for [[ishmael]] and [[javier]] to self-organize and lead it.

### David Zamora

Noted as missing from the conversation — would be in the fully-AI-adopted camp. Currently on paternity leave.

---

## Actions

- [ ] **Tom** — Continue AI group sessions to socialize team-level ideas; mix up the groups
- [ ] **Tom** — Consider an engineering AI breakfast to surface individual wins and pull toward team-level practice
- [ ] **Fergus** — Explore dropping into acquisition team to unblock and accelerate submissions pipeline delivery
- [ ] **Tom + Jordi + Fergus** — Decide how hard to push team-level practice change vs wait for Ishmael/Javier to lead it

---

## Name flags

- **"Alex unova"** in transcript → [[aleks-yanova|Aleks Yaneva]] (new transcription error — add to name-resolution.yaml)
- **"Harvey"** alongside Ishmael/Rob in engineering context → [[javier]] (per standard name resolution)
- **"J"** → the J product team / Jemima's product area
