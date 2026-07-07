---
title: Ed meeting prep — Q3 delivery plan + concrete deliverables (Wed 8 Jul, 13:00)
created: 2026-07-07
updated: 2026-07-07
domain: ai-enablement
type: reference
tags: [ed, q3, prep, deliverables, operationalisation]
---

# Ed <> Tom — Wed 8 Jul, 13:00 (1 hour)

**Ed's question from last week: "how do we operationalise this — who meets who, when, what targets?"** This is the hour that answers it. Two halves: the delivery machinery (HOW) and the concrete deliverables (WHAT). Draws on [[2026-07-02-ed-tom-q3-operationalisation]], [[2026-07-02-tom-eraaz-pgr-ai-pillar]], [[q3-slide8-operationalisation-map]].

> ⚠️ PLACEHOLDER — the second Eraaz conversation (post-Jul-2, "how he can help") is not yet imported; Granola needs re-auth. Merge its commitments into the People-team lane below once pulled.

---

## Opening 5 minutes — what's already moved since we spoke

- Deck updated with everything from the Jul 2 walkthrough: P80 labelling fixed, un-rounded floats, Pricing split out (the inverted-pyramid finding is NEW to Ed: Francesco/Harry ahead of Milan/Michael), claims folded into Ops, Kaylee scored (Stage 1, new starter framing).
- Baseline now n=50 of 57. Three at Stage 1 — one brand-new, two blocked, none unwilling.
- Eraaz engaged and building: PGR tooling session with Rakhee happened Mon Jul 6 — report the outcome (chase Eraaz before the meeting).

## Half 1 — HOW we deliver: the machinery (25 min)

**The three-lane operating model** (the pen-holder matrix from Eraaz):

| Lane | Owner | The mechanism |
|---|---|---|
| Strategy + initiatives | Tom | Team workshops (monthly), 1:1 boot list, deputies network, this baseline |
| Performance + talent | People team (Eraaz/Rakhee) | PGR "Growth" pillar (Q1 2027), tooling trial (Q3), JD/hiring screens, new-hire baseline |
| Team-level progression | Hiring managers + deputies | Fortnightly team demos, Slack what's-working reports to Tom |

**The deputies network — names, not a concept.** Propose formally asking: Jacob or David Z (Prodtech eng), Mima or Ollie (Prodtech product), Shreya (Ops), Ivan (Finance — evidence-led choice; Christian as exec sponsor), Jake (Underwriting), Francesco (Pricing), Adam Smith or Matt Lees (BDM), Eraaz (People). Mechanics per Ed's own framing: fortnightly half-hour team demo + Slack channel reporting to Tom — covering what's working, what's not, **quality problems observed, and issues/improvements their team should be floating but isn't**. **Ask Ed: does he want to bless the names or have managers nominate?**

**The cadence:**
- Weekly: Tom 1:1s (boot list: Kaylee, Adam Sandle, Connie re-onboarding)
- Fortnightly: deputy demos per team; deputy Slack reports
- Monthly: team workshops (finance + UW get doubled frequency); AI Breakfast with deputy-fed agenda
- Quarterly: re-score against baseline (PGR tooling makes this a byproduct, not a project)

**The two focus teams — different interventions:**
- Finance = infrastructure-gated → Moss rollout finishing (AI-148/149), NetSuite MCP, weekly workshops. Evidence it works: David Pilley 1→3 once unblocked.
- Underwriting = propagation-gated → Jake-led peer rollout to Andrew/Curtis/Billy/Matt Smith as they return; Darren Nightingale deliberately last.
- NEW since the deck: Pricing needs a third intervention — downward propagation (ICs coach their heads of function).

## Half 2 — WHAT the concrete deliverables are (25 min)

**By end of Q3, Ed can hold us to:**

