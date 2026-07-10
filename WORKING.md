# Working

## Current task

**AI tool uptake measurement (Jul 10)**: initiative `initiatives/ai-tool-uptake-measurement.md`. Schema v0.2; 3 vendors normalised (anthropic aggregates, cursor events, openai UI-transcription + name-to-email map). First bucket run: **27 power / 29 regular / 9 light**, report `reference/ai-tool-usage-reports/uptake-report-2026-06-01-to-2026-07-09.md` + **shared Flock-branded dashboard** https://claude.ai/code/artifact/87df4747-ea14-4be7-9b1d-ca9e77cb11c6 (source: session scratchpad `uptake-report.html`; regen = metrics.py → JSON → embed → redeploy same URL). Dashboard excludes jai.patel@ (unrecognised acct in Anthropic export — IDENTIFY) and Alex Smith (departed, people file marked).

**Jul 10 SCORE CHANGES (telemetry challenge)**: Matt Price 4→3 medium (777 req/18th agentic pct vs stage-4 cohort 1.7k-13.7k/≥57th; Jun 30 evidence self-reported; restore = artifact-level evidence at next 1:1). David Zamora 4→3 medium (paternity leave = 2-month evidence gap; strong May evidence = short restore path). **Distribution now 1:3 · 2:15 · 3:22 · 4:13** (was 3:20 · 4:15). Kaylee→**Kayleigh Bradbury** (email directory; name-resolution entry added). Screen flags pending: Phoebe/Fred/Milan/Michael Matthews (stage 2, power telemetry); unscored actives Antton/Charlie Dowrick/Joan Canellas/craig.hill; Geran frontmatter-4-vs-body-3.

NEXT: (1) ChatGPT pages 2-4 + Custom calendar ranges + Codex analytics check, (2) fuller Cursor export (Jun 1-9), (3) dept headcount denominator, (4) consider soft flag: stage 4 + bottom-quartile agentic pct.

## Previous task

Post-London consolidation. Four Jul 8-9 meetings imported and processed (Finance workshop, Ops sync, AI Underwriting w/ Darren Nightingale present, Digital Futures Athena demo). Scores updated in one pass.

## Baseline state (2026-07-09)

**n=53 scored of 58 in scope** (was 50/57: +Matt Smith UW, +Andrew Dodd, +Pavel scored; +Sarah Phillips new joiner into scope).
Distribution: **1:3 · 2:15 · 3:20 · 4:15**. Unassessed remaining (5): Darren Nightingale (attended Jul 9 mtg — nothing attributable, do NOT score second-hand), Curtis Bailey (assessment vehicle = his Mon Jul 13 demo-call prep), Billy Bone (still no signal), Antton, Sarah Phillips (new joiner).

**Jul 9 score changes** (evidence in people files, all sourced to the four meetings):
- Kirsty 2→4 RESTORED (self-audit/guardrails evidence; the last environment-vs-practice conflict resolved)
- Ivan 3→4 (fully autonomous daily pipeline)
- Matt Dipre 2→3 (calculator 1mo in production, code-reviewed; AI-014 closed obsolete)
- Jonny 2→3 (Zapier ambiguity resolved — real co:work builder)
- Queency 1→2 (self-invented approvals iteration)
- Anneliese 1→2 (Looker-MCP dashboards, attribution caveat; AI-149 STILL open)
- New: Matt Smith 2 (low-med), Andrew Dodd 1, Pavel 1 (low, attribution caveat)
- Tom Rogers builder-verified (own daily-plan skill), edging 4; Emily conf→high, restoration path visible; Fred holds 2

**DECK IMPACT: slide numbers are now stale** (Slides copy says 49/56, vault was 50/57, now 53/58; stage-1 count changed 3→3 but names changed; UW no longer "no stars" claim shifts — Tom Rogers builder + team chart P20s move: UW min stays 2; Finance 80%-at-or-above stays 2.0; Prodtech unchanged). Regenerate before next Ed share.

## New issues Jul 9
- **AI-157 URGENT: Anna knowledge transfer — she leaves Jul 10** (renewal Zap walkthrough/export today)
- AI-158 Emily renewal automation first slice · AI-159 NetSuite role scope (Geran) · AI-160 Tom Rogers skill → Andrew (with personalisation session — Ikea effect) · AI-161 UW central platform + HubSpot hygiene prerequisite (mid-Aug) · AI-162 Matt Dipre calculator holiday-cover/bus-factor · AI-163 Athena pilot decision (due Jul 17)

## Digital Futures verdict (for AI-163)
No pricing given; benchmark-pool question dodged; diagnostic = simulated scenarios not observed behaviour; their ceiling below our Stage 3; soft-no on ingesting our stages. Ed effusive but pivoted to advising their GTM; wants Admiral to fund any pilot. Fair hit: our measurement "doesn't scale beyond ~70" → AI-125 survey is the answer.

## Open threads
1. **Jul 8 Ed <> Tom 13:00 outcome is UNRECORDED** (in-person, no Granola). Need Tom's debrief: were targets/AI Champions/pod slate ratified? Blocks AI-152 closure.
2. Jul 3-7 meetings (Matthew 1:1, Jordi 1:1, ProdTech Heartbeat, Q3 OKR session ×2, Fergus weekly) have no Granola records — in-person week.
3. AI-149 verify Anneliese fix happened Jul 8 PM; write up for Kirsty→Christian.
4. Eraaz PGR build outcome (Mon Jul 6 session with Rakhee) — chase.
5. Rob's interview initiative: eng session "Technical Interview Improvements" ran Jul 9 13:00 — get outcome, update ai-first-hiring.
6. Pavel surname: Granola says Soulimov, vault says Souliman — verify with HR directory.
7. Quartz running detached on :8080 (pkill -f quartz to stop). Moss-secrets screenshot deleted; datadog-secrets.txt STILL untracked in repo root.

## Standing
- Deck source: reference/ai-capability-deck-2026-07.md; final Slides (Tom-edited): https://docs.google.com/presentation/d/1_b7wuaukJjmEHJ23U1vxXwi2g_r_P9hfBfsj0m0-XOo/
- Pod visual: outbox/ai-pod-structure-2026-07-08* (role = AI CHAMPIONS)
- Q3: 100% Stage 3+, majority 4 (Ed/Tom/Rakhee initiative, NOT company OKR)
