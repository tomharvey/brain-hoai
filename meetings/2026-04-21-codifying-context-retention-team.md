---
title: "Codifying context for retention team"
created: 2026-04-21
updated: 2026-04-21
domain: ai-enablement
type: meeting
tags: [shared-context, skills, team-os, retention]
---

# Codifying context for retention team

**Combined from two Granola recordings** — Tom's "Context sharing meeting" and Jemima's "Codifying Context for Retention Team."

## Attendees

- [[mima|Jemima Pitceathly]]
- [[ishmael|Ismael Jebril]]
- [[jacob-holland|Jacob Holland]]
- [[stephen-millington|Stephen Millington]]
- Tom Harvey

## Key themes

### Shared skills as clear first win

Team agrees Granola→Linear ticket creation, code review processes, and ticket naming conventions are shared skills everyone needs. Writing up tickets is the most obvious starting point.

### Context distribution challenge

Where do shared resources live? GitHub (version control, developer-native) vs Notion (integrates well for non-devs, MCP available but poor quality) vs markdown files (efficient, vector-searchable, but distribution unclear). No resolution — the "where" is the hardest question.

### Individual vs team context

Personal communication styles, stakeholder opinions belong in personal OS. Team expertise mapping, domain knowledge, technical definitions (database structure, calculations) could be shared. Jemima's Lovable prototype for trips page was technically feasible because she had access to technical context via Granola/MCP.

### Memory problem

"I've lost count of the times we've said 'remember that thing?'" — team repeatedly loses and rediscovers information. Slack messages resent, pipeline conversations from 18 months lost. Meeting memory and conversation history identified as valuable if privacy boundaries exist.

### Personal OS momentum

Tom demoed his "orb" (Head of AI vault consuming Granola, updating people files and initiatives). Jemima has similar. Harvey touring around with developer OS. Fergus exploring. Jacob built automated documentation agents. Question: how do we go from personal OS to team?

### Authentication/infrastructure barrier

AWS SSO, OAuth tokens, laptop dependency. "If my laptop's off, the agent doesn't run." Lambda deployment discussed as evolution path for shared team agents. Jemima's vision: "Gandalf" as a team-level agent with portal/AWS/Slack access — an actual Flock worker.

### Developer bias risk

Stephen flagged that shared context approaches skew toward developer workflows. Non-engineers need different access patterns.

## Actions

- [ ] **[[mima|Jemima]]**: Facilitate tomorrow's team time — identify minimal daily-use items for standardization
- [ ] **Tom**: Share development environment bootstrap prompt with the team (via Slack)
- [ ] **[[mima|Jemima]]**: Plan cross-team workshop Thursday morning with non-engineers
- [ ] **Tom**: Explore Slack channel analysis agent for repetition/overlap detection between teams
- [ ] **[[jacob-holland|Jacob]]**: Consider encoding data extraction skills for wider team ([[ishmael|Ismael]], Kirsty, Ben)

## Transcript

Full transcript: [[2026-04-21-codifying-context-retention-team-transcript]]