1. **The number: 100% of scored people at Stage 3+, majority (>50%) at Stage 4.** Baseline today: 64% at 3+, 26% at 4. Gap = 18 people below Stage 3, all named, each with an owner and intervention. NOT a company OKR — Ed/Tom/Rakhee initiative.
2. **Stage 5 exists and has a demo.** Prodtech pushed into orchestration ("gardening agents, not producing code") during London week; **CEO demo of Stage 5 in practice** (AI-153) — candidate: adherence-measured multi-agent workflow on J or finance tickets. Ed asked for this explicitly.
3. **Full coverage: 57 of 57 scored.** The 7 unscored have named routes: 4 UW ICs via Jake on return, Pavel via finance workshops, Antton via discovery 1:1, Ben/Daisy via calendar-forced 1:1s.
4. **The benchmarking survey shipped** (AI-125, with Rakhee — Ed committed it to Admiral Pioneer). 60-second survey, AI-delivered, results visualised; validates/corrects the conversation-based baseline.
5. **PGR tooling trial live with a named opt-in cohort** (AI-156): Granola+JD+deliverables → Claude-scored matrix. Framing locked: opt-in commitment, not "trial"; nobody marked down; formal "Growth" pillar Q1 2027 (acquisition bonus constraint).
6. **Deputies network live** (AI-127): named deputies, first fortnightly demos done, Slack channel running.
7. **Every "at-risk" person has a dated intervention** — the four groups (blocked/unmeasured/pulled-back/habit-not-formed) each get their own treatment; a single "level up" message misfires on three of the four.

**The open problem to put on the table (don't hide it):** structured measurement of *additionality* — "what got done that would never have been done." Examples exist (login bug, BDM research, Michael's pricing research); the measurement isn't designed. Proposal: deputies collect additionality stories fortnightly; AI evaluates/synthesises them; quarterly narrative to SLT. Ask Ed if that's sufficient rigour for Admiral Pioneer or if he wants a harder metric.

