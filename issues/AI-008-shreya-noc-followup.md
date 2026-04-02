---
title: "Follow up with Shreya on Claude NOC test results"
id: AI-008
created: 2026-04-02
updated: 2026-04-02
due: 2026-04-07
origin: "[[2026-04-02-shreya-ai-discovery]]"
domain: operational-tooling
type: issue
status: todo
priority: medium
assignee: tom
tags: [shreya, cancellations, claude, hubspot, noc]
---

## Description

Shreya is testing the Claude + HubSpot approach for NOC (cancellation notice) automation — feeding the Word template to Claude and asking it to fill in details from HubSpot tickets. Follow up to see how it went and help iterate on the prompt if needed.

## Acceptance criteria

- [ ] Check in with Shreya — did the Claude + template test work?
- [ ] If it worked: help refine prompt filtering (stage, date, connectivity threshold)
- [ ] If blocked: diagnose and suggest next steps

## Notes

- She connected HubSpot to Claude live on the call — initial test pulled tickets correctly but included closed/historical ones
- Policy numbers follow ADMFL or HVFL format — good for prompt hints
- NOC Word template needs to be replicated (not edited) for each cancellation
- She was going to try immediately after the call

## Links

- [[2026-04-02-shreya-ai-discovery]]
- [[underwriting-assistance-ai]]
- [[shreya-chowta]]
- Process doc: [[noc-cancellation-workflow]]
