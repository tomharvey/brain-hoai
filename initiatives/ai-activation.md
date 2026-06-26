---
title: Company-wide AI Activation
created: 2026-06-02
updated: 2026-06-02
domain: ai-enablement
type: initiative
status: active
origin: directed
owner: tom
due: 2026-06-30
tags: [activation, enablement, company-wide, ceo-endorsed]
---

## Summary

Measure every person at Flock against the [[activation-pathway]] framework and move the majority across the activation threshold by end of June 2026. CEO-endorsed goal: 80% of Flock activated. The framework is already validated against a sample of ~13 people; the work now is completing the assessment and closing the gaps.

## Goal

> 80% of Flock crosses the activation threshold by 2026-06-30.
> — Ed (CEO), confirmed 2026-05-14

**Activation threshold**: complete 3 useful tasks in a context-fuelled Claude project. Oddly specific is intentional — it forces concrete action and rules out "I've tried it a few times."

## Relationship to other initiatives

- **[[ai-capability-uplift]]** is the delivery layer: workshops, 1:1 pairing, skills distribution, discovery. This initiative is the measurement layer — the framework that tracks whether the delivery is working.
- **[[ai-native-engineering]]** is where the stage framework was first articulated (developer context). The canonical definitions now live in [[activation-pathway]].

## Current state

**Framework**: validated. Stage 0–5 pathway defined, role-specific variants documented (developer, PM, ops, sales). Scoring convention in place (`ai_activation_stage` frontmatter + `## AI Activation` section in person files).

**Sample scored**: ~13 people across engineering, product, ops, finance, and leadership. See [[ai-activation-map]] for the full distribution.

| Stage | Count | People (selected) |
|---|---|---|
| 5 — Orchestration | 1 | Ishmael |
| 4 — Delegation | 20 | Jordi, Javier, Jacob, Stephen, Sam, Aleks, Chris, Rob, David Z · Mima, Ollie, Geran, Matt (product) · Emily, Shreya · Kirsty, Christian · Matt Lees, Adam Smith · Fergus |
| 3 — Fluency | 15 | Anna · Kevin, Ivan, Harry, David P · Alex D, Sophie, Liam · Jake, Darren M, Tom R · Eraaz, Rakhee, Phoebe · Ed |
| 2 — Context + tools | 11 | Jonny, Fred · Jade, Paul, Anneliese, Matt D, Milan, Michael · Adam Sandle, Ben, Daisy |
| 1 — First win | 1 | Queency |
| ? — Unassessed | 7 | Pavel · Antton · Darren N, Billy, Curtis, Andrew, Matt S |

**Not yet assessed**: Jacob, Sami, David Zamora, Geran, Anna, Shreya, Fred, Ivan, Kirsty, David P, Antton, Darren, Alex (engineer), Francesco, Milan, Chris, Eraaz, Paul, Jonny, Matt DiPré, and others.

## What needs to happen

1. **Complete the assessment** — score every remaining person; priority on those being actively worked with (workshop attendees, 1:1 pairing participants)
2. **Target the threshold crossers** — identify people at Stage 0–1 who are close enough to cross by June 30; design targeted interventions
3. **Validate framework gaps** — Stage 1 splitting (Queency pattern), non-dev Stage 5 definition (Emily pattern), confidence decay model
4. **Track progress** — update [[ai-activation-map]] as scores change; report against the 80% target

## Framework gaps to resolve

These surfaced in the first scoring pass and should be resolved before rolling out to all staff. Full detail in [[activation-pathway]] § Refinements.

- Stage 1 sub-stages (1a: first win; 1b: multiple use cases)
- Ops/non-dev Stage 5 definition — use Emily as the worked example
- Product domain vs personal practice distinction (Mima pattern)
- Data freshness model — how fast does a score decay?
- Stage 5 frontier description — involve Ishmael

## Key issues

| Issue | Topic |
|---|---|
| [[AI-047]] | Define activation threshold (criteria for "crossed") |
| [[AI-048]] | Plan group workshops (delivery mechanism) |
| [[AI-049]] | Ed in-person rollout session |
| [[AI-013]] | Capability baseline report (pre-condition for measuring progress) |

## Risks

- **Time**: June 30 is close. ~25+ people unassessed; workshops not yet fully scheduled.
- **Quality over coverage**: rushing assessments to hit 80% risks low-confidence scores that don't drive useful interventions. Score behaviour you've actually observed.
- **The "checkbox" trap**: the threshold metric (3 tasks in a project) can be gamed. What matters is whether people are genuinely changed — returning to AI habitually, not just completing an exercise.

## Log