**Quality ownership (slide-8 item 5 — now owned):** Tom + [[kirsty|Kirsty]] + [[jacob-holland|Jacob]] own "the numbers people ship are validated." Tom sets the guardrail patterns (calculations stay in Looker/auditable systems; Claude surfaces insight); Kirsty carries them into Finance/data workflows (Looker MCP + pod-metrics owner, mid-Moss rollout); Jacob carries them into Prodtech (DBT golden rules Claude-enforced, push-to-main guardrail — already builds exactly this). Deputies have a hard requirement in this loop, not a courtesy role: they must **feed back quality problems** from their team and **ensure people are floating issues and improvements** rather than sitting on them (the norm from the Jun 29 Moss call: "ping when you hit data query issues" — that behaviour, made every deputy's job). The trio owns fix-and-standardise; deputies own detection-and-escalation. A quality incident that never reached the trio is a deputy-lane failure, not a trio failure.

## Hiring — Rob Grice's AI-first engineering interview (5 min, inside Half 2)

Rob has been working on what an AI-first engineering interview looks like (now tracked: [[ai-first-hiring]]). This answers Ed's Jun 24 hiring bar ("if an engineer says they use Copilot and have never used Claude or Cursor, don't hire them") with something better than a screening question — an interview where AI use IS the assessment surface.

**Why it lands with Ed:** the current format treats AI as cheating — a candidate was literally "caught using AI live during interview" this June (Jun 11 Jordi weekly) and it counted against them. Rob's format inverts that: watch how a candidate dresses the model, argues with output, and reviews what comes back. That's the capability framework applied at the front door. Bonus narrative: the early-career engineer who worried about AI brain-rot is the one designing the assessment.

**How we expand it (the plan to put to Ed):**
1. Rob documents the format as a reusable artifact — interview structure, task bank, scoring rubric mapped to framework stages (candidates get a provisional stage, feeding AI-128 new-hire assessment directly).
2. Trial it live: the senior engineering lead search is running NOW (two recruiters engaged since June) — pilot on real candidates this quarter, calibrate against the hiring managers' reads.
3. Port beyond engineering with Eraaz: he already asks AI questions "in every single screening"; Rob's format gives those questions teeth. Eraaz adapts per function with hiring managers (ties to AI-155 JD work — assess what the JD now advertises).
4. Close the loop at onboarding: interview stage-read becomes the new joiner's baseline score (AI-115) — coverage never degrades as the company grows, and Kaylee-style "personal use, no work practice" starters get spotted on day one.

**Ask Rob first** (London, this week — he's already on the AI-150 push): does he want to own this as his named Q3 artifact? It's his strongest builder evidence yet and a better story than "hand-finishes code".

## Firing — take it head-on, don't park it (10 min, after deliverables)

Ed's Jun 24 position: "start firing people if they're not the right place on the framework and don't level up… meritocracy everywhere… the best people survive and thrive." He wanted it rolled out "in a week". We've deferred twice; tomorrow, engage it properly.

**The position to take in the room:** consequences are legitimate — but only on a measurement system that would survive being challenged by the person being fired. Today's baseline can't carry that weight, and saying so is what makes the rest of the plan credible:

- Scores are conversation-derived, several low-confidence (Ben, Daisy scored on inference only), some contested in-file (Geran 4-vs-3), and the framework's own rule is "low confidence = gather more data before acting".
- The at-risk list decomposes to blocked / unmeasured / pulled-back / habit-not-formed — nobody currently at the bottom is *refusing*. Firing anyone on today's list would be firing someone we failed to unblock (Anneliese's Python install) or never measured (Ben, Daisy).
- The same acquisition retention-bonus constraint that delayed the PGR pillar applies to consequence-bearing changes generally — Eraaz flagged it; changing the rules mid-retention-period reads badly.

**The sequence to propose:** Q3 = measurement becomes defensible (survey + full 57/57 coverage + PGR tooling trial + one re-score cycle) and every at-risk person gets a dated, resourced intervention. Q4 = the honest fork: anyone still below bar *after a real offer of help* is having a performance conversation — with Rakhee running it as performance management, not an AI purge. Hiring bar (Rob's interview) starts NOW, so the front door tightens before the exit does.

**Where to agree with Ed enthusiastically:** promotion side first — the champions table is the shortlist, Mima was his own example. Recognition before consequences builds the meritocracy story he wants without a fear phase; fear drives usage-theatre, which corrupts the additionality measurement we're trying to build.

## Decisions to extract from Ed (write these down in the meeting)

1. Deputy names — bless the list or manager-nominated?
2. Target ratification: 100% @ 3+ / majority @ 4 — is that the number he presents to Admiral Pioneer?
3. Additionality: is story-collection + AI synthesis enough, or does he want a harder metric?
4. Quality ownership = Tom + Kirsty + Jacob (deputies required to escalate) — approve?
5. Hiring: green-light Rob's AI-first interview pilot on the live senior-eng-lead search + Eraaz port to other functions?
6. Firing: agree the sequence — Q3 defensible measurement + interventions, Q4 performance conversations via Rakhee; promotions start now?
7. Intensive company week — park explicitly or schedule.
8. What does HE show Admiral Pioneer, and when? (Shapes how polished the survey/deck must be.)

## Logistics / prep before 13:00

- [ ] Pull the second Eraaz transcript once Granola re-authed; merge his commitments into the People lane and delete the placeholder above.
- [ ] Chase Eraaz for the Mon Jul 6 PGR-build outcome (with Rakhee) — it's the freshest evidence the machinery works.
- [ ] Apply the two open deck edits before the meeting: slide-8 targets on the slide (AI-152/154) + drop "Ghostbusters" label.
- [ ] The 11:00 AI Finance workshop and 12:00 Ops sync that morning are live evidence — carry one fresh example from each into the 13:00.
- [ ] Send Eraaz the slides first (promised Jul 2, AI-154) if not yet done.
- [ ] Grab Rob before the 13:00 (he's in London this week): confirm he'll own the AI-first interview artifact and is happy being named to Ed.
