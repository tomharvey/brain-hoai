---
title: AI Capability Deck — July 2026 (source markdown)
created: 2026-07-02
updated: 2026-07-02
domain: ai-enablement
type: reference
tags: [capability, activation, deck, ed, benchmarking]
---

# AI Capability — Where Flock Stands
### Deck source markdown · Audience: Ed · Data as at 2026-06-30

Six slides. Slide text is deliberately sparse; presenter notes carry the evidence and caveats.

---

## Slide 1 — Headline

> **The centre of gravity of the company is Stage 3 — Fluency.**
> A quarter of the company is already delegating whole tasks. Nobody is at zero.

- 49 of 56 in-scope people scored (87.5% coverage)
- Nobody below Stage 2 — the company floor is "context loaded, tools connected"
- The frontier: 13 people at Stage 4 — nobody yet at Stage 5

**Presenter notes**
- Activation framing deliberately removed from the slides pending definition alignment with Ed — his verbal shorthand for "activated" (Jun 24: "building tools, bringing in the data") maps to Stage 2–3, not the framework's Stage-1-exit threshold, and the two definitions give very different headline numbers (87.5% vs 57–65% of scope). Numbers preserved in the appendix; realign the definition with Ed before reintroducing.
- The 7 unscored are the coverage gap: 5 underwriting ICs (holiday/paternity/deliberate deferral), Pavel (finance, no signal), Antton (CCO, no 1:1 yet).
- Denominator caveat: `ai-activation-map.md` (updated Jun 25) uses ~63 in scope; this deck uses the 56-person scope from the June assessment. Reconcile before Ed forwards numbers to Admiral Pioneer.
- Do NOT reuse the Jun 24 verbal numbers ("90% activated, 75% building tools, 50% at top end") — see Slide 3 notes for the honest bridge.

---

## Slide 2 — The framework

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
- Scores carry confidence tiers (high/medium/low). Low confidence = "gather more data", not "this is true". Five headline-relevant scores are low-confidence: Queency, Michael Matthews, Ben Allen, Daisy Mae (+ Aleks medium with contested range).
- Ed's "does it extend to 6, 7, 8?" question (Jun 24, Chesky story): Stage 5 is the current defined ceiling and **nobody currently sits there** — Ismael was recalibrated 5→4 on Jun 30 under tighter "sustained practice, not spikes" standards. Stage 6 is deliberately uncharacterised; Ismael is the person to help define the frontier. This preserves comparability with past scores, which Ed said he wants.
- External benchmark gap: this is a Flock-native rubric — it can't be compared across companies. Ed's aipilled.com score (~40–50) is the available external anchor; the AI-125 benchmarking survey with Rakhee (due Jul 7) is the systematic answer.

---

## Slide 3 — Where the company sits

```
Stage 0  ·                                (0)
Stage 1  ·                                (0)
Stage 2  █████████████████                (17)
Stage 3  ███████████████████              (19)   ← centre of gravity
Stage 4  █████████████                    (13)
Stage 5  ·                                (0)
```

**Company: min 2 · median 3 · p80 4 · max 4** (n=49 scored)

- Fluent or better (Stage 3+): **65%** of scored
- Delegating whole tasks (Stage 4): **27%** of scored

**Who actually builds their own tools** (artifact-level audit, Jul 2):

| | | |
|---|---|---|
| **51%** build independently — reusable tools in live use | **71%** have built or co-built at least one skill | **29%** no artifact yet |

