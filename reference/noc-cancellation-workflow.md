---
title: Notice of Cancellation (NOC) — Zapier workflow design
created: 2026-04-02
updated: 2026-04-02
domain: operational-tooling
type: reference
author: shreya-chowta
tags: [noc, cancellation, zapier, hubspot, gdrive, underwriting]
---

## Source

Designed by [[shreya-chowta|Shreya Chowta]]. Converted from `Shreya Zapier - NOC workflow.docx` on 2026-04-02. This was Shreya's proposed Zapier automation — the current direction is to iterate via Claude prompt first (see [[AI-008-shreya-noc-followup]]).

## Workflow — complete step-by-step

### Step 1 — HubSpot (Trigger)

New ticket is created in HubSpot. This kicks off the entire Zap automatically.

### Step 2 — Filter by Zapier

Checks that the ticket category equals "Notice of Cancellation." Stops the Zap if it doesn't match — no accidental runs.

### Step 3 — Google Drive: Copy File

Makes a copy of the master NOC template and saves it to the NOC Archive folder. The original is never touched. Name the copy dynamically: `NOC - {{contact_name}} - {{policy_number}} - {{date}}`

### Step 4 — Google Docs: Update Document

Takes the copied file and replaces all placeholders with real ticket data — policy name, policy number, amount, connectivity %, date, and contact name.

### Step 5 — Google Drive: Get File (as PDF)

Exports the populated Google Doc as a PDF, ready to attach to the email draft.

### Step 6 — HubSpot: Find Contact

Looks up the contact record associated with the ticket, pulling in their full name and email address.

### Step 7 — HubSpot: Create Draft Email

Creates a draft email inside the ticket — linked to the contact, with the PDF attached and subject/body pre-filled. It is **not** sent automatically.

### Step 8 — HubSpot: Update Ticket

Changes the ticket status to "Pending Send" so the team knows the draft is ready and waiting.

## Notes

- Human-in-the-loop: draft email created but never auto-sent — review required before sending (confidential data)
- Cancellation threshold: connectivity below 75%
- Batched: typically triggered every Monday after fleet clinic meets
- Ticket triggered by finance team or Johnny (handles connectivity)
- Current direction: Tom suggested iterating via Claude prompt first (Claude + HubSpot connector), then automate once prompt is stable

## Links

- Issue: [[AI-008-shreya-noc-followup]]
- Initiative: [[underwriting-assistance-ai]]
- Meeting: [[2026-04-02-shreya-ai-discovery]]
