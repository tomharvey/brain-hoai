---
title: Fergus <> Tom — Weekly
created: 2026-04-16
updated: 2026-04-16
domain: ai-enablement
type: meeting
tags: [weekly, fergus, leadership, roadmap, ai-adoption, infosec, ai-native-engineering]
---

## Attendees

- [[fergus|Fergus Doyle]]
- Tom Harvey

## Key themes

### Team news

- **Smith leaving** — taken a remote-first role enabling move to Portugal. Announced internally Wed, company announcement next week. Serving full notice. Counterbalanced by Happy's promotion, Rob just joined, ongoing hiring.

### AI adoption — emerging framework

Tom progressing well on per-cohort approach:
1. **Non-users** (various reasons) — basic onboarding
2. **Dabblers** — structured guidance
3. **Advanced users** — optimisation, not restrictions

Current state:
- [[darren|Darren McCauley]] using AI extensively despite earlier resistance — now defending it as "his toy"
- [[fred-bush|Fred]] nearly converted — would mean all UWAs running at pace
- Pattern noted: "every team has someone over here and someone down here"
- Tom to send framework to Fergus once written up

### HubSpot data quality — reframe

Repeated excuse for not adopting AI ("HubSpot data isn't good enough"). Fergus's reframe: **make it a solvable problem space**. Dedicate effort to data quality so it stops being a blocker. Show people that AI itself can fix the data (LLM updating contacts from email history is a powerful example).

### Looker access wishlist

- Multiple teams asking for Looker MCP — high demand
- More HubSpot AI permissions needed (Emily holds keys, 30-second fix)
- Looker access for Anna lets us delete the PMT spreadsheet
- Open question: where's HubSpot → Looker pipeline / data quality work being done?

### Roadmap & Pioneer

- Pioneer board next week — Fergus presenting roadmap (low fidelity, 2-year)
- Concern: visual constraints mean 2026 looks small, but implicit commitments could pile up around Admiral / claims in-housing
- **Premium financing + installments** moved forward into 2026 — need to confirm scope still achievable
- Fergus wants to confirm 2026 docket aligns with what we'd be doing absent Pioneer

### InfoSec working group

- Inaugural session held Wed — Fergus standing it up
- Tom welcome to join
- Key risk topic: **MCP connectivity blast radius on individual Claude accounts** — superuser with Gmail + HubSpot + everything else connected = high blast radius
- Need oversight on who has what enabled and whether permissions match actual need
- Background process, not urgent answer

### AI-native engineering — cracked open

Big conversation thread. Fergus aligned with the direction:

- **Auto-generated draft PRs from Linear tickets** — Tom raised, Fergus jumped on it
- **Acquisition squad as sandbox** — Rob just joined, greenfield problem, perfect testbed
- **"Try this for a month"** as the framing
- **Confidence-building first step**: auto-merge Dependabot patch versions on green CI. Lowest-risk building block. Highlights the gap in CI confidence we'd need to close anyway.
- **Feed-in question**: a one-line Linear ticket isn't enough — needs the 5 relevant Notion docs as context. Codifying institutional knowledge is the prerequisite.
- **Cross-repo / dev environment**: harder than Tom's pet project. Tom thinks he has answers.
- **Philosophical split**: agents augmenting **teams** vs agents augmenting **individuals**. Fergus's gut: team-level. Tom unsure — engagement/teaching loop may need individual ownership first. Discussed as live tension, not resolved.
- **Telemetry/feature discovery pipeline** (Darren's work with Michael & Francesco) — Fergus thinks this is engineering-worthy, could become a self-healing pipeline of proposals. "Build a Harvey so Harvey can do the human judgment bit."

This conversation maps directly to [[ai-native-engineering]] initiative.

### Engineering drop-ins / EMM cadence

Tom noticed engineering drop-ins are mostly people/performance topics, product drop-ins mostly product topics. Fergus reflected on whether the audience and description still match. No firm conclusion — Fergus to mull. Tom can step back from EMMs if useful, attend product drop-ins which give better line of sight.

### Logistics

- Tom in London Tue afternoon (Gatwick → Thameslink → Farringdon)
- Thursday rail strikes — Fergus leaving early
- AWS Summit Wed (AI track) — Flock under-represented, scheduling clash

## Actions

- [ ] Tom: send AI cohort framework write-up to Fergus
- [ ] Tom: draft 90-min offsite AI session — by end of today/tomorrow. Direction: stations + rotation, disparate topics
- [ ] Tom: speak to Harvey about the telemetry feature-discovery pipeline (longer session, possibly next week in office)
- [ ] Tom: pitch the AI-native engineering pilot to Acquisition squad ([[matt-lees|Matt Lees]] / Rob) as the sandbox — "try this for a month"
- [ ] Tom: explore Dependabot auto-merge on green CI as a confidence-building step
- [ ] Fergus: mull on engineering drop-in audience/cadence
- [ ] Fergus: confirm 2026 roadmap scope with Anton given premium financing + installments pull-in

## Notes

Strong alignment on AI-native engineering as the strategic direction. Fergus framed it instinctually rather than as a hard thesis — useful to know it's directional intuition rather than firm policy. The team-vs-individual augmentation question is the one to keep open and feed evidence into.

The "make HubSpot data quality a solvable problem" reframe is a useful one to repeat back to teams who are using it as an excuse.

Full transcript: [[2026-04-16-fergus-tom-weekly-transcript]]
