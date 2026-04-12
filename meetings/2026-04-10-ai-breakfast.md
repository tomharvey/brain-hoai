---
title: AI Breakfast
created: 2026-04-10
updated: 2026-04-10
domain: ai-enablement
type: meeting
tags: [ai-breakfast, demos, show-and-tell]
---

# AI Breakfast

Team-wide AI show-and-tell session. Brought forward from next week by [[ollie-crowe]]. Good turnout despite short notice. Three demos planned; two delivered (Ollie postponed his).

## Attendees

- [[matt]] (presenter — sales outreach pipeline)
- [[kirsty]] (presenter — AI-powered dashboarding)
- [[ollie-crowe]] (organiser, postponed demo on Claude Co-Work scheduled briefings)
- [[fergus]]
- [[adam-smith]]
- [[emily]]
- Tom (me)
- Others on call (Anton mentioned, Francesco referenced)

---

## Demo 1: Automated sales outreach pipeline — [[matt]]

Matt built an end-to-end prospecting pipeline using Claude Code scheduled agents (~10 days of work). Chain of agents running daily:

### How it works
1. **Evening**: Pipeline expansion agent finds new target accounts (large fleets, 200+ vehicles)
2. **Morning**: Pipeline importer consolidates into a master JSON file (single source of truth)
3. **Email monitor agent**: Checks replies, bounces, out-of-offices from last 24hrs
4. **Validation agent**: Enriches new accounts with contact details, email formats
5. **Draft agent**: Creates personalised Gmail drafts for review
6. **Slack summary**: Daily digest of all activity

### Integrations
- **Gmail** — reads replies/bounces, creates drafts
- **Slack** — daily activity summaries
- **Apollo.io** — third-party contact validation (not perfect yet, needs work)
- **HubSpot** — checks for existing relationships to avoid upsetting brokers (critical guardrail)
- **Granola** — pulls context from previous calls
- **Google Drive** — account action plans as PDFs

### Results (1 week in)
- 549 accounts in pipeline (including CSV import of prior manual list)
- 44 companies engaged
- **89% email accuracy** (vs ~60% with manual tools)
- 3 genuine replies, 1 meeting booked (Speedy Hire, ~900 vehicles, Monday)
- A/B testing different outreach styles (short vs detailed)
- Human-in-the-loop throughout — all drafts reviewed before sending

### HubSpot example
Surfaced Sixt as a target, identified low-level contacts, found better contact (Andrew Smith, MD), discovered Anton had met him at MOVE conference — correctly flagged to pause and loop in Anton.

### What's working / not working
- Contact sourcing, validation, draft quality, HubSpot checking — all working well
- Scheduled tasks unreliable (needs laptop open) — running manually on login for now
- Apollo integration needs improvement
- Some drafts use full names in a way that reads as obviously AI

### Next steps
- Simplify the pipeline (Matt feels it's over-engineered)
- Fix scheduling reliability
- Push data into HubSpot as source of truth
- Scale outreach volume
- Goal: full TAM coverage with progress tracking per account
- Adam interested in replicating for broker distribution team
- Potential to export agent template for other commercial roles
- Use similar approach to clean up stale HubSpot contact data

---

## Demo 2: AI-powered revenue driver dashboard — [[kirsty]]

Kirsty demonstrated an interactive HTML dashboard built in Claude, pulling data via Looker MCP. Originally shown at Flock O'Clock two weeks ago; presented here at Ollie's request.

### Three problems AI solves for dashboarding
1. **Insight extraction** — AI can summarise what's happening in natural language rather than forcing users to drill down manually
2. **Visualisation** — moving beyond KPI blocks and charts to "driver trees" that show causal relationships (if this goes up, that goes up)
3. **Requirements capture** — photographed a hand-drawn tree diagram, Claude built the dashboard from it. Shortcuts the traditional BA-to-developer back-and-forth

### How it was built
- Connected to Looker via MCP
- Uploaded a photo of a hand-drawn driver tree
- Claude got it ~60% right first time; 40% was tweaking (data source corrections, dynamic animated lines, layout)
- Insights auto-generated along each node of the driver tree

### Example insight
902 submissions last quarter. 57% were trade, but only 19% of closed deals are trade — highlighting a conversion gap.

### Discussion highlights
- [[fergus]] raised the key caveat: making things look cool is easy; the real skill is ensuring insights are actionable ("the so what")
- [[matt]] counter-point: the visual format itself triggers different thinking and creative connections
- I raised the "insight loop" problem: how do we stop the same insights appearing week after week? The insight text itself needs to become input data for future analysis
- Adam noted this replaces archaic/disparate screenshot-based trading packs

### Productionisation ideas
- Convert to a Claude skill file (Kirsty: ~10 mins)
- Cron job to regenerate daily, save to Google Drive
- Or serve as HTML on a server with live API connections
- **Blocker from me**: need to give everyone's Claude access to Looker MCP (on my to-do list)

---

## Demo 3: Scheduled daily briefing with Claude Co-Work — [[ollie-crowe]]

Postponed to next session (ran over time).

---

## Actions

- [ ] **Tom**: Give all Claude users access to Looker MCP — mentioned as a key enabler for dashboarding and data access across the business
- [ ] **Matt**: Share token usage/cost analysis with the group (Notion page exists)
- [ ] **Matt**: Catch up with Tom re: Apollo.io integration issues
- [ ] **Matt**: Review and simplify pipeline in ~1 week — reduce Slack summary complexity
- [ ] **Kirsty**: Convert dashboard into a shareable skill file
- [ ] **Kirsty/Tom**: Get dashboard in front of Adam/Christian for feedback on insight quality
- [ ] **Ollie**: Demo scheduled briefings at next AI Breakfast

---

## Themes

- **HubSpot as source of truth** — strong consensus that HubSpot should be the canonical data store for sales/broker data, with Claude as a window into it. Kirsty and Adam both reinforced this.
- **Data quality compounds** — Kirsty's point that the best results from Telemetry MCP came from investing in data quality, not prompt engineering. Same principle applies to contact data.
- **Human in the loop** — Matt emphatic that full automation of outreach is not the goal. Human review of drafts is essential to avoid obvious AI tone.
- **Insight loops** — recurring insight is stale insight. Need to feed previous insights back as context so dashboards surface what's *changed*, not what's *known*.
- **Engagement as value** — even "just cool" dashboards serve a purpose by drawing people in and changing how they think about data.

---

Full transcript: [[2026-04-10-ai-breakfast-transcript]]
