---
title: Fergus <> Tom — Weekly
created: 2026-06-04
updated: 2026-06-04
domain: ai-enablement
type: meeting
tags: [ai-enablement, engineering-workflows, fergus, lean-units, mcp, bdm-brain, platform-reliability]
---

# Fergus <> Tom — Weekly

**Date:** 2026-06-04 11:15 GMT+2
**Attendees:** [[fergus]], Tom Harvey
**Full transcript:** [[2026-06-04-fergus-weekly-transcript]]

---

## Key themes

### AI framework and activation progress
- Framework covers most of the company across 5 stages (0=search, 1=conversation, 2=context+tools, 3=fluency, 4=proactive delegation)
- ~6 people need sweep-up to reach stage 1–2
- Split emerging: half-dozen champions at advanced levels; equal or more doing nothing or actively avoiding
- Jade avoiding weekly AI check-ins — when finally discussing, spoke about team hackathon rather than personal usage; Tom suspects conflation of individual and team work
- Ed (CEO) framing is **process and action** oriented, not outcomes oriented — recommending reading X for "3–5 years ahead" information rather than focusing on practical application. Counter-framing needed: "more Antoine, less Ed"

### AI skill adoption pattern
- Fred took Emily's Driver Referral skill and created a Fred-specific version — right instinct
- Tick-boxing risk: "I have built a skill" vs. "this skill is doing what I need"
- Next quarter focus: use-case specificity, not company-wide "burn the tokens" push
- People who haven't yet made the personal use-case leap need guided identification of *their* outcome, not examples from others

### Group therapy sessions output
- Key concerns surfacing: "How do I find the joy?" and "How do I not lose my mind?"
- Alex Dyball's code review concern: "if I'm working in a thing I don't understand, how do I validate its output?"
- Tom's answer: require explanation, not just action — send receipts; ask for trade-offs and alternatives; teach it like a junior engineer
- Metacognition (thinking about thinking) is where genuine learning re-emerges

### BDM AI Brain — explained
- Not the standard Notion MCP — a custom MCP proxying Notion with extra validation context
- Semantic layer specific to BDM thinking patterns: cross-referencing, front-matter categorisation, BDM-domain first-class objects
- Integration with HubSpot and Granola alongside Notion
- Self-improvement loop: usage analysis built in so the system can improve itself
- First-class objects exist in BDM world that differ from engineering/CS — BDM layer is different from a Flock-wide layer
- Start with BDM; end goal is company-wide spread if proven
- Fergus's vision: company-wide approach to storing context in Notion through a consistent filter regardless of team

### MCP read/write governance gap
- More people connecting to HubSpot, Notion, etc. via standard MCP connectors — good for sense-making; risk is inadvertent writes or deletes
- Example: Ivan accidentally deleted all content in a Notion page (audience of one — low blast radius); same pattern on HubSpot would be catastrophic
- Read vs. write distinction is **not yet in the governance vernacular**
- No staging environments in the rest of the org the way engineering would use them
- No clear answer yet — but needs to be thought through; AWS MCP gateway exists as a possible routing solution
- Interim quick answer: can we just prevent deletes from HubSpot entirely? Most delete use cases can be replaced with archiving/pipeline moves

### Platform reliability
- Reliability noise is partly a **communications problem**: platform was over-sold as fixing all legacy bugs; reality is bugs still happen, need hypercare framing
- Root cause also partly structural: lack of systematic release approach, limited automated testing, no unit test coverage metrics tracked (decision made during DD with Admiral)
- Not entirely explained by velocity; some structural gaps in engineering discipline

### Lean units
- Fergus exploring: small teams (2–3 people) on specific objectives with removed obstacles and full AI/tooling access
- Prototype: [[ivan-boix]] + [[ishmael-jebril]] on J — covered a lot of ground
- Risk: creating a two-tier system between exciting sprint teams and the maintenance work
- Possible model: a team goes "bankrupt on their bug budget" and becomes temporarily platform-focused until stable again
- Tension: how do you maintain a lean unit's focus after the sprint phase transitions to maintenance?

### London visit
- Tom coming to London the week after Cardiff (~mid-July 2026)
- Passport expected back by then
- Half-day workshop rather than full day (to leave room for other meetings, potential Admiral overlap)
- Fergus to schedule something that same week

---

## Actions

- [ ] Tom: visit London week after Cardiff — schedule half-day workshop with Fergus — [[AI-095]]
- [ ] Tom + Fergus: agree approach to MCP read/write governance, at minimum a quick answer on HubSpot delete prevention — [[AI-096]]
