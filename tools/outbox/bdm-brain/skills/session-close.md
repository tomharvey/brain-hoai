# Skill: /session-close

End-of-session observability pass. The agent reviews its own performance,
classifies roles used, checks tool call outcomes, and writes a structured
entry to the Brain Health Log.

Run at the end of every interactive conversation. The EOD nudge reminds the BDM to do this.
Do NOT run for scheduled tasks (morning brief, pre-meeting brief, EOD nudge, weekly pulse) —
those tasks are server-side and cannot write to the local filesystem.

---

## Why this exists

The brain improves from real usage, not guesses. Each session log entry is one
data point. The weekly pulse reads them all, finds patterns, and generates specific
rewrites of skill files with evidence backing. Without session logs, improvement
suggestions are speculation.

---

## Steps

### Step 1 — Recall the session

Summarise the session internally (do not show this to the BDM):
- What was the BDM's primary intent when they opened this session?
- What were the 2–3 main topics or brokers discussed?
- Was this an ad-hoc session, a skill run (e.g. /granola), or a scheduled task?

---

### Step 2 — Classify roles used

From the 8-role taxonomy, which roles were active in this session?
Classify each one that genuinely appeared — don't force-fit.

| Role | Was it used? | Notes |
|------|-------------|-------|
| Librarian | yes / no | "What do we know about X?" |
| Secretary | yes / no | Tracking/writing commitments |
| Forecaster | yes / no | Ghost detection, pipeline risk |
| Strategy partner | yes / no | Pre-call synthesis + recommendation |
| Coach | yes / no | Pattern-matching to past deals |
| Sparring partner | yes / no | Challenging deal assumptions |
| Caretaker | yes / no | Write rules, data quality |
| Apprentice | yes / no | Self-improvement suggestions |

---

### Step 3 — Tool call review

For each MCP tool called in this session, recall:
- Was it called when it should have been?
- Did it return useful data, empty results, or an error?

Score each connector used:

| Connector | Calls | Hits (useful result) | Misses (empty/unexpected) | Errors |
|-----------|-------|----------------------|--------------------------|--------|
| HubSpot | — | — | — | — |
| Notion | — | — | — | — |
| Granola | — | — | — | — |
| Slack | — | — | — | — |
| Gmail | — | — | — | — |
| GCal | — | — | — | — |

**Miss patterns to watch:**
- HubSpot company not found → broker name mismatch? Not yet in CRM?
- Granola transcript not found → meeting not recorded? Wrong date range?
- Notion page returned stale data → page not updated recently?
- Tool not called when it should have been → skill prompt gap?

---

### Step 4 — Role alignment check

For each role used in Step 2, check: did the response actually match the intent?

Use this rubric:

| Role | ✓ Matched | ✗ Mismatch looks like |
|------|-----------|----------------------|
| Librarian | Returned accurate, relevant records | Empty result for a query that should have matched; hallucinated detail |
| Secretary | Commitment written to Notion (not just mentioned in conversation) | Action noted in text but not logged |
| Forecaster | Surfaced a signal before being asked | Signal only appeared when directly queried |
| Strategy partner | Synthesised context AND gave a recommendation | Listed facts with no "here's what I'd do" |
| Coach | Connected current deal to a pattern from the BDM's own history | Generic advice with no personal grounding |
| Sparring partner | Held a counter-position and defended it | Agreed with everything; hedged every pushback |
| Caretaker | Applied write rules correctly and consistently | Rule silently ignored or fired incorrectly |
| Apprentice | Improvement suggestions grounded in session evidence | Speculation without evidence |

Rate each role used: **matched / close / mismatch**

---

### Step 5 — Proactivity check

Did the brain surface anything the BDM did not explicitly ask for?

Examples of proactive behaviour:
- "I noticed while looking this up that [broker] hasn't been contacted in 18 days"
- "One thing I'd flag: another BDM touched this account yesterday"
- "Based on your commitments, you have something due tomorrow you haven't mentioned"

