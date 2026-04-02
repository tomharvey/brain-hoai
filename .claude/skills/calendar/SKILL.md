---
name: calendar
description: Find availability, create and update calendar events using the gws CLI
disable-model-invocation: true
---

# /calendar — Manage calendar events

Find availability, create, and update calendar events using the `gws` CLI tool.

## When to use

When the user wants to schedule a meeting, find free time, check their calendar, or update an existing event.

## Tools

Uses `gws calendar` CLI. Key commands:
- `gws calendar events list` — list events
- `gws calendar events insert` — create events
- `gws calendar events patch` — update events
- `gws calendar events delete` — delete events
- `gws calendar freebusy query` — check availability across multiple people

## Rules

### Never send without confirmation

**NEVER** create or send a calendar invite without explicit user approval. Always present the full details first and wait for a "yes":

1. **Title** — proposed event title
2. **Description** — what the meeting is about
3. **Attendees** — full names of all attendees (not just email addresses)
4. **Time** — in both CET (Tom's timezone) and UK time
5. **Duration**

Only after the user confirms, call the API.

### Time preferences

- Tom prefers **morning** slots when given a choice.
- Tom is in **Valencia, Spain (CET/CEST)**. Always show his time first, then UK time.
- When finding mutual availability, look for the **earliest available slot** unless told otherwise.

### Finding availability

1. Use `gws calendar freebusy query` with both participants' email addresses.
2. Calculate mutual free slots (minimum 15 min unless told otherwise).
3. Present a shortlist of options, earliest first.
4. Email addresses usually follow the pattern `firstname.lastname@flockcover.com`. Some compound surnames are concatenated (e.g. `jordi.pallaresroset@flockcover.com`). Check `people/` files if unsure, and verify with freebusy (a "notFound" error means wrong email).
5. **Always convert UTC to local time when presenting to the user.** API uses UTC (Z suffix) but Tom is in CEST (UTC+2 in summer, UTC+1 in winter) and UK colleagues are in BST (UTC+1 in summer, UTC+0 in winter). Never present UTC as if it were UK time.

### Creating events

- Use `sendUpdates: "all"` so attendees receive the invite.
- Set `timeZone: "Europe/London"` (the company is UK-based).
- **Always include a Google Meet link.** Use `conferenceDataVersion: 1` in params and include `conferenceData.createRequest` in the body (see format below).
- Always include a description. If the user doesn't provide one, suggest one and confirm.
- Title format: `Tom <> Name: Topic` for 1:1s, descriptive title for group meetings.

### Updating events

- When updating, use `patch` not `insert`.
- Include `sendUpdates: "all"` so attendees see changes.

### Listing events

- When showing a calendar view, filter out `workingLocation` and `cancelled` events.
- Show: time (CET + UK), title, attendees (names not emails).
- Group by day.

## Freebusy query format

```bash
gws calendar freebusy query --json '{
  "timeMin": "YYYY-MM-DDT08:00:00Z",
  "timeMax": "YYYY-MM-DDT17:00:00Z",
  "items": [
    {"id": "person@flockcover.com"},
    {"id": "tom.harvey@flockcover.com"}
  ]
}'
```

## Event creation format

```bash
gws calendar events insert --json '{
  "summary": "Event title",
  "description": "Event description",
  "start": {
    "dateTime": "YYYY-MM-DDTHH:MM:00Z",
    "timeZone": "Europe/London"
  },
  "end": {
    "dateTime": "YYYY-MM-DDTHH:MM:00Z",
    "timeZone": "Europe/London"
  },
  "attendees": [
    {"email": "attendee@flockcover.com"},
    {"email": "tom.harvey@flockcover.com", "responseStatus": "accepted"}
  ],
  "conferenceData": {
    "createRequest": {
      "requestId": "unique-id-here",
      "conferenceSolutionKey": {
        "type": "hangoutsMeet"
      }
    }
  }
}' --params '{"calendarId": "primary", "sendUpdates": "all", "conferenceDataVersion": 1}'
```