### 2026-06-22–25 — Discovery week: 10 conversations, 6 stage movements

Highest-volume assessment week of the programme. Key movements confirmed:

- **Fergus**: Stage 3 → 4. Built full finance ledger service prototype overnight with Claude despite no prior production code in the codebase. Self-healing loop framing (agents auto-solve tickets; engineer reviews/approves PRs) confirms Stage 4 orientation.
- **Christian Leth Nielsen** (CFO): unassessed → Stage 4. SPA vendor obligations, GWP budget analysis, distribution cost analysis — all replacing old spreadsheet workflows. First leadership-tier Stage 4 outside Engineering.
- **Phoebe Woodman**: Stage 1 → 3. Flock O'Clock automation designed (spreadsheet → Claude → Slack → HTML slides); HTML deployed to Netlify; Claude Design discovered live on call; Alar daily briefings live.
- **Rakhee**: Stage 2 → 3. Granola-to-tracker pipeline live for entire People team, each member with a custom variant.
- **Eraaz Ali**: Stage 2 → 3 (approaching 4). OS-layer usage confirmed: rejection skill with relational guardrails, agency terms ranked + 3 emails sent directly from Claude, Alar calendar/feedback automation.
- **Liam Thomson**: confidence upgraded to high. Chrome MCP budget tracker live, Claude Design for high-stakes decks, full ChatGPT → Claude switch confirmed.

**Week pattern**: Stage 2 → 3 continues to be the most common movement, triggered by a concrete domain win (budget tracking, Flock O'Clock, Granola pipeline). Stage 3 → 4 requires autonomous delegation — Fergus's overnight prototype is the clearest new example. The Finance and People teams are now substantially activated; underwriting ICs remain the main gap.

**PGR skills decision**: decided NOT to roll out Francesco's Pace (over-engineered, 15-20 skills). Rakhee + Eraaz to build simpler prompt/co-work skill instead. Workshop for volunteers planned. Target: co-work project that tracks 1:1s and auto-populates next PGR prep. See [[AI-115]].

**Ivan Boix (Finance/Credit Control)**: confirmed Stage 3; exploring NetSuite MCP to eliminate manual XLS download step from daily priorities report. Month-end automation (bad debt provision, commission income journals) is the next horizon. Broker payment behaviour HTML dashboard live.

### 2026-06-15 — Ed mandate reinforced + benchmark ready

Ed came into an impromptu Rakhee/Phoebe 1:1 last week with the K-shaped diagram, enthusiastically reinforcing his AI mandate. Board has agreed Flock should be "AI first"; Admiral is looking to learn from Flock. Ed's estimate: 10% of Flockers on the upward curve — Tom disagrees, estimates ~30% based on observed data.

80% company activation benchmark is ready to share with Rakhee this week. Standalone AI survey to be rerun end of Q2 as a progress measure.

Key gap: Ed may not know the volume of work already happening (workshops more than weekly, squad-level, informal champions). Tom to send proactive comms to Ed this week rather than waiting for a Gina-arranged slot. → [[AI-113]], [[AI-114]]

Next quarter framing shift: from "just use AI" → "are you using it well?" — the go-use-it phase is largely done (80-90% of company at least at that point).

### 2026-06-12 — Underwriting activation strategy

Darren Nightingale identified as the number one cynic in the company. Engagement strategy is explicitly bottom-up: activate his ICs (Billy Bone, Curtis Bailey, Andrew Dodd, Matt Smith) before approaching Darren N directly. Jake Wood is the internal champion — already pushing AI to Billy and Curtis independently. When Darren N's own team is demonstrably using it, his ability to push back is structurally undermined. Do not approach Darren N until the IC layer is assessed and partially activated.

Priority conversations next week: Harry Dowrick (1:1 booked), Michael Matthews (1:1 booked), Ben Allen, Daisy Mae Baker, Billy Bone, Curtis Bailey. Group session (Jake as host) is the likely format for the underwriting ICs.

### 2026-05-26 — First scoring pass
Applied the framework to ~13 people across all departments. Surfaced 9 refinements. Distribution confirms the top of the company (Ishmael, Emily, Adam, Mima, Stephen) is well ahead; middle layer (ops, finance, distribution) is at Stage 1–3 with clear paths forward; leadership layer (Ed, Fergus, Matt) has high conceptual understanding but lagging practice.

### 2026-05-14 — CEO alignment
Ed set the 80% threshold goal directly in a 1:1. Framing: "complete 3 useful tasks in a context-fuelled Claude project." Tom is the enabler, not the centre of excellence. The programme scales through workshops and pairing, not 1:1 dependency on Tom. ([[2026-05-14-ed-tom-121]])
