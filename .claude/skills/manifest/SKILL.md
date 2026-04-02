---
name: manifest
description: Rebuild MANIFEST.md vault index from current vault contents
---

# /manifest — Rebuild Vault Index

Rebuild MANIFEST.md from vault contents.

## When to use

Run at the end of a session, or whenever the vault structure has changed.

## Steps

1. Walk all directories, skipping `.claude/`, `.git/`, `node_modules/`, `.obsidian/`, `.devcontainer/`, `meetings/transcripts/`.
2. For each `.md` file found (excluding root-level README.md, CLAUDE.md, AGENTS.md, BOOTSTRAP.md, WORKING.md, MANIFEST.md), parse YAML frontmatter to extract title, domain, type, status, created, and updated dates.
3. Group notes by domain, then by type.
4. Generate a "Recent (last 7 days)" section listing notes with updated or created dates within the last 7 days.
5. Write the result to `MANIFEST.md` with the format:

```markdown
# Manifest

> Auto-generated. Rebuild with `/manifest`. Last updated: YYYY-MM-DD.

## Recent (last 7 days)

- [[filename]] — title (status)

## By domain

### Engineering Workflows
- [[filename]] — title (status)

### Operational Tooling
...

### Product AI
...

### AI Enablement
...

## Initiatives
...

## Decisions
...

## Meetings
...

## Reviews
...

## People
...

## Reference
...
```

6. Entry format: `- [[filename]] — title (status if applicable)`. Omit status for types that don't use it.
7. Show "_No notes yet._" for empty sections.
