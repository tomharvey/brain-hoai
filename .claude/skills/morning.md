# /morning — Morning Brief

Generate a morning brief to start the day.

## When to use

Run at the start of a working session to get oriented.

## Steps

1. Read `WORKING.md` for any interrupted work from a previous session.
2. List files modified in the last 48 hours using `git log --since="48 hours ago" --name-only --pretty=format:""` or file timestamps if git is unavailable.
3. Count items in `inbox/` (excluding .gitkeep).
4. Scan `initiatives/` for all active initiatives (status: active in frontmatter). Summarise each in one line.
5. Check yesterday's meeting notes (if any) in `meetings/` for unchecked action items.
6. Check if a weekly review is due: look at `reviews/` for the current ISO week file. If missing, it's due.

## Output

Print to terminal only — do not create a file. Format as:

```
# Morning Brief — YYYY-MM-DD

## Interrupted work
[contents of WORKING.md current task, or "None"]

## Inbox
[N items pending triage, or "Empty"]

## Active initiatives
[one-line summary per active initiative, or "None yet"]

## Open actions
[unchecked actions from recent meetings, or "None found"]

## Upcoming
- Weekly review: [due / not due]
```
