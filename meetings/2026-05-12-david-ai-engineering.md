---
title: "Tom <> David: AI Engineering — Super Repo, Coding Standards, Agent Harness"
created: 2026-05-12
updated: 2026-05-12
domain: engineering-workflows
type: meeting
tags: [engineering, super-repo, coding-standards, agent-harness, knowledge-structure, code-review]
---

# Tom <> David: AI Engineering

**Date**: 2026-05-12 11:30
**Attendees**: [[tom-harvey]], [[david]]

Full transcript: [[2026-05-12-david-ai-engineering-transcript]]

---

## Context

David going on paternity leave in ~1 week. Covering AI engineering direction, super repo structure, coding standards from code review, and multiplayer agent challenges. Also: knowledge handoff before he leaves.

---

## Key themes

### Shared context across repos — the super repo pattern

- David created a Notion doc and a draft PR (platform-services/pull/3961) on structuring knowledge for AI coding agents
- Problem: context needed for the inboxes service is the same as for the document service — but you can't duplicate it across every repo
- **Super repository approach**:
  - Main ("super") repo holds shared context in a common `agents.md`
  - Individual repos maintain their own `agents.md` files that link up to the shared context
  - Allows cross-repo agent work from the super repo; agents can still work focused within a single repo
  - Analogy: like hoisting state in React — run your agent higher up the tree
- Agents can now switch between planning and building modes automatically (at least in Cursor) — David no longer needs to explicitly prompt "investigate before coding"
- Architecture enforcement through AI: front-end features shouldn't reference other features; onion pattern and CQRS rules prevent improper layer communication — import analysis could catch violations automatically

### Code review → coding standards skill

- Tom's proposal: take GitHub review comments and convert them into explicit coding standards
- Structure: `rules/` directory, one file per rule, each rule links to the originating comment, conflicting comments, validating comments
- Generate ESLint rules where appropriate; embed examples otherwise
- Focuses on architectural rules (wrong layer references, CQRS violations) more than syntax fixes
- Connects to backlinking idea: forcing the agent to cite its decisions limits hallucination and makes reviews readable
- David's current AI usage: much more focused on context-setting than code-writing
  - Uses Google Meet transcripts as context input (available 15-30 mins after calls) — can extract a specific team member's idea from a transcript and feed it to the agent

### Markdown files as a data layer, not human documents

- Key mindset shift: stop thinking of agents.md and rules files as documents to be read; they're a binary data layer for agents
- David: "it's even more interesting for agents to update that data if they feel it's wrong rather than for you to do that work"
- Backlinking in files (agent cites sources for its decisions) limits hallucination and makes outputs auditable
- Need for evals/harness testing: how do you verify that the context you've given the agent produces the right results?

### Multiplayer — unsolved

- 10-15 developers, 3 teams, different approaches and preferences
- Getting everyone onto the same patterns = consistency, less refactoring, less tech debt
- But: developer context is personal; forcing one setup kills individual effectiveness
- Tom's view: probably a spectrum — some context is shared (architecture rules, team standards), some is personal (individual workflows, preferences)
- No clear industry answer yet
- Alex Smith (David's team) is careful/deliberate — a good target for demonstrating that agent-assisted code can meet Chris and Alex's quality bar

### Knowledge handoff before paternity leave

- Everyone has skills stashed on local machines — David included
- Need to push David's skills to Alex Smith before David leaves
- Tom to tag David in on super repo approach + structure

---

## Actions

- [ ] **David**: Share all skills with Alex Smith before paternity leave
- [ ] **Tom**: Create super repo structure and tag David in (can start today)
- [ ] **Tom**: Draft code-review → coding standards skill
- [ ] **Tom + David**: Get David's skills pushed to team before he goes — treat as priority this week
