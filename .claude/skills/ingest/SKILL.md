---
name: ingest
description: Triage and route inbox items to their correct vault locations
---

# /ingest — Process Inbox

Triage and route inbox items to their correct locations.

## When to use

When `inbox/` has items that need sorting — flagged by `/morning` or noticed during a session.

## Steps

1. List all files in `inbox/` (excluding .gitkeep).
2. Read each file and determine:
   - **Type**: initiative, decision, meeting, person, reference, or remains inbox
   - **Domain**: engineering-workflows, operational-tooling, product-ai, ai-enablement, or none
   - **Destination**: the target directory and filename (kebab-case)
3. Present the triage plan as a table:

```
| Source | → Destination | Domain | Type |
|--------|---------------|--------|------|
| inbox/raw-note.md | initiatives/copilot-rollout.md | engineering-workflows | initiative |
```

4. Ask the user for confirmation before moving anything.
5. For each confirmed move:
   - Move the file to the destination.
   - Add or update YAML frontmatter (title, created, updated, domain, type, status, tags).
   - Preserve the original creation date.
6. Apply these rules:
   - Never delete files — move or leave in place.
   - Items that are too vague to classify: leave in `inbox/` with a `needs-context` tag added.
   - Multi-topic notes: split into separate files, one per topic.
   - Update wikilinks in other files if filenames change.
7. Report what was moved and what remains in inbox.
