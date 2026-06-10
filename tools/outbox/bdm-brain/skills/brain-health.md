# Skill: /brain-health

Caretaker/Apprentice review. Two modes:

- **Quick mode** (default): stale records + data gaps for this BDM
- **Deep mode** (`/brain-health deep`): reads Brain Health Log across all BDMs,
  detects patterns, generates ranked improvement suggestions with specific rewrites

Also runs automatically as part of the Monday weekly pulse (deep mode).
Triggered by `/brain-health` or "what should we improve?"

---

## Quick mode steps

### Step 1 — Stale record scan

Check My Commitments:
- Any action items >7 days old with no note? → OVERDUE
- Any items due today or tomorrow? → DUE SOON

Check My Accounts:
- Any broker with no HubSpot activity AND no Granola transcript in >14 days? → GHOST CANDIDATE
- Any broker not found in HubSpot at all? → UNREGISTERED

Check Shared Activity Log:
- Any entries >30 days old that show "next action" but no follow-up? → DROPPED THREAD

---

### Step 2 — Gap detection

Read Brain Health Log entries for [BDM_NAME] from the last 7 days.

Tally:
- Sessions with data completeness score ≥ 2 → note what caused the gap
- Sessions with role alignment score ≥ 2 → note which role mismatched
- Tool misses: which connector had the most empty returns?
- Improvement suggestions with status "new" → list them (not yet reviewed)

---

### Step 3 — Quick report

> **Brain health — [date] — [BDM_NAME]**
>
> **Stale records:** [list or "None"]
> **Tool gaps this week:** [e.g. "HubSpot: 3 misses — likely broker name mismatches"]
> **Pending improvements:** [count, or "None pending"]
>
> Want me to run a deeper cross-BDM analysis?

---

---

## Deep mode steps

Run when invoked as `/brain-health deep`, or called from the weekly pulse.

### Step D1 — Read all Brain Health Log entries this week

Read the Brain Health Log (Notion). Filter for entries from the last 7 days.
If running as part of the weekly pulse: read the last 7 days.
If running manually mid-week: read since last Monday.

For each entry, extract:
- BDM name
- Session type
- Roles used
- Tool call hits/misses per connector
- Data completeness score (1/2/3)
- Role alignment score (1/2/3)
- Proactivity score (1/2)
- Gap description
- Improvement suggestion (text + applies-to field)
- Status

---

### Step D2 — Pattern detection

Aggregate across all entries:

**Tool miss patterns:**
For each connector, count total misses across all sessions this week.
Group misses by pattern if the gap descriptions are similar.
Threshold: ≥ 2 misses of the same type = a pattern worth flagging.

**Role alignment patterns:**
Which roles had mismatch scores? Which BDMs? Same role mismatching across multiple BDMs
= project instructions gap. Single BDM only = may be that person's usage pattern.

**Recurring gaps:**
Group gap descriptions by type (data / prompt / role / tool / write).
Find any gap description that appears in ≥ 2 sessions this week.
These are the priority improvements.

**Proactivity trend:**
What fraction of sessions scored "proactive"? If < 30%: the brain is being used
reactively. This is not a prompt gap — it's a usage pattern. Flag to Adam for discussion.

**Improvement backlog:**
How many improvement suggestions have status "new" (not yet reviewed)?
If > 5 outstanding: flag. The backlog is growing faster than it's being cleared.

---

### Step D3 — Rank improvements

Take all improvement suggestions from Brain Health Log entries with status "new".
Add any new suggestions from Step D2 that don't yet have a log entry.

Rank by:
1. **Frequency** — how many sessions surfaced this gap?
2. **Severity** — score 3 gaps > score 2 gaps
3. **Effort** — quick fixes (data/Notion updates) before skill file rewrites

Output the top 3 as actionable items.

---

### Step D4 — Generate specific rewrites

For each of the top 3 improvements, if it's a prompt gap or skill gap:

Generate a specific rewrite in this format:

```
Improvement #[N]
Priority: [high / medium] — seen in [N] sessions
Gap type: [data / prompt / role / tool / write]

Applies to: [exact filename + section header]

CURRENT TEXT:
"[exact quote from the skill file or project instructions]"

SUGGESTED REWRITE:
"[replacement text — be precise, not vague]"

Why this change:
[one sentence grounded in the session log evidence]

Effort to apply: [5 min / 30 min / Tom to decide]
```

If the improvement is a data gap (something missing from HubSpot or Notion):
```
Improvement #[N]
Priority: [high / medium] — seen in [N] sessions
Gap type: data

What's missing: [specific broker / field / record type]
Where to add it: [HubSpot company record / Notion Accounts DB / BDM Directory]
Who should add it: [Adam / the BDM / Tom]
Effort: [5 min]
```

---

### Step D5 — Write weekly summary

Compose a Brain Health Log weekly summary entry:

```
## Weekly summary — week of [date]

**Sessions logged this week:** [total count across all BDMs]
**BDMs with sessions:** [names]

**Top patterns:**
- [pattern 1]: seen in [N] sessions — [one line description]
- [pattern 2]: seen in [N] sessions — [one line description]

**Tool call health:**
- HubSpot: [total hits] hits / [total misses] misses — [dominant miss reason if any]
- Notion: [total hits] hits / [total misses] misses
- Granola: [total hits] hits / [total misses] misses

**Role alignment:** [N] sessions matched / [N] close / [N] mismatch
**Proactivity rate:** [N]% of sessions scored proactive

**Top 3 improvements (ranked):**
1. [Improvement #1 — one line summary]
   Applies to: [filename]
   Evidence: [N] sessions
2. [Improvement #2]
3. [Improvement #3]

**Backlog:** [N] suggestions pending review
**Status:** awaiting Adam / Tom review
```

Show to BDM (or send directly if running as part of weekly pulse — see weekly-pulse.md).
Write to Brain Health Log on confirmation.

---

### Step D6 — Notify

Send the top 3 improvements to Adam via Slack DM:

```
@adam — Brain health summary for week of [date].

3 improvements this week (evidence-backed):

1. [one line — what to change, where, why — N sessions]
2. [one line]
3. [one line]

Full detail in Brain Health Log: [Notion link]

[N] other suggestions in the backlog.
```

Show draft. Send on confirmation (or automatically if this is the weekly pulse run).
