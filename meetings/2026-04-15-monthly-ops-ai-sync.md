---
title: Monthly Operations Automation & AI Sync
created: 2026-04-15
updated: 2026-04-15
domain: operational-tooling
type: meeting
tags: [ops, ai-sync, noc, hubspot, looker, driver-referrals, data-analysis]
---

## Attendees

- [[emily|Emily Staton]]
- [[shreya-chowta|Shreya Chowta]]
- [[anna|Anna Spriggs]]
- [[jonny-smith|Jonny Smith]]
- [[fred-bush|Fred Bush]]
- Tom Harvey

## Key themes

### Shreya's NOC letter generator demo

- Successfully sent first automated NOC on Monday — live, working, in production use
- Pulls policy details from HubSpot tickets (new status), calculates dates, picks correct template (connectivity vs finance)
- Creates drafts not emails — can't get Claude to create a HubSpot email directly, only notes/drafts
- Downloads folder permission workaround: keep same chat session open
- **Address blocker**: confirmed address is not in HubSpot anywhere. Lives in Retool only (drives policy documents). New portal will eventually have it but not yet.
- Shreya to share skill with the rest of the team
- Team discussed: Jonny's NOC requests come from his "Excel database" which pulls from Looker — so address might be findable in Looker
- **Emily has a meeting with Kirsty tomorrow** — will ask if address data lives in Looker

### Emily's data analysis work

- Using HubSpot connector for Q1 quote-to-price timeline analysis (OKR baseline)
- Claude analysed all Q1 deals and broke down average/median processing times across pipeline stages
- Handles inconsistent underwriter stage progression automatically (some skip stages)
- Automated Slack reminder every Monday to re-run Q2 data for OKR tracking
- "This would have taken me hours and hours manually on HubSpot"
- Idea floated: get Claude to auto-update monthly ops slides with fresh data

### Driver referral automation

- Fred confirmed it's "top of mind" for the team — many components (convictions, age, etc.)
- Shreya offered to help: "it's probably similar to my NOC skill — analysing documents and extracting data"
- Fred already has VRN extraction and CC parsing working — "probably halfway there"
- **Blocker**: authority framework needs sign-off from [[darren|Darren]]. He's "more than happy to give authority" once framework approved — expected within a month
- Once authority + automation in place: email in → everything extracted → notes created automatically

### HubSpot connector access

- Emily confirmed she's the go-to for permissions (super admin access)
- Issue: some seats don't have third-party app toggle enabled — 30-second fix
- Emily happy to keep handling directly: "just send people to me"
- CeeToo (IT) don't have super admin access and redirect to Emily anyway

### Jonny

- On catch-up this week, getting connectivity back above 85%
- Will present his automation work at next month's sync
- Confirmed his "Excel database" for NOC data pulls from Looker

## Actions

- [ ] Share NOC letter generator skill with the team — Shreya
- [ ] Ask Kirsty tomorrow if address data is in Looker — Emily
- [ ] Set up Looker connector for the team — Tom
- [ ] Add Retool MCP/connector to backlog — Tom
- [ ] Continue handling HubSpot permission requests — Emily
- [ ] Explore driver referral automation once authority framework approved — Fred/Shreya
- [ ] Jonny to present automation work at next monthly sync — Jonny

## Notes

Great energy in this session — Shreya's demo landed well, Emily's data analysis work impressed the room, and Fred/Shreya naturally paired up on driver referrals without prompting. Format works: ad hoc, no rigid agenda, people show what they've built. Monthly cadence confirmed.

Key finding: Jonny's "Excel database" pulls from Looker. If address data is in Looker, the entire NOC process can be fully automated — no Retool dependency. Emily meeting Kirsty tomorrow is the critical next step.

Jonny has multiple "databases" that are Excel spreadsheets — worth investigating what data lives where and whether these can be consolidated or queried directly.

Full transcript: [[2026-04-15-monthly-ops-ai-sync-transcript]]
