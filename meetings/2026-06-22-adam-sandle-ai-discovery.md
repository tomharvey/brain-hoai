---
title: "AI discovery — Adam Sandle"
created: 2026-06-22
updated: 2026-06-22
domain: ai-enablement
type: meeting
tags: [adam-sandle, claims, ai-discovery, automation, admiral]
---

## Attendees

- [[adam-sandle]] (Adam Sandle, Claims Operations Associate)
- Tom Harvey

Full transcript: [[2026-06-22-adam-sandle-ai-discovery-transcript]]

---

## Key themes

### Current AI usage

- ChatGPT: mainly email tone checking ("make sure it's not aggressive" / "make it firmer")
- Claude MCP: reviewing telemetry data on high-end vehicles to flag unwanted risks
- FNOL report skill (built with Ollie): sends first notice with a prompt that generates a 2-page large-loss report for Hamilton Fraser (HF) on claims likely over £100k
- Brokers often send vague complaints; uses AI to decode what the actual issue is
- "Company-wide AI sessions are too broad; one-to-one sessions get 100x more done"

### Admiral claims review automation — live session

- Daily Admiral data arrives via Snowflake download link (Jacob's setup, 12pm each day)
- Process: filter by fleet, copy data into a multi-tab template (one per fleet), ~5–6 fleet renewals/month, Admiral reviews ~35–40
- Live session: shared Snowflake download link + Google Sheet template with Claude (Opus 4)
- Approach: "pretend you're a new staff member — ask me questions, don't make assumptions"
- Goal: teach Claude the job so it eventually runs from a single prompt/skill
- Treat it like a junior hire: correct it daily until it gets it right

### Cadence

- Agreed fortnightly check-ins to find and automate the next thing
- Tom to share recording of Tuesday AI session if available

---

## Actions

- [ ] Adam Sandle: continue teaching the Admiral claims review to Claude; correct it daily → create a skill once working
- [ ] Tom: fortnightly check-in with Adam to find next automation → [[AI-131]]
- [ ] Adam: check Google Calendar for recording of Tuesday AI session (missed due to Admiral meeting)
