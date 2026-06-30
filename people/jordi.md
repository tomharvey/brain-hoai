---
title: Jordi Pallares Roset
created: 2026-03-27
updated: 2026-06-30
type: person
role: Head of Engineering
team: Engineering
email: jordi.pallaresroset@flockcover.com
tags: [engineering, leadership, ai-discovery]
ai_activation_stage: 3
ai_activation_confidence: medium
ai_activation_assessed: 2026-06-30
---

## Role

Head of Engineering

## Team

Engineering

## Relationship

Replaced Tom after his time as interim Head of Engineering — handed over as a permanent role. Key coordination partner for Head of AI role.

## Working style notes

- Observed the OKR session and underwriting/distribution team dynamics
- Blog post work that Abs was contributing to
- Strategy: stays close to business side, asks about AI needs, discovers opportunities
- Coordination model with Tom: Jordi discovers, Tom supports complex implementations — "when you run into something you don't have time for, see me as a resource"
- Self-started AI projects: Engine Room triage automation (Lambda + Bedrock), renewal automation with [[anna|Anna]]
- Practical builder — will spin up a Lambda MVP to validate an idea before asking for resources

## AI Activation
**Stage**: 3 — Tool building
**Confidence**: medium
**Assessed**: 2026-06-30
**Evidence**: Self-started cron job that checks repo vulnerabilities and auto-raises PRs (personal repos); Engine Room triage automation (Lambda + Bedrock); renewal automation with Anna; architectural thinking with Claude before delegating implementation; `CLAUDE.md` updated per task; records team calls as transcripts for agent context. Jun 11: presented at InsurTech conference about AI — market sees Flock as ahead. Installing Moss MCP for finance team. Jun 2: discussing finance system architecture — debating whether to build platform screens vs just use Claude. Interested in Stripe's AI capabilities (MCP, product catalog via prompt). Thinks about data quality challenges for AI in finance. Agrees Flock should be more aggressive with AI in product.

**Not Stage 2**: Beyond just connecting tools — has built automations (Engine Room triage, vulnerability cron job) and thinks architecturally about AI integration. Installing MCPs for other teams (Moss for finance).
**Not Stage 4**: June evidence positions Jordi more as a leader/enabler than a daily builder of autonomous systems. The cron job and triage automation are individual pipelines, not delegated agentic workflows. Primary mode is architectural thinking and enabling others, not personal delegation at scale.
**To progress**: Move from enabling others and individual automations to running delegated agentic workflows personally. The finance system architecture decision (platform screens vs Claude) is a natural on-ramp — if he builds and delegates it, that's Stage 4.
**Framework note**: Stage revised down from 4 to 3 based on June reassessment. Prior assessment weighted the automation builds heavily, but Jordi's primary mode is leadership/enablement — discovering opportunities, installing MCPs for teams, presenting externally — rather than daily agentic delegation. The automations are real but represent peak capability, not sustained practice.

## 1:1 Log

### 2026-03-30 — Head of AI x Engineering

- Agreed coordination model: Jordi discovers business AI opportunities, Tom supports complex implementations
- Weekly 1:1 scheduled for **Fridays**
- Sam: redirect to evals + documentation for Q2; Jordi setting goals with him Thursday
- Engine Room triage: Jordi building Lambda + Bedrock MVP, very early stage
- Renewal automation with Anna: blocked by Google MCP needing local hosting — Tom reviewing tomorrow
- WhatsApp bot ([[ollie-crowe|Ollie Crowe]]): deployed to render.com, not customer-facing, testing with fleets next
- Skills: need public vs private governance, testing standards before company-wide sharing
- Insights database: Tom framing 3-month vision for extracting insight from previously unanalysable data
- "Other Tom" interested in automating things — catch-up in ~2 weeks

### 2026-05-12 — Weekly 1:1
- [[2026-05-12-jordi-weekly]]
- FinOps wish list review: Jade's document is a year's worth of work. Tom to reframe with Jade — Q3 is about pressure-release, not boiling the ocean. Geran's concern: "fish vs teaching to fish."
- Finance team is too busy to invest in shortcuts — diagnosis confirmed by Ivan's situation (personal fire drove adoption; once under control, flourished).
- J product traffic/retention concerns: need to avoid end of quarter where everyone loves J but Anton asks "what did it do for retention numbers?"
- Incident management process: Jordi to draft. → [[AI-076]]
- Shared engineering harness (super-repo concept): discussed "AI prison" risk vs "tragedy of commons" — need the right onboarding so people find it useful, not constraining.

### 2026-04-16 — Underwriting AI conversation (with Tom Rogers)

- Joint session with Tom Rogers on underwriting and AI
- See: [[2026-04-16-tom-rogers-underwriting-ai]]

### 2026-05-26 — Weekly 1:1

- Alex (engineer) raised AI job security concerns citing Facebook layoffs → Tom's counter: unrelated business reasons, Anthropic hiring at $500k contradicts it. Plan: targeted 1:1s + curated team sessions. → [[AI-062]]
- Activation pathway formalisation discussed: 5-stage framework, Stage 3–4 target for most, Stage 5 for exceptions. Agent babysitter reframe unclear where it threads in — Rob already showing harness-engineering instincts at Stage 3.
- Admiral Business data point: common pathway to success confirmed across their 5-engineer team.
- Incident management process: Fergus raised uptick over 4–5 weeks. Jordi building lightweight process. → [[AI-061]]
- Insurance Tech conference Thursday — "embedded insurance at scale" panel. Preparing Flock positioning.
- Cardiff visit uncertain: Tom passport renewal + 5-year NIE residency renewal. Town hall provides limited value vs tactical days.
- Tom using Super Whisper for voice→Claude. Jordi finds Claude voice mode poor; uses ChatGPT's voice-note-to-text instead.
- Factorial CEO podcast (Factorial = Barcelona HR SaaS unicorn, Microsoft/Satya Nadella event) — Jordi to share.
- See [[2026-05-26-jordi-weekly]]

### 2026-04-20 — Weekly Kickoff (referenced)

- KR2 kickoff with Adam, Tom, Darren — trading evolution, connectivity chicken/egg
- Haulage fact find needed — Liam doesn't have current version, may need restart

### 2026-06-30 — June assessment update

- Jun 11: presented at InsurTech conference about AI — did very well, market sees Flock as ahead
- Installing Moss MCP for finance team
- Hiring freelance engineers
- Jun 2: discussing finance system architecture — debating whether to build platform screens vs just use Claude
- Interested in Stripe's AI capabilities (MCP, product catalog via prompt)
- Thinks about data quality challenges for AI in finance
- Agrees Flock should be more aggressive with AI in product
- Stage revised from 4 to 3 — primary mode is leader/enabler rather than daily builder of autonomous systems
