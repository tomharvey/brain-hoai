---
title: Push pricing team toward deterministic scripts for reporting
id: AI-121
created: 2026-06-17
updated: 2026-06-17
domain: engineering-workflows
type: issue
status: todo
priority: high
assignee: Tom
due: 2026-09-30
origin: "[[2026-06-17-harry-dowrick-ai-hackathon]]"
tags: [pricing, deterministic, reporting, governance]
---

## Description

Pricing team is using Claude for reporting tasks that should be deterministic — rebuilding datasets from scratch every time instead of freezing canonical versions. Wrong data was shown to Admiral (90M GWP figure). Harry raised it but it was shown anyway.

Fix: use Claude to generate LookML once, freeze as a Look, then have skills call frozen Looks with date parameters. Agents for ideation, deterministic scripts for reporting.

This quarter was "make mistakes and get your hands dirty." Next quarter is "why are you doing it like that?" The Admiral incident is the forcing function for buy-in.
