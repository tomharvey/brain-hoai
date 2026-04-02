---
title: "Tom <> Shreya: AI Discovery"
created: 2026-04-02
updated: 2026-04-02
domain: operational-tooling
type: meeting
tags: [shreya, underwriting, cancellations, hubspot, submissions]
attendees:
  - "[[shreya-chowta|Shreya Chowta]]"
---

## Context

Discovery call with Shreya (Underwriting Assistant, reports to Emily). Emily flagged her as the most advanced AI user on the ops team. Focus: understand her processes, pain points, and where AI fits. Surfaced the cancellation notice workflow as the primary automation candidate.

## Notes

### Cancellation notice (NOC) automation — primary pain point

- Cancellation notices issued when fleet connectivity drops below 75%
- Batched — typically triggered every Monday after fleet clinic meets
- Currently manual: copy/paste policy number, name, connectivity % from HubSpot/Retool into a Word template
- Shreya had already designed a Zapier + Google Drive + HubSpot workflow:
  1. Ticket triggered in HubSpot (finance team or Johnny)
  2. Pull policy number, name, amount, connectivity % from HubSpot
  3. Replicate NOC Word template from Google Drive (can't edit original)
  4. Populate copy with ticket data
  5. Export as PDF
  6. Draft email in HubSpot (not auto-send — human review required before sending)
- She'd pitched this to Sam; they were due to work on it together

### Claude + HubSpot approach (discussed as faster path)

- Tom suggested: iterate on a Claude prompt before building Zapier automation
- **Connected HubSpot to Claude live on the call** — worked immediately
- Claude pulled up Shreya's assigned HubSpot tickets correctly
- Issue: pulling in closed/historical tickets too — prompt needs filtering
- Approach: feed Claude the NOC Word template + ask it to fill in details for a specific deal
- Iterate until prompt reliably handles filtering (stage, date, connectivity threshold)
- Once stable: ask Claude to iterate through 6-7 tickets, fill a document for each, output as PDFs
- Once confident: automate the HubSpot upload step
- Policy numbers follow known format (ADMFL or HVFL prefix) — good prompt hint
- Shreya planned to try this immediately after the call
- Shreya also wants Emily to add structured fields to HubSpot tickets (policy name, number, reasoning) — Tom's view: Claude can find policy numbers in free text, so may not be strictly necessary

### Submissions / new business logging

- Entirely manual — flagged as a much larger project
- Multiple people thinking about it: Shreya, Tom, Fergus
- Challenge: scheduling time to actually work on it together
- Next step: break into small, achievable goals across dedicated meetings

### CC parsing

- Retool CC parser (Abs built) still works well
- Haulage portal now has a Claude prompt that converts CCs to CSV for upload
- Ana tested it — reportedly faster than the Abs-built version
- **Key observation from Shreya: "We're relying more on Claude now than tech automation"**

### Other notes

- Shreya prefers Word documents over Google Docs ("very old school")
- Knew Sam via Tracy from a previous company

## Decisions

- NOC automation: iterate via Claude prompt first, automate later — faster path than Zapier workflow
- Submissions project needs dedicated meetings to break into small goals

## Actions

- [ ] Shreya: send Tom the NOC workflow document
- [ ] Shreya: test Claude + HubSpot connector — feed NOC template, fill in details for a live ticket
- [ ] Shreya: report back to Tom on Claude NOC test results
- [ ] Tom: follow up with Shreya on Claude NOC test results
- [ ] Tom: schedule meetings with Shreya (and likely Fergus) to break submissions project into small goals

## Links

- Related: [[underwriting-assistance-ai]], [[submissions-automation]]
