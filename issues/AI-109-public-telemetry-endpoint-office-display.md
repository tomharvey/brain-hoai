---
title: "Public telemetry endpoint for office display"
created: 2026-06-12
updated: 2026-06-12
domain: operational-tooling
type: issue
status: cancelled
priority: low
origin: "[[2026-06-09-thomas-matthew-1-1]]"
tags: []
---

Matthew is building a PostHog-style IoT display (Arduino with TFT screen) that can show aggregated company telemetry. He needs a public endpoint with aggregated, non-identifiable stats — not raw data or anything tied to individual drivers.

## Action

- Coordinate with Fergus (happy to build a public endpoint with aggregated summary data)
- Define which metrics to expose: total mileage (near real-time), trip count (previous day lag), and potentially fun stats like "clean runs in last hour"
- Ensure the endpoint uses AWS IAM with locked-down permissions — read-only access to aggregated data only
- No driver location, no identifiable data — anything we'd be happy to publish externally

## Context

Ed specifically asked for a mileage counter display. Matthew's Arduino project is the vehicle (no pun intended). Hourly refresh is sufficient — Matthew can bridge gaps with animation. Check with Jacob on what's achievable near-real-time vs. day-lag per metric.
