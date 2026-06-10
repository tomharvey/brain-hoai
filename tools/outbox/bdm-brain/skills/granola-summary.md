# Skill: /granola

Post-meeting Granola summary with BDM mention detection, Activity Log write,
HubSpot note, and cross-BDM notification.

Run after any broker meeting. Triggered by BDM typing `/granola` or
"log this meeting" in a co:work session.

---

## Steps

### Step 1 — Get the transcript

Ask:
> Which meeting should I summarise? You can:
> - Give me the broker name and I'll find it in Granola
> - Paste the transcript directly

If the BDM gives a broker name: search Granola for the most recent meeting
with that person/company. If multiple matches, list them and ask which one.

If pasted: use the text directly.

---

### Step 2 — Build the structured summary

Generate a summary using this exact template. Do not skip sections — write
"Nothing noted" if a section is empty.

```
## Meeting summary
**Broker:** [company name]
**Contact(s):** [names and roles if mentioned]
**Date:** [from transcript or Granola metadata]
**BDM:** [BDM_NAME]

### Key signals
What did you learn about their situation, needs, or priorities?
- [signal]
- [signal]

### Commitments — you
What did [BDM_NAME] promise to do?
- [ ] [action] — due: [date if mentioned]

### Commitments — them
What did the broker agree to do?
- [ ] [action] — due: [date if mentioned]

### Objections / blockers
What came up that could slow or block progress?
- [objection or blocker]

### Competitive signals
Any mentions of other insurers, brokers, or alternatives?
- [signal or "Nothing noted"]

### Hypothesis tested
Which conversion bet did this meeting touch?
(ghost account recovery / deal acceleration / proactive prospecting / none obvious)

### Next action
Single most important next step:
**[action]** — owner: [BDM_NAME] — due: [date or "TBD"]
```

Show the summary to the BDM. Ask: "Does this look right? Any corrections before I log it?"

Wait for confirmation or corrections. Apply any corrections, then proceed.

---

### Step 3 — BDM mention scan

Load the BDM Directory. Extract all BDM names.

Scan the transcript for any mention of a BDM name (first name OR full name).

If found:
> I noticed [Name] is mentioned in this transcript.
> Would you like me to send them a quick Slack heads-up?

If yes: draft the message (Step 6 handles sending).
If no: note it and move on.

---

### Step 4 — Activity Log entry

Draft an Activity Log entry:

```
| [today's date] | [BDM_NAME] | [broker name] | [one-line summary of what happened] | [next action] | [BDM_NAME] | [due date or —] |
```

Show it:
> Here's the Activity Log entry I'll write:
> [entry]
> Shall I add it?

Write only on confirmation.

---

### Step 5 — Cross-BDM ownership check

After writing the Activity Log entry:

1. Query HubSpot: `search_companies(name=[broker name])`
2. Get owner_id from the result
3. Look up owner_id in BDM Directory
4. If owner != [BDM_NAME]:
   - Note: "[Broker] is owned by [Owner name] in HubSpot."
   - Go to Step 6 for notification
5. If broker not in HubSpot:
   - Flag: "[Broker] isn't in HubSpot yet. Want me to add them?"
   - If yes: offer to create the Company record (show draft, confirm before creating)

---

### Step 6 — Cross-BDM Slack notification

If another BDM owns this broker (from Step 5) OR a BDM was mentioned in the
transcript (from Step 3):

Draft a Slack DM:

```
@[owner_slack_handle] — [BDM_NAME] just had a touchpoint with [broker].

Summary: [one line from the Activity Log entry]

Check the Shared Activity Log for full context.
```

Show the draft:
> Here's the Slack message I'll send to [Name]:
> [message]
> Send it?

Send only on confirmation.

---

### Step 6b — HubSpot data quality check (from this transcript)

The transcript just captured live deal state. Use it to spot stale or missing HubSpot data:

- **New contact introduced?** Someone attended who isn't in HubSpot → offer to add them
  (extract name, role, email if mentioned; search Gmail for email if not)
- **Deal stage mismatch?** What stage did the conversation imply vs. what HubSpot shows?
  If different, offer to update the deal stage
- **Company details corrected?** Broker mentioned company name, size, or HQ differently
  from HubSpot → flag the discrepancy, offer to update
- **New opportunity emerged?** Conversation implied a new deal that isn't in HubSpot yet
  → offer to create it

Present each as a specific offer before writing anything:
> "I noticed [Name] attended but isn't in HubSpot. I found their email in your Gmail
> thread from last week. Want me to add them as a contact on [Company]?"

---

### Step 7 — HubSpot engagement note (optional)

Ask:
> Want me to add an engagement note to [broker]'s HubSpot record?

If yes: draft the note:

```
[date] — [BDM_NAME]
[2-3 sentence summary: what was discussed, next action, key signal]
```

Show draft. Write only on confirmation.

---

### Step 8 — My Commitments update

Take any commitments from Step 2 (Commitments — you) that are new.

Check My Commitments: are they already logged?

If not: offer to add them:
> I'll add these to your commitments:
> [list]
> OK to write?

Write on confirmation.

---

### Step 9 — Close

> Done. Logged: Activity Log ✓, [HubSpot note ✓ if done], [Slack to [Name] ✓ if sent].
> Your commitments from this meeting are in My Commitments.
