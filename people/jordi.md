---
title: Jordi Pallares Roset
created: 2026-03-27
updated: 2026-06-02
type: person
role: Head of Engineering
team: Engineering
email: jordi.pallaresroset@flockcover.com
tags: [engineering, leadership, ai-discovery]
ai_activation_stage: 4
ai_activation_confidence: medium
ai_activation_assessed: 2026-05-26
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
**Stage**: 4 — Multi-agent orchestration  
**Confidence**: medium  
**Assessed**: 2026-05-26  
**Evidence**: Self-started cron job that checks repo vulnerabilities and auto-raises PRs (personal repos, moving to Flock platform); Engine Room triage automation (Lambda + Bedrock); renewal automation with Anna; architectural thinking with Claude before delegating implementation; `CLAUDE.md` updated per task; records team calls as transcripts for agent context. Coordination model with Tom: discovers, Tom supports complex implementations.

**Not Stage 3**: Self-started multiple production automations without prompting. Architectural thinking with Claude before delegating implementation — not one-shotting, but pre-thinking with Claude then handing off. Updates `CLAUDE.md` per task and uses call transcripts as context — systematic context engineering, not ad hoc loading.  
**Not Stage 5**: Automations are individual pipelines, not orchestrated multi-agent systems. No evidence of adherence measurement or the engineering problems of the new paradigm (persuasion tools, adherence spectrum). Sophistication is in the volume and quality of individual builds, not in orchestrating them together.  
**To progress**: Move from individual automation projects to multi-agent coordination — connect the pipelines. Start measuring whether the `CLAUDE.md` updates are actually improving agent adherence, rather than updating by feel.

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
