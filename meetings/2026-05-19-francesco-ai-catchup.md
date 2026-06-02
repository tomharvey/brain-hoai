---
title: Francesco Venerandi — AI catchup
created: 2026-05-19
updated: 2026-05-19
domain: ai-enablement
type: meeting
tags: [francesco, pricing, performance-coach, hackathon, transcripts]
---

## Attendees

- [[francesco-venerandi|Francesco Venerandi]]

Full transcript: [[2026-05-19-francesco-ai-catchup-transcript]]

## Key themes

### Performance coach system (Francesco + Ollie)

Francesco and [[ollie-crowe|Ollie]] have built a career coaching system using MCP:

- Instructions stored as MD files in GitHub, auto-updated via MCP — releasing new versions is just a push
- Connects to Granola (transcripts), Slack, Notion, and Google Calendar for data aggregation
- Saves progress locally in Claude workspace (doesn't overwrite personal context on update)
- **Three functions:**
  1. **Weekly progress tracking** against [[milan-chavda|Milan]]'s promotion criteria — ranks activities against goals, generates monthly progress logs with gap analysis
  2. **1:1 meeting prep and follow-up** — pre-meeting agenda with focus areas; post-meeting action items and feedback breakdown; connected to GCal for automated scheduling
  3. **Weekly performance coaching** — identifies improvement areas, currently focused on assertiveness and leadership framing for Francesco
- Currently used by Francesco, [[ollie-crowe|Ollie]], and potentially [[javier|Javier]]
- Code on GitHub — Francesco to share access with Tom
- Requires a promotion rubric from your manager as the starting point; prompts for it if missing

**Tom's reaction**: Milan providing a written promotion rubric is the right practice and Flock should do this more broadly. The tool makes the implied visible.

### Pricing team AI bottleneck

- Pricing team consistently deprioritised despite strong interest
- Core blocker: pricing model inputs scattered across 20–30 database tables; the JSON sent to the pricing service is not saved anywhere
- Planned solution with [[ollie-crowe|Ollie]]'s team: save pricing JSON automatically when quotes are generated; output model relativities for underwriter transparency
- **Tom's alternative approach**: extract data directly from Postgres/Snowflake/data lake — it's all there. Build a script to recreate the JSON formation process. Don't wait for team resources.
- Tom: "I may be wrong but if this JSON gets created and sent to the pricing service, you could ask Claude Code to find where it's constructed and write a script to also save it — could knock that out in an hour"
- Francesco wants to transition from "using AI to build things" to "building AI systems" — wants more involvement in the technical AI layer

### Planned hackathon

- Francesco and [[javier|Javier]] planning a 2-day office hackathon to accelerate pricing automation
- Easier to block 2 days and sit together than keep context-switching

### Transcript service

- Tom flagged that every team needs a transcript service and only Ben/Daisy currently have one
- Francesco's existing Granola-based service is the starting point
- Will follow up separately

## Actions

- [ ] **Francesco**: Share GitHub repo access for performance coach (Tom's username: tomvey)
- [ ] **Francesco**: Research pricing data extraction requirements this week — what's in Postgres/Snowflake that could reconstruct the JSON
- [ ] **Tom + Francesco**: Schedule 2-day office hackathon with [[javier|Javier]] for pricing automation
- [ ] **Tom**: Follow up with all teams on transcript service needs (see [[AI-050]])

## Notes

- Milan gave Francesco a written promotion rubric — this is the input that makes the performance coach work. Not the norm at Flock, should be.
- The performance coach tool is a real candidate for company-wide adoption once polished.
- Francesco has been back from Mexico one day — in the office tomorrow.
