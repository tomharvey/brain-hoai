---
title: Fred / Thomas — AI Catch-up
created: 2026-06-03
updated: 2026-06-03
domain: ai-enablement
type: meeting
tags: [ai-enablement, underwriting, skills, driver-referral, fred-bush]
---

# Fred / Thomas — AI Catch-up

**Date:** 2026-06-03 13:00 GMT+2
**Attendees:** [[fred-bush]], Tom Harvey
**Full transcript:** [[2026-06-03-fred-thomas-ai-catchup-transcript]]

---

## Key themes

### Driver Referral Skill
- Fred is using the Driver Referral Decision skill Emily built — processes HubSpot tickets for out-of-standard drivers (age, experience, claims, convictions)
- Connects to Looker, checks connectivity and loss ratios, generates a decision against the underwriting framework, updates HubSpot with reasoning
- Team now has decision authority — no longer sends referrals to underwriters
- Still manually checking AI decisions during early implementation; it's saving time even with oversight
- Known limitation: connected to Looker but not Resource — vehicle count pulled from schedule (all-time) not current cover

### Skills vs. long chats
- Fred has been training the AI in a single long chat rather than updating the skill — context accumulation risk
- Four team members each want different output layouts; standardising the skill is not always the right call
- During the meeting, created a "Fred Driver Referral Decision" skill incorporating all learning from the existing chat
- Key pattern: if you keep correcting the AI in a chat, do a weekly "bake in" to the skill rather than relying on long-context memory

### Parallel processing
- While the AI processes a driver referral in the background, Fred works other tickets — genuine parallel productivity gain
- No existential fear of AI; Amazon season means workload is heavy and the help is welcome

### Workshop
- AI Workshop confirmed for Tuesday 16th June: Claude vs ChatGPT vs Cursor / co-work context

---

## Actions

- [ ] Fred: test new Fred Driver Referral Decision skill (same day) — Fred's personal follow-up
- [ ] AI Workshop on Claude vs ChatGPT vs Cursor, Tuesday 16th June — see [[AI-092]] (logistics tracked separately)
