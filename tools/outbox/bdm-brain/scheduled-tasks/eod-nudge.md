# Scheduled task: EOD Nudge
# Runs: 5:30pm Monday–Friday
# Replace [BDM_NAME] and [SLACK_HANDLE] before activating

End-of-day check-in for [BDM_NAME]. Surfaces what needs logging before tomorrow.

## Steps

1. **Today's external meetings**
   Read GCal for today. Find any events that have already ended with external attendees.

2. **Granola coverage check**
   For each external meeting: does a Granola transcript exist for it?
   - If yes: note it as available to log
   - If no: flag it as needing a manual note

3. **Commitments completed today**
   Read My Commitments. Are any items due today or marked complete?

4. **Open actions due this week**
   Any My Commitments items due in the next 2 days that haven't moved?

5. **Compose nudge**
   Keep it brief. This is a 30-second read.

   If meetings happened today:
   > **EOD — [date]**
   >
   > **Meetings to log:**
   > - [Meeting] with [broker] — Granola transcript available ✓ (type `/granola` to log it)
   > - [Meeting] with [broker] — no transcript found. Anything worth logging manually?
   >
   > **Upcoming:**
   > - [action] due [day] — still open
   >
   > [link to open co:work session]

   If no external meetings today:
   > No external meetings today. [Commitments due soon if any, otherwise: "All clear — see you tomorrow."]

6. **Send**
   Send as Slack DM to [SLACK_HANDLE].
   Do not ask for confirmation — this is a scheduled task. Send directly.
   Include a direct link to open this co:work project if the platform supports it.
