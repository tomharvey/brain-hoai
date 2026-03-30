# /granola — Import meetings from Granola

Import meeting notes and transcripts from Granola into the vault, with user confirmation on which meetings are in scope.

## When to use

When the user wants to import recent meetings from Granola, or when running as part of a session startup or weekly review.

## Steps

### 1. Fetch meetings

Use `mcp__granola__list_meetings` to fetch recent meetings. Default to `this_week` unless the user specifies a range. For custom ranges, use `custom` with ISO date strings.

### 2. Present for scoping

Display meetings in a numbered table:

```
| # | Meeting | Date |
|---|---------|------|
| 1 | Title   | Day  |
```

Ask: **"Which of these are in scope for the project? Give me the numbers."**

Do NOT assume which meetings are relevant. The user works across multiple contexts — only they know what belongs in this vault.

### 3. Fetch full content

For each selected meeting, fetch in parallel:
- `mcp__granola__get_meetings` (summary, private notes, attendees)
- `mcp__granola__get_meeting_transcript` (verbatim transcript)

### 4. Create meeting notes

For each selected meeting, create two files:

**Meeting note** at `meetings/YYYY-MM-DD-kebab-title.md`:
- Standard vault frontmatter (title, created, updated, domain, type: meeting, tags)
- Infer `domain` from content. If unclear, ask or use the most likely fit.
- Structure: attendees (as `[[person]]` wikilinks), key themes (grouped, summarised from the AI summary), actions (as checkboxes with owners), and notes.
- Link to transcript: `Full transcript: [[YYYY-MM-DD-kebab-title-transcript]]`

**Transcript** at `meetings/transcripts/YYYY-MM-DD-kebab-title.md`:
- Frontmatter: title (with "— transcript" suffix), meeting (filename of parent note), created, type: transcript
- Raw transcript text as-is from Granola

### 5. Naming

- Kebab-case the meeting title for filenames
- If a meeting note already exists at that path, warn the user before overwriting
- Use the meeting date from Granola, not today's date, for the filename and `created` field

### 6. Confirm

Report what was created:

```
Imported N meetings:
- meetings/YYYY-MM-DD-title.md (+ transcript)
- ...
```
