---
name: granola
description: Import meeting notes and transcripts from Granola into the vault
---

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

### 4. Resolve names against the org chart

Before writing any meeting note, validate every person name that appears in the transcript against `people/` and the known team structure.

**Load the name resolution data store first:** Read `people/name-resolution.yaml`. It contains four sections:

- `substitutions` — names Granola mishears (errors to correct). Each entry has a `heard` value (what appears in the raw transcript), a `person` (canonical `people/` filename), `phonetics` (why the error happens), and an optional `guard` condition. Apply every substitution whose guard condition is satisfied.
- `nicknames` — correct short forms that are NOT errors. Map each to its canonical person.
- `disambiguation` — people who share a first name. Use `context_clues` to decide which person is meant based on topic, team, and domain.
- `speaker_context` — known accent and speech patterns per person. Use this to anticipate likely transcription errors even before they appear in the transcript.

**How to resolve:**
1. Read `people/name-resolution.yaml` and load all four sections.
2. List all `people/` files — each filename is a canonical ID.
3. For every name in the transcript: check substitutions first (apply if guard is met), then nicknames, then disambiguation.
4. For any name with no match: glob `people/*.md` and look for phonetic neighbours. Use `speaker_context` accent notes to guide the search. A name that sounds like a known person but differs by one phoneme is almost certainly a transcription error.
5. Use the canonical name (from the `title:` field in `people/<person>.md`) in all meeting notes and issues.
6. Do NOT silently accept a name that appears in no people file — surface it to the user.

### 5. Create meeting notes

For each selected meeting, create two files:

**Meeting note** at `meetings/YYYY-MM-DD-kebab-title.md`:
- Standard vault frontmatter (title, created, updated, domain, type: meeting, tags)
- Infer `domain` from content. If unclear, ask or use the most likely fit.
- Structure: attendees (as `[[person]]` wikilinks), key themes (grouped, summarised from the AI summary), actions (as checkboxes with owners), and notes.
- Link to transcript: `Full transcript: [[YYYY-MM-DD-kebab-title-transcript]]`

**Transcript** at `meetings/transcripts/YYYY-MM-DD-kebab-title.md`:
- Frontmatter: title (with "— transcript" suffix), meeting (filename of parent note), created, type: transcript
- Raw transcript text as-is from Granola

### 6. Naming

- Kebab-case the meeting title for filenames
- If a meeting note already exists at that path, warn the user before overwriting
- Use the meeting date from Granola, not today's date, for the filename and `created` field

### 7. Create issues for actions

For each action item in the imported meeting notes, create an issue in `issues/` (AI-NNN format, sequential). Set:
- `origin: "[[meeting-note-filename]]"`
- `due` date if the action had a deadline or one can be inferred
- `status: todo`
- Assign `domain` from the meeting note

### 8. Synthesis pass

After all files are created, ask: does this meeting change what we believe?

- Read the relevant `domains/<domain>/index.md`. If the meeting content confirms, challenges, or adds nuance to a belief bullet, update it in-place (add, revise, or move a bullet).
- Scan `initiatives/` for any active initiatives touched by the meeting. Update `updated` date and add a one-line note if the meeting advances or changes status.
- Check `issues/` for any open issues whose context this meeting adds to. Add a brief note if relevant.
- If the meeting introduces a brand-new strategic question not yet captured anywhere, add it to the domain's "What we're uncertain about" section.
- Keep edits tight — one or two sentences per change. The goal is live documents, not rewrites.

### 9. Confirm

Report what was created:

```
Imported N meetings:
- meetings/YYYY-MM-DD-title.md (+ transcript)
- issues/AI-NNN-action-item.md
- Updated: domains/<domain>/index.md
```
