---
title: AI Hackathon — ML Ops Pipeline and Pricing Features with Harry Dowrick
created: 2026-06-17
updated: 2026-06-17
domain: engineering-workflows
type: meeting
tags: [pricing, ml-ops, deterministic-vs-nondeterministic, harry-dowrick, francesco-venerandi, hackathon]
---

# AI Hackathon — ML Ops Pipeline and Pricing Features with Harry Dowrick

**Date:** Tue 17 Jun 2026, 13:31
**Attendees:** [[harry-dowrick]], Tom Harvey

Full transcript: [[2026-06-17-harry-dowrick-ai-hackathon-transcript]]

---

## Key themes

### ML Ops pipeline hackathon

Harry and [[francesco-venerandi]] blocked the day to build an AI-powered ML Ops pipeline for feature ideation. Problem: too many ways to define telemetry features, current tooling (Lucid) is manual and limited. Flow: make thematic decision → hand off to agent → get best features back → auto-generate test quotes. Implementation already done by an agent; need to string it together and validate productivity gains.

[[geran]] supportive; Francesco better at justifying upward to stakeholders. Harry's instinct: own the timeline rather than waiting for [[milan-chavda|Milan]] to say when — "run until tackled." *(Note: "Gran" in transcript → [[geran]], new transcription error)*

Framing for stakeholders: more features per quarter, not just faster work.

### AI's effect on the pricing role

Harry has a weekly existential crisis about AI replacing his role. Resolution: "steal other people's jobs instead of having my job stolen."

Two-hour tasks now taking ~30 minutes, mainly through Claude Code on versioning work:
- Points Claude at v12 vs v13 diff, applies that delta to v16 to produce v17, auto-commits
- Works well despite Claude guessing from variable names; occasionally loses context across repos

**Deeper vs faster framing:** Speed is the mechanism, but depth is the real signal — covering all features in parallel is humanly impossible without AI. Same logic applies to BDMs. Risk of burnout if the job becomes pure thinking, especially as feature complexity compounds (10th feature is genuinely hard).

Explainability still a hard constraint: Darren and Admiral need to hear reasoning from a person, not a black box.

### Deterministic vs non-deterministic tooling

Pricing team leaning too heavily on Claude for reporting tasks that should be deterministic:
- Wrong data shown to Admiral (90M GWP figure, clearly incorrect) — raised but shown anyway
- Root issue: rebuilding datasets from scratch every time instead of freezing a canonical version

Proposed fix: use Claude to generate LookML once, freeze it as a Look, then have the skill just call that Look with a date parameter. Buy-in is hard because Claude Code feels easy; LookML feels janky.

**Verdict:** agents for non-deterministic ideation, deterministic scripts for reporting and versioning. Likely needs a visible mistake (like the Admiral incident) to land the lesson. Next quarter: push toward deterministic scripts for reporting. This quarter was "make mistakes and get your hands dirty."

### Sharing and collaboration friction

Two live pain points in the pricing team:
- **Streamlit impact dashboard:** figuring out how to host and share it (spoke to [[sam]])
- **Skills and project files:** Claude can't write to shared Google Drive folders, causing version conflicts

Concurrent skill editing (Harry and Milan both editing the same skill) is a real problem. Short-term fix: don't edit at the same time. Longer-term question: where should CSVs, SQL files, and the underwriting report actually live?

Google Drive permission issues are fixable; the concurrent editing problem is a legitimate engineering challenge.

---

## Actions

- [ ] **Harry** — Resolve Google Drive permissions blocking Claude's write access (raise with team)
- [ ] **Harry + Milan** — Decide canonical home for pricing project files (CSVs, SQL, underwriting report, skills)
- [ ] **Tom** — Push pricing team toward deterministic scripts for reporting next quarter

---

## Name flags

- **"Gran"** in transcript → [[geran]] (truncated transcription of "Geran" — new error, add to name-resolution.yaml)
- **"Francesca"** used interchangeably with **"Francesco"** by Harry in speech → [[francesco-venerandi]]
