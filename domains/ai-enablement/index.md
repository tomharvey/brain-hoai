---
title: Domain — AI Enablement
created: 2026-05-08
updated: 2026-06-02
domain: ai-enablement
type: reference
tags: [domain, strategy, enablement, capability]
---

# AI Enablement

**What this domain is trying to achieve:** Every department uses AI tools confidently and independently. People design processes with AI in mind. The Head of AI role makes itself redundant by building self-sustaining capability. One platform (Claude), governed, with skills that scale.

---

## What we currently believe is true

- **Emily's ops team is the reference model.** Daily AI usage, process-first thinking, monthly AI/Automations sync. The goal for every other department is to get to where ops already is.
- **Confidence before automation.** Getting people to feel like Kirsty (showing their work, self-starting) matters more right now than automating the "right" things. Demos breed dependency; pairing breeds capability.
- **Capability is a spectrum, not a binary.** Matt Lees (9-agent pipeline, £294M managed) → Kirsty (self-started Looker MCP) → average user (using Claude daily, basic tasks) → Sophie (needs a ready-made toolkit, not "go explore"). Programme design must serve all four, not just the enthusiastic middle.
- **Token spend anxiety is cultural, not budgetary.** Ishmael was on Sonnet despite an explicit unlimited AI budget. Fergus runs every submission through the pipeline; others are afraid to spend. The constraint is permission, not cost.
- **Rate limits are the next concrete unlock.** Matt Lees hit the Team plan cap running 9 agents. Enterprise deal removes this blocker and adds admin controls. This is now the strongest argument for accelerating the deal.
- **Skills are the scaling mechanism.** The best capability uplift is a skill that embeds best practice and can be used by anyone, not a workshop that fades in a week. But skills built in isolation don't scale — skills need governance and visibility.
- **Sprawl prevention must start now.** When building is free, the natural coordination mechanism (cost of creation) disappears. Flock is small enough to build the immune system before it needs retrofitting. The Amazon lesson: 247 tools in one division is what "too late" looks like.
- **Personal OSes are spreading.** Tom, Jemima, Javier, Fergus, Jacob all building personal operating systems. The next question is not "should I build one?" but "how do they talk to each other?" Jemima has added vector encoding; Tom treats his vault as unreadable binary — as long as the AI can read it, that's sufficient. Product team (Matt, Geran, Ollie, Mima) held a dedicated multiplayer session (2026-05-18) — Matt has GitHub repos with persona/LOB context that others haven't yet ingested; sneaker-netting files is the agreed first step before building shared infrastructure. ([[2026-05-18-product-team-context]])
- **Transcripts are an untapped data substrate.** BDMs (Ben, Daisy) already have loose team-level transcript querying. Others (Sophie, Adam, Alex, Matt Lees) do not. A company-wide transcript service (medallion: bronze raw → silver tagged → gold insights) is a near-term unlock. RBAC and [[francesco-venerandi|Francesco]]'s existing Granola service are the starting points. Underwriting gap: most calls are phone/in-person, creating a class imbalance. Granola Enterprise API is the likely route to raw programmatic access — Tom to confirm. The J feedback pipeline (Francesco-built) is the first candidate for improvement: add persistent memory of known context so it surfaces novel insight rather than re-raising known issues weekly. Tom raised the company-wide transcript need directly with Francesco 2026-05-19. ([[AI-050]], [[AI-051]], [[2026-05-19-francesco-ai-catchup]])
- **Finance AI adoption is further along than previously assumed.** The 2026-05-19 workshop revealed Kevin, Ivan, and [[kirsty]] are already doing sophisticated, daily-use AI work (Excel automation, document generation, credit control reports, Looker-connected dashboards). The remaining gap is: not everyone has the Excel plugin, NetSuite MCP access is manual, and the team hasn't shared techniques internally. The right next move is MCP enablement (NetSuite) and lateral sharing, not capability uplift from zero. ([[2026-05-19-finance-team-ai-workshop]]) Ivan's credit control daily cycle (NetSuite export → Claude chat → prioritisation report) is the archetype for data-heavy finance use cases: flat-file data, clear daily output, runs in 2 minutes. 2 months in, still working. ([[2026-05-13-ivan-ai-discovery]])
- **MCP-based personal development tools are emerging bottom-up.** [[francesco-venerandi|Francesco]] and [[ollie-crowe|Ollie]] built a career performance coaching system (connects Granola, Slack, Notion, GCal) that tracks progress against manager promotion criteria, preps 1:1s, and gives weekly coaching. The release model (instructions as MD files, deployed via MCP update) is a pattern worth reusing. Currently used by Francesco, Ollie, potentially [[javier|Javier]]. Key dependency: requires a written promotion rubric from manager — surfaces a Flock process gap. ([[AI-059]], [[2026-05-19-francesco-ai-catchup]])
- **Non-engineering teams can use Google Drive as a shared AI context layer.** Milan's pricing team already has a shared Drive folder with all their analysis. Drop a `claude.md` at the top level, use an `outputs/` subfolder, and it becomes a team second brain — not for calendar/notes, but for data analysis. Skills fragmentation (Francesco and Milan independently built similar actuarial skills) is the forcing function for consolidation. ([[2026-05-11-milan-ai-discovery]])
- **A secretary → coach → strategic partner pattern is emerging independently across teams.** Adam, Matt Lees, and Alex Dyball all developed AI-as-coach usage (meeting review, performance feedback, accountability) without being prompted to do so — and Adam uses it for complex stakeholder navigation at the strategic partner level. This pattern appeared in all three distribution discovery calls (2026-05-26–27). It is the progression that matters most for non-engineering roles: secretary (admin/automation), coach (feedback, accountability, reflection), strategic partner (shaping thinking on hard problems). Most programme framing has been secretarial ("second brain") — the coach and strategic partner framings are the ones that stick at leadership level. Flag to [[rakhee]] as a people/culture signal.
- **The activation threshold is now a company-wide goal, CEO-endorsed.** Ed's goal: 80% of Flock crosses the activation threshold by end of June. Hypothesis: complete 3 useful tasks in a context-fuelled Claude project. Oddly specific is intentional — it forces concrete actions. The blocker is activation energy, not use cases: people ask one question, get a mediocre answer, and move on. They need to learn to have a conversation. ([[2026-05-14-ed-tom-121]])
- **Tom is the enabler, not the centre of excellence — CEO's explicit framing.** Ed's words: "We need everyone at Flock being like, Tom teaches me and enables me to do it rather than I'll go to Tom and he'll do it." This gives air cover to scale through workshops rather than 1:1s. ([[2026-05-14-ed-tom-121]])
- **Three cohorts confirmed at CEO level.** (1) Hardcore AGI-pilled: Tom, Mima, Ollie, Ed (philosophically if not yet proficient). (2) Hardcore naysayers: Darren Nightingale, some finance. (3) Middle 80%: interested, occasionally use, wish they were better. Within the middle: a meaningful split between those who found a resonant use case and those who don't know where to start. Both halves need different interventions. The K-curve framing (Mark, CEO of ScreenCloud): AI splits everyone onto upper or lower arm of K. ([[2026-05-14-ed-tom-121]])

