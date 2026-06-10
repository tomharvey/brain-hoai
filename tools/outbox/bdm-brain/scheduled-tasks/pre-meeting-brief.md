# Scheduled task: Pre-meeting Brief
# Runs: every 15 minutes, 7:30–18:00 Monday–Friday
# (fires only when a qualifying event is found 25–35 minutes out)
# Replace [BDM_NAME] and [SLACK_HANDLE] before activating

Check for an upcoming external meeting in the next 25–35 minutes.

## Step 1 — Check calendar

Read GCal. Find any event starting 25–35 minutes from now.

Qualifying event = has at least one attendee with an external email domain
(not @flockcover.com).

If no qualifying event: do nothing. Do not send anything.

If qualifying event found: continue.

---

## Step 2 — Identify the broker

Extract company/broker name from:
- Event title
- Attendee email domains
- Event description

If unclear: use the attendee's email domain as the company name for lookups.

---

## Step 3 — Pull Layer 3 context

Run these in parallel:
- HubSpot: search_companies(name=[broker]) → get stage, last_activity_date, open tasks, last note
- Granola: search for most recent 2–3 meetings with this broker
- Gmail: recent threads with this broker's email domain (last 5)
- Activity Log: has any other BDM touched this broker this week?

---

## Step 4 — Check My Commitments

Did [BDM_NAME] make any promises to this broker in past meetings that aren't
yet marked complete in My Commitments?

---

## Step 5 — Compose brief

Format:

> **Pre-call brief — [broker] — [time]**
>
> **What I know:**
> [2–4 bullet points: stage, last contact, key context from Granola/Gmail]
>
> **Open commitments from you:**
> [list from My Commitments, or "None outstanding"]
>
> **From the team:**
> [any Activity Log entries from other BDMs this week, or "No team activity this week"]
>
> **Lead with:**
> [1 suggested opening based on context — informed by My Shortcuts pre-call priority]
>
> **Watch for:**
> [1 thing to watch: an objection pattern, a stalled point, a ghost risk]

Keep it short. This is read in 60 seconds before picking up the phone.

---

## Step 6 — Send

Send as Slack DM to [SLACK_HANDLE].
Do not ask for confirmation — this is a scheduled task. Send directly.
