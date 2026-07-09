---
title: AI Underwriting
created: 2026-07-09
updated: 2026-07-09
domain: ai-enablement
type: meeting
tags: [underwriting, ai-adoption, claude, apollo, hubspot]
---

# AI Underwriting — 2026-07-09

**Attendees**: Tom Harvey, Curtis Bailey, Andrew Dodd, [[jake-wood|Jake Wood]], Matthew Smith, [[tom-rogers|Tom Rogers]], Darren Nightingale, Billy Bone

**Transcript**: [[2026-07-09-ai-underwriting-transcript]]

> Note on attribution: the raw transcript merges all in-room speakers into "Me"; remote speakers ("Them") include Andrew Dodd (confirmed by name) and possibly Darren Nightingale. Where attribution is uncertain below, it is marked.

## Current AI practice across the team

- **Tom Rogers** has built his own Claude skill: top 10 most urgent deals from the HubSpot pipeline, a Gmail scan for unanswered emails linked to active deals, and a daily plan with suggested actions. Started from "two or three things" and evolved it iteratively; spent an hour trying to adapt it for others but "it was still stuff that was wrong". HubSpot remains his source of truth.
- **Jake Wood** previously built a shared pipeline tool ("Jake's thing") that Tom Rogers, Matthew Smith and Curtis Bailey tried; adoption faltered — the shared prompt didn't fit individual workflows, and Matthew Smith dropped it when the busy period hit. Jake also used Claude computer use ("give it access... we see the cursor come up") and demoed "Flock Lord" (likely Flock Claude) analysis of last year's Amazon New Ventures win — "within 20 minutes of asking questions... that would take me hours".
- **Matthew Smith** uses Gemini in Google Sheets for underwriting analysis: pulls individual pipelines from HubSpot, GWP written since 2025, loss ratio split new vs existing, capped for large losses. "If I was trying to do that myself... you wouldn't get it accurately."
- **Andrew Dodd** (remote): "I have used Claude, I'll have you know." Hasn't received Tom Rogers' skill yet but committed to using it: "I would use it if you can — can you send it to me?"
- **Curtis Bailey**: met a broker (Broadshire?) on Monday — Tom Harvey demoed Apollo/Claude research on that contact live. Has a demo call with a prospect on Monday and volunteered it as a test case. Provided the "food distribution in London" risk for the live background-check demo.
- **Darren Nightingale / Billy Bone**: no clearly attributable AI usage in this meeting (speaker labels don't separate them). Billy is name-checked once in a HubSpot/Looker aside.
- Claude connectors (Customize → Connectors): Google Drive, HubSpot, Looker available. Looker periodically logs you out — treat as an auth quirk. Apollo.io demoed for prospect research; team has pulled 3,500+ HGV operator contacts through it.

## Central platform vs personalisation

- Recurring tension: individually built skills work ("Ikea effect" — value comes partly from building it yourself), but shared prompts handed over rarely stick.
- HubSpot inconsistency is a prerequisite problem: "everyone in the team is a different way... people keep it at different stage at different times. There's no consistency, so it's very difficult to create something that everyone uses."
- Proposal: a central database/platform everyone works off, with each person personalising their own view on top. To be revisited mid-August after holidays.
- Advice given: start with 2–3 specific things you want, let it evolve — don't ask someone else to send you theirs.

## Use cases worth exploring

- **Pre-meeting company research**: feed a prospect name, get background, key people, LinkedIn, emails. Tested live on Curtis's Monday demo client (family-run construction firm, ~21 employees, Midlands) — no phone numbers, but emails and LinkedIn returned.
- **Broker/risk background checks** (raised by a remote attendee, likely Andrew Dodd or Darren Nightingale): search the internet for negative signals on risks where broker information is thin — "sometimes our brokers don't always give us much background information to companies."
- **Underwriting rationale drafting**: co:work skill using Google Drive (client info, broker presentation), Gmail, internet search + the existing rationale guidance documentation to auto-draft structured rationales.
- **Claims data centralisation**: ingest insurer claims listings, normalise to a Flock format, drive analysis. Submissions data store went live last week. An underwriter offered to brain-dump "the 20 things I do in a risk" into co:work.
- **Post-call dictation**: Whisper or Claude's transcribe button for brain-dumps straight after face-to-face broker meetings. Granola flagged, with hesitation about broker-call privacy.

## Barriers

- **Time** is the main blocker — busy period, half the team on holiday/paternity. Counterpoint made: "an hour or two of work doing that extra bit makes the rest of your work" faster; quieter periods are the time to invest.
- Claude desktop must stay open (not standby) to be reachable from the mobile app.
- Open-plan office makes voice dictation awkward; easier from home.

## Actions

- [ ] Tom Rogers: send his Claude skill (urgent deals + Gmail scan + daily plan) to Andrew Dodd
- [ ] Curtis Bailey: use Apollo/Claude company research to prep Monday's demo call (construction firm) — due 2026-07-13
- [ ] Tom Harvey: explore a centralised Claude setup for the underwriting team that still allows personal views — revisit mid-August after holiday
