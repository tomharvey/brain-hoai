---
title: Domain — AI Enablement
created: 2026-05-08
updated: 2026-05-08
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
- **Personal OSes are spreading.** Tom, Jemima, Javier, Fergus, Jacob all building personal operating systems. The next question is not "should I build one?" but "how do they talk to each other?" Jemima has added vector encoding; Tom treats his vault as unreadable binary — as long as the AI can read it, that's sufficient.
- **Transcripts are an untapped data substrate.** BDMs (Ben, Daisy) already have loose team-level transcript querying. Others (Sophie, Adam, Alex, Matt Lees) do not. A company-wide transcript service (medallion: bronze raw → silver tagged → gold insights) is a near-term unlock. RBAC and Granola's existing service (Francesco) are the starting points. Underwriting gap: most calls are phone/in-person, creating a class imbalance.
- **Finance AI adoption is stuck in the "too busy for the shortcut" trap.** Capable team (Jade, Kirsty, Christian, Matt) but not making time. The right intervention is a forcing-function session, not more demos.

## What we're uncertain about

- Whether group workshops can work at scale or whether it's all 1:1 pairing from here. Saturation of the willing is real — people who were going to come have come.
- Whether the enterprise deal will land before rate limits become a serious productivity blocker.
- How to get underwriting into the programme. No underwriter has attended AI Breakfast. Darren's team not yet spoken to. Milan discovery is scheduled (Mon 11 May).
- Whether the capability baseline report (AI-013) will get done — it's a precondition for measuring progress.
- How personal OSes federate. Geran's question: "how do personal OSes talk to each other?" No answer yet.
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
