---
title: Skills AI session
created: 2026-03-27
updated: 2026-03-27
domain: ai-enablement
type: meeting
tags: [skills, training, claude, cross-functional]
---

# Skills AI session

**Date**: 2026-03-27 12:03
**Attendees**: Tom, group session (dev and non-dev)

Full transcript: [[2026-03-27-skills-ai-session-transcript]]

## Key themes

### What is a skill?
- Files containing context and procedures to make AI agents smarter about Flock-specific workflows
- Three core components:
  1. **Context**: company info, terminology, brand rules, customer details
  2. **Procedure**: step-by-step workflow instructions, escalation triggers
  3. **References**: code snippets, templates, document links
- Skills sit on top of MCPs (data access) to provide procedural knowledge
- Created via conversation with Claude using a skill creator skill

### Problems skills address
- Flock knowledge siloed across teams — every new Claude conversation starts from scratch
- No shared vocabulary between devs and non-devs for AI solutions
- MCPs provide data access without usage instructions — like giving database access without documentation

### Skill creation process
- Use skill creator skill in Claude
- Provide initial context prompt, Claude asks clarification questions iteratively
- Generates skill with proper structure automatically
- Review content with domain expert, test and refine
- Can create skills retroactively after successful workflows

### Skills currently in development
- **Flock deck builder** ([[mima]]) — brand-consistent presentations
- **Engine room review** — policy change investigation procedures
- **Renewals spreadsheet** (Job, [[anna|Anna]]) — weekly manual process automation
- **Broker deck** ([[kirsty]]) — customer context compilation
- **Platform frontend patterns** ([[sam]]) — consistency standards
- **NPM library skills** ([[chris]]) — T3 stack integration
- **Linear ticket creator** — standardised ticket formatting

### Distribution challenges
- No central catalogue of existing skills
- Unclear ownership for non-engineering skills
- Manual version updates required
- Good prompts disappear into private conversations
- Proposed solution: dedicated skills repo with GitHub integration (automatic updates to Claude plugins, clear ownership, version control)

## Actions

- [ ] Try existing skills (presentation builder, ticket creator)
- [ ] Identify repetitive workflows suitable for skill creation
- [ ] Reach out to initiative owners for collaboration
- [ ] Consider GitHub repo structure for company-wide sharing
- [ ] Explore template-based approaches for more deterministic outputs

## Notes

Session 1 of a planned series. Goal: get everyone at Flock — dev and non-dev — speaking the same language about how they work with AI tools that include skills.
