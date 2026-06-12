---
title: "005 — BDM Brain scheduling and filesystem architecture"
created: 2026-06-11
updated: 2026-06-11
domain: ai-enablement
type: decision
status: active
tags: [bdm-brain, co-work, scheduling, observability, architecture]
---

# 005 — BDM Brain scheduling and filesystem architecture

## Context

The BDM Brain is implemented as a co:work (Claude.ai) project per BDM. It includes
four scheduled tasks (morning brief, pre-meeting brief, EOD nudge, weekly pulse) and
an observability system that writes session logs to a Google Drive-synced local filesystem.

Two architectural questions required resolution before pilot deployment:

1. Do co:work scheduled tasks fire server-side (app closed) or client-side (app must be open)?
2. Can the filesystem MCP server be used in scheduled task context?

A secondary question:

3. How do we make HubSpot company lookups reliable given broker name variations?
   (e.g. "Brown & Brown" vs "Brown and Brown" vs "B&B Ltd")

## Decisions

### Scheduling: server-side connectors only for scheduled tasks

The BDM Brain folder lives on Google Drive, synced locally by Drive for Desktop.
The filesystem MCP server is a local process — it requires the Claude desktop app
to be open on the BDM's machine.

Co:work scheduled tasks are expected to fire server-side (Anthropic infrastructure),
meaning they cannot access the local filesystem.

**Therefore:**
- Morning brief, pre-meeting brief, EOD nudge: use Slack, HubSpot, Granola, Notion,
  GCal, Gmail only (all server-side connectors). These fire correctly regardless of
  whether the desktop app is open.
- Session-close observability logs: filesystem write — interactive sessions only.
  The desktop app is always open during interactive sessions.
- Brain-health deep mode: reads `logs/**/*.md` — must be run interactively. Adam runs
  `/brain-health deep` manually (typically Monday morning after the pulse lands in Slack).
- Weekly pulse: does NOT run brain-health deep mode automatically. Instead, it sends a
  team activity summary to Adam's Slack and prompts him to run `/brain-health deep`.

**Assumption to validate in pilot:** confirm co:work scheduled tasks fire server-side
by running a simple test: schedule a 5-minute task that sends a Slack message, close
the desktop app, observe whether it fires.

**Fallback if assumption is wrong:** n8n or GitHub Actions as the external scheduler.
All scheduled task logic is already expressed as self-contained markdown files — they
can be invoked via API call from an external trigger without refactoring.

### HubSpot name matching: store company ID on first touch

Broker name search (`search_companies(name=...)`) is fragile when names vary between
Granola transcripts and HubSpot records. Brown & Brown, B&B, and "Brown and Brown
(South East)" all refer to the same company but may return different results.

**Fix:** capture the HubSpot company ID at first touch and persist it in My Accounts.

- During `/onboarding` Q1: after the BDM names a broker and HubSpot is queried,
  extract and store the company ID alongside the broker entry in My Accounts.
- During `/granola` Step 5: after the ownership check resolves a company record,
  store the company ID in My Accounts if not already present.
- All subsequent HubSpot lookups for known brokers use `get_company(id=...)` directly.
  Name search is only used for brokers not yet in My Accounts.

This makes the lookup deterministic after first contact — no disambiguation needed
for returning brokers.

### Phase 1 → Phase 2 trigger

Phase 2 = thin MCP server that exposes BDM-world semantics natively. The co:work
architecture is Phase 1.

The specific trigger for Phase 2 investment: **Notion Activity Log contention with
3+ active BDMs**. A single Notion page written to by multiple BDMs simultaneously
will produce version conflicts and context window costs that grow linearly with
team size. This becomes visibly painful around 3–4 concurrent BDMs generating
2+ log entries per day.

Secondary trigger: Google Drive sync proving unreliable (missed syncs, conflicts)
for the observability log directory.

**What to preserve in Phase 2:** the data layer (HubSpot notes, Notion Activity Log
entries, Granola transcripts) is already the canonical record. Phase 2 replaces the
brain's orchestration; the data trail persists regardless.

Likely timeline: Q3 2026 if the Matt Lees pilot succeeds and 2–3 more BDMs are added.

## Consequences

- Session-close observability loop covers all interactive sessions (ad-hoc,
  /granola, /ghost-check) but not scheduled task runs. This is acceptable — the
  high-value sessions are interactive ones.
- The weekly pulse sends a Slack summary and prompts Adam to review improvements
  manually. Adam reviews once per week, accepts/rejects suggestions, and edits
  skill files directly. This is a human-in-the-loop system, not fully automated.
- HubSpot ID capture requires one manual confirmation per broker at first touch.
  After that, lookups are ID-based and reliable.
- If server-side scheduling assumption fails: fallback is n8n (no refactoring needed).
