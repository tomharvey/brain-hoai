---
title: AI-097 — Trading pack data integrity review
created: 2026-06-10
updated: 2026-06-10
domain: ai-enablement
type: issue
status: todo
priority: high
origin: "[[2026-06-10-adam-thomas-bdm-team-ai]]"
tags: [adam-smith, trading-pack, kirsty, data-quality, cowork, skill]
---

# AI-097 — Trading pack data integrity review

Adam's Claude-generated trading pack (co:work skill, FP&A + HubSpot data) produced
data discrepancies in the June SLT trading meeting. Flo flagged it; Adam linked up
with Tom to fix.

## What to do

1. Adam to share: the trading pack skill file + transcript of the SLT meeting where
   discrepancies were raised
2. Tom: review the skill prompts — identify where the validation logic is weak
3. Recommend: skill should store the SQL queries it generates as named examples
   inside the skill file. On each subsequent run, the skill uses those stored queries
   (repeatability), not freshly generated ones (drift risk)
4. Share the stored queries with [[kirsty]] — she validates whether the queries are
   pulling from the right FP&A sources and match what she surfaces in reporting
5. Tripartite: Adam's prompt iteration → Tom's prompt engineering → Kirsty's data
   validation. Don't show up to Kirsty with vague questions — show up with specific
   queries and hypotheses for her to confirm or correct

## Why this matters

The trading pack is used in SLT meetings. Data errors in SLT context erode trust in
AI-generated outputs more broadly. Getting this right is also a proof-of-concept for
the SQL query persistence pattern — applicable to any skill that pulls structured data.

## Related

- [[adam-smith]] — owner of the trading pack skill
- [[kirsty]] — FP&A validation, source of truth for trading numbers
- [[2026-06-10-adam-thomas-bdm-team-ai]] — origin meeting
