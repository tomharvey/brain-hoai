---
title: Enterprise Engine — Technical Review (2 Apr 2026)
created: 2026-04-02
updated: 2026-04-02
domain: engineering-workflows
type: reference
author: matt-lees
tags: [enterprise-engine, agents, apollo, hubspot, pipeline, distribution]
---

## Source

Written by [[matt-lees|Matt Lees]] for Fergus and Tom. Converted from Notion export on 2026-04-02. This is the most detailed agent architecture document in the company.

## What changed in 48 hours

Pipeline went from **18 accounts to 64 accounts** and from 5 agents to **9 scheduled agents + 1 action plan updater**. Three new capabilities: Apollo.io integration for verified contact data, MEDDPICC-scored account action plans, and 3-day follow-up timing rule.

Total estimated pipeline value: **£294M** across utilities, construction, logistics, public sector, facilities management, and telecoms.

## Agent architecture

Nine agents run autonomously on weekday schedules. Each reads from and writes to a central pipeline JSON file. All outputs go to Matt's Slack DM — nothing posts to team channels.

### Morning chain (sequential dependencies)

| Time | Agent | What it does | Connectors |
|------|-------|-------------|------------|
| 06:15 | Email-CRM Sync | Scans Gmail for replies, bounces, OOOs. Updates pipeline contacts and statuses. | Gmail |
| 06:30 | Pipeline Validator | Scores all accounts by renewal urgency, premium, data completeness. Flags critical gaps. | File system |
| 07:00 | Research & Enrichment | Uses Apollo + web search to verify emails, find contacts, fill insurer/broker/telematics gaps. Target: 8-12 accounts/run. | Apollo, Web |
| 07:45 | Outreach Drafts | Generates personalised emails using approved template. Enforces 3-day follow-up rule. Saves as Gmail drafts. | Gmail |
| 08:00 | Daily Briefing | Compiles all overnight outputs into a single summary. | Slack (DM) |
| 08:15 | Outreach Validator | Cross-references contacts across Gmail, Slack, Granola, web. Creates validated Gmail drafts. | Gmail, Slack, Granola |

### Afternoon batch

| Time | Agent | What it does | Connectors |
|------|-------|-------------|------------|
| 17:00 | Pipeline Expansion | Uses Apollo prospecting + web research to discover 8-12 new accounts/day matching Flock's ICP. | Apollo, Web |
| 17:30 | Action Plan Updater | Refreshes all account action plan cards with the day's progress from every other agent. | File system |

### Weekly

| Time | Agent | What it does | Connectors |
|------|-------|-------------|------------|
| Fri 17:00 | Weekly Report | Pipeline funnel analysis, outreach metrics, email validation, key wins/risks, next-week priorities. | File system, Slack (DM) |

### Design rules baked into every agent

- Never send emails — always create Gmail drafts for Matt's review
- Never post to team Slack channels — DM only
- 3 working day minimum before follow-up (exceptions: OOO redirects, warm referrals, prospect replies)
- Minimum 2-3 contacts per account before outreach
- Apollo is primary enrichment tool; web research is fallback

## Connectors

| Connector | Purpose | Used by |
|-----------|---------|---------|
| Gmail | Read replies/bounces, create drafts | Email-CRM Sync, Outreach Drafts, Outreach Validator |
| Slack | DM briefings and alerts to Matt | Daily Briefing, Weekly Report, Outreach Validator |
| Granola | Meeting transcript search for deal context | Outreach Validator |
| Apollo.io | Contact enrichment, email verification, ICP prospecting | Research & Enrichment, Pipeline Expansion |
| Google Drive | Account action plan storage (Enterprise Prospecting folder) | Action Plan Updater |
| Notion | Internal documentation and reporting | Ad-hoc |

## Token consumption and cost

Measured from full run on 2 Apr 2026:

