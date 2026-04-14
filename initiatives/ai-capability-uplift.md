---
title: AI capability uplift programme
created: 2026-03-30
updated: 2026-04-12
domain: ai-enablement
type: initiative
status: active
origin: directed
owner: tom
tags: [capability, training, culture, company-wide]
---

## Summary

Company-wide programme to build AI capability so that "everyone is their own Head of AI." Not just training sessions — systematic capability building across all departments so AI usage grows independently of a dedicated role.

## Goal

Every department uses AI tools confidently and independently. People design processes with AI in mind. The Head of AI role makes itself redundant by building self-sustaining capability.

## Current state

- **Ops (Emily's team)**: already self-sufficient — daily AI usage, Zapier automation, process-first thinking. Monthly AI/Automations sync running. This is the model to replicate.
- **Engineering**: mixed. Some power users (Abs, Chris, Mima), some sceptical. Skills sessions started (session 1 delivered 2026-03-27). Code quality concerns with AI-generated output.
- **Product**: PMs shifting to Cursor/Claude as IDE. Matt and Mima leading. Output quality is the gap.
- **Distribution**: Adam's team needs ready-made toolkit, not "go explore." Kirsty is the power user anchor — team needs to book sessions with her.
- **Finance**: Kirsty is a standout — Looker→Claude MCP, AI-generated insights, self-started. Christian, Kevin, David trialling. Jade conversation done (2026-04-07).
- **Underwriting**: Fred (ops) early-stage but receptive. Attended prompting workshops. Darren's team not yet spoken to.
- Claude desktop being installed company-wide by IT.

## Dependencies

- [[claude-standardisation]] — need a single tool to build capability around
- [[skills-distribution]] — skills are the scaling mechanism
- Discovery round completing — can't design the programme without knowing each team's baseline
- Emily's monthly AI/Automations sync as a template for other departments

## Risks

- People see AI demos and think "magic" rather than "I can do that" — Fergus flagged this
- Training without follow-up = forgotten within a week
- Different departments at wildly different starting points — one-size-fits-all won't work

## Workshop delivery strategy

Three-layer approach agreed at AI Workshops steering group ([[2026-04-10-ai-workshops]]):

1. **Company-wide workshops** — Oli leading Claude Co-Work + MCP connectors session. Target: April 23rd town hall (Rakhee checking slot availability).
2. **Department workshops** — Two-part: discovery session → digest → implementation/training. Finance or People team first, late April/early May.
3. **1:1 pairing** — Tom continues individual sessions. Most effective for hesitant/unsure people.

Key principle: **confidence before automation**. Getting people to feel like Kirsty (confident, showing their work) matters more right now than automating the "right" things.

### What already exists

| What | Owner | Status |
|---|---|---|
| Beginner prompting workshops | Unknown | Delivered. Well-received but beginner-only |
| Skills AI session 1 | Tom | Delivered 2026-03-27 |
| AI Breakfast (weekly) | Ollie | Running — sharing tools, demos, best practices |
| Business continuity workshop | Sam + Paul | Parked for later Q2 |
| Emily's Monthly AI/Automations sync | Emily | Running — ops team reference model |
| Jordi's EM+PM leadership workshop | Jordi | Proposed ([[2026-03-26-fergus-hoai-001]]) |

### Adoption blockers

- Distribution team (Alex, Sophie) can't attend existing workshops due to broker meeting conflicts
- No underwriter has attended AI Breakfast
- Mima's presentation skill communicated many times but still unknown to some — only 3 users
- Saturation of the willing: people who were going to come have come. Focus shifts to the persuadable middle (open but confused — Anna, Shreya, Fred, Sophie)

## Next actions

- [ ] Complete discovery round to understand each department's baseline
- [ ] **Produce AI capability baseline report** — department-by-department snapshot of current AI maturity, tool usage, blockers, and readiness. Serves as: (1) measurable starting point to track progress, (2) foundation for the uplift strategy. → AI-013
- [ ] Document Emily's ops team as the reference model
- [ ] Design department-specific onboarding paths (not one-size-fits-all)
- [ ] Work with Adam to define a distribution-specific AI toolkit — ready-made skills for slide decks, broker prioritisation, data interrogation. Keep lightweight for now. (from [[2026-04-02-adam-ai-discovery]])
- [ ] Explore "teach the agent your job" framing as capability-building tool
- [ ] Rakhee to confirm April 23rd town hall slot for Oli's Co-Work/MCP workshop (from [[2026-04-10-ai-workshops]])
- [ ] Oli to prepare Claude Co-Work + connectors workshop and drop dates in the group channel (from [[2026-04-10-ai-workshops]])
- [ ] Plan first department workshop — Finance or People team, late April/early May (from [[2026-04-10-ai-workshops]])
- [ ] Work out how 1:1 pairing sessions feed into department workshops (from [[2026-04-10-ai-workshops]])

## Log

### 2026-03-30

- Created from pitch document review
- Emily's team identified as reference model — daily usage, process-first thinking
- Skills session 1 delivered to cross-functional group (2026-03-27)
- **Sam's AI CoP pitch** ([[2026-03-30-sam-ai-cop]]): full operational model with 4 streams (Workshops, Processes, Products, Policy) and 8-week delivery cycles. Tom and Jordi pushed back — too ambitious, company doesn't respond to big-hit approaches. Agreed to strip back to single initiative (documentation pipeline). Sam to show value first, then expand. Redirecting Sam to evals + documentation for Q2 — tighter scope, measurable goals. Jordi setting Q2 goals with Sam Thursday.
- **Adam discovery**: Distribution team needs a different uplift model — ready-made toolkit, not "go explore." Sophie, Alex, and new hire need structured tools; Matt and Ollie need freedom. Adam's "selfish with AI" framing = use it for efficiency, don't build models. Kirsty's Looker MCP already a win — team needs to book sessions with her.
- **Matt Lees' Enterprise Engine**: strongest capability uplift case study. Self-described "layman" built a 9-agent pipeline managing £294M in 5 days. Board story: if a non-technical Enterprise Fleet Lead can do this, what's the ceiling when you give the whole company structured tools and support? Spectrum runs from Sophie (needs a toolkit) to Matt Lees (needs freedom + governance).

### 2026-04-08

- **Fred discovery**: Baseline established. Early-stage user, attended beginner prompting workshops. Key learning: "have a conversation with it" vs one-shotting. Previous employer actively discouraged AI — complete culture shift at Flock. Open and willing, needs direction not convincing. Emily is the right lever for pushing his team further.

### 2026-04-12

- Incorporated workshop delivery strategy from AI Workshops steering group ([[2026-04-10-ai-workshops]]). Three-layer approach: company-wide (Oli), department-specific (Finance/People first), 1:1 pairing (Tom). Consensus: confidence before automation.
- Added Jordi's proposed EM+PM leadership workshop from Fergus conversation ([[2026-03-26-fergus-hoai-001]]).
- Documented adoption blockers: distribution scheduling conflicts, underwriting no-shows, skill awareness gaps, saturation of the willing.

### 2026-04-09

- **Kirsty discovery**: Finance team's capability is higher than expected. Kirsty is a power user exemplar — self-started Looker→Claude MCP, producing AI-generated insights that change business decisions. Christian, Kevin, David trialling locally. Multiple business users requesting access. The spectrum now runs: Fred (needs enablement) → average user (needs toolkit) → Kirsty/Matt Lees (needs infrastructure + freedom).
