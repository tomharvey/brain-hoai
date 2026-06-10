# Skill: /brain-health

Manual trigger for the Caretaker/Apprentice review. Surfaces stale records,
flags data gaps, and suggests improvements to skills and context.

Also runs automatically as part of the Monday weekly pulse.
Triggered by `/brain-health` or "what should we improve?"

---

## Steps

### Step 1 — Stale record scan

Check My Commitments:
- Any action items that are >7 days old with no note? → OVERDUE
- Any action items that are >3 days old and due today or tomorrow? → DUE SOON

Check My Accounts:
- Any broker with no HubSpot activity AND no Granola transcript in >14 days? → GHOST CANDIDATE
- Any broker not found in HubSpot at all? → UNREGISTERED

Check Shared Activity Log:
- Any entries >30 days old that show "next action" but no follow-up entry? → DROPPED THREAD

---

### Step 2 — Gap detection

Review the most recent 10 conversations in this project (this session + recent sessions).

Look for:
- Questions [BDM_NAME] asked that the brain couldn't answer well
  (e.g. "I don't have that information", "I can't find that in Notion")
- Topics that came up multiple times without resolution
- Layer 3 lookups that returned nothing useful

Classify each gap:
- **Missing data** — the information exists but isn't connected (e.g. broker not in HubSpot)
- **Missing context** — the information doesn't exist anywhere (e.g. no Granola transcript)
- **Skill gap** — the brain handled a request poorly (e.g. summary was too generic)
- **Stale context** — information exists but is out of date

---

### Step 3 — Improvement suggestions

Based on Step 2, generate 1–3 concrete improvement suggestions.

Format for each:
```
Suggestion: [specific improvement]
Type: [missing data / missing context / skill gap / stale context]
Effort: [5 mins: update a Notion page / 30 mins: refine a skill file / Tom to decide]
How to apply: [exact action — what to change, where]
```

Be specific. "Improve the granola skill" is not a suggestion.
"Add a 'competitive signals' section to the Granola skill template" is.

---

### Step 4 — Report

Present:

> **Brain health check — [date]**
>
> **Stale records:**
> - [list from Step 1, or "None — all clean"]
>
> **Gaps from recent sessions:**
> - [list from Step 2, or "No notable gaps this period"]
>
> **Suggested improvements:**
> 1. [suggestion 1]
> 2. [suggestion 2]
>
> Want me to write these to the Brain Health Log in Notion?

---

### Step 5 — Write to Brain Health Log (optional)

If [BDM_NAME] confirms:

Draft the Brain Health Log entry:

```
## Week of [date] — [BDM_NAME]

**Stale records flagged:** [count]
[details]

**Gaps detected:** [count]
[details]

**Suggested improvements:**
1. [suggestion]
2. [suggestion]

Status: awaiting Adam / Tom review
```

Show draft. Write on confirmation.

If any suggestion is flagged as "Tom to decide": offer to Slack Tom directly.
