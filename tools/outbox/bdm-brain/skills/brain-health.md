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

Read all `.md` files in `logs/[bdm-kebab-name]/` from the last 7 days.
Filter by `date:` frontmatter field.

Tally:
- Files with `data_completeness: 2` or `3` → note what caused the gap
- Files with `role_alignment: 2` or `3` → note which role mismatched
- Tool misses: which connector had the most empty returns?
- Files with `status: new` → list improvement suggestions not yet reviewed

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

### Step D1 — Read all session log files this week

Read all `.md` files under `logs/*/` that have a `date:` frontmatter field
from the last 7 days (or since last Monday if running mid-week).

Each BDM has their own subdirectory: `logs/matt-lees/`, `logs/alex-dyball/`, etc.
Glob: `logs/**/*.md` — read all, filter by date in frontmatter.

For each file, extract from frontmatter + body:
- BDM name (`bdm:`)
- Session type (`session_type:`)
- Roles used (`roles:`)
- Tool call hits/misses (from body — parse the Tool calls section)
- Data completeness score (`data_completeness:`)
- Role alignment score (`role_alignment:`)
- Proactivity score (`proactivity:`)
- Gap description (from body — the **Gap:** line)
- Improvement suggestion (from body — full text)
- Applies to (`improvement_applies_to:`)
- Status (`status:`)

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

### Step D5 — Write weekly summary file

Write to: `logs/weekly-summary-YYYY-WNN.md` (ISO week number,
e.g. `logs/weekly-summary-2026-W24.md`).
If the file already exists (re-run mid-week): overwrite it.

```markdown
---
week: YYYY-WNN
generated: YYYY-MM-DD
bdms_covered: [comma-separated list]
sessions_total: [N]
top_improvements: [count]
status: awaiting-review
---

## Weekly brain health summary — week of [date]

**Sessions logged:** [N] across [BDMs]

**Top patterns:**
- [pattern]: seen in [N] sessions — [one line]
- [pattern]: seen in [N] sessions — [one line]

**Tool call health:**
- HubSpot: [total hits] / [total misses] — [dominant miss reason]
- Notion: [total hits] / [total misses]
- Granola: [total hits] / [total misses]

**Role alignment:** [N] matched / [N] close / [N] mismatch
**Proactivity rate:** [N]% of sessions scored proactive

**Top 3 improvements:**

### 1. [short title] — [N] sessions
[full formatted improvement with current text + suggested rewrite]

### 2. [short title] — [N] sessions
[full formatted improvement]

### 3. [short title] — [N] sessions
[full formatted improvement]

**Backlog:** [N] session log files with status: new
```

Write directly (no confirmation needed for weekly pulse run).

---

### Step D6 — Notify

Send the top 3 improvements to Adam via Slack DM:

```
@adam — Brain health summary for week of [date].

3 improvements this week (evidence-backed):

1. [one line — what to change, where, why — N sessions]
2. [one line]
3. [one line]

Full detail in logs/weekly-summary-[YYYY-WNN].md

[N] other suggestions in session logs.
```

Show draft. Send on confirmation (or automatically if this is the weekly pulse run).
