---
title: Context sharing meeting
created: 2026-04-21
updated: 2026-04-21
domain: ai-enablement
type: meeting
tags: [shared-context, team-workflows, personal-os, skills, knowledge-management]
---

# Context sharing meeting

**Date**: 2026-04-21
**Attendees**: [[tom-harvey]], [[ismael-jebril]], [[jacob-holland]], [[jemima-pitceathly]]

## Key themes

### Shared context vs individual setups
- Current AI usage mostly terminal-based and local to individuals
- Technical context more useful for developers than broad company/customer context
- Exception: investigating user behaviour in PostHog — boundary between PM-triggered and developer-triggered agents is unclear
- Shared workflows (e.g. Granola → Linear tickets) identified as clear value area

### Where should shared context live?
- **Notion**: integrates with MCP but "not very good" — endless documents, hard to navigate
- **Markdown files**: efficient for individuals but distribution and merge conflicts are problematic at team scale
- **Linear tickets**: natural shared context bridge between agents and team members
- **GitHub**: good for version-controlled skills; Notion better for broader unstructured context
- Skills can reference shared Notion docs with version control baked in

### Authentication and deployment hurdles
- Cron jobs require local machines running — if laptop is off, agent doesn't run
- AWS SSO complexity for non-technical users — biases toward developer users
- Suggestion: create limited programmatic access keys instead of SSO for bot-like agents
- Evolution path: prompts → skills → functions → Lambda deployment

### "Gandalf" agent concept
- [[jemima-pitceathly]] would build a full team member agent with portal, AWS, Slack access
- Train it locally first, then tackle OAuth/deployment challenges
- Concept: simulate a human team member rather than shared context layer

### Team memory and knowledge management
- Frequent "remember that thing we discussed" moments — answers often buried in Slack
- Team relies heavily on individual memory (acknowledged as poor)
- 1.5 years of pipeline discussions would be valuable if searchable
- Cross-team overlap detection needed — agent to review Slack channels for repetitive discussions
- Privacy concerns about recording boundaries for shared transcripts

### Granola sharing mechanics
- Individual vs collaborative notes distinction
- Full transcripts only available to note-taker
- Having multiple agents debate answers from the same meeting could be valuable

## Actions

- [ ] **[[jemima-pitceathly]]**: Identify minimal shared daily-use workflows for the retention team — discuss in tomorrow's team time
- [ ] **[[tom-harvey]]**: Send bootstrap prompt to Jemima's team channel for setting up personal dev environment OS
- [ ] **[[tom-harvey]]**: Consider Slack channel overlap analysis agent (seen externally, relates to [[AI-020-slack-channel-analysis-agent]])

## Notes

- Tom demoed the evolution of his personal OS ("the orb") — consumes Granola transcripts, updates people files, feeds into initiative tracking, used for workshop prep
- Jemima's Lovable prototype for new trips page benefited heavily from having access to database telemetry structure and definitions — example of technical context enabling PM output
- Discussion about whether non-engineers need the same tooling or a different approach — risk of biasing toward developer users

Full transcript: [[2026-04-21-context-sharing-meeting-transcript]]
