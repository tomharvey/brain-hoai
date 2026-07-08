---
title: "BDM Brain — co:work Implementation Design"
created: 2026-06-10
updated: 2026-06-10
domain: ai-enablement
type: reference
tags: [bdm, shared-brain, cowork, implementation, granola, hubspot, notion, slack]
---

# BDM Brain — co:work Implementation Design

> **Status: ACTIVE DESIGN.** Low-engineering Phase 1 implementation using Claude co:work
> as the delivery mechanism. Replaces the thin-MCP strawman for the initial deployment.
> The MCP architecture remains the target for Phase 2 (when usage patterns justify it).

This doc is the build sheet for the co:work implementation. Read alongside
`strawman-sales-ontology.md` (the conceptual model) and `strawman-notion-schemas.md`
(the Notion schema detail).

---

## What co:work gives us

Claude co:work (desktop app) provides per-person:
- **Project instructions** — a system prompt that persists across all sessions
- **Project knowledge** — files and pages the agent has in context
- **MCP connectors** — Notion, HubSpot, Slack, Gmail, Google Calendar, Granola
- **Scheduled tasks** — cron-like triggers that fire without the BDM opening the app
- **Shared projects** — multiple people can contribute to the same project

No custom servers. No hosting. No Lambda. The co:work runtime is the MCP client.

---

## Three-layer structure

Every BDM project is built on three layers of context:

### Layer 1 — Team shared (read + write by all)

Lives in Notion, in a shared teamspace. Every BDM project includes these:

| Page / DB | Purpose |
|-----------|---------|
| **BDM Directory** | Canonical team roster — names, Slack handles, HubSpot owner IDs, emails. Used for notification lookup and Granola transcript scanning. |
| **Shared Activity Log** | Cross-BDM touchpoint log. Date \| BDM \| Broker \| What happened \| Next action \| Owner \| Due. Written at EOD with agent help, read at morning brief. |
| **Broker Ownership** | Flat table: Broker → owning BDM. Redundant with HubSpot owner field but faster to read. Adam maintains. Reconciled weekly against HubSpot. |
| **Sales Playbook** | Objection handling, messaging, ICP definitions. Read-only for the agent. |
| **Broker Tiers** | Classification of brokers by relationship quality/segment. Read-only for the agent. |
| **OKRs** | Current quarter targets: qualified submissions, conversion, GWP. Read-only. |
| **Brain Health Log** | Weekly Caretaker/Apprentice output — improvement suggestions, stale record flags, recurring gaps. Adam and Tom review and apply. |

### Layer 2 — Individual (each BDM owns their own)

Also lives in Notion, but in each person's own space:

| Page | Purpose |
|------|---------|
| **My Accounts** | Brokers this BDM owns. Linked to Accounts DB. Updated by the agent (with approval) as deals progress. |
| **My Development Focus** | Current skill / technique the BDM is working on. Fed by Coach role. |
| **My Shortcuts** | Personal preferences: how to open calls, what to lead with for key brokers, preferred cadence. Populated during onboarding, refined over time. |
| **My Commitments** | Open actions from Granola transcripts. Written by the Secretary role. Reviewed daily. |

### Layer 3 — Broker context (pulled dynamically per session)

Not stored in the project — fetched at query time via MCP connectors:

| Source | What it provides |
|--------|-----------------|
| **HubSpot** | Deal stage, last activity, engagement history, contact details, company owner |
| **Granola** | Recent meeting transcripts for this broker |
| **Gmail** | Recent email threads with this broker or their contacts |
| **GCal** | Upcoming meetings, past meeting history |

The project instructions tell the agent: when a broker is named in a session, pull Layer 3
before answering anything about them.

---

## BDM Directory — the backbone

This Notion page is what makes cross-BDM intelligence possible without engineering.

```
| Name      | Slack Handle  | HubSpot Owner ID | Email              | Start Date |
|-----------|---------------|------------------|--------------------|------------|
| Matt Lees | @matt.lees    | usr_abc123       | matt@flockcover.com| 2026-06-16 |
| Alex D.   | @alex.dyball  | usr_def456       | alex@flockcover.com| 2026-06-16 |
| ...       | ...           | ...              | ...                | ...        |
```

