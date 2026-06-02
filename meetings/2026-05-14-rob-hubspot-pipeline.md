---
title: Rob — HubSpot pipeline code review (May 14)
created: 2026-05-14
updated: 2026-05-14
domain: engineering-workflows
type: meeting
tags: [engineering-workflows, hubspot, etl, coding-standards, ai-assisted-dev]
---

# Rob — HubSpot pipeline code review (May 14)

**Attendees:** Tom Harvey, Rob (developer — HubSpot ETL pipeline)

> **Note:** Only Tom Harvey listed as participant in Granola; Rob is a developer building the HubSpot ingestion pipeline and wasn't captured as a Granola participant.

Full transcript: [[2026-05-14-rob-hubspot-pipeline-transcript]]

---

## Key themes

### HubSpot ETL pipeline context
- Rob building an ETL pipeline: HubSpot → S3
- Three components: ingestion (ripping documents and email conversations from HubSpot), extraction (agentic conversion of files to JSON), presentation/persistence
- Originally coded in a spike repo with Claude; ported to platform submissions repo
- Email extraction issue fixed Friday: was pulling attachments but missing actual email conversations
- 5,000-line PR for the port; Tom provided extensive code review

### Learning Flock coding standards
- Rob previously was own technical lead with no code review culture
- Goal: build the muscle for identifying poor patterns Claude might generate
- Key refactors from Tom's review:
  - Dependency injection for testing isolation
  - Single responsibility principle violations
  - Driver/engine separation (printer/printer queue analogy)
  - Breaking 250-line functions into ~20-line components
- Rob's approach: ask Claude "is this a no-brainer refactor or ambiguous?", evaluate options, commit incrementally

### AI-assisted development challenges
- Problem: how to persist Flock coding standards knowledge in Claude's context
- Current: Claude doesn't know Flock patterns; generates code that needs manual correction
- Rob created a refactoring checklist from Tom's review comments — a starting point for a standards skill
- David flagged a Slack message about cross-repo Claude context management; Rob hadn't followed up

### Team-wide standards — open problem
- Tom's proposal: individual rule files in a `rules/` folder; skill that learns from PR reviews and creates/updates rules; links back to originating comments; records exceptions
- Challenge: developer engagement across VS Code, Cursor, JetBrains users
- ~50% of team not using AI in an AI-first way
- Social/political problem as much as a technical one

---

## Actions

- [ ] Tom: Explore rules-based coding standards approach; involve Rob in the process (→ AI-078)
- [ ] Tom: Set up a space for team-contributed rules vs. personal rules (shared vs. personal ownership)
