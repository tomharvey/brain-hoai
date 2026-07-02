---
title: AI Capability Deck — July 2026 (source markdown)
created: 2026-07-02
updated: 2026-07-02
domain: ai-enablement
type: reference
tags: [capability, activation, deck, ed, benchmarking]
---

# AI Capability — Where Flock Stands
### Deck source markdown · Audience: Ed · Data as at 2026-07-02

Eight slides. Per Ed's comms playbook: every title is a statement, one argument per slide, titles alone tell the story. Deliberate deviation (Tom's call): slide bodies stay information-rich — this is a consumable document, not a talk-track prop. Presenter notes carry provenance and caveats.

**The story in titles:** fluency is the centre of gravity → we score behaviour, not talk → almost everyone is past first contact → half the company builds its own tools → BDM and Prodtech lead, Finance and UW are the focus → every team has a champion → the at-risk list is blocked, not unwilling → Q3: unblock, propagate, deputise.

---

## Slide 1 — The centre of gravity is fluency; a quarter of the company already hands off whole tasks

- 50 of 57 in-scope people scored (88% coverage)
- Median person: Stage 3 — argues with output, thinks with the model
- 13 people at Stage 4 (delegation) — nobody yet at Stage 5
- Only three people sit at Stage 1 — one brand-new starter, two blocked; none unwilling

**Presenter notes**
- Activation framing deliberately removed from the slides pending definition alignment with Ed — his verbal shorthand for "activated" (Jun 24: "building tools, bringing in the data") maps to Stage 2–3, not the framework's Stage-1-exit threshold, and the definitions give very different numbers (82% vs 56–64% of scope). Numbers preserved in the appendix; realign with Ed before reintroducing.
- The 7 unscored are the coverage gap: 5 underwriting ICs (holiday/paternity/deliberate deferral), Pavel (finance, no signal), Antton (CCO, no 1:1 yet).
- Denominator caveat: `ai-activation-map.md` (updated Jun 25) uses ~63 in scope; this deck uses the June assessment scope plus new joiner Kaylee (57). Reconcile before Ed forwards numbers to Admiral Pioneer.
- Do NOT reuse the Jun 24 verbal numbers ("90% activated, 75% building tools, 50% at top end") — see Slide 3 notes for the honest bridge.
- Playbook timeline note (Rule 1: three iterations, a week apart): compressed, not skipped — this document went through five reviewed iterations on Jul 2 alone.

---

## Slide 2 — We score six stages of behaviour: what people do, not what they understand

| Stage | Name | What it looks like | Expanded: the behaviours we check for |
|---|---|---|---|
| 0 | Search | Single prompt, read answer, done | No follow-up or correction; doesn't come back after "fine but unremarkable" output |
| 1 | First win | Pushes back, iterates, has a conversation | Gets genuinely useful wins that become a default, not one-offs |
| 2 | Context+tools | Loads context, connects data sources, dresses the model | CLAUDE.md / strategy docs / process maps; real systems connected (MCP, files, APIs) |
| 3 | Fluency | Argues with output, thinks with the model, builds tools | "What are the failure modes?"; builds on partial output; named, reusable artifacts |
| 4 | Delegation | Hands off whole tasks, reviews at output level | Trusts the agent within constraints; parallel sessions; catches errors via domain knowledge |
| 5 | Orchestration | Directs systems, measures adherence | Context quality judged by agent behaviour, not by reading it; composes human/agent/function |

**Presenter notes**
- Stage/Name/What-it-looks-like columns use **verbatim** the wording shared with Ed on Jun 24 (`reference/framework-stages-shared-with-ed-2026-06-24.png`) — he should recognise the table. The fourth column is the expansion.
- "Builds tools" sits inside Stage 3's description — so any Stage 3+ claim implies tool-building. See the builder-audit caveats before leaning on that number.
- **Behaviour, not understanding.** The framework scores what people do, not what they grasp — that's why the CEO can score below a junior ops person, and why this is not a capability ranking. Say this out loud before showing team numbers.
- Scores carry confidence tiers (high/medium/low). Low confidence = "gather more data", not "this is true". Low-confidence scores in the headline numbers: Michael Matthews, Ben Allen, Daisy Mae (+ Aleks medium with contested range).
- Ed's "does it extend to 6, 7, 8?" question (Jun 24, Chesky story): Stage 5 is the current defined ceiling and **nobody currently sits there** — Ismael was recalibrated 5→4 on Jun 30 under tighter "sustained practice, not spikes" standards. Stage 6 is deliberately uncharacterised; Ismael is the person to help define the frontier. This preserves comparability with past scores, which Ed said he wants.
- External benchmark gap: this is a Flock-native rubric — it can't be compared across companies. Ed's aipilled.com score (~40–50) is the available external anchor; the AI-125 benchmarking survey with Rakhee (due Jul 7) is the systematic answer.

