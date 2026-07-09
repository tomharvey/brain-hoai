---
title: Digital Futures — Athena AI demo
created: 2026-07-09
updated: 2026-07-09
domain: ai-enablement
type: meeting
tags: [digital-futures, athena, benchmarking, vendors, admiral, assurance]
---

# Digital Futures — Athena AI demo

**Date:** Thu 9 Jul 2026, ~11:15–12:45, Digital Futures office (Turing room)
**Attendees:** [[ed|Ed]], Tom Harvey (Flock); Jack Nightingale (Digital Futures, commercial), Scott Vincent (Digital Futures, founder & CEO)
**Prep:** [[digital-futures-meeting-prep-2026-07-09]] · **Transcript:** [[2026-07-09-digital-futures-athena-demo-transcript]]

> Note: Jack Nightingale (vendor) is no relation to Darren Nightingale (Flock UW).

## What Athena actually is (as demoed, vs the marketing)

Marketing says four layers (diagnostic / knowledge / assurance / intelligence). What was demoed is a **persona-based assessment + micro-learning platform with dashboards**, organised around four personas: Apply (everyone), Build (engineers), Lead (leaders), Assurance (control functions — still being built out). Demo was the Apply persona.

- **Self-assessment entry**: confidence ratings per persona skill (Apply = data literacy, prompt engineering, AI collaboration, solution design, insights generation) + free-text strengths/development areas + "what AI tools do you use at work" — deliberately surfaces shadow AI (people admitting to ChatGPT on personal phones). Agents, not humans, process the inputs.
- **Scenario assessment** (their "secret sauce"): 4 scenarios × 6–8 questions, ~45–60 min for Apply. Situational-judgement style — drag-and-drop prioritisation with free-text rationale, fire/solution matching, prompt completion — marked by a dynamic rubric in the backend. Explicitly designed to test *thinking before prompting*. Scenarios customisable per client/industry/level ("we can customize to any extent"), with out-of-the-box defaults; difficulty adapts to the learner. Deliberately not tied to any tool or model stack.
- **Skills fingerprint** → personalised learning plan of 5–7 minute exercises (pilot data: people do them during the working day). In-platform AI tutor with "highlight for clarification". A **content engine** (shared with their Frontier academy) keeps content current; they're debating leaning more on Anthropic-related content given an emerging Anthropic relationship.
- **Reflection diary** before reassessment captures impact stories and environmental blockers — this is where value evidence comes from (e.g. a bank turned a 4-day, 300-page contract review into hours; ~700 hours saved across a 50-person pilot).
- **Manager/enterprise dashboards**: individual deep-dives (cognitive approach, behavioural patterns, risk profile, strengths + how to deploy them), met/partially-met/not-met transparency per skill; enterprise "god view" of fluency vs adoption curves, department drill-down, suggested actions (e.g. adoption declining post-tool-launch). Can ingest adoption data (e.g. Anthropic insights API); token spend / cost-per-employee flagged as a data point they want to add.
- **Assurance persona**: maps the org's AI model inventory to departments, then assesses whether the people overseeing each model have the literacy to do so; maps skills to regulatory frameworks (EU AI Act Article 4 etc.) down to article level; builds audit-grade attestations for regulator engagement. Their strategic wedge — "moves spend from discretionary to mandatory". Customer-led: enterprises asked for compliance evidence.
- **Commercial thesis**: fluency → adoption → value (margin expansion) + assurance (risk reduction). Athena is also a trojan horse for their forward-deployed-engineer services model — ~90% of their ~20 current pursuits are Athena-led.

## Answers to the prep questions

