---
title: "Ollie / Tom — Weekly"
created: 2026-06-09
updated: 2026-06-09
domain: ai-enablement
type: meeting
tags: [ollie-crowe, bdm-brain, acquisition-brain, data-consistency, semantic-layer, apple-wwdc, harvey-ai, jake-wood, milan-chavda]
---

# Ollie / Tom — Weekly

**Date:** 2026-06-09
**Attendees:** [[ollie-crowe]], Tom

Full transcript: [[2026-06-09-ollie-tom-weekly-transcript]]

---

## Key themes

### Harvey.ai meetup

[[ollie-crowe]] attended a meetup with the [Harvey.ai](http://Harvey.ai) founder discussing their legal AI product. Key observations:
- Companies training models internally with proprietary legal data built from their own lawyers
- CMA (Cloud Managed Agents) architecture positioned as the key future direction
- Synthetic data generation with custom, open-sourced benchmarking standards
- Impressive but probably overvalued at ~$1B valuation

### Finance AI workshop recap

Finance AI workshop last week: everyone got to use some tools. Comms issue between Tom and [[kirsty]] cost ~3 hours (Kirsty used Claude Code to build a Moss MCP that Tom had literally sent her that morning). Good start — hands-on experience achieved. Part of their wider finance team development day.

### Jake's underwriting dashboard — data consistency problem

[[ollie-crowe]] met with Adam and [[jake-wood]] to review Jake's underwriting dashboard (ready to roll out). Key finding: **non-deterministic conversion rate definitions** — because conversion rate isn't defined in the prompt upfront, different people using the HubSpot MCP get different results depending on how the MCP resolves it. This is causing confusion across teams (Alex is using different tools, building separate dashboards).

Proposed unified approach: build standardised dashboards via Lovable, connecting HubSpot and Claude APIs, with shared definitions baked in. BDM brain is a natural starting point.

Note: [[jake-wood]] added a colourblind mode to the dashboard because Billy is colourblind. Good accessibility signal.

### BDM brain architecture — semantic/ontology layer concept

Tom's emerging view on the BDM brain technical architecture:
- Claude connects to a relatively customized MCP client
- That MCP client holds the **semantics and ontology** of what exists in the BDM world: conversations, brokers, accelerators, ghost contacts
- The MCP then hands off to Notion (as a data store) and HubSpot, managing where things should live in each and how to tie them together
- A **validation layer** ensures that when writing to Notion, it's structured data, not sloppy prose
- Proactive distribution: a transcript from a Sophie call could be analyzed through five lenses and distributed automatically

Ollie's accelerator broker panel in Notion is a good migration test case — what edge cases aren't captured in the current ontology?

Consensus: BDM brain is the right starting point. Underwriters aren't there yet — let the process work for BDMs first, then take lessons to underwriting. By team, there's a clear difference in readiness.

### Acquisition brain status

All team members (Rob and Harvey = Tom Harvey) have access. Tom Harvey has added technical documentation. Alex (engineering) had laptop issues slowing adoption. Structure is in place: Google Drive–synced folder shared with the team, onboarding skill. Usage needs to start properly — the structure is there but real experimentation is pending.

Key observation from Tom: the acquisition brain is a good trial environment for the BDM brain patterns. If Harvey feeds things in, how do we validate it was structured correctly and distributed to the right places?

### Apple WWDC AI presentation

Apple's WWDC presentation discussed. For people living in Claude all day, it looks underwhelming. Broader take: it was customer-first and hyper-specific. Examples:
- Password manager detects exposed password → automatically changes it on the website and updates the manager
- Tabs grouped by topic automatically
- Web page product out-of-stock → keep checking and notify when back in stock

This is the right framing for AI at Flock too: meaningful tasks that help with everyday things. Same pattern as what underwriting assistants have been building — how do I do this little task — not superintelligence.

### Milan's pricing conversation

[[milan-chavda]] had a good conversation with Tom on Friday about the pricing deck he took to SLT. Key points:
- Targets were ambitious/arbitrary — realistic target is closer to £5.4M per quarter vs. £9M set
- Biggest unlock for conversion: large fleets and big deals
- Sales process is unstandardized but it's not Tom's job to tell them how to sell

---

## Actions

- [ ] **Tom**: kick off BDM brain co:work project this week — start small with Ollie-style resolver + basic skills structure
- [ ] **Tom + Ollie**: resolve HubSpot name inconsistencies (also flagged for Adam/Emily meeting)
- [ ] **Tom**: validate that acquisition brain is feeding through properly and Rob/Alex are experimenting with it

---

## Name flags

- **Billy** — underwriter, colourblind ([[jake-wood]] added colourblind mode to his dashboard for him). No people file. Confirm identity.
- **Mat** / **Curtis** — underwriters mentioned in context of Jake's rollout. No people files.
