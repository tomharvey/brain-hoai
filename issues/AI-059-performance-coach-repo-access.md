---
title: "AI-059: Get access to performance coach repo and evaluate for wider adoption"
created: 2026-05-19
updated: 2026-05-19
domain: ai-enablement
type: issue
status: todo
priority: medium
origin: "[[2026-05-19-francesco-ai-catchup]]"
tags: [francesco, performance-coach, mcp, tooling]
---

## Summary

[[francesco-venerandi|Francesco Venerandi]] and [[ollie-crowe|Ollie Crowe]] have built a MCP-based career performance coaching system. Francesco to add Tom (GitHub: tomvey) to the repo. Evaluate for company-wide adoption.

## Context

The system connects Granola transcripts, Slack, Notion, and Google Calendar to:
1. Track weekly progress against manager-defined promotion criteria
2. Prep and follow up on 1:1 meetings
3. Provide weekly performance coaching with improvement suggestions

Currently used by Francesco, Ollie, and potentially [[javier|Javier]]. Requires a written promotion rubric from your manager as the starting point — which surfaces a broader Flock process gap ([[milan-chavda|Milan]] gives one, most managers don't).

The MCP-based release model (instructions as MD files in GitHub) means updates deploy without users having to reinstall anything — elegant pattern worth examining.

## Actions

- [ ] **Francesco**: Add Tom to GitHub repo (username: tomvey)
- [ ] **Tom**: Review code and architecture
- [ ] **Tom**: Assess whether this should be presented at AI breakfast or rolled out more broadly
- [ ] **Tom**: Flag the promotion rubric gap to Rakhee — should this be standard practice?

## Notes

- The tool is only as good as the quality of the promotion rubric. Milan's approach (written criteria, cleared with Darren) is the gold standard.
- Bob is the official system for goals but is widely considered too low-frequency and too disconnected from day-to-day work to be useful.