## What we're uncertain about

- **Phone-based roles need a narration workflow, not call-recording.** Underwriting (and likely sales) work primarily via phone — short calls, often unrecordable. Granola-for-transcription isn't a natural fit. The unlock is post-call voice narration: speak a 2-minute summary into Granola after hanging up instead of typing shorthand. The shorthand-becomes-cryptic problem is the concrete pain point that sells it. ([[2026-06-01-jake-thomas-ai-uw]])
- **AI job security anxiety is a live concern in engineering, not a background noise.** Alex (engineer) raised Facebook layoffs as evidence of displacement in a 1:1 with Tom (2026-05-22). Tom has a counter-narrative (Facebook made redundancies for unrelated business reasons; Anthropic hiring at $500k contradicts the replacement story). But the concern needs structured response: targeted 1:1s + curated team sessions. [[rakhee]] is the people partner to loop in. → [[AI-062]] Aleksandra confirmed (2026-05-22) that Steve explicitly frames AI monitoring as "babysitting" and it's landing badly — the dismissiveness is a symptom of an unresolved "understand vs trust" tension engineers feel when they can't read code they ship. ([[2026-05-22-aleksandra-ai-catchup]])
- **Finance AI workshop design has surfaced a useful exercise format.** Jade's team: individual work + roaming tutors + core exercise (write down job objectives → Granola records conversation about role → feed to Claude → ask how it can help). Precedent: tech hackathon team talked, Granola recorded, Claude built it. Adaptable to other non-technical departments.
- **BDM team (Sophie) represents a high-leverage, underserved cohort.** Sophie is motivated, does many customer calls, but the default Granola summary format doesn't match what BDMs need (next steps, broker intent, follow-up commitments). A custom summary skill + team workshop is the unlock — team AI adoption at zero, single internal champion in place. → [[AI-069]], [[AI-070]] ([[2026-05-29-sophie-dodds-ai-catchup]])
- Whether group workshops can work at scale or whether it's all 1:1 pairing from here. Ed has endorsed Flock o'clock format and wants to co-run — this may be the answer, but curriculum design is still open.
- Whether the enterprise deal will land before rate limits become a serious productivity blocker.
- **Underwriting is now on the board.** [[jake-wood|Jake Wood]] built a HubSpot deal-tracking system after seeing a peer demo at AI breakfast — spent all of Friday building it unprompted. First concrete underwriter-built AI tool. Pattern: 10 months of domain context was the prerequisite before use cases became obvious. Peer demos (not workshops) were the trigger. Darren's team not yet spoken to. ([[2026-06-01-jake-thomas-ai-uw]])
- Whether the capability baseline report (AI-013) will get done — it's a precondition for measuring progress.
- How personal OSes federate. The product team session (2026-05-18) gave a clearer direction: sneaker-net files first → validate that cross-team context actually changes decisions → then build shared infrastructure. The clearest multiplayer value is cross-pollination of Granola transcripts (Ollie's acquisition calls are useful to Geran; Mima's J data is useful to everyone). The ideal end state is post-processing that auto-routes relevant conversations to the right person based on shared OKR context — but that requires the shared strategy layer first.
- Whether the multiplayer second brain use case (manager using their OS to coach reports) is a viable adoption path for leadership layer, or whether it needs to be demonstrated at SLT level first.
- What the right governance model is for a company-wide transcript service — RBAC approach, which conversations are in scope, and who defines the "lenses" for each team.

---

## Active initiatives

| Initiative | Status | Owner | Notes |
|---|---|---|---|
| [[ai-capability-uplift]] | active | Tom | Past discovery, shifting to applied 1:1 pairing |
| [[ai-governance-framework]] | active | Tom | Risk/compliance deferred; sprawl prevention is urgent |
| [[claude-standardisation]] | active | Tom | Enterprise deal is the unlock; rate limits proven constraint |
| [[skills-distribution]] | active | Tom | Governance and distribution model still unresolved |

## Key decisions

- **002**: Governance deferred to later Q2 — practical governance (evals, observability, security audit) not waiting
- Discovery round complete (20+ conversations); four cohorts identified

## Key people

- [[emily]] — reference model for ops AI adoption
- [[kirsty]] — standout builder in Finance; Looker→Claude MCP
- [[matt-lees]] — power user ceiling (Enterprise Engine, 9-agent pipeline)
- [[sam]] — governance research capacity
- [[ollie-crowe]] — AI Breakfast host; adoption culture
