# Scheduled task: Weekly Pulse
# Runs: 8:00am Monday
# Replace [BDM_NAME] and [SLACK_HANDLE] before activating

Monday morning pulse for [BDM_NAME]. Team-wide patterns + personal priorities
+ Caretaker/Apprentice maintenance pass.

## Steps

1. **Last week's team activity**
   Read Shared Activity Log. Filter for last 7 days.
   - Which brokers were touched across the team?
   - Any broker touched by multiple BDMs? (potential coordination need)
   - Any BDM with zero Activity Log entries last week? (note — don't flag publicly)

2. **[BDM_NAME]'s account health**
   Read My Accounts + cross-reference Activity Log + HubSpot last_activity_date.
   - Any accounts with no contact in >14 days? → ghost candidates this week
   - Any accounts with a next action due this week?
   - Any accounts where another BDM made a move last week?

3. **Hypothesis signals**
   Read OKRs. What are we trying to move this quarter?
   Based on last week's Activity Log entries: any signals (positive or negative)
   on qualified submissions, conversion, or GWP trends?
   Keep this brief — 1–2 observations at most.

4. **Caretaker pass** (run /brain-health logic internally — do not invoke the skill)
   - Any My Commitments items overdue by >7 days?
   - Any brokers in My Accounts not found in HubSpot?
   - Any dropped threads in the Activity Log (next action logged >14 days ago, no follow-up)?
   Flag these quietly in the pulse — don't make them alarming.

5. **Apprentice suggestion** (1 item max)
   Based on last week's sessions: what one thing would make the brain more useful?
   Write it to the Brain Health Log in Notion (no confirmation needed for this write —
   it's an internal maintenance log).
   If the suggestion requires Tom's input: include it in the pulse with a note.

6. **Compose pulse**
   Format:

   > **Weekly pulse — [week of date]**
   >
   > **Team last week:**
   > [2–3 bullet observations from Step 1]
   >
   > **Your accounts this week:**
   > [priority accounts + any ghost candidates]
   > [next actions due this week]
   >
   > **One signal on the OKRs:**
   > [1 observation, or skip if nothing notable]
   >
   > **To tidy up:**
   > [overdue commitments / HubSpot gaps / dropped threads — keep to max 3]
   >
   > **Brain improvement this week:**
   > [1 suggestion, or "Nothing this week — brain's in good shape"]

   Keep the whole pulse to under 200 words. It's a Monday scan, not a report.

7. **Send**
   Send as Slack DM to [SLACK_HANDLE].
   Do not ask for confirmation — this is a scheduled task. Send directly.
