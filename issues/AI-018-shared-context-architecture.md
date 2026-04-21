---
title: "Define shared context architecture for teams"
id: AI-018
created: 2026-04-21
updated: 2026-04-21
origin: "[[2026-04-21-codifying-context-retention-team]]"
domain: ai-enablement
type: issue
status: todo
priority: medium
assignee: tom
tags: [shared-context, team-os, skills, architecture]
---

## Description

The retention team's codifying context session surfaced the key unresolved question: **how do teams share AI context, skills, and knowledge?**

Everyone is building personal operating systems (Tom, Jemima, Harvey, Fergus, Jacob, Ismael). The next step is sharing useful context across the team without:
- Biasing toward developer-only workflows
- Sharing private/sensitive context
- Creating git conflict hell with shared markdown
- Depending on laptops being on

### Options discussed

| Option | Pros | Cons |
|--------|------|------|
| GitHub repo | Version control, developer-native | Non-devs excluded, git conflicts |
| Notion | Non-dev friendly, existing MCP | MCP quality poor, "never-ending ball of documents" |
| Markdown + vector search | Efficient, fast search | Distribution unclear, laptop-bound |
| Shared Lambda/agent | Team-level access, always-on | Auth complexity, AWS SSO headaches |

### Concrete shared needs identified
- Granola → Linear ticket creation skill
- Code review process/style standards
- Ticket naming conventions
- Team expertise mapping (for auto-assignment, onboarding)
- Database/telemetry structure definitions (for non-technical roles)

## Acceptance criteria

- [ ] Identify the minimal shared context items (retention team workshop Tue Apr 22)
- [ ] Decide where shared skills/context lives (GitHub, Notion, or hybrid)
- [ ] Prototype one shared skill distributed across the team
- [ ] Plan cross-team session (Thu Apr 24) to extend beyond engineering

## Links

- [[2026-04-21-codifying-context-retention-team]]
- [[skills-distribution]]
- [[ai-capability-uplift]]