| Prep question | What we got |
|---|---|
| **1. Benchmark pool size/sectors** | **Not answered.** No numbers on how many orgs are in the pool or sectors. Closest: cohort averages within a client, and the argument that "one consistent assessment methodology gives a level playing field for comparison". The one thing we came for was not evidenced. |
| **2. Can it ingest our six-stage framework?** | Partially. Scott's stated preference is the reverse of ours: Athena ingests clients' "simple metrics" (completion stats etc.) to complement *their* richer data, rather than mapping onto an external rubric. But: "there's no reason why, if you want some of these other signals as part of our model, it'll be very simple to bring the two together." No explicit yes to mapping their levels onto our stages. He did note (fairly) that Tom's measurement approach "doesn't scale beyond a ~70-person company". |
| **3. Self-report vs behaviour** | **Neither survey nor observed real work — it's simulated behaviour.** Self-assessment is confidence-based, but scoring comes from the scenario assessment (situational judgement + free-text rationale, rubric-marked). Better than pure self-report; still not artifacts-in-production evidence like ours. Tom's in-room note: the design builds the *challenge-the-AI-answer* behaviour, which is good. |
| **4. Ceiling — tool builders?** | Confirmed low ceiling. Asked directly how often assessees are at the tool-building level: "there's not loads of people at that level… almost nobody is really doing that in regulated clients because they're just not allowed to." They capture such people via the reflection diary rather than the rubric. Tom's in-room note: nobody in their world is reaching the tool-building stage; competing platforms aren't incentivised to get people to the fluency level we aim for. Our Stage 3–5 people are beyond their assessed range. |
| **5. Adoption signals** | Real telemetry, not just course completions: they ingest enterprise adoption data (Anthropic insights API and others) and set it against proficiency; shadow-AI self-reports get reconciled against the enterprise dataset (Tom pushed on this; Jack confirmed "all of those gaps straight away"). Token spend/cost-per-employee is roadmap. |
| **6. Generic vs our-workflows content** | Scenarios customisable to any extent, but the learning layer is generic micro-exercises (e.g. CO-STAR prompting framework) — classroom/lab-practical, not in-workflow coached reps on Flock systems. |
| **7. Content currency** | "Content engine" continuously scanning tech + regulatory developments; no specifics on what shipped in the last 60 days. Possible Anthropic-flavoured content direction. |
| **8. Assurance for an Admiral entity / FS references** | Assurance persona demoed and it maps cleanly to Flock (Tom tested: org-specific model inventory incl. pricing-team models → relevant functions get relevant rubrics — "we would feed that inventory in"). References: an unnamed bank (200k employees, 50-person pilot) and unnamed regulated enterprises; **no FS/insurance client of our size offered**. |
| **9. Pricing / smallest engagement** | **No pricing given.** Smallest engagement confirmed as: identify a cohort, run the baseline assessment (no customisation needed, ~1 hour per person), use insights to decide next steps. Buyers vary — P&L owners, MDs, engineering, shared services, L&D; often sold department-by-department in large orgs; value-based deals only work at C-suite. Economic model still being debated internally (Ed fed them the MuleSoft "cost of not buying" playbook). |

## Ed's reactions

- Effusive: "one of the best products I've seen in such a long time… so well thought out… it's not going fucking anywhere." Called it mind-blowing at the close.
- Bought the assurance/regulatory wedge instantly ("moves spend from discretionary to mandatory… such a good wedge") and riffed on lock-in: win an Admiral now and they never switch audit/HR-integration partners.
- Spent much of the meeting **advising their GTM** rather than evaluating for Flock: MuleSoft cost-of-not-buying playbook, Coalition-style insurance distribution (cyber insurers as Athena distributors, subsidised by claims savings — "the black box you put in the car"), AIUC parallel (founded by Rune, ex-Anthropic safety lead; quantified risk framework + insurance for agentic deployment).
- Floated a second Flock use case: could Athena's ontology assess **product-level** AI safety/compliance for J (prompt-injection testing at scale, EU AI Act conformity)? Scott: "not in its current guise, but a very interesting angle" — ontology transferable, would need agents connecting the two.
- Leaned toward Flock as a **willing pilot / entry point** for a broader Admiral adoption — with the explicit attraction that "we can actually roll this out and test it and get Admiral to pay for it". No commitment to buy anything directly.
- Redirected their Admiral pursuit: current contacts Russell (partnerships, right energy but wrong level) and Katie (junior people role, presenting a proposal to the Pioneer board imminently) are too junior. Right targets: **Milena** (deploying hundreds of millions into gen AI, all-in) and **Emma** (CEO of Admiral Pioneer, Russell's boss's boss). Path: pilot with Admiral Pioneer, then roll out to Admiral Group.

## Commitments and next steps

| Action | Owner | Notes |
|---|---|---|
| Facilitate introduction to Milena and Emma at Admiral | Ed | "I will just do my absolute best"; DF to keep their existing track running in parallel |
| Share the Admiral proposal details + stakeholder map with Ed | Scott / Jack | So Ed can help navigate the org |
| Intro Digital Futures to AIUC | Ed | Offered ("I can make an intro"); relevant to their assurance persona + insurance distribution angle |
| Catch up with Katie re her Pioneer board proposal | Digital Futures | Timing unclear in transcript |

**Not committed / still open for us:** the actual buying-intent items — benchmark pool evidence, rubric mapping onto our six stages, pricing, and a diagnostic-only pilot against our baseline — none were pinned down. If we pursue, the next concrete ask is a baseline assessment on a Flock cohort (their own stated smallest engagement) plus benchmark-pool numbers in writing.

## Unresolved names (transcript)

- "souki" — Digital Futures person running their ~20 pursuits; spelling unknown
- "Milena" — Admiral gen-AI exec (transcribed as "millena"/"millennial"/"my lac"); surname unknown
- Russell, Katie, Emma — Admiral / Admiral Pioneer contacts, no people files (external)
