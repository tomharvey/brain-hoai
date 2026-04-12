---
title: Paul O'Neill — AI Discovery
created: 2026-04-10
updated: 2026-04-10
domain: operational-tooling
type: meeting
tags: [discovery, compliance, risk, measurement, data-quality]
---

# Paul O'Neill — AI Discovery

Discovery call with [[paul]] (Head of Risk and Compliance). Extremely rich conversation. Paul is a thoughtful, experienced user whose core frustration is that the things he most needs to measure aren't being captured as data — so AI can't help him yet.

## Attendees

- [[paul]]
- Tom (me)

---

## Current AI usage

### Tools
- **ChatGPT and Claude** — task-driven, not repetitive/process-embedded
- Uses memory function to store Flock context
- Not building workflows or embedded processes — each use is a one-off task

### Use cases
1. **Policy drafting and document summaries**
2. **Web scraping / horizon scanning** — regulatory updates, new legislation, filtered for Flock relevance (motor fleet, MGA, broker distribution)
3. **Comparison analysis** across multiple sources
4. **Risk analysis** and compliance plan restructuring with additional KPIs

### Prompt skill
Paul has strong prompt writing instincts from years of targeted Google searching for regulatory intelligence. Already iteratively refining prompts to reduce irrelevant results (e.g. filtering out South American regulations).

---

## The measurement gap

Paul's central thesis: **AI can't help with compliance if we're not capturing the data that compliance needs to measure.**

### Underwriting compliance
- Admiral delegated authority comes with guardrails and red lines
- The underwriting system doesn't capture data against those guardrails
- Example: Billy has a £25k authority limit — but the system doesn't enforce or monitor it
- Andy manually checks underwriting quality, but his outputs don't create reusable datasets
- **Can't deploy an agent to monitor compliance because there's no data capture**
- Even referral triggers (the guardrails that keep people within authority) aren't systematically captured — referrals happen offline

### The three-step requirement
1. **Define what good looks like** — hard KPIs, not subjective assessments
2. **Capture the relevant data points** — system must record against the definition
3. **Measure and police** — then AI/agents can do ongoing compliance monitoring

### Delegated authority pressure
- As referrals decrease, oversight expectations increase
- Must demonstrate adherence to both explicit and implicit requirements
- If underwriters aren't referring, they're presumably acting within authority — but we can't prove it

---

## Cultural measurement

Paul extended the measurement gap beyond compliance into culture:

- **Meeting attendance** (Start the Week, Flock O'Clock) — not tracked
- **Notion readership** — supposed to measure policy understanding, but Notion isn't a real single source of truth
- **Time allocation** — in Google Calendar but not analysed
- **Slack traffic patterns** — unmeasured
- **Survey validation** — SLT visibility survey says leadership is less visible, but Anton was on 6 weeks paternity, Ed on 6 weeks paternity, in a 15-week period. Christian in Denmark. Darren in office daily, Fergus 4 days/week. The data would have challenged the survey finding.

### Key quote
*"If we measure more, then AI helps me more. But if we don't create those data points, we can't do that analysis."*

---

## Connection to broader themes

- Resonates with the automation conversation: can't automate a poorly defined business process (same issue I'm hitting with cancellation notices for UW assistants)
- The strategic value isn't in automating individual tasks — it's in **documenting business processes so we can measure compliance against them**
- Paul has wanted this for 12 months but it hasn't been a business priority at current scale
- At scale, it becomes essential — build the measurement infrastructure now

I committed to **trying to answer some of his pointed measurement questions next week** — particularly around calendar analysis and time allocation data.

---

## Actions

- [ ] **Tom**: Attempt calendar/time analysis for Paul next week — meeting time, attendance patterns
- [ ] **Tom**: Explore what cultural data points are capturable now (Google Calendar, Slack, Notion readership)
- [ ] **Paul/Tom**: Longer-term — define underwriting compliance KPIs that could be measured if data capture was in place

---

Full transcript: [[2026-04-10-paul-ai-discovery-transcript]]