**Presenter notes**
- p80 method: nearest-rank — the stage that 80% of people sit at or below. Company p80 = 4 means the top fifth of the company is delegating whole tasks.
- **Bridge from what Tom told Ed on Jun 24** (claims → recalibrated data):
  - "50% at the top end, two at the very furthest" → actually **27% at Stage 4, zero at Stage 5**. Reframe: "About a quarter are at delegation; on closer review nobody has genuinely reached orchestration yet."
  - "90% activated" → **100% of scored / 87.5% of scope** (after the Jul 2 re-scores separated Moss environment blockers from practice — see appendix). The mechanism claimed was right: the remaining gap is entirely people not yet sat down with.
  - "75% building their own tools" → the Stage 3+ proxy gives **65% of scored**, the artifact-level audit (Jul 2) splits it into a ladder: **51% verified independent builders · 71% built or co-built at least one skill (even guided — Fred's tier) · 29% no artifact**. So the "75%" was roughly right under the loose definition and ahead of the evidence under the strict one — say which definition you mean, and use the ladder: the middle rung is one coached rep away from verified, which is the Q3 conversion story.
  - "Finance and underwriting lag, broad distribution" → both confirmed lowest by mean (now tied at 2.5 after the Jul 2 re-scores). Finance spans 2–4 with the biggest Stage-2 cohort (six of ten) and the CFO as its lone Stage 4; UW is the tightest cluster in the company (everyone at 2–3, no stars, no stragglers).
  - "~30% of underwriting past activation, same for finance" → Finance: exactly right at 30% fluent+. UW: actually **50% fluent+** — but zero at Stage 4, which is why it still reads as lagging.
  - "90% there on presenting benchmarking with Rakhee" → 49/56 scored = 87.5%. Holds as "high-80s".
- **Bridge from the Jun 18 assessment doc** (in case Ed saw it): it said "Engineering & Product every person at Stage 4+" and 19 people at Stage 4. The Jun 30 re-assessment applied tighter evidence standards — sustained practice, not peak spikes — and pulled 7 of 10 engineers down (Ismael 5→4, Jordi/Chris/Sam/Rob 4→3, Stephen/Aleks 4→2). The company didn't get worse; the measurement got honest. Same standards will be used for the company-wide survey, so the baseline is defensible.
- Provenance: stages from `people/*.md` frontmatter (source of truth), re-assessed 2026-06-30 for 28 people against Jun 22–30 transcripts; remainder assessed Jun 2–25. Evidence base: 115+ Granola transcripts Mar–Jun 2026. The three meetings from the past 7 days (Jun 29 Moss, Jun 30 David Pilley, Jun 30 Matt Price) are incorporated in the Jun 30 scores and their transcripts are now in the vault.

---

## Slide 4 — The spread by team

| Team | n | min | p80 | max | Shape |
|---|---|---|---|---|---|
| Distribution | 5 | **3** | 4 | 4 | Nobody below fluency; two building agentic systems |
| Prodtech | 15 | 2 | **4** | 4 | Over half at delegation — deep vanguard, fragile tail |
| Operations | 5 | 2 | 3 | 4 | One star, mixed middle |
| People | 3 | 2 | 4 | 4 | One star, two early |
| **UW & Pricing** | 10 | 2 | 3 | **3** | Uniform — no laggards, **no stars** |
| **Finance** | 10 | 2 | 3 | 4 | Bottom-heavy — six of ten at Stage 2, the CFO alone at 4 |

```
Distribution  2:      3:███     4:██
Prodtech      2:██    3:█████   4:████████
Operations    2:██    3:██      4:█
People        2:██    3:        4:█
UW & Pricing  2:█████ 3:█████   4:
Finance       2:██████ 3:███   4:█
```

**Presenter notes**
- Small-team caveat: for People (n=3), p80 ≡ max — read the dots, not the percentile.
- Ed (Stage 3) and Tom sit outside the team view by design (confirmed with Tom, Jul 2) — Ed counts in the company-level stats only.
- **Finance and UW are confirmed as the Q3 focus teams, but for different reasons.** Finance is infrastructure-gated: six of ten sit at Stage 2 and the blockers are Moss MCP installs, Python-less machines, and NetSuite/Looker access — not skill or will (Jun 29/30 meetings are the direct evidence; the Jul 2 re-scores of Anneliese 1→2 and David Pilley 1→3 formalised exactly this separation of environment from practice). UW is propagation-gated: five genuine builders at Stage 3, zero at 4, and practice staying private — Darren McCauley is "secretly all over it, not pushing down"; Jake Wood is the deliberate bottom-up bridge to the 5 unassessed ICs and Darren Nightingale ("number one cynic" — do not approach yet).
- Prodtech's shape is the subtle story: p80 of 4 with a min of 2 — 8 of 15 at Stage 4, but a tail of 2s. The vanguard (Ismael, Jacob, David Z) is real; the middle was recalibrated down amid craft-loss anxiety (Javier "associate factory", Aleks "I've learned nothing", Stephen pulling back). The intervention is teaching capacity + shared quality infrastructure, not more tooling.
- Operations context: Antton (CCO) now belongs to this team but is unassessed (no 1:1 yet) — he is Operations' coverage gap, so n=5 understates the team by one.
- Team labels here follow the new July groupings (Prodtech = former Engineering + Product + Fergus); several people's files still carry a "Leadership" team tag but are bucketed by function, now spanning even more teams (Christian→Finance, Darren McC→UW, Paul→Finance, Rakhee→People, Fergus→Prodtech, Ed→unassigned). Numbers reconcile; don't let a live vault click-through surprise you.
- Unassessed (not in these stats): Darren Nightingale (tentative 0, skeptic), Andrew Dodd, Curtis Bailey (holiday; tentative 0–1), Billy Bone (paternity; tentative 1 — Jake built colourblind mode for him), Matt Smith (tentative 1, went quiet after week one), Pavel (tentative 0, no signal), Antton (tentative 1–2, engages with outputs, asks governance questions — Operations' gap).

---

## Slide 5 — Champions and at-risk

**Champions — recognise them (Ed: "meritocracy everywhere")**

| Team | Champion | The one-liner |
|---|---|---|
| Distribution (BDM) | **The whole team** 🏆 | Nobody below fluency; two agentic systems in production — a 9-agent enterprise pipeline and the SLT trading review |
| Product pod (Prodtech) | **The whole pod** 🏆 | All four PMs at Stage 4 — eval suites, the acquisition brain, production Streamlit apps |
| Prodtech | Ismael | ~90% AI-generated code; parallel agents writing PRs he reviews |
| Operations | Shreya | 3 production tools built independently; now teaching the method |
| Finance | Christian (CFO) | co:work budget artifact shared to SLT; SPA extraction via 10–11 self-checking runs |
| UW & Pricing | Jake Wood | Dashboard drove HubSpot notes 0→90%; the peer bridge into underwriting |
| People | Eraaz | 3×/day co:work optimisation system; builds prompts for his own team |

**At-risk — the honest list**

| Team | Who | Why |
|---|---|---|
| Finance | Anneliese | Stage 2 — practice is fine; one Python install (AI-149) from shipping her month-end tool |
| Finance | Queency | Stage 2 low-confidence; MCP connected but not yet queried in real work |
| Prodtech | Stephen · Aleks | Recalibrated 4→2; pull-back and skill-displacement grief |
| UW & Pricing | Michael M · Milan | Heads of function at Stage 2; "still not ingrained" |
| UW & Pricing | Ben · Daisy Mae | Stage 2 on inference only — near-zero individual data |
| People | Rakhee · Phoebe | Stage 2 — the people coordinating the AI programme trail it |
| Ops | Jonny · Fred | Stage 2; unclear AI vs traditional automation, guided-only wins |

**Presenter notes**
- Table rule: max one named individual per team; where most of a team is at champion level (BDM, the Product pod), the team itself is the champion — that's the stronger story for Ed anyway ("whole teams get there, not just heroes").
- The full bench behind the table (promotion-conversation shortlist + deputy pool for the Q3 AI partnering team, AI-127): Jacob, David Z, Fergus (Prodtech); Mima, Ollie, Geran, Matt Price (the Product pod call-out — Ed named Mima on Jun 24 as the promote-the-boundary-pushers example); Matt Lees, Adam Smith (the BDM call-out); Kevin (Finance — teaching David Pilley); Emily (Ops); Tom Rogers, Francesco (UW).
- **Watch flags on champions and near-champions** (over-trust, the company-wide failure mode): Adam Smith presented wrong Claude numbers to SLT (Jun 11), validation still not in place; Tom Rogers promised a customer an unconfirmed feature; David Pilley (now Stage 3, Moss unblocked Jun 30) carries Kevin's "thinks it's magic... cedes to it" flag — his 3→4 path is review muscle, not more tools. Celebrate the output, install the guardrails.
- Queency's Stage 2, justified: she has a connected data source (Moss MCP — reinstalled it herself on the Jun 29 call) and her daily approvals workflow runs on loaded context (feeds files to Claude as the first step). That's Stage 2 behaviour by the book. Not Stage 1: regular multi-task use, not a single win. Not Stage 3: no iteration or building, still setup-dependent. Low confidence stands until she queries Moss data in real work — the expense-type filtering bug (her Slack-shared chat) is the current blocker.
- At-risk framing: nobody on this list is refusing. The list splits into *blocked* (finance installs), *unmeasured* (Ben, Daisy — assess before judging), *pulled back* (Stephen, Aleks — needs the craft conversation, not pressure), and *habit not formed* (Michael, Milan, Rakhee, Phoebe). Different interventions per group; a single "level up or else" message would misfire on three of the four.
- Rakhee/Phoebe sensitivity: Ed will spot that the People team trails the programme it coordinates. Eraaz is the in-team fix (already building their prompts). Rakhee is also the partner for the benchmarking survey — position as "her programme skills + my practice coaching", not as a problem child.
- Score conflicts to resolve before this goes company-wide (don't present, just know): Kirsty scored 2 on Moss context while her Stage-4 Looker evidence "remains valid" (the same environment-vs-practice case that was corrected for David Pilley and Anneliese on Jul 2 — Kirsty is the remaining one); Geran's frontmatter says 4 while his file body argues 3. If challenged, the honest answer is "scored on current sustained practice; noted, under review."

---

## Slide 6 — What this means for Q3

1. **The baseline exists.** 49 of 56 scored on one rubric; the remaining tail is 7 named people with dates and owners, not a programme.
2. **Focus shifts to the two gap teams** — Finance (unblock infrastructure) and UW (propagate via Jake + peer demos). Monthly team workshops continue; company-wide sessions don't scale.
3. **Deputise the champions** — AI partnering team pilot for Q3 (the Ghostbusters model), drawn from Slide 5's left column.
4. **Measure outcomes, not tool usage** — PGR pressure to count skills built is the wrong metric; the benchmarking survey (with Rakhee, this week) gives the baseline, then targets go on the rubric.
5. **The new failure mode is over-trust** — everyone owns the quality of what they ship. Guardrails ship with delegation.

**Presenter notes**
- Near-term dated commitments (all open): benchmarking survey with Rakhee (AI-125, due Jul 7 — Ed committed this to Admiral Pioneer), new-hire assessment integration (AI-128, Jul 8), AI partnering pilot (AI-127, Jul 1, needs launch), Moss rollout completion (AI-148, Jul 6) and Anneliese's Python fix (AI-149, Jul 3), London push on Rob & Javier to 100% AI-assisted (AI-150, Jul 10), Geran finance-metrics session (AI-151, Jul 9).
- Several older workshop/access issues are past-due but open (AI-045/046 Ed's own Cursor/MCP access from May; AI-056 NetSuite MCP; AI-014 Matt Dipre Looker access) — sweep these before Ed asks "what's blocking finance" and the answer includes items assigned to you since April.
- Ed's provocations from Jun 24 not answered by this deck (park explicitly if raised): the company-wide intensive week, hiring bar ("no Copilot-only engineers"), firing implications, external speakers. The deck's line: benchmark first, then set the bar.

---

## Appendix — builder audit (2026-07-02, not for presentation)

Per-person artifact audit (8 dept agents, people files + transcript corroboration). Rubric: **builder = named, reusable artifact they created with AI (skill, dashboard, automation, MCP workflow, app, pipeline) in repeated use** — not one-off chats, guided builds, or using others' tools.

**Result: 25 of 49 verified builders (51%) · 10 assisted/decayed (20%) · 14 no build evidence (29%).**

Verified: Ismael, Jordi, David Z, Javier, Jacob, Chris, Rob, Stephen†, Mima, Ollie, Geran (Prodtech — Fergus, also Prodtech, stays BUILDER-ASSISTED, see below); Emily, Shreya (Ops); Christian‡, Kevin, Ivan, Kirsty†, David Pilley (Finance — re-scored to Stage 3 on Jul 2, dagger resolved); Adam Smith, Liam (Distribution); Francesco, Jake, Harry, Milan† (UW); Eraaz (People). († = builder-verified while scored Stage ≤2 — score understates them. ‡ = initially misclassified no-build by the audit; corrected 2026-07-02 — his co:work HTML budget artifact was shared to SLT/Antton and his distribution-cost workflow replaced the old flow as default; the Jun 11 source note had his identity unresolved, now fixed.)

The Stage 3+ proxy fails in both directions:
- **Too generous (4 no-build at Stage 3+):** Sam, Anna, Alex Dyball, **Darren McCauley** (Stage 3 rests on one uncorroborated observation; Jun 22 transcript: "pretty much a ChatGPT guy"). Plus 6 assisted-only at 3+: Matt Price, Tom Rogers (one-offs), Matt Lees (flagship decayed, Jun 24 manual-search regression), Sophie (template-based), Fergus and Ed (prototypes/demos, not tools in service).
- **Too strict (3 builders at Stage ≤2, was 4):** Stephen (Databricks monitoring system real but dormant), Kirsty (Looker MCP + pod-metrics skill still in use by Distribution), **Milan** (claims-triangle + UW-report skills, corroborated by Harry — his own file wrongly says "hasn't built anything independently"). David Pilley was the fourth; resolved by his Jul 2 re-score to Stage 3.

Structural conclusion: the stage axis conflates *how someone works* (fluency, delegation) with *what they've shipped*. Ed's Stage 3 wording literally says "builds tools", so either (a) enforce a named-artifact gate on Stage 3+ scores, or (b) track a separate builder badge (verified/assisted/none) in people-file frontmatter and report it as its own number. Recommend (b) — it preserves stage comparability and fixes the false positives without re-scoring everyone.

Corrections to feed back into people files: Milan (builder evidence), Darren McC (stage likely overstated), Stephen/Kirsty (builder-verified flags; David Pilley and Anneliese resolved by Jul 2 re-scores). Identity flag: some June engineering references to "Alex Dyball" are likely a different Alex (name-resolution conflation) — excluded from his audit.

## Appendix — provenance (not for presentation)

- **Source of truth:** `people/*.md` frontmatter (`ai_activation_stage/confidence/assessed`). 28 people re-assessed 2026-06-30 against Jun 22–30 transcripts (commit 8f627a3); others assessed Jun 2–25. Framework: [[activation-pathway]]. Prior snapshots: [[ai-activation-assessment-2026-06]] (Jun 18 — stages superseded, groupings retained), [[ai-capability-baseline-2026-04]].
- **Past-7-days check (2026-07-02):** three Granola meetings from Jun 29–30 were not in the vault; imported today ([[2026-06-29-moss-finance-rollout]], [[2026-06-30-david-pilley-moss-install]], [[2026-06-30-thomas-matthew-1-1]]). Their evidence was already reflected in the Jun 30 scores.
- **Verification:** per-person evidence audit (49 agents) against the transcript corpus; department syntheses; adversarial claims-vs-data check; completeness critique. Stats computed nearest-rank.
- **Jul 2 re-scores:** Anneliese 1→2 and David Pilley 1→3 after separating the Moss environment blocker (no Python, guided installs) from AI practice — the framework scores practice, not machine administration. David Pilley's Moss install completed Jun 30. Company min moved 1→2 as a result.
- **Known data-quality flags:** stale scores (Mima 05-26 with an unincorporated 06-24 transcript; Kevin, Matt Lees, Matt Dipre, Ben, Daisy 06-02); context-scoped downgrade still under review (Kirsty — same case shape as the two resolved on Jul 2); frontmatter/body disagreements (Geran 4 vs 3, Javier 3 vs "3–4", Aleks 2 vs "2–3"); Emily's cited source meeting not present in the vault; scope denominator 56 (assessment) vs ~63 (activation map, Jun 25).
