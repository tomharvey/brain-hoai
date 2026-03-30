---
title: Skills in engineering drop-in meeting
created: 2026-03-25
updated: 2026-03-27
domain: engineering-workflows
type: meeting
tags: [skills, claude, tooling, community]
---

# Skills in engineering drop-in meeting

**Date**: 2026-03-25 14:10
**Attendees**: Tom, engineering group

## Key themes

### Skills development and distribution
- Skills reduce Claude's thinking time on frequent tasks
- Risk of broken implementations when relying solely on AI-generated skills without content validation
- Need structured approach to sharing: public repos, cross-team adoption
- Avoid individual "superpowers" that don't scale to whole team

### Building blocks defined (pre-recording discussion)
1. Prompts
2. MCP tools
3. MCP resources
4. MCP queries
5. Plugins

### Claude vs ChatGPT standardisation
- Company currently split between Claude and ChatGPT users
- Skills development creates barrier for ChatGPT users
- Recommendation: standardise on Claude for tool development
- Enterprise deal negotiation potential (ToS concerns)

### Performance testing demo
- Automated 42-second performance tests on every PR
- Configured for agora contract manager (accruals and marks)
- 5,000 test runs each, captures mean from middle three results
- Non-blocking PR comments for 30%+ performance degradation

### WhatsApp driver reporting flow demo
- Built in 1.5 hours using co-work, GitHub, render.com
- Integrated with Anthropic API and Twilio
- Full driver flow with contextual responses (not structured Q&A)

## Actions

- [ ] Install Claude desktop company-wide
- [ ] Evaluate ChatGPT removal and migration tools
- [ ] Determine skill release/versioning strategy (local repo vs centralised distribution)
- [ ] Set up communication channels — rename MCP stomp works channel, create non-technical AI discuss channel