**Uses:**
- Cross-BDM Slack DMs after Activity Log writes
- Granola transcript scanning (scan for any name in this table)
- HubSpot owner ID → person mapping
- Monday weekly pulse (who hasn't logged this week?)
- New BDM onboarding (add to directory → all projects pick it up on next run)

**Maintained by:** Adam. Update when someone joins, leaves, or changes role.
New BDM joins 2026-07-21 — first real test.

---

## HubSpot as ownership oracle

Don't maintain a separate Broker Ownership table just for ownership. HubSpot already
enforces a single owner per Company record. Use it:

1. Activity Log write → agent queries `search_companies(name=broker_name)`
2. HubSpot returns company record with `owner_id`
3. Agent looks up `owner_id` in BDM Directory → gets Slack handle
4. If owner is different from current BDM → Slack DM notification

The Broker Ownership Notion table is a fast-path cache and a fallback for brokers not yet
in HubSpot. Reconcile weekly (Caretaker task): any broker in Activity Log but not in
HubSpot gets flagged for graduation.

---

## Granola skill — BDM custom summary

Each BDM runs this after broker meetings. Either triggered manually or auto-detected
by a scheduled task that checks for new Granola meetings each evening.

### Skill steps

1. **Fetch transcript** — via Granola MCP (or BDM pastes it)
2. **Structured summary** — custom template:
   - **Broker & context**: who attended, company, current stage
   - **Key signals**: what did you learn about their situation?
   - **Commitments — you**: what did you promise to do?
   - **Commitments — them**: what did they agree to?
   - **Objections / blockers**: what came up that could stall?
   - **Competitive intel**: any mentions of other brokers or providers?
   - **Next action**: single most important next step, with date
   - **Hypothesis tested**: which conversion bet did this touch?
3. **BDM mention scan**: load BDM Directory names → scan transcript for any match →
   flag: "Matt is mentioned — do you want to notify them?"
4. **Activity Log write** — draft entry, show to BDM, write on approval
5. **HubSpot engagement note** — offer to write a CRM note (with approval)
6. **Cross-BDM notification** — if another BDM is flagged (from step 3 OR HubSpot owner
   mismatch): draft Slack DM, show to BDM, send on approval

### Mention detection logic

```
For each name in BDM Directory:
  If name appears in transcript AND name != current BDM:
    Flag: "[Name] is mentioned in this transcript."
    Offer: "Shall I send them a Slack DM with context?"
```

This catches both explicit mentions ("Matt told me they'd spoken to Alex") and indirect
references (another BDM appears as an attendee or is quoted).

---

## Scheduled tasks

Four tasks per BDM project. All fire without the BDM opening the app.

### Task 1: Morning Brief (8:00am weekdays)

```
Run a morning brief for [BDM name]:

1. Check the Shared Activity Log — any team activity since yesterday?
2. Check My Commitments — anything due today or overdue?
3. Check GCal — what meetings do I have today?
4. For each broker meeting today: pull Layer 3 (HubSpot last activity, Granola recents, 
   any Gmail threads). Flag anything I should know before calling them.
5. Check Shared Activity Log: has another BDM touched any of my brokers this week?
6. Output: a short morning brief. Lead with anything urgent. 
   Send to Slack as a DM to [slack_handle].
```

### Task 2: Pre-meeting Brief (30 minutes before calendar event)

```
I have a meeting with [attendee/company] in 30 minutes.

1. Fetch: last 3 Granola transcripts with this broker.
2. Fetch: HubSpot deal stage, last activity, open tasks.
3. Fetch: last 5 Gmail threads with this broker's email domain.
4. Check: My Commitments — did I promise them anything I haven't done?
5. Check: Shared Activity Log — has any other BDM touched them this week?
6. Output: a pre-meeting brief. What do I know? What should I lead with?
   What do I need to watch out for?
   Send to Slack as a DM to [slack_handle].
```

Trigger: GCal event with an external attendee, detected 30 minutes before start.
(Requires GCal polling — check every 15 minutes during business hours, or run at 7:30am
with a look-ahead at the day's calendar.)

### Task 3: EOD Nudge (5:30pm weekdays)

```
End-of-day check-in for [BDM name].

1. Check GCal — what broker meetings happened today?
2. For each: is there a Granola transcript available? If yes, offer to run the 
   Granola skill summary. If no: prompt the BDM to log the meeting manually.
3. Check My Commitments — mark anything completed today.
4. Check: any open actions due this week that haven't moved?
5. Output: a brief EOD nudge. "Here's what I think you should log today."
   Send to Slack as a DM to [slack_handle].
   Include a link to open co:work for the Granola skill session.
```

### Task 4: Weekly Pulse (Monday 8:00am)

```
Weekly pulse for [BDM name].

1. Review the Shared Activity Log from last week. What patterns do you see?
2. Check My Accounts — any broker with no activity in >14 days? Flag as ghost.
3. Compare: what the team touched last week vs. the week before. 
   Any accounts going quiet across the whole team?
4. Check: any hypotheses being tested this week? What's the current signal?
5. CARETAKER CHECK: review Brain Health Log from last week. 
   Did any suggested improvements get applied?
6. APPRENTICE SUGGESTION: what 1-2 things would make the brain more useful this week?
   Write suggestions to Brain Health Log. Slack Adam if anything is high-priority.
7. Output: weekly brief for [BDM name]. 
   Send to Slack as a DM to [slack_handle].
```

---

## Caretaker / Apprentice maintenance loop

The brain's ability to improve itself is built in from day one.

### Caretaker (Phase 1, immediate)

The Caretaker enforces write-gate rules and flags degraded data:

**Write-gate rules (enforced in all tasks and sessions):**
- Never write to HubSpot without BDM confirmation of the draft
- Never write to Shared Activity Log without BDM confirmation
- Never write to team-owned pages (Playbook, Broker Tiers, OKRs)
- Never send a Slack DM to another BDM without showing the draft first
- Never graduate a prospect to HubSpot without BDM confirmation
- On HubSpot: never delete. Create or update only.

**Stale record detection (in weekly pulse):**
- My Accounts: broker with no Granola transcript AND no HubSpot activity in >14 days → ghost flag
- My Commitments: any action item >7 days overdue with no note → escalate to morning brief
- Shared Activity Log: entries >30 days old with no resolution → flag for Adam

### Apprentice (Phase 1+, starts immediately)

After each week, the brain reflects on its own usefulness:

**What to look for:**
- Queries that required multiple re-prompts to get a good answer → context gap
- Questions the BDM asked that the brain couldn't answer → missing data
- Friction points in the Granola skill (e.g. transcript summaries consistently missing something)
- Patterns in what's being logged vs. what's being acted on

**Output format (Brain Health Log entry):**
```
Week of [date] — [BDM name]
Suggested improvements:
1. [Specific improvement — what's missing, where it's missing, how to add it]
2. ...
Stale records flagged: [count]
Queries that hit gaps: [count, with examples]
```

**Who acts on suggestions:** Adam reviews Brain Health Log weekly. Tom reviews monthly
to assess whether patterns recur (→ update project instructions, Notion schemas, or 
Granola skill template). This is the feedback loop into the brain design.

---

## Onboarding prompt

Run once per BDM at setup. Seven questions that build Layer 2 and personalise
project instructions.

```
I'm going to ask you 7 quick questions to set up your personal brain layer.
This takes about 10 minutes. Your answers stay in your project only —
the team sees the Shared Activity Log, not this.

1. Which brokers are currently your top 3 priorities? (I'll make sure I know 
   their full context before we discuss them.)

2. For each of those three — what's the current status and your single 
   most important next action?

3. When you're about to call a broker, what's the one thing you most want 
   to know before you pick up the phone?

4. Is there a broker you've worked on before who taught you the most about 
   how to sell well? What was the pattern that worked?

5. What's your biggest current challenge — is it finding new brokers, 
   moving deals forward, or something else?

6. How do you prefer your morning brief — short bullet points, or a bit 
   more context on each item?

7. Slack or email for daily digests? (Both are fine — I'll use Slack for 
   quick nudges and Gmail draft for the weekly summary if you want it.)
```

Answers are written to Layer 2 (My Shortcuts, My Development Focus) and used to
personalise the project instructions. Stage 2 activation moment: the BDM is now
setting context, not just asking questions.

---

## Project instructions template

The system prompt for each BDM's project. Personalised during onboarding.

```
You are the shared brain for the Flock BDM team, personalised for [Name].

Your primary goal: help [Name] close more deals by combining team-wide 
context with their personal account knowledge.

TEAM CONTEXT (always in scope):
- BDM Directory: [link] — team roster, Slack handles, HubSpot IDs
- Shared Activity Log: [link] — cross-BDM touchpoints
- Broker Ownership: [link] — who owns what
- Sales Playbook: [link] — objection handling, messaging, ICP definitions
- OKRs: [link] — current quarter targets (qualified submissions, conversion, GWP)

PERSONAL CONTEXT (for [Name] only):
- My Accounts: [link]
- My Commitments: [link]
- My Shortcuts: [link]
- My Development Focus: [link]

WHEN A BROKER IS MENTIONED:
Before answering, pull Layer 3: HubSpot record (last activity, deal stage),
last 3 Granola transcripts, any recent Gmail threads.
Check the Shared Activity Log: has anyone else touched this broker this week?

WRITE RULES (never skip these):
- Draft first, confirm before writing — for HubSpot, Activity Log, and Slack DMs
- Never write to team-owned pages
- Never delete anything in HubSpot
- Always show what you're about to send before sending

NOTIFICATION RULE:
After writing to the Activity Log, check Broker Ownership + HubSpot owner.
If the broker is owned by another BDM, draft a Slack DM to them and confirm 
before sending.

BRAIN ROLES (adapt your mode to what's needed):
- Secretary: tracking commitments, flagging missed follow-ups
- Librarian: answering "what do we know about X?"
- Forecaster: ghost account detection, pipeline risk flags
- Strategy partner: pre-call brief, "what do I know and what should I lead with?"
- Coach: connecting current deal to patterns from past deals
- Caretaker: enforcing write rules, flagging stale records
```

---

## Signal sources for cross-BDM intelligence

In priority order:

| Signal | Source | How it works | Reliability |
|--------|--------|-------------|-------------|
| HubSpot company owner | HubSpot MCP | Query company by name → get owner_id → map to BDM Directory | High — CRM enforces single owner |
| Granola transcript mention | Granola MCP + scan | Load BDM Directory names → scan transcript | High — catches explicit mentions |
| Shared Activity Log | Notion MCP | Read recent entries at morning brief and EOD | High — manual but habitual |
| Broker Ownership table | Notion MCP | Fast-path lookup, Adam-maintained | Medium — needs reconciliation |
| GCal event overlap | GCal MCP | Does another BDM have a meeting with this broker this week? | Requires shared calendar access |

Start with HubSpot + transcript scan + Activity Log. Add GCal overlap if the team
shares calendars.

---

## Ghost account detection logic

The Forecaster role. Runs in the weekly pulse, and on demand.

```
Ghost detection for [BDM name]:

For each broker in My Accounts:
  1. Check HubSpot: when was the last activity? (email, call, meeting)
  2. Check Granola: when was the last transcript?
  3. Check Activity Log: when was this broker last logged?
  
  If all three are >14 days ago:
    Flag as GHOST. Include in morning brief.
    If >30 days: escalate — include in Slack DM to [BDM name] directly.

Also check cross-team: are any brokers in the Shared Activity Log 
that appear in no BDM's My Accounts? These are unowned — flag to Adam.
```

---

## Delivery channels

| Channel | When to use | Mechanism |
|---------|-------------|-----------|
| **Slack DM to BDM** | Morning brief, pre-meeting brief, EOD nudge, ghost alerts | `slack_send_message` — always confirm first |
| **Slack DM to another BDM** | Cross-BDM notification after Activity Log write | `slack_send_message` — always show draft first |
| **co:work interactive session** | Granola skill, deep broker research, onboarding | BDM opens app, runs session |
| **Gmail draft** | Weekly summary (optional) | `create_draft` only — never `send`. BDM reviews and sends. |
| **HubSpot engagement note** | After broker meeting (from Granola skill) | Write on BDM confirmation only |

---

## Rollout plan

### Week 0 (before first BDM)
- Adam creates Notion teamspace with Layer 1 databases (from `strawman-notion-schemas.md`)
- Populate BDM Directory with current team
- Create Broker Ownership table (Adam populates from HubSpot export)
- Tom sets up one BDM project in co:work as reference model

### Week 1: Matt Lees pilot
- Run onboarding prompt with Matt
- Enable 3 scheduled tasks (morning brief, EOD nudge, weekly pulse)
- Pre-meeting brief on hold until GCal trigger is confirmed working
- Matt runs Granola skill after 3 broker meetings — refine template

### Week 2: Add remaining BDMs
- Onboard Alex, other BDMs one at a time
- Cross-BDM notifications go live once ≥2 BDMs are active
- Brain Health Log starts accumulating improvement suggestions

### Week 3+: Caretaker live
- Weekly pulse includes Apprentice suggestions
- Adam reviews Brain Health Log Friday afternoons
- Monthly: Tom reviews Brain Health Log for recurring patterns → update design

---

## Relationship to the strawman MCP architecture

The co:work implementation covers Phase 1 of the initiative (brain works):
- Federated search ✓ (via MCP connectors, not a custom MCP server)
- Cross-BDM visibility ✓ (Activity Log + BDM Directory)
- Telemetry ✗ (deferred — no CloudWatch until thin MCP exists)
- Write gate ✓ (enforced via project instructions, not code)
- Proactivity ✓ (scheduled tasks replace Lambda/cron)

The thin-MCP architecture (`strawman-stack-decisions.md`) remains the target for Phase 2
when usage patterns are established and the complexity is justified. The co:work
implementation produces the usage data that informs whether the full MCP stack is needed.

**Migration path**: when the thin MCP is built, the co:work project instructions become
the agent instructions for the MCP client. The Notion schemas don't change. The write-gate
rules move from natural language (project instructions) to code (MCP lint). Everything else
is additive.