---

## Slide 3 — Almost everyone is past first contact; the few at Stage 1 are new or blocked, not unwilling

```
Stage 0  ·                                (0)
Stage 1  ███                              (3)
Stage 2  ███████████████                  (15)
Stage 3  ███████████████████              (19)   ← centre of gravity
Stage 4  █████████████                    (13)
Stage 5  ·                                (0)
```

**Company: min 1 · median 3 · p80 4.0 · max 4** (n=50 scored)

- Fluent or better (Stage 3+): **64%** of scored
- Handing off whole tasks (Stage 4): **26%** of scored
- At Stage 1: Anneliese (install blocked — AI-149) · Queency (daily use, single-shot) · Kaylee (new in claims, heavy personal use, first work 1:1 booked)

**Presenter notes**
- P80 = the stage 80% of the team sits at or below, computed with **linear interpolation** (hence the 3.2s — nearest-rank on integer stages can only produce round numbers, which read as false precision the other way). Company p80 = 4.0: the top fifth of the company is delegating whole tasks. Label changed from "top fifth" to "P80" after it confused Ed live on Jul 2 ("that would be top four fifths"); he now knows the concept.
- **Jul 2 evidence challenges (Tom) moved four scores** — the honest ledger: David Pilley 1→3 and Anneliese briefly 1→2 (Moss environment blockers separated from practice), then Anneliese corrected back to 1 and Queency 2→1 on a second evidence pass (guided setups and single-shot patterns don't clear Stage 2's behaviour bar). Adam Sandle's 2 survived the same challenge (telemetry MCP + FNOL skill in real use). Kaylee (new claims joiner) scored Stage 1 on Tom's direct read, Jul 2 — extends scope to 57 and scored to 50.
- **Bridge from what Tom told Ed on Jun 24** (claims → recalibrated data):
  - "50% at the top end, two at the very furthest" → actually **27% at Stage 4, zero at Stage 5**. Reframe: "About a quarter are at delegation; on closer review nobody has genuinely reached orchestration yet."
  - "90% activated" → **94% of scored / 82% of scope**. The mechanism claimed was right: of the nine not counted, seven are simply unmeasured; only two are confirmed below the line — and both are blocked, not stalled.
  - "75% building their own tools" → Stage 3+ proxy gives **65% of scored**; the artifact audit says 50% strict / 70% loose — see Slide 4.
  - "Finance and underwriting lag, broad distribution" → confirmed: Finance (2.3), Operations (2.4), Pricing (2.5) and Underwriting (2.6) are the lowest means (buckets re-cut Jul 2; the old combined UW & Pricing was 2.5). Finance is genuinely broad (Stage 1–4, CFO at the top); Underwriting and Pricing are tight clusters at 2–3, no stars.
  - "~30% of underwriting past activation, same for finance" → Finance: exactly right at 30% fluent+. Old combined UW & Pricing: **50% fluent+**; after the Jul 2 re-cut, Underwriting 60% and Pricing 50% — but zero at Stage 4 in either, which is why they still read as lagging.
  - "90% there on presenting benchmarking with Rakhee" → 50/57 scored = 88%. Holds as "high-80s".
- **Bridge from the Jun 18 assessment doc** (in case Ed saw it): it said "Engineering & Product every person at Stage 4+" and 19 people at Stage 4. The Jun 30 re-assessment applied tighter evidence standards — sustained practice, not peak spikes — and pulled 7 of 10 engineers down (Ismael 5→4, Jordi/Chris/Sam/Rob 4→3, Stephen/Aleks 4→2). The company didn't get worse; the measurement got honest. Same standards will be used for the company-wide survey, so the baseline is defensible.
- Provenance: stages from `people/*.md` frontmatter (source of truth), re-assessed 2026-06-30 for 28 people against Jun 22–30 transcripts; four scores corrected 2026-07-02 on evidence challenge; remainder assessed Jun 2–25. Evidence base: 115+ Granola transcripts Mar–Jun 2026. The three meetings from the past 7 days (Jun 29 Moss, Jun 30 David Pilley, Jun 30 Matt Price) are incorporated and their transcripts are in the vault.

