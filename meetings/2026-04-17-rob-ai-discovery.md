---
title: Rob Grice — AI Discovery / Introduction
created: 2026-04-17
updated: 2026-04-17
domain: ai-enablement
type: meeting
tags: [discovery, rob, acquisition, developer-os, ai-native-engineering, submissions]
---

## Attendees

- [[rob|Rob Grice]]
- Tom Harvey

## Key themes

### Background

- First week at Flock. Former Boxfish engineer (cyber security awareness platform).
- First in-house engineer hire at Boxfish — full-stack across entire stack. Left because he hit a learning plateau and needed senior mentorship.
- Strong AI user since 2023-24. Claude is his primary tool — uses it as "senior engineer" for code review and brainstorming.
- Previous sub-agent experience: orchestrating agent + sub-agents across 9 repos to debug database performance issues at Boxfish.
- Initially feared career displacement when ChatGPT launched (2022) — now deeply integrated into workflow.

### Current work at Flock

- Acquisition team (Ollie's squad). All greenfield.
- Building ingestion/extraction pipeline for submissions (discovery phase).
- Connected Claude to HubSpot MCP already — exploring underwriting process through it.
- Working toward "golden schema" for quote field extraction from documents — document classification, data extraction, required vs optional fields, ping underwriter for missing data.
- Running Claude at repo root level. Hasn't seen many CLAUDE.md files in repos yet.

### AI workflow patterns

- Single prompting with iterative editing for smaller tasks
- "Word vomiting" context at Claude for brainstorming — picks out golden bits from mixed-relevance responses
- Doesn't currently encode lessons ("I just kind of work around when it does make mistakes")
- Interested in the progression: markdown instructions → formal skills → deterministic scripts

### Developer OS conversation

- Tom showed his vault live. Rob was visibly engaged.
- Discussed: Linear/GitHub integration, automated ticket awareness, AI-assisted PR reviews, draft implementations from Linear tickets
- Rob's former colleague at Boxfish had a working Jira→GitHub→OpenClaw pipeline — small tickets sometimes done first try
- Key framing from Rob: "even if AI gets really good, humans need to remain in the loop at the specification stage"
- Rob asked what to expect from Wednesday — Tom said hands-on, not just waffling

### AI industry observations

- Aware of subsidy economics ($20 subscription costs Anthropic ~$200 in inference)
- Pragmatic about SaaS: "just build your own CRM" is a nonstarter, but development tooling is different
- "I would pay a lot... competing with rent" for AI access

## Actions

- [ ] Rob to ping Tom on Slack with ideas for Wednesday session — Rob
- [ ] Create CLAUDE.md awareness — Rob hasn't seen many in the repos — Tom to flag

## Notes

Rob is exactly the profile for the AI-native engineering pilot: brand new (no legacy habits), already using AI as primary tool, on the greenfield acquisition squad, engaged with the OS/harness concept, and explicitly interested in the "how do we encode learning" question. Week 1 ramp-up is a factor but his enthusiasm and prior sub-agent experience suggest fast adoption.

Ollie was discussed but not on the call. Rob has heard the developer OS pitch and the pilot concept. Ollie has not — he'll need separate briefing before Station B.

Full transcript: [[2026-04-17-rob-ai-discovery-transcript]]