| Agent | Tokens | Tool calls | Runtime |
|-------|--------|-----------|---------|
| Pipeline Validator | 122,480 | 6 | 102s |
| Research & Enrichment | 136,583 | 44 | 194s |
| Pipeline Expansion | 114,783 | 31 | 268s |
| Daily Briefing | 113,630 | 6 | 26s |
| Email-CRM Sync | ~60,000 (est.) | 8 | ~60s |
| Outreach Drafts | ~80,000 (est.) | 12 | ~90s |
| Outreach Validator | ~100,000 (est.) | 20 | ~120s |
| Weekly Report | ~80,000 (est.) | 8 | ~60s |
| Action Plan Updater | ~100,000 (est.) | 15 | ~90s |
| **Daily total** | **~910,000** | **~150** | **~17 min** |

**Monthly projection (22 working days):**
- Scheduled agents: ~20M tokens/month
- Ad-hoc conversations: ~5-10M tokens/month
- **Total: ~25-30M tokens/month**

**Cost:**
- Claude Team plan: ~$25-30/month (existing)
- Apollo Growth plan: **$104/month** (10,000 credits/month, currently using ~750/month)
- **Total incremental cost: $104/month**

**Risk:** Team plan rate limits may trigger at scale. If so, evaluate moving some agents to Claude API (~$130/month on Sonnet).

## Account action plans

Each priority account gets a living document:
- Account overview (fleet, premium, insurer, broker, telematics, renewal)
- Stakeholder map with email verification status and multi-threading gap analysis
- MEDDPICC qualification scored 1-5 per dimension
- Flock-specific value proposition hooks
- Phased tactical action plan (phone, email, LinkedIn, broker, events, senior stakeholder engagement)
- Competitive intelligence
- Daily progress log auto-populated from all agent runs

Stored as HTML cards (viewable in browser) + JSON (for programmatic updates). Action Plan Updater refreshes daily at 17:30.

## Data security

| Concern | Current state |
|---------|--------------|
| Pipeline data | Local JSON file in Claude workspace. Not synced to external databases. |
| Email access | Gmail MCP — read-only + draft creation. Cannot send without Matt's manual action. |
| Contact data | Apollo (commercial data provider) + publicly available web sources. No scraping. |
| Slack access | DM delivery only. No channel posting. Read access for context. |
| Account action plans | Locally + Google Drive (Enterprise Prospecting folder). |
| Who can trigger agents | Matt only — via Cowork desktop app. Scheduled tasks run under Matt's session. |
| Data retention | Pipeline JSON persists in workspace. Agent outputs overwritten daily. Weekly reports archived. |

**Open question:** Local-file approach acceptable at this stage, or move to structured storage (HubSpot custom objects, lightweight database) as pipeline scales past 100 accounts?

## Claude API vs current approach

| | Current (Agents + Apollo) | Claude API + Apollo |
|---|---|---|
| How it works | Scheduled agents, automatic | API calls from dashboard UI, on-demand |
| Enrichment speed | Batch (scheduled times) | On-demand, instant |
| Cost | Team plan + $104/month Apollo | ~$130-660/month API + $104/month Apollo |
| Setup effort | Done — fully operational | Needs API key, front-end integration, auth, error handling |
| Best for | Daily pipeline maintenance at scale | Ad-hoc deep dives, real-time enrichment during calls |

**Matt's recommendation:** Agent approach covers 90%. API integration only for real-time enrichment during calls and bulk segment discovery.

## Pipeline snapshot (2 Apr 2026)

- **64 accounts** (was 18 on 31 Mar)
- **£294M** total estimated premium
- **2 engaged** accounts with replies (Manchester City Council, Wincanton/GXO)
- **12 accounts enriched** via Apollo today
- **12 new accounts** discovered and added today
- **22% reply rate** on first outreach batch (2 replies from 9 emails)

## Links

- [[matt-lees]]
- [[2026-04-02-matt-lees-enterprise-engine]]
- [[agent-framework]]
- [[AI-005-hubspot-enterprise-engine]]
