---
title: "Assess HubSpot architecture for Enterprise Engine integration"
id: AI-005
created: 2026-04-02
updated: 2026-04-02
due: 2026-04-07
origin: "[[2026-04-02-matt-lees-enterprise-engine]]"
domain: operational-tooling
type: issue
status: done
priority: high
assignee: tom
tags: [hubspot, enterprise-engine, matt-lees, agents]
---

## Description

Matt Lees' Enterprise Engine (9 autonomous agents managing a £294M enterprise sales pipeline) currently stores all data in a local JSON file on his laptop. The next step — agreed with Fergus — is connecting to HubSpot so enriched fleet data is visible and backed up.

## Acceptance criteria

- [ ] Understand HubSpot's current company record structure — what fields exist, who owns the schema
- [ ] Confirm enriched fleet data (company size, sector specialisms, Apollo contacts, email verification status) can be stored on **company records** without impacting existing **deal records**
- [ ] Identify any conflicts with Adam + Emily's HubSpot clean-up project
- [ ] Recommendation ready before Matt Lees call (Tue 7 Apr, 10:30 CEST)

## Notes

- Matt is not yet connected to HubSpot in Claude — this is the biggest gap and easiest governance win
- Data to store: fleet size, sector, insurer, broker, telematics provider, renewal date, Apollo-enriched contacts with verification status
- Must go on company records, not deal records — per call with Fergus
- Adam + Emily have a parallel HubSpot clean-up project — check for overlap
- HubSpot MCP connector is available but not yet connected in Matt's Cowork

## Resolution

Resolved in [[2026-04-07-matt-lees-enterprise-engine-002]]. Matt connected HubSpot to Claude (with Emily's help). Direction confirmed: AI-generated data goes on **company records**, not deal records — avoids overlap with underwriting team's BAU on deal properties. Matt is leading the conversation with Emily and Adam on data structure as he explores write permissions incrementally.

## Links

- [[2026-04-02-matt-lees-enterprise-engine]]
- [[2026-04-07-matt-lees-enterprise-engine-002]]
- [[agent-framework]]
- [[matt-lees]]
