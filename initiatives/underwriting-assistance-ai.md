---
title: Underwriting assistance AI
created: 2026-03-27
updated: 2026-04-09
domain: operational-tooling
type: initiative
status: active
origin: self-started
owner: emily
tags: [underwriting, ops, automation, zapier, claude]
---

## Summary

AI-driven operational efficiency in the underwriting assistance process. Emily's ops team is already using AI tools daily — this initiative is about accelerating and coordinating, not introducing. Third-party vendor was rejected in favour of in-house approach.

## Goal

Reduce manual effort in the quoting process while maintaining quality and building institutional knowledge. Consolidate ad-hoc tool usage into repeatable, shareable workflows.

## Current state

- Team uses ChatGPT and Claude **daily** for PDF data extraction (VRM lists, claims info)
- Claude showing higher success rates than ChatGPT for extraction — Anna migrated prompts successfully
- Zapier is the primary automation backbone — connects HubSpot, Slack, and internal processes
- Key wins already delivered:
  - Transfer of agency notifications (fixed a fundamentally broken process via Zapier + Slack)
  - Underwriter deviation tracking (HubSpot properties + Zapier → compliance audit trail)
- Emily designs new processes with AI in mind from the start
- Monthly AI/Automations sync exists within the ops team — Tom now attending
- Emily uses ChatGPT for complaint resolution letter compliance checking (FCA/ICOBS) — potential skill candidate, Emily to own
- Emily building submission/ticket volume forecasts using HubSpot historical data for headcount planning

### Team readiness

- **Shreya Chowta**: most advanced — post-buying processes, driver referral authority, MTA authority
- **Anna Spriggs**: experienced daily user, migrated ChatGPT prompts to Claude with better results
- **Fred Bush**: early AI journey but receptive. Uses Claude daily for VRN extraction and document parsing. Switched from ChatGPT to Claude (better at PDFs). Attended prompting workshops. Driver referrals identified as biggest manual gap (AI-011). HubSpot not yet connected to Claude.

## Dependencies

- Individual conversations with Shreya, Anna, and Fred (scheduled Tue 31 Mar / Wed 1 Apr)
- Understanding Zapier landscape and overlap with engineering's MCP/agent approach
- Claude standardisation (company-wide initiative)

## Risks

- Automating a broken process instead of fixing it
- Building another "Retool replica"
- Zapier automations becoming load-bearing without visibility from engineering

## Next actions

- [x] Discovery conversation with Emily
- [x] Join monthly AI/Automations sync
- [x] Speak to Shreya, Anna, and Fred individually
- [ ] Understand Zapier setup and what's connected
- [ ] Explore ChatGPT→Claude migration path for remaining use cases
- [ ] Suggest Emily builds complaint resolution checking as a Claude skill (her to own)

## Log

### 2026-03-27

- Fergus flagged as fertile ground in HoAI 001
- Third-party approach rejected — in-house preferred

### 2026-03-30

- Discovery call with Emily completed
- Team further along than expected — daily AI usage, Zapier automation, process-first thinking
- Transfer of agency fix = great example of "fix what's broken" vs "automate what's slow"
- Joined monthly AI/Automations sync
- Shreya/Anna/Fred calls scheduled for Tue 31 Mar and Wed 1 Apr
- **Via Jordi 1:1**: Jordi working with [[anna|Anna]] on renewal spreadsheet automation
  - **Blocker**: Google MCP requires local hosting + Google Cloud auth — Jordi runs prompts manually on calls
  - Existing Claude Google connector: Calendar only; Drive connector is read-only (file list, not edit)
  - Workaround ideas: G Drive sync to local filesystem, G Scripts — none ideal
  - Deeper issue: 3 spreadsheets with different structures + Zapier workarounds to HubSpot — process may need rethinking
  - Tom reviewing Google MCP hosting 2026-03-31
- **Anna discovery (2026-04-02)**: renewals process fully mapped. Four steps: Looker → PMT → Billy allocates → Renewals Tracker → Zapier → HubSpot. Jordi was automating step 3 (PMT→Tracker copy/paste). **New direction: eliminate PMT and Renewals Tracker entirely, go Looker→HubSpot direct.** Google MCP hosting question is now moot — we're solving the wrong problem if spreadsheets go away. Requires: understanding Kirsty's Looker→Claude connection, new HubSpot views for Billy's allocation, and potentially reviving the old renewal pipeline in HubSpot.
  - Anna's next project: G Drive folder automation (auto-create folders + drop broker docs per deal). Company name matching is the hard part.
  - HubSpot already connected to Anna's Claude via connectors panel — trivially easy. Can help Matt Lees do the same.
- **Shreya discovery (2026-04-02)**: NOC (cancellation notice) automation is primary pain point — manual copy/paste from HubSpot into Word templates when connectivity drops below 75%. Shreya had designed a Zapier workflow; Tom suggested iterating via Claude prompt first. Connected HubSpot to Claude on the call — worked immediately. Shreya testing Claude + template approach.
  - Key cultural shift: "We're relying more on Claude now than tech automation"
  - Submissions/new business logging flagged as much larger project — needs dedicated meetings to scope
  - CC parsing: haulage portal Claude prompt reportedly faster than Abs's Retool version
  - Shreya's NOC workflow design: [[noc-cancellation-workflow]]

### 2026-04-08

- **Fred discovery**: Confirmed as early-stage AI user. Benefits from Anna's automated renewals (sees tickets, doesn't engage with AI directly for that). Uses Claude daily for VRN extraction and document parsing. Switched from ChatGPT — Claude better at PDFs.
  - **Driver referrals** identified as biggest manual gap: 10-20/day, ~15min each, fully manual email→HubSpot template flow. No automation exists. Structured input/output = strong automation candidate. → AI-011
  - New business submissions still partially manual (Gmail→Flock port), partially covered by existing skills
  - HubSpot not connected to Claude yet — quick win to set up
  - Emily encouraging team AI development — she's the right lever for this team

### 2026-04-09

- **Kirsty discovery**: Renewals Looker→HubSpot direct flow confirmed technically viable via MCP. Kirsty was unaware the team uses Zapier to push spreadsheet data back to HubSpot. Depends on cloud MCP deployment (AI-010). AI-007 now in-progress.
