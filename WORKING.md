# Working

## Current task

**AI-016 — Offsite AI session v4 locked.** Pre-work items are the critical path for Mon-Tue in London. Board roadmap (AI-001) due Sun 20 Apr — needs a pass this weekend or Monday morning.

## Context

Week 16 as Head of AI. Offsite Wed 22 / Thu 23 Apr. Flying to London Tuesday (Gatwick, strike dependent).

## Friday 17 Apr — completed

### Meetings ingested
- [x] Ishmael — Jay agent walkthrough. Datadog integrated (issues with user ID/session grouping). Switched from Strands to Vercel. 111 eval tests. Skills implemented file-based. Memory via Bedrock Agent Core. Most eng team has written skills. Tom extracted all Jay conversations via Datadog API.
- [x] Geran — AI Discovery. Complete team turnover (Alex left, Abs gone). Streamlit apps on Snowflake. Wants visual PM OS. "Million-dollar question: how do personal OSes talk to each other?"
- [x] Rob Grice — AI Discovery / Introduction. Week 1, former Boxfish. Strong AI user. Connected HubSpot MCP immediately. Previous sub-agent experience. Strong candidate for AI-native engineering pilot.
- [x] Jordi — Weekly. Validated three-thread model (insight → encode → self-healing). Quality/ownership concern (AI slop to stakeholders). Alerts workshop follows AI session — deliberate sequencing.
- [ ] Queency Gonsalves — AI Discovery (11:45). Not yet ingested.

### Workshop planning (AI-016)
- v4 locked in [[offsite-ai-session-draft]]
- Three stations: A4 (Jay conversations, Ishmael+Mima), B (engineering harness, Javier), C (context quality, Ollie+Liam)
- Three threads: surface insight → encode fixes → self-healing
- Three rounds × 24 mins, groups of ~6, real data at every station
- Implementation plans produced in session, Claude builds during wrap-up
- Liam Thomson invited to the offsite for Station C

### Other
- Created people file for Rob Grice
- Updated Geran people file with discovery conversation
- Updated [[ai-native-engineering]] with Rob context
- Jordi meeting note captured

## Monday 21 Apr — pre-work day (London)

### AI-016 pre-work (CRITICAL PATH)

| Task | Owner | Notes |
|---|---|---|
| LLM analysis of 200+ Jay sessions | Tom + Ishmael | Data already extracted. Run classification + trend analysis. Select top 20 worst. |
| Generate batch of draft PRs from Linear tickets | Tom + Javi | Use Claude Code against real acquisition tickets. |
| LLM review of draft PRs vs source tickets | Tom | Categorise failures: ticket gaps, implementation mistakes, review issues. |
| Pull real Linear tickets + Notion docs + external comms | Tom | Good + bad examples. Include known slop. Anonymise if sensitive. |
| Brief Ishmael (anchor A4) | Tom | In person. Station progression, co-anchor with Mima. |
| Brief Mima (co-anchor A4) | Tom | `/create-test-cases` skill is Round 2 tool. |
| Brief Javi (anchor B) | Tom | His pilot, his squad. Draft PRs are the opening data. |
| Brief Ollie (anchor C) | Tom | In person. Frame as "you're closest to this problem." |
| Brief Liam (co-anchor C) | Tom | His workflow is the reference model for Round 2. |
| Share plan with Fergus | Tom | "Three stations, real data, hard outputs. You float." |
| Confirm room layout for 3 stations | Tom | |
| Print/prepare station materials | Tom | Tue evening |

### AI-001 — Board roadmap
- Due Sun 20 Apr. Updated last Mon with capability spectrum + discovery log.
- Still needs: Fergus review, Jade conversation (unscheduled), final pass.
- Consider doing a final pass over the weekend or first thing Monday.

## Tuesday 22 Apr — offsite day 1

- Team time (morning)
- AI session (afternoon) — 90 mins
- Alerts workshop (after AI session) — Jordi leads
- Beverages with Matt Price (evening)

## Open issues

| Issue | Priority | Status | Due | Notes |
|-------|----------|--------|-----|-------|
| **AI-016** Offsite AI session | Urgent | v4 locked | Apr 22 | Pre-work Mon-Tue |
| **AI-001** Board roadmap | High | todo | Apr 20 | Final pass needed |
| **AI-010** Looker MCP cloud | High | in-progress | | Scaffolded in `outbox/`, Fargate+ALB+sidecar |
| **AI-014** Dipre Looker access | Medium | todo | Apr 18 | Resolve with Kirsty/Jaren |
| **AI-003** Discovery round | High | in-progress | | Geran + Rob done. Queency done (not ingested). |
| **AI-013** AI capability baseline | High | in-progress | Apr 20 | Feeds AI-001 |
| **AI-007** Renewals Looker→HubSpot | Medium | todo | | Blocked on AI-010 |
| **AI-009** Submissions scoping | Medium | todo | | Not started |
| **AI-011** Driver referral automation | Medium | backlog | | Fred + Shreya pairing |
| **AI-002** Skills repo ownership | Medium | todo | | Not progressed |

## Waiting on

- [ ] Emily: did Kirsty confirm address data is in Looker? (unblocks Shreya NOC full automation)
- [ ] Kirsty: HTML dashboard file + ICP analysis results
- [ ] Matt Lees: HubSpot data structure alignment with Emily + Adam
- [ ] Jemima: Three communication style guides
- [ ] Rakhee: Apr 23 town hall slot confirmation for AI workshop
- [ ] Javier: PoC progress on HubSpot→Claude→Flock API quoting (~by Apr 24)
- [ ] Belbin assessment: complete before Thu 23 Apr morning
- [ ] Fergus: review board roadmap before Sun 20

## Reminders

- Look at Flock Roadmap DRAFT in Flock PbA Strategy in Notion
- London next week: fly Tue (Gatwick→Thameslink→Farringdon), in office Wed/Thu
- Beverages Wed with Matt Price
- Smith leaving — announcement next week
- AWS Summit Wed 22 (AI track) — Flock under-represented, scheduling clash with offsite
- Ingest Queency Gonsalves meeting on Monday