---

## Slide 4 — Half the company builds its own tools, and another fifth is one coached rep away

| | | |
|---|---|---|
| **50%** build independently — reusable tools in live use | **70%** have built or co-built at least one skill | **30%** no artifact yet |

- The middle rung (20%) built something with guidance — Fred's personalised referral skill, Phoebe's Netlify slides, Adam Sandle's FNOL reports
- Converting that rung to independent builders **is** the Q3 enablement plan: coached reps, not more workshops

**Presenter notes**
- Artifact-level audit, Jul 2: one agent per team verified every claim against people files + transcripts. Rubric: builder = named, reusable artifact they created with AI (skill, dashboard, automation, MCP workflow, app, pipeline) in repeated use. 25 verified / 10 assisted / 15 no-artifact of 50.
- This slide is the honest version of the "75% building their own tools" claim from Jun 24: roughly right under the loose definition (70%), ahead of the evidence under the strict one (50%). Say which definition you mean.
- The Stage 3+ proxy (64%) over- and under-counts builders both ways — full mismatch list in the builder-audit appendix (e.g. Darren McC at Stage 3 with no artifact; Milan at Stage 2 with two corroborated skills).

---

## Slide 5 — BDM and Prodtech lead; Finance and Underwriting are the Q3 focus, for different reasons

| Team | n | min | P80 | max | Shape |
|---|---|---|---|---|---|
| Distribution | 5 | **3** | 4.0 | 4 | Nobody below fluency; two agent systems in production |
| Prodtech | 15 | 2 | **4.0** | 4 | Over half at delegation — deep vanguard, fragile tail |
| People | 3 | 2 | 3.2 | 4 | One star, two early |
| **Underwriting** | 5 | 2 | 3.0 | **3** | Capped at fluency — no stars |
| **Pricing** | 4 | 2 | 3.0 | **3** | ICs ahead of their heads — inverted pyramid |
| Operations | 7 | **1** | 3.0 | 4 | One star, broad middle — claims folded in, incl. a new starter |
| **Finance** | 10 | **1** | 3.0 | 4 | Widest spread — Stage 1s and the Stage-4 CFO |

```
Distribution  2:      3:███     4:██
Prodtech      2:██    3:█████   4:████████
Operations    2:██    3:██      4:█
People        2:██    3:        4:█
UW & Pricing  2:█████ 3:█████   4:
Finance       1:██  2:████  3:███  4:█
```

**Presenter notes**
- Small-team caveat: People is n=3, so any percentile is fragile — interpolation fixes the old artifact where nearest-rank made their p80 equal the max (Eraaz alone dragged it to 4); 3.2 is the honest figure.
- Ed (Stage 3) and Tom sit outside the team view by design (confirmed with Tom, Jul 2) — Ed counts in the company-level stats only.
- **Finance and UW are confirmed as the Q3 focus teams, but for different reasons.** Finance is infrastructure-gated: the blockers are Moss MCP installs, Python-less machines, and NetSuite/Looker access — not skill or will (Jun 29/30 meetings are the direct evidence; both Stage-1s sit here and both are one unblock-plus-one-win from Stage 2). Underwriting is propagation-gated: capped at Stage 3, practice staying private — Darren McCauley is "secretly all over it, not pushing down"; Jake Wood is the deliberate bottom-up bridge to the 5 unassessed ICs and Darren Nightingale ("number one cynic" — do not approach yet). Pricing (split out Jul 2) is an inverted pyramid: the ICs (Francesco, Harry — Stage 3 builders) are ahead of the heads of function (Milan, Michael Matthews — Stage 2, "still not ingrained"); the intervention is downward propagation inside the function.
- Prodtech's shape is the subtle story: p80 of 4.0 with a min of 2 — 8 of 15 at Stage 4, but a tail of 2s. The vanguard (Ismael, Jacob, David Z) is real; the middle was recalibrated down amid craft-loss anxiety (Javier "associate factory", Aleks "I've learned nothing", Stephen pulling back). The intervention is teaching capacity + shared quality infrastructure, not more tooling.
- Operations context (regrouped Jul 2: claims folded in): Adam Sandle (2, fortnightly coaching AI-131) and Kaylee (1 — brand-new, heavy personal AI use, none at work yet) join; Antton (CCO) remains the unassessed coverage gap, so n=7 understates the team by one.
- Team labels follow the Jul 2 groupings (Prodtech = Engineering + Product + Fergus; Pricing split from UW; claims in Operations); several files carry differing team tags (Christian "Leadership"→Finance, Darren McC "Leadership"→Underwriting, Paul "Leadership"→Finance, Rakhee "Leadership"→People, Michael Matthews "Underwriting"→Pricing, Adam Sandle "Claims"→Operations, Ed→unassigned). Numbers reconcile; don't let a live vault click-through surprise you.
- Unassessed (not in these stats): Underwriting — Darren Nightingale (tentative 0–1, second-hand only), Andrew Dodd, Curtis Bailey (holiday; tentative 0–1), Billy Bone (paternity; tentative 1 — Jake built colourblind mode for him), Matt Smith (tentative 1, went quiet after week one). Finance — Pavel (tentative 0, no signal). Operations — Antton (tentative 1–2, engages with outputs, asks governance questions).

