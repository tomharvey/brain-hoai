---
title: "AI — Sophie Dodds"
created: 2026-06-23
updated: 2026-06-23
domain: ai-enablement
type: meeting
tags: [sophie-dodds, distribution, bdm-brain, daily-brief, ai-discovery]
---

## Attendees

- [[sophie-dodds]] (Sophie Dodds, Broker Distribution Manager)
- Tom Harvey

Full transcript: [[2026-06-23-sophie-dodds-ai-transcript]]

---

## Key themes

### BDM Brain — gaps and friction

- Sophie using her personal Claude folder more than the BDM Brain — daily brief is more evolved from personal folder
- Adding BDM folder to queries sometimes, but inconsistently
- Daily brief (Notion): urgent actions from Granola/email/Slack, upcoming meetings, last week's overview, open pipeline
  - Pipeline data still inaccurate; broker name missing from entries
  - Used as a quick morning scan — what's in price, what needs a call, any new submissions
- Meeting summaries auto-Slack 15 mins after each call but require manual proofread (AI misses nuance, occasionally conflates conversations)
- Distribution channel updates still done manually (copy/paste from Granola summary, add context)
- Granola template for distribution updates degrades with repeated edits — keeps losing GWP, client context, underwriter tags. Root cause: Granola template vs a proper Claude skill

### Improvement plan

- Daily brief should be rebuilt as a Claude skill inside the BDM Brain
  - Select both personal and BDM folders; store output in "Sophie's Daily Briefings" folder
  - Also output top 5 urgent/overdue items to Slack each morning
- Slack ping loop: set Claude to check for replies every 10 mins so Sophie can respond on mobile without opening laptop
- BDM Brain value grows with more data fed in — raw Granola transcripts are the foundation; distribution channel summaries teach it what the team cares about
- Cross-referencing payoff: if Alex speaks to a broker Sophie also knows, the brain can surface the connection proactively
- Coaching setup: easy to start — point at last 10 transcripts plus feedback received; keep in personal folder (not BDM Brain)

### On AI more broadly

- Biggest gap between "wow" and "goodish" users is context fed in, not the tool itself
- AI better at task-driven work partly because it's easier to give task-based instructions
- Relationship-driven work needs more context to be useful — but the brain is building it up over time

---

## Actions

- [ ] [[sophie-dodds]]: rebuild daily brief as a Claude skill in the BDM Brain → [[AI-134]]
- [ ] [[sophie-dodds]]: set up coaching task in personal Claude folder, point at last 10 transcripts
- [ ] [[sophie-dodds]]: start piping Granola transcripts into the BDM Brain
