---
title: "Thomas / Matthew 1:1"
created: 2026-06-09
updated: 2026-06-09
domain: product-ai
type: meeting
tags: [matt, posthog, arduino, telemetry, conversion-workshop, pricing]
---

# Thomas / Matthew 1:1

**Date:** 2026-06-09
**Attendees:** [[matt]], Tom

Full transcript: [[2026-06-09-thomas-matthew-1-1-transcript]]

---

## Key themes

### PostHog Arduino hack day

[[matt]] bought a PostHog Arduino device from their open-source hack day project. Spec: TFT screen (280×130), hardware buttons, Wi-Fi/Bluetooth, temperature sensor, 3D printed case. PostHog hack day outputs included Flappy Hog, Pong, Tamagotchi, and a Pomodoro timer. Device has built-in PostHog integration for displaying line graphs and big numbers from your PostHog instance.

Matthew has been extending it with Claude Code — good low-level C++ experimentation using AI assistance. Claude Code was surprisingly capable with microcontroller/Arduino code (has slurped up a lot of hobbyist content).

### Public telemetry endpoint for office display

Sparked by Ed's ask for a mileage counter in the office. Premise: hook the Arduino (or eventually a larger LED matrix screen) to a publicly accessible endpoint showing aggregated, non-sensitive telemetry.

**What's feasible:**
- Total mileage counter (Ed's ask) — likely can be near-real-time
- Trip counts — overnight job so ~1-day delay; hourly-ish refresh is fine
- Fun metrics like "critical speeding events in last hour"
- Not: live location data (identifiable, must stay private)

**Technical approach:**
- AWS role with locked-down permissions specific to the telemetry database
- Or: event bridge subscription for read-only access to specific events
- Webhook from AF notifications could ping the device
- Public endpoint with aggregated summary stats — OK to publish externally too

Tom to check with Jacob Holland on what metrics are available and at what refresh rates. → [[AI-109]]

### Conversion improvement workshop planning

Matthew working through the roadmap with Anton. Anton's key framing: focus on **price-proximate deals** specifically — deals where Flock is already competitively priced but still losing. This avoids conversations drifting into pricing and instead focuses on non-price conversion drivers.

There's sufficient data for this segment. Workshop to analyse lost deals in detail to identify the real barriers: broker relationships with competitors, claims process trust, service level concerns.

**Participants**: Fergus, Matthew, Ollie, Anton, Tom, Adam. [[fergus]] coordinating logistics. → [[AI-088]] (already open)

---

## Actions

- [ ] **Tom**: set up AWS role / public endpoint for aggregated telemetry data; check with Jacob on metric availability and refresh rates → [[AI-109]]
- [ ] **Fergus**: coordinate conversion workshop logistics (already in [[AI-088]])
