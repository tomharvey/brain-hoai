---
title: Shreya Chowta
created: 2026-03-30
updated: 2026-04-14
type: person
role: Underwriting Assistant
team: Ops (reports to Emily Staton)
tags: [underwriting, ops, ai-user, zapier, hubspot, cancellations]
---

## Role

Underwriting Assistant

## Team

Ops — reports to [[emily|Emily Staton]]

## Relationship

First spoke 2026-04-02. Proactive, keen, already designing automations independently. Knew Sam via Tracy from a previous company.

## Working style notes

- Most advanced AI user on the ops team (Emily's assessment)
- Working on post-buying processes, driver referral authority, MTA authority
- Proficient with Zapier — designs workflows independently
- Uses AI to sense-check business writing and proposals
- Emily describes her as "boot on the ground" — daily hands-on usage
- Prefers Word documents over Google Docs ("very old school")
- Key observation: "We're relying more on Claude now than tech automation"
- Connected HubSpot to Claude live during discovery call — immediately productive
- Had already designed a full NOC automation workflow and pitched it to Sam before Tom arrived

## 1:1 Log

### 2026-04-02 — AI Discovery

- **NOC automation** is her primary pain point — cancellation notices when connectivity drops below 75%. Currently manual copy/paste from HubSpot into Word templates. She'd designed a Zapier workflow; Tom suggested iterating via Claude prompt first as faster path.
- Connected HubSpot to Claude on the call — pulled up her tickets correctly, needs filtering refinement
- Approach: feed NOC Word template to Claude, iterate prompt until reliable, then scale to batch processing, then automate upload
- **Submissions/new business logging** flagged as much larger project — needs dedicated meetings to break into small goals
- CC parsing: Retool version (Abs) still works, but haulage portal Claude prompt (CC→CSV) reportedly faster
- Testing Claude + HubSpot NOC approach immediately after the call — will report back

### 2026-04-13 — Slack update

- Built a working Claude skill: "NOC letter generator" — pulls data from HubSpot accurately
- Steps covered: find tickets → get company/deal info → parse ticket → calculate dates → fill template → save as .docx
- No longer needs Google Drive — Claude edits the Word template directly
- **Blocker**: steps 6-8 of original workflow still require manual Retool intervention
- Demoing at Wednesday AI/Automations sync
- Offered to schedule 15 mins tomorrow (Tue 14 Apr) to walk through how it works

### 2026-04-14 — NOC skill walkthrough

- Walked through skill editing together — updated to check both ticket description and notes for data
- Listed explicit data points in skill (policy number, inception date, etc.) to reduce template parsing overhead
- **Address blocker**: client addresses only in Retool, not HubSpot. Discussed migrating to HubSpot (supports broader Retool transition)
- Downloads folder permission friction — exploring persistent folder options
- Growing confidence: "I feel like I'm integrating Claude really well"
- Inspired by Mima's CC generator and wake-up schedule skills
- See: [[2026-04-14-shreya-chowta-noc-skill]]
