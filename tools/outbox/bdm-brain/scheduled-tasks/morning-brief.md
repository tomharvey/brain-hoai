# Scheduled task: Morning Brief
# Runs: 8:00am Monday–Friday
# Replace [BDM_NAME] and [SLACK_HANDLE] before activating

Run a morning brief for [BDM_NAME].

## Steps

1. **Team activity since yesterday**
   Read the Shared Activity Log. Filter for entries from the last 24 hours.
   Any entries from other BDMs that touch [BDM_NAME]'s accounts (cross-reference My Accounts)?

2. **Commitments due today**
   Read My Commitments. Anything due today? Anything overdue?

3. **Today's meetings**
   Read GCal for today. List all external meetings (with broker/company names).
   For each external meeting:
   - Pull HubSpot record: current stage, last activity, any open tasks
   - Pull Granola: most recent transcript with this contact
   - Note: has another BDM touched this broker this week? (check Activity Log)
   Flag anything [BDM_NAME] should know before the call.

4. **Ghost alert (if any)**
   Read My Accounts. Are any brokers at 14+ days with no contact?
   If yes: flag 1–2 most urgent. Don't list all of them — just the most time-sensitive.

5. **Compose brief**
   Format depends on preference:
   - BULLETS: 5–7 items, one line each. Lead with anything urgent or time-sensitive.
   - NARRATIVE: short paragraph per theme. No more than 3 paragraphs total.

   Always lead with: "No urgent items — good morning" if there's nothing pressing.

6. **Send**
   Send as Slack DM to [SLACK_HANDLE].
   Do not ask for confirmation — this is a scheduled task. Send directly.
