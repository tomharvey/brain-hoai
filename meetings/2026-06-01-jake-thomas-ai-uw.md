---
title: "Jake / Thomas — AI use cases in underwriting"
created: 2026-06-01
updated: 2026-06-01
domain: ai-enablement
type: meeting
tags: [underwriting, hubspot, granola, adoption, knowledge-transfer, paternity-leave]
---

# Jake / Thomas — AI use cases in underwriting

**Date**: 2026-06-01 11:30  
**Attendees**: [[tom-harvey]], [[jake-wood]]

Full transcript: [[2026-06-01-jake-thomas-ai-uw-transcript]]

---

## Key themes

### Activation trigger — AI breakfast demo

Jake had previously attended AI breakfasts without finding a direct personal use case. Last Friday, someone named "Eras" (name unresolved — not in vault) presented a HubSpot integration demo. Jake immediately saw the parallel to his own deal-tracking problem and spent the entire day building.

Key insight: 10 months of domain context was the prerequisite. Without knowing the job well enough, there was nothing obvious to automate.

### HubSpot deal-tracking system

Jake built a system that:
- Syncs with HubSpot every 15 minutes — pulls new deals automatically
- Pushes notes and updates back to HubSpot
- Addresses gaps: HubSpot doesn't show chase dates or pricing; previously required manual notes + separate portal/retail lookup

Testing solo for 1 week, then rolling out to other underwriters if it holds up.

Challenge surfaced: the system is very Jake-specific. Hard to hand to Billy and have it be immediately useful — this is the general personalisation problem with AI tooling.

### Granola for knowledge transfer — Billy's paternity leave

Billy going on paternity leave within 2 weeks. Current state: poor HubSpot notes mean anyone covering for a colleague has to reverse-engineer deal status from scratch.

Tom's proposal (well-received): use Granola to record handover sessions. Billy won't document everything formally, but will talk through his deals over a beer. Granola captures the context; AI extracts what matters.

Jake extended this to broker calls: instead of typing shorthand notes post-call (which become cryptic a week later), narrate into Granola or use Claude's voice input. Actual example: Jake has a note from Friday that just says "unlikely to win. Another market is better" — and has already lost the context for a closed-loss reason.

See [[AI-070]].

### Hyper-personalisation vs team sharing

The broader challenge: because AI tooling is so personalised, getting people to adopt someone else's tool is hard. It requires each person to go on their own journey. Tom's framing: encourage the journey, not just the tool.

### Claude vs ChatGPT

Jake has switched from ChatGPT to Claude. Finds Claude significantly better — largely because of the Flock-specific connectors (HubSpot, platform data, Looker). The integrations are the differentiator, not the base model.

Tom pointed Jake to [[jacob-holland|Jacob]] for retail/portal data extraction questions.

---

## Actions

- [ ] **Jake** — Try Granola for post-call note capture; experiment with voice narration workflow → [[AI-070]]
- [ ] **Jake / Billy** — Schedule handover session with Granola running before paternity leave
- [ ] **Jake** — Test HubSpot deal-tracking system for 1 week then offer to other underwriters

---

## Name flag

⚠️ **"Eras"** — mentioned as someone who presented a HubSpot demo at the AI breakfast that triggered Jake's activation. No people file found. Please identify.