---

## Slide 6 — Every team has a champion, and two teams are champions

| Team | Champion | The one-liner |
|---|---|---|
| Distribution (BDM) | **The whole team** 🏆 | Nobody below fluency; two agent systems in production — a 9-agent enterprise pipeline and the SLT trading review |
| Prodtech | **The Stage-4 vanguard** 🏆 | 8 of 15 delegating: parallel agents writing PRs (Ismael ~90% AI-generated code), test suites, the acquisition brain, production apps |
| Operations | Shreya | 3 production tools built independently; now teaching the method |
| Finance | Ivan | Daily credit-control skill running 2+ months (Slack nudge); broker-payment dashboard; co-built the NetSuite MCP |
| Underwriting | Jake Wood | Dashboard drove HubSpot notes 0→90%; the peer bridge into underwriting |
| Pricing | Francesco | MCP performance coach in weekly 1:1 use; claims-triangle skill; J feedback pipeline |
| People | Eraaz | 3×/day co:work optimisation system; builds prompts for his own team |

**Presenter notes**
- Table rule: max one named individual per team; where most of a team is at champion level (BDM, Prodtech's vanguard), the team itself is the champion — the stronger story for Ed anyway ("whole teams get there, not just heroes").
- The full bench behind the table (promotion-conversation shortlist + deputy pool for the Q3 AI partnering team, AI-127): Jacob, David Z, Fergus, Mima, Ollie, Geran, Matt Price (Prodtech — Ed named Mima on Jun 24 as the promote-the-boundary-pushers example); Matt Lees, Adam Smith (the BDM call-out); Christian (CFO — exec sponsor: co:work budget artifact to SLT, provides leadership rather than holds the pen), Kevin (teaching David Pilley — strongest evidence but fractional contractor), Matt Dipre (near-champion; flagship automation broke on a NetSuite update, unblocking AI-014 resurrects him) — all Finance; Emily (Ops); Tom Rogers (Underwriting); Harry (Pricing).
- **Watch flags on champions and near-champions** (over-trust, the company-wide failure mode): Adam Smith presented wrong Claude numbers to SLT (Jun 11), validation still not in place; Tom Rogers promised a customer an unconfirmed feature; David Pilley (Stage 3, Moss unblocked Jun 30) carries Kevin's "thinks it's magic... cedes to it" flag — his 3→4 path is review muscle, not more tools. Celebrate the output, install the guardrails.

---

## Slide 7 — The at-risk list is blocked or unmeasured, not unwilling

| Team | Who | Why |
|---|---|---|
| Finance | Anneliese · Queency | Stage 1 — Anneliese: guided setup, install blocked (AI-149), one real win from Stage 2; Queency: daily file-feed use but single-shot, connected Moss unqueried in real work |
| Prodtech | Stephen · Aleks | Recalibrated 4→2; pull-back and skill-displacement grief |
| Underwriting | Ben · Daisy Mae | Stage 2 on inference only — near-zero individual data ("Chinese wall of a calendar") |
| Pricing | Michael M · Milan | Heads of function at Stage 2, "still not ingrained" — while their own ICs sit at Stage 3 |
| People | Rakhee · Phoebe | Stage 2 — the people coordinating the AI programme trail it; both have live 2→3 paths (PGR prompt AI-144, Flock O'Clock AI-141) |
| Ops | Jonny · Fred · Adam Sandle · Kaylee | Stages 1–2; guided-only wins; Sandle on fortnightly coaching (AI-131); Kaylee new — heavy personal use, none at work yet |

**Presenter notes**
- At-risk framing: nobody on this list is refusing. Four groups, four different interventions: *blocked* (Anneliese — a Python install; Queency — a filtering bug), *unmeasured* (Ben, Daisy — assess before judging), *pulled back* (Stephen, Aleks — the craft conversation, not pressure), *habit not formed* (Michael, Milan, Rakhee, Phoebe, Adam Sandle — coached reps on real work), plus *new starters* (Kaylee, Connie returning — onboarding, not remediation). A single "level up or else" message would misfire on three of the four groups.
- Queency downgrade rationale (Jul 2, on Tom's challenge): the connected Moss MCP was installed with support and her working pattern is single-shot — when Moss returned wrong data she stopped rather than iterated. Stage 2 requires the behaviour, not the tool. Decisive test: one self-driven, iterated Moss query in her real approvals work.
- Rakhee, checked against the Jun 25 meetings (Tom's question): Claude is her primary tool — strategy thought partner, policy review, drafting, Alar daily agenda, workflow down to two Notion trackers. That's genuine daily fluency *usage*, but no demonstrated arguing-with-output and every artifact around her is someone else's (Eraaz builds the team's prompts; she tested the PGR prompt, didn't build it). The Jun 24 bump to 3 was reverted on exactly this evidence on Jun 30. Hold at 2 (high end). Decisive test: the AI-144 session (booked Monday Jul 6) — if she builds and trials the PGR prompt with Eraaz rather than framing while he builds, that's her 3.
- Rakhee/Phoebe sensitivity: Ed will spot that the People team trails the programme it coordinates. Eraaz is the in-team fix (already building their prompts). Rakhee is also the partner for the benchmarking survey — position as "her programme skills + my practice coaching", not as a problem child.
- Score conflicts still open (don't present, just know): Kirsty scored 2 on Moss context while her Stage-4 Looker evidence "remains valid" — the same case shape that was corrected for David Pilley on Jul 2; Geran's frontmatter says 4 while his file body argues 3. If challenged, the honest answer is "scored on current sustained practice; noted, under review."

---

## Slide 8 — Q3: unblock Finance, propagate Underwriting, deputise the champions

1. **The baseline exists.** 49 of 56 scored on one rubric; the remaining tail is 7 named people with dates and owners, not a programme.
2. **Focus shifts to the two gap teams** — Finance (unblock infrastructure) and UW (propagate via Jake + peer demos). Monthly team workshops continue; company-wide sessions don't scale.
3. **Deputise the champions** — AI partnering team pilot for Q3 (the Ghostbusters model), drawn from Slide 6.
4. **Measure outcomes, not tool usage** — counting skills built is the wrong metric; the benchmarking survey (with Rakhee, this week) gives the baseline, then targets go on the rubric.
5. **The new failure mode is over-trust** — everyone owns the quality of what they ship. Guardrails ship with delegation.

**Presenter notes**
- Near-term dated commitments (all open): benchmarking survey with Rakhee (AI-125, due Jul 7 — Ed committed this to Admiral Pioneer), new-hire assessment integration (AI-128, Jul 8), AI partnering pilot (AI-127, Jul 1, needs launch), Moss rollout completion (AI-148, Jul 6) and Anneliese's Python fix (AI-149, Jul 3), London push on Rob & Javier to 100% AI-assisted (AI-150, Jul 10), Geran finance-metrics session (AI-151, Jul 9).
- Several older workshop/access issues are past-due but open (AI-045/046 Ed's own Cursor/MCP access from May; AI-056 NetSuite MCP; AI-014 Matt Dipre Looker access) — sweep these before Ed asks "what's blocking finance" and the answer includes items assigned to you since April.
- Ed's provocations from Jun 24 not answered by this deck (park explicitly if raised): the company-wide intensive week, hiring bar ("no Copilot-only engineers"), firing implications, external speakers. The deck's line: benchmark first, then set the bar.

---

## Appendix — builder audit (2026-07-02, not for presentation)

Per-person artifact audit (8 team agents, people files + transcript corroboration). Rubric: **builder = named, reusable artifact they created with AI (skill, dashboard, automation, MCP workflow, app, pipeline) in repeated use** — not one-off chats, guided builds, or using others' tools.

**Result: 25 of 50 verified builders (50%) · 10 assisted/decayed (20%) · 15 no build evidence (30%).** (Kaylee added Jul 2, no artifact yet.)

Verified: Ismael, Jordi, David Z, Javier, Jacob, Chris, Rob, Stephen†, Mima, Ollie, Geran (Prodtech — Fergus, also Prodtech, stays BUILDER-ASSISTED, see below); Emily, Shreya (Ops); Christian‡, Kevin, Ivan, Kirsty†, David Pilley (Finance — re-scored to Stage 3 on Jul 2, dagger resolved); Adam Smith, Liam (Distribution); Jake (Underwriting); Francesco, Harry, Milan† (Pricing); Eraaz (People). († = builder-verified while scored Stage ≤2 — score understates them. ‡ = initially misclassified no-build by the audit; corrected 2026-07-02 — his co:work HTML budget artifact was shared to SLT/Antton and his distribution-cost workflow replaced the old flow as default; the Jun 11 source note had his identity unresolved, now fixed.)

The Stage 3+ proxy fails in both directions:
- **Too generous (4 no-build at Stage 3+):** Sam, Anna, Alex Dyball, **Darren McCauley** (Stage 3 rests on one uncorroborated observation; Jun 22 transcript: "pretty much a ChatGPT guy"). Plus 6 assisted-only at 3+: Matt Price, Tom Rogers (one-offs), Matt Lees (flagship decayed, Jun 24 manual-search regression), Sophie (template-based), Fergus and Ed (prototypes/demos, not tools in service).
- **Too strict (3 builders at Stage ≤2, was 4):** Stephen (Databricks monitoring system real but dormant), Kirsty (Looker MCP + pod-metrics skill still in use by Distribution), **Milan** (claims-triangle + UW-report skills, corroborated by Harry — his own file wrongly says "hasn't built anything independently"). David Pilley was the fourth; resolved by his Jul 2 re-score to Stage 3.

Structural conclusion: the stage axis conflates *how someone works* (fluency, delegation) with *what they've shipped*. Ed's Stage 3 wording literally says "builds tools", so either (a) enforce a named-artifact gate on Stage 3+ scores, or (b) track a separate builder badge (verified/assisted/none) in people-file frontmatter and report it as its own number. Recommend (b) — it preserves stage comparability and fixes the false positives without re-scoring everyone.

Corrections to feed back into people files: Milan (builder evidence), Darren McC (stage likely overstated), Stephen/Kirsty (builder-verified flags; David Pilley, Anneliese and Queency resolved by Jul 2 re-scores). Identity flag: some June engineering references to "Alex Dyball" are likely a different Alex (name-resolution conflation) — excluded from his audit.

## Appendix — provenance (not for presentation)

- **Source of truth:** `people/*.md` frontmatter (`ai_activation_stage/confidence/assessed`). 28 people re-assessed 2026-06-30 against Jun 22–30 transcripts (commit 8f627a3); others assessed Jun 2–25. Framework: [[activation-pathway]]. Prior snapshots: [[ai-activation-assessment-2026-06]] (Jun 18 — stages superseded, groupings retained), [[ai-capability-baseline-2026-04]].
- **Past-7-days check (2026-07-02):** three Granola meetings from Jun 29–30 were not in the vault; imported today ([[2026-06-29-moss-finance-rollout]], [[2026-06-30-david-pilley-moss-install]], [[2026-06-30-thomas-matthew-1-1]]). Their evidence was already reflected in the Jun 30 scores.
- **Verification:** per-person evidence audit (49 agents) against the transcript corpus; department syntheses; adversarial claims-vs-data check; completeness critique; builder audit (8 team agents). Stats computed nearest-rank.
- **Jul 2 score corrections (evidence challenges by Tom):** David Pilley 1→3 (Moss environment blocker separated from his Stage-3 dashboard practice; install completed Jun 30). Anneliese 1→2→1 same day (Python blocker rightly discounted, but the Jun 1 connector setup turned out to be a guided session — no independent Stage-2 behaviour evidenced). Queency 2→1 (assisted MCP install + single-shot working pattern don't clear Stage 2). Adam Sandle challenged and upheld at 2 (telemetry MCP + FNOL skill in real, repeated use). Kaylee (new claims joiner) added at Stage 1 on Tom's direct read. Net: company distribution 1:3 · 2:15 · 3:19 · 4:13, n=50 of 57 scope.
- **Known data-quality flags:** stale scores (Mima 05-26 with an unincorporated 06-24 transcript; Kevin, Matt Lees, Matt Dipre, Ben, Daisy 06-02); context-scoped downgrade still under review (Kirsty — same case shape as David Pilley's resolved one); frontmatter/body disagreements (Geran 4 vs 3, Javier 3 vs "3–4", Aleks 2 vs "2–3"); Emily's cited source meeting not present in the vault; scope denominator 56 (assessment) vs ~63 (activation map, Jun 25).
