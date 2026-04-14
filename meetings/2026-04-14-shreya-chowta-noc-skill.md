---
title: Shreya Chowta — NOC skill walkthrough
created: 2026-04-14
updated: 2026-04-14
domain: operational-tooling
type: meeting
tags: [noc, hubspot, claude-skill, automation, retool]
---

## Attendees

- [[shreya-chowta|Shreya Chowta]]
- Tom Harvey

## Key themes

### NOC letter generator skill — working but with caveats

Shreya built the skill and it runs end-to-end in a single execution. Two blockers remain:

1. **HubSpot data access** — skill only reads from ticket description, not from notes. Claude claimed different user access levels prevent reliable note reading. Workaround: updated skill instructions to check both description and notes, and listed specific data points needed (policy number, inception date, company name, broker info).

2. **Client address not in HubSpot** — stored in Retool only. Required for NOC letter completion. Currently manual copy/paste.

### Address integration options discussed

1. Start workflow in Retool, feed address to Claude
2. Have Claude prompt for addresses during execution (ask as it processes each ticket)
3. **Migrate address data to HubSpot** (preferred long-term) — supports broader Retool transition strategy

### Skill editing session

- Walked through editing the skill.md file together
- Key teaching: list data points explicitly in the skill rather than relying on Claude to parse the template each time — reduces overhead
- Explained "tell Claude the problem and let it fix the skill" approach vs manually editing

### Downloads folder friction

- Must manually grant downloads folder permission each time a new chat starts
- Explored alternatives: storing as asset, using a folder Claude always has access to

### Workflow optimisation path

Current: 7 tickets -> 7 Word templates -> manual address insertion -> PDF -> upload to HubSpot

Target: Claude generates complete PDFs with all data (including address) and uploads directly to HubSpot — eliminates Word editing step entirely

## Actions

- [ ] Continue iterating on NOC skill today — Shreya
- [ ] Decide on address storage: migrate to HubSpot or prompt during execution — Shreya/Tom
- [ ] Test automated PDF generation and HubSpot upload — Shreya

## Notes

Shreya increasingly confident with Claude — "I feel like I'm integrating Claude really well." Good example of ops team member moving from observer to builder. Demoing at Wednesday AI/Automations sync.

Full transcript: [[2026-04-14-shreya-chowta-noc-skill-transcript]]
