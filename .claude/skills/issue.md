# /issue — Create or update an issue

Manage issues in the local markdown tracker (`issues/` directory).

## When to use

When the user wants to create a new issue, update an existing one, list issues, or view a board/kanban of current work.

## Creating an issue

1. Determine the next issue ID by scanning `issues/` for the highest existing `AI-NNN` number and incrementing by one. If no issues exist, start at `AI-001`.
2. Ask for or infer: title, domain, priority (default: medium), assignee (optional), and description.
3. Create the file at `issues/AI-NNN-kebab-case-title.md` using the template at `reference/templates/issue.md`.
4. Set `id: AI-NNN`, `status: backlog` (unless told otherwise), `created` and `updated` to today's date.
5. Confirm creation with the issue ID and title.

## Updating an issue

1. Find the issue file by ID (e.g. `AI-007`) or keyword search in `issues/`.
2. Update the requested fields in frontmatter (status, priority, assignee, etc.) and/or body content.
3. Set `updated` to today's date.
4. Confirm what changed.

## Listing issues

When asked to list, show, or board issues:

1. Read all files in `issues/`.
2. Parse frontmatter from each.
3. Display grouped by status in this order: `in-progress`, `todo`, `backlog`, `done`, `cancelled`.
4. Format each entry as: `AI-NNN | priority | title | assignee | domain`.
5. Omit `done` and `cancelled` unless explicitly asked for.

## Closing an issue

1. Set `status: done` and `updated` to today's date.
2. If the user provides a reason or resolution, append it under a `## Resolution` section.
