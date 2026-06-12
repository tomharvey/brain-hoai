---
title: "Co:work artifact convention — data layer + view layer"
created: 2026-06-12
updated: 2026-06-12
domain: operational-tooling
type: issue
status: todo
priority: high
origin: "[[2026-06-11-fergus-tom-weekly]]"
tags: []
---

Co:work artifacts should follow a two-layer convention:

- **Data layer**: CSV or spreadsheet — the raw structured output, shareable and importable anywhere
- **View layer**: HTML artifact or Looker dashboard — the human-readable presentation

These two should be kept separate and independently shareable. The HTML artifact lives ephemerally in Claude; the CSV persists and can be version-controlled or sent to stakeholders.

## Action

- Document this convention in `reference/shared-brain/cowork-implementation.md`
- Apply it retroactively to existing co:work use cases (BDM brain, trading packs, etc.)
- Ensure Ollie and the BDM team understand the distinction when building new workflows

## Context

Fergus articulated this clearly. It prevents the failure mode of "the analysis lives only in a chat window." The data layer is the durable artifact.
