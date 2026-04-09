---
title: "AI Workshops — meeting prep"
created: 2026-04-09
updated: 2026-04-09
domain: ai-enablement
type: meeting
tags: [workshops, prep, capability-uplift, cop]
---

## Meeting details

- **Title**: AI Workshops
- **Time**: 12:30 CET / 11:30 UK, 30 min
- **Organiser**: Rakhee Gohil (Senior People Business Partner)
- **Description**: "Regroup on everything AI — changes and new ideas, align to maximise efficient use of everyone's time"
- **Likely trigger**: You becoming Head of AI. Rakhee is People — she probably sees the new role as the moment to formalise what was previously informal.

## The room

| Person | Role | What they bring |
|---|---|---|
| **Rakhee Gohil** | Sr People BP | Coordinating people/comms side. Wants a structured plan she can communicate company-wide |
| **Fergus Doyle** | Interim CPTO | Your boss. Wants board-level AI story. Warned about "magic" thinking from demos |
| **Jordi Pallares Roset** | Head of Eng | Already aligned with you on "start small". Key coordination partner |
| **Jemima (Mima)** | PM | AI skills champion (deck builder skill). Pushed back on Sam's CoP: "we're already doing this" |
| **Sam Adeniyi** | Staff Eng | Pitched the 4-stream AI CoP on Mar 30 — you and Jordi narrowed him to docs + evals only |
| **Ollie Crowe** | Tech PM | Runs the weekly AI Breakfast. Self-starter (WhatsApp bot) |
| **Abdul (Abs)** | Engineer | AI pioneer (CC extraction). Leaving soon — knowledge transfer risk |

## Posture

This is not a defensive meeting. Rakhee is likely asking you to own the workshop strategy. Go in as the person with the mandate and the cross-company picture.

**Don't**: present a framework on a whiteboard, or get pulled into designing a workshop schedule on the spot.

**Do**: show you've done the legwork, share what the discovery round is revealing, and ask for input on gaps.

## Background: Sam's CoP pitch (Mar 30)

Sam presented a full AI Community of Practice to you and Jordi — 4 streams (Workshops, Processes, Products, Policy), 8-week delivery cycles, filterable initiative dashboard, you as sponsor. You and Jordi pushed back:

- **You**: "It might take 8 weeks to take everyone through it. The company doesn't respond well to big-hit approaches. A beachhead strategy will land easier."
- **Jordi**: "Start with one small thing, show value, then people will ask how you did it."
- **Agreed**: Sam strips back to documentation pipeline only. Show value first, then expand.

**Risk**: Sam sees this meeting as an opportunity to re-pitch the broader framework. If workshops come up as a CoP stream, hold the line on what was agreed. Workshops should be an output of the discovery round, not a parallel governance structure.

See: [[2026-03-30-sam-ai-cop]]

## What you can point to

### Discovery round — nearly complete

13+ people spoken to across every department (engineering, product, underwriting, distribution, finance, ops). Liam, Paul, Alex, Jonny tomorrow — then you've covered the company. Nobody else in the room has this cross-company picture.

### Nine active initiatives with clear ownership

| Initiative | Owner | Domain |
|---|---|---|
| AI capability uplift | Tom | ai-enablement |
| Claude standardisation | Tom | ai-enablement |
| Skills distribution | Tom | ai-enablement |
| AI governance framework | Tom | ai-enablement |
| Underwriting assistance AI | Emily | operational-tooling |
| Enterprise Engine | Matt Lees | operational-tooling |
| Engine Room triage | Jordi | engineering-workflows |
| Platform architecture docs | Chris | engineering-workflows |
| CC extraction handover | Abs | product-ai |

### Tracked issues

11 issues in the tracker including Looker MCP cloud deployment (unblocks renewals + insight layer + distribution toolkit), discovery round completion, driver referral automation (2.5–5 hrs/day saving), and the board roadmap for the Pioneer meeting Apr 20.

### Real case studies

- **Matt Lees**: non-technical Enterprise Fleet Lead built a 9-agent pipeline managing £294M in 5 days. $104/month contact enrichment. Board story.
- **Kirsty**: self-started Looker→Claude MCP producing AI-generated insights that change business decisions. Christian, Kevin, David now trialling.
- **Emily's ops team**: daily AI usage, Zapier automation, process-first thinking. The model to replicate.

### Roadmap draft exists

Now/next/later across all 4 domains, feeding into the board meeting Apr 20.

## Fresh context: eval testing regroup (Apr 8, you were absent)

Mima led this. Significant progress — not just test cases but decisions on approach, tooling, and observability.

### What was delivered

- **111 test cases** in Notion + GitHub (`redteam-evals` branch): golden dataset (53), red team/security (49), PromptFoo plugins (9)
- **`/create-test-cases` skill**: stakeholders describe what they need to test via conversation → skill formats output into PromptFoo config → techies ingest and run. This is the skills-as-scaling-mechanism thesis in action.

