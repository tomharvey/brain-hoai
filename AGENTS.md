# Head of AI Operating System — Agent Guide

This vault is a markdown-native personal operating system for a Head of AI at an insurtech company. It is the single source of truth for strategy, decisions, initiatives, meeting notes, and weekly operating rhythm across four domains: engineering-workflows, operational-tooling, product-ai, and ai-enablement.

## Folder structure

| Directory | Contents |
|-----------|----------|
| `inbox/` | Unsorted captures, raw notes, quick thoughts |
| `domains/` | Strategy and roadmap docs per domain (engineering-workflows, operational-tooling, product-ai, ai-enablement) |
| `initiatives/` | Active initiatives with status tracking |
| `decisions/` | Decision records in MADR format |
| `meetings/` | Meeting notes by date |
| `people/` | Stakeholder notes, 1:1 logs |
| `reviews/` | Weekly reviews, monthly reflections |
| `reference/templates/` | Note templates |

## Frontmatter conventions

Every note has YAML frontmatter with these fields:

```yaml
---
title: Note title
created: YYYY-MM-DD
updated: YYYY-MM-DD
domain: engineering-workflows | operational-tooling | product-ai | ai-enablement
type: initiative | decision | meeting | person | review | reference | inbox
status: active | paused | completed | abandoned  # for initiatives and decisions
tags: []
---
```

## Links

Use wikilinks: `[[note-name]]` or `[[note-name|display text]]`.

## Getting started

- Read `WORKING.md` for current task state and interrupted work.
- Read `MANIFEST.md` for a navigable index of all vault contents.
