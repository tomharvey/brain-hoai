---
title: ProdTech Leadership Heartbeat (May 26)
created: 2026-05-26
updated: 2026-05-26
domain: engineering-workflows
type: meeting
tags: [engineering-workflows, platform, incidents, lexisnexis, admiral]
---

# ProdTech Leadership Heartbeat — May 26

**Attendees:** Tom Harvey, [[matt|Matt Price]], [[jordi|Jordi Pallares]], [[ollie-crowe|Ollie Crowe]], [[mima|Jemima Pitceathly]], [[fergus|Fergus Doyle]], [[chris|Chris Fothergill]] (ProdTech leadership group)

Full transcript: [[2026-05-26-prodtech-leadership-heartbeat-transcript]]

---

## Key themes

### Platform: OnCover check not working on new policies
- Claim submissions on Carrier v1 / haulage policies: on-cover check fails
- Jacob created a PR; needs follow-up on status
- Likely a data modelling issue — policy lookup works fine, only claims flow affected
- Tom to loop in with Jacob

### Platform repo access for product team
- Product team had read-only access; couldn't make copy changes or minor updates
- Resolution: Chris gave product team admin access to platform services repos (done in-meeting)
- Guard: no merging to main; can bypass checks in emergencies only
- Ollie now can make MTA flow changes and minor copy edits

### LexisNexis via Admiral group contract
- Admiral adding Pioneer to their existing LexisNexis contract → Flock gets free access post-deal completion
- Contact: Tom Coxon at Admiral
- Reversing sensors example: 10% frequency reduction, 42% of quote set has reversing sensors
- ADAS features already designed but blocked without data access
- Caution: Admiral contract is B2C focused; Flock needs fleet/commercial data types — may need separate negotiation for those specific databases

### Reliability and incident management
- Increase in incidents over past 4–5 weeks: bad deployments + insufficient testing
- [[jordi|Jordi]] drafting a lightweight incident management process
- Current gap: incidents scattered across threads, DMs, tickets — no visibility into patterns or frequency
- Need: incident owner, customer impact assessment, priority classification, centralised channel
- Goal: build the muscle of raising incidents (even small ones) to get signal and improve over time

### AI adoption anxiety — engineering team (Tom raised)
- Visible anxiety from different angles: job apocalypse fear, "I don't want to be an agent babysitter", scepticism about AI hype
- [[chris|Chris]]: Flock is lean — automation frees capacity, unlikely to cause layoffs here
- Broader diagnosis: teams optimised for "cranking through work", not stepping back to rethink roles
- Missing: a clear vision of what an engineer/PM/ops person looks like in 2027 with AI
- Agreed: this needs Anton and Ed to espouse a company-wide framing, not just ProdTech
- Tom to go around squad-by-squad for philosophical conversations on job identity

---

## Actions

- [ ] Tom: Follow up with Jacob on OnCover check PR status (→ AI-074)
- [ ] Tom: Connect with Tom Coxon (Admiral) on LexisNexis timeline and scope (→ AI-075)
- [ ] Jordi: Draft incident management process; share for feedback this week (→ AI-076)
- [ ] Tom: Schedule squad-by-squad conversations on AI and job identity (→ AI-073)
