---
title: "Follow up with Shreya on Claude NOC test results"
id: AI-008
created: 2026-04-02
updated: 2026-04-13
due: 2026-04-07
origin: "[[2026-04-02-shreya-ai-discovery]]"
domain: operational-tooling
type: issue
status: done
priority: medium
assignee: tom
tags: [shreya, cancellations, claude, hubspot, noc]
---

## Description

Shreya is testing the Claude + HubSpot approach for NOC (cancellation notice) automation — feeding the Word template to Claude and asking it to fill in details from HubSpot tickets. Follow up to see how it went and help iterate on the prompt if needed.

## Acceptance criteria

- [x] Check in with Shreya — did the Claude + template test work? **Yes — built a working Claude skill**
- [x] If it worked: help refine prompt filtering (stage, date, connectivity threshold) — **Done in 14 Apr walkthrough**
- [x] If blocked: diagnose and suggest next steps — N/A, it worked

## Notes

- She connected HubSpot to Claude live on the call — initial test pulled tickets correctly but included closed/historical ones
- Policy numbers follow ADMFL or HVFL format — good for prompt hints
- NOC Word template needs to be replicated (not edited) for each cancellation
- She was going to try immediately after the call

## Resolution (2026-04-13)

Shreya built a working Claude skill ("NOC letter generator") that covers steps 1-6 of the original workflow:
1. Find tickets in HubSpot (cancellation + new status)
2. Get company & deal info (insured, not broker)
3. Parse ticket (policy number, debt amount, template type)
4. Calculate dates (today + 7 days)
5. Fill Word template
6. Save as .docx

Google Drive eliminated from the flow — Claude edits the template directly. Steps 6-8 from original Zapier workflow still require Retool (manual). Demoing at Wednesday AI/Automations sync. 15-min walkthrough scheduled for Tue 14 Apr.

## Update (2026-04-14)

Walkthrough completed. Remaining blockers identified:
1. **HubSpot notes access** — skill only read ticket descriptions, not notes. Fixed by updating skill instructions to check both and listing explicit data points.
2. **Client address in Retool** — not in HubSpot. Options: prompt during execution, or migrate addresses to HubSpot (preferred, supports Retool transition).
3. **Downloads folder permission** — must grant each session. Exploring persistent folder options.

Next: Shreya iterating today, demoing Wed. Address storage decision needed.

## Links

- [[2026-04-02-shreya-ai-discovery]]
- [[2026-04-14-shreya-chowta-noc-skill]]
- [[underwriting-assistance-ai]]
- [[shreya-chowta]]
- Process doc: [[noc-cancellation-workflow]]
