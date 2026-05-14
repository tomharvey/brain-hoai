---
title: "AI-043: Create super repo for shared engineering context"
created: 2026-05-12
updated: 2026-05-12
type: issue
status: todo
priority: high
domain: engineering-workflows
origin: "[[2026-05-12-david-ai-engineering]]"
tags: [super-repo, agents, context, engineering, coding-standards]
---

# AI-043: Create super repo for shared engineering context

Agreed pattern with David and Chris: a "super repository" that holds common agent context (`agents.md`) at the top level. Individual repos (platform-services, platform-frontend, etc.) maintain their own `agents.md` files that link up to the shared context.

Allows agents to work cross-repo from the super repo, or focused within a single repo while still referencing shared architecture principles.

Tom to create the repo structure and tag David in before paternity leave (~1 week).

Related: David's Notion doc and PR (platform-services/pull/3961) contain his thinking on this.

## Also includes
- `rules/` directory for explicit coding standards (one file per rule, linked to originating review comments)
- ESLint rule generation where applicable
- Backlinking: agents cite sources for decisions → limits hallucination, makes reviews auditable
