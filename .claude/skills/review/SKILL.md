---
name: review
description: Generate a weekly review template pre-populated with automated vault data
---

# /review — Weekly Review

Generate a weekly review template, pre-populated with what can be automated.

## When to use

At the end of each week, or when the `/morning` brief flags that a review is due.

## Steps

1. Determine the current ISO week number and year. File will be `reviews/YYYY-WNN.md`.
2. Scan `meetings/` for notes dated within this week.
3. Scan `initiatives/` for active initiatives; extract the latest log entry from each.
4. Scan `decisions/` for any decisions created this week.
5. Count items in `inbox/`.
6. Create the review file with this structure:

```markdown
---
title: "Week NN Review"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: review
tags: []
---

## Three wins

1.
2.
3.

## Domain progress

### Engineering Workflows

### Operational Tooling

### Product AI

### AI Enablement

## Decisions made

- [[decision-file]] — title

## Meetings this week

- [[meeting-file]] — title

## Open loops

## Inbox backlog

N items pending triage.

## Next week focus

-

## Energy and effectiveness

```

7. Auto-populate: domain progress from initiative logs, decisions made, meetings this week, inbox count.
8. Leave blank for human reflection: three wins, next week focus, energy and effectiveness.
9. Report the created file path.
