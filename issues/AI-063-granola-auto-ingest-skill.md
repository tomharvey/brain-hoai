---
title: Build Granola auto-ingestion skill triggered from Google Calendar
created: 2026-05-26
updated: 2026-05-26
type: issue
status: todo
priority: medium
domain: ai-enablement
owner: tom
origin: "[[2026-05-26-matt-lees-ai-catchup]]"
---

# AI-063 — Granola auto-ingestion skill from Google Calendar

## Context

Matt Lees manually copies every Granola transcript into Claude after meetings to extract actions, diarise, and find connections. This is a pattern multiple people are doing manually (Matt, Sophie, others).

Tom said in the meeting: "AI take note — maybe I need a skill for the team to be like, at the end of each Google Calendar event, go see if there's a Granola transcript and consume it and look for these things when you consume it."

## What's needed

A skill / scheduled task pattern that:
1. Detects when a Google Calendar event has ended
2. Checks if a Granola transcript exists for that meeting
3. Auto-ingests the transcript
4. Extracts actions, looks for connections to existing context, surfaces novel insight

Could be implemented as:
- A cron-style scheduled task (check every N minutes for new completed meetings)
- A `/post-meeting` skill users run manually to trigger ingestion

## Notes

The scheduled task approach ("check every hour") starts to feel like proactivity once it pings before you noticed. Matt's use case: chief-of-staff-style AI that processes meetings without being prompted. The skill should be team-usable, not just Tom's vault-specific.

Key insight from Matt: "use the user's memory to work out what's important to the user" — generic transcript skills won't land, but personalised ones will.