Score: **proactive** (surfaced at least one unsolicited insight) / **reactive** (only answered what was asked)

---

### Step 6 — Identify the single biggest gap

In one sentence: what went least well in this session?

Choose from:
- **Data gap**: a query that needed data that wasn't available (tool returned empty, or data was stale)
- **Prompt gap**: the skill or project instructions didn't cover a case that came up
- **Role gap**: the brain responded in the wrong mode for what the BDM needed
- **Tool gap**: a tool should have been called but wasn't
- **Write gap**: a write rule was unclear or was nearly broken

If everything went well → "No significant gap this session."

---

### Step 7 — Generate improvement suggestion (if gap found)

If Step 6 identified a gap, generate one specific improvement.

Format:
```
Gap type: [data / prompt / role / tool / write]
Applies to: [skill file name + section, or "project-instructions.md + section"]

Current text:
"[quote the exact text from the skill file that should change]"

Suggested rewrite:
"[the specific replacement text]"

Evidence from this session:
"[one sentence: what happened that makes this change necessary]"
```

If the gap is a data gap (broker not in HubSpot, no Granola transcript): suggest
the specific Notion page or HubSpot record that needs updating instead.

If no clear improvement can be articulated → "No specific improvement this session."

---

### Step 8 — Self-rate (three scores, 1–3)

| Dimension | 1 — Good | 2 — Acceptable | 3 — Needs work |
|-----------|----------|----------------|----------------|
| **Data completeness** | Tools returned what was needed | Some gaps but session still useful | Multiple misses; couldn't fully answer |
| **Role alignment** | Responses matched intent | Mostly right, one off | Noticeable mismatch |
| **Proactivity** | Surfaced something unsolicited | Purely reactive but thorough | Reactive and incomplete |

---

### Step 9 — Write to local log file

**File path:** `logs/[bdm-kebab-name]/YYYY-MM-DD-HHMM-[session-type].md`

Examples:
- `logs/matt-lees/2026-06-10-0930-ad-hoc.md`
- `logs/matt-lees/2026-06-10-1745-granola.md`
- `logs/matt-lees/2026-06-10-0800-morning-brief.md`

Use the kebab-case version of [BDM_NAME] for the directory.
Use 24-hour time in the filename. Use the session type slug (ad-hoc, granola,
ghost-check, morning-brief, eod-nudge, weekly-pulse).

If a file already exists at that path (rare): append `-2` to the filename.

**File contents:**

```markdown
---
date: YYYY-MM-DD
time: HH:MM
bdm: [BDM_NAME]
session_type: [ad-hoc / granola / ghost-check / morning-brief / eod-nudge / weekly-pulse]
roles: [comma-separated list]
data_completeness: [1 / 2 / 3]
role_alignment: [1 / 2 / 3]
proactivity: [1 / 2]
gap_type: [data / prompt / role / tool / write / none]
improvement_applies_to: [filename:section or none]
status: new
---

## Session — [date] [time] — [BDM_NAME]

**Primary intent:** [one line]
**Topics / brokers:** [list]

**Roles used:**
[For each role used: role name — matched / close / mismatch]

**Tool calls:**
- HubSpot: [N] calls — [N] hits / [N] misses [miss reason if any]
- Notion: [N] calls — [N] hits / [N] misses
- Granola: [N] calls — [N] hits / [N] misses
- Slack: [N] sent
- GCal: [N] calls — [N] hits / [N] misses

**Gap:** [one sentence, or "None"]

**Improvement suggestion:**
[full formatted suggestion from Step 7, or "None this session"]
```

Show the entry to the BDM:
> Here's the session log I'll write to `logs/[bdm-kebab-name]/[filename]`:
> [entry]
> Shall I log it?

Write on confirmation.

---

### Step 10 — Close

> Session logged. [If improvement found: "Flagged one improvement for the weekly review."]
>
> See you [tomorrow morning / next session].