### Key decisions made

- Test against **production data** (not synthetic) — on-demand runs before major changes, not full CI/CD
- Auth/user-isolation testing belongs in **Playwright**, not PromptFoo
- Non-technical staff don't need PromptFoo locally — techies run centrally
- Consistency of the suite matters more than 100% pass rate

### Observability pipeline emerging

- Ismael connecting agent framework to **Datadog** — demo with Datadog architect this Fri/Mon
- Investigating **S3 storage** for all agent outputs (organised by user/policy) for security, compliance, analytics
- Longer-term: agents analysing stored conversations for higher-level insights

### Security

- Jordi raised whether AI features need pen test / security audit before launch
- Chris to be asked about existing third-party scanner contract
- Anthropic's Project Glass Wing noted as potentially relevant

### Open actions

- Paul: review Notion doc for compliance gaps (ASAP)
- Mima: capture compliance test case requirements from Paul
- Mima + Ismael: scope E2E testing (Playwright, auth/isolation, test user setup)
- Jordi: investigate third-party security audit (check Chris + Fergus)

### Why this matters for the AI Workshops meeting

- This is the evals work Sam was redirected toward — but **Mima's group drove it independently**. Reinforces her "we're already doing this" position. Don't duplicate or undermine this.
- The `/create-test-cases` skill workflow is a concrete example of how non-technical people can contribute to technical governance — worth referencing if workshops come up as a delivery mechanism.
- Paul has been asked to review compliance gaps — you're seeing him at **12:00 CET right before this meeting**. Ask how that review went and whether he has governance concerns to surface.
- The Datadog + S3 observability work shows that production-grade agent monitoring is being stood up. This is governance through engineering, not governance through meetings.
- Demonstrates that real testing and governance is happening organically — your job is to connect and support these efforts, not create a new structure on top.

See: [[2026-04-08-eval-testing-regroup]]

## What already exists for workshops / enablement

| What | Owner | Status |
|---|---|---|
| Beginner prompting workshops | Unknown | Delivered. Well-received but beginner-only |
| Skills AI session 1 | Tom | Delivered 2026-03-27 to cross-functional group |
| AI Breakfast (weekly) | Ollie | Running — sharing tools, ideas, best practices |
| Business continuity workshop | Sam + Paul | Parked for later Q2 |
| Emily's Monthly AI/Automations sync | Emily | Running — ops team reference model |

## The key insight from discovery

One-size-fits-all doesn't work. The spectrum is wider than anyone expected:

- **Fred** (underwriting ops): attended prompting workshop, early stage, needs direction not convincing
- **Average user**: needs a ready-made toolkit — "don't tell me to go explore"
- **Kirsty / Matt Lees**: power users who need infrastructure, freedom, and governance — not training

Workshops must be department-specific. Distribution needs slide decks and broker prioritisation tools. Engineering needs code quality and eval frameworks. Finance needs Looker + Claude integration support. Underwriting needs process automation.

## Framing for the room

> "I've spent the last two weeks talking to people in every department. The picture is clearer than I expected — but the gap between teams is wider. We have Emily's ops team using AI daily without any help from me. We have Matt Lees managing £294M through agents he built himself. And we have people who attended a prompting workshop and aren't sure what to do next.
>
> One workshop programme doesn't serve all three. What I'm building is department-specific enablement paths — toolkits for people who need them, infrastructure for the power users, and governance so none of it goes sideways.
>
> The discovery round finishes this week, and I'll have a full roadmap ready for the board on April 20th."

## Talking points

- "I'd like to understand what triggered this meeting — what are the changes and new ideas?"
- "Before we design workshops, I want to share what I'm finding in the discovery round — the gap between departments is bigger than expected"
- "Some of you are already doing great work — Ollie's AI Breakfast, Mima's eval testing and process automation. I don't want to replace any of that. I want to support it and fill the gaps."
- "We agreed with Sam on Mar 30 to start small — one initiative, show value, expand. I want to keep that discipline here too."
- If Sam re-pitches the CoP: "These are valid long-term ideas but we agreed to prove the model with documentation first. Let's not expand scope until that's delivered."

## Questions to get answered

1. What triggered this meeting? What are the "changes and new ideas" Rakhee mentioned?
2. What's the desired outcome — a plan, a schedule, or just alignment?
3. Who owns workshop delivery? (People team, engineering, you, distributed?)
4. Does Abs's departure create urgency to capture his knowledge?
5. What format works best — working sessions (like the value statement workshop) or classroom-style training?
6. Does the People team want a role in logistics, scheduling, comms?

## What Rakhee probably wants from you

- A signal that there **is** a plan (or one forming)
- Clarity on **who does what** — she can't communicate to the company if ownership is fuzzy
- A rough **timeline** — even "discovery finishes end of April, programme design in May" gives her something to work with
- Whether People team has a role (comms, scheduling, logistics)
