---
title: "Ollie Crowe: conversion bet reframing (Antton + Curtis)"
created: 2026-04-27
updated: 2026-04-27
type: reference
domain: product-ai
tags: [pricing, conversion, submissions, underwriting, distribution]
---

## Context

Slack update from [[ollie-crowe|Ollie Crowe]] on 2026-04-27, relaying two conversations that shift how the product-ai sprint work is framed. Sprint plan unchanged (Ingestion + Extraction + Presentation, 30 April deadline from 22 Apr lock-in), but the narrative around it is widening.

## Distribution sync with Antton

Antton challenged the pitch that document extraction + driver-data capture -> better pricing sophistication -> more conversion.

- **"Pricing sophistication won't get us there"** — low confidence in that lever
- Document automation is a quick efficiency win but not a conversion driver
- What excites him: Adam's pipelining tool, joining Admiral + Flock pipelines, broker-facing proposition work
- **Ask**: come back with five ranked conversion bets grounded in data, not opinion

## 1:1 with Curtis

Curtis independently confirmed Antton's diagnosis from the underwriting floor:

- **UW process is already good** — login, data entry, turnaround times. Automation is nice-to-have, not a bottleneck.
- **Real pricing gap vs competitors is 30-40%, not 5-10%.** Can't close that with better extracted data.
- **Underwriters routinely override the pricing model by 40%+** — model is a guide, not an answer. More rating factors on a model people override doesn't move conversion.
- **Development factor is the biggest fixable lever**: Flock applies ~30% uplift to current-year claims figures ("development factor") that Curtis believes no other insurer in the market applies. Legacy assumption from the Andi book. If provable/disprovable with data, it's a direct price lift at no loss-ratio cost.
- **Broker commission structures (18-27% at big composites)** are how large brokers decide placement. Structural lever, owned by Adam.
- **Unconnected-fleet proposition** (no telematics requirement) could unlock conversion but is complex.

## Narrative shift

| Before | After |
|--------|-------|
| Extract better data -> Milan's pricing models use it -> conversion goes up | We're building the substrate that enables several specific conversion bets |

## The three bets the pipeline now underwrites

### Bet 1 — Development factor question

Every submission ingested brings 2+ years of claims history. Structuring that across carriers enables a market-wide benchmark to test whether Flock's methodology is above market norm. This is a data problem the pipeline directly enables, and likely a bigger pricing lift than anything on the exposure-led side.

### Bet 2 — Submission scoring layer

Once the pipeline is ingesting and #underwriting-losses channel is structured, incoming submissions can be scored by likelihood to convert. This is where Adam's pipelining ask and the MVP converge.

### Bet 3 — Milan's driver-data payload

Still next on the roadmap but no longer leading the story.

## Ollie's parallel work

- Spiking a small version of Adam's pipelining tool next week (self-run, Claude-Cowork, not eng time)
- Pulling #underwriting-losses channel into a structured dataset (same approach)
- Scoping the development-factor data work with Milan standalone

## Links

- [[submissions-automation]] — pipeline is the substrate for all three bets
- [[insight-layer]] — submission scoring (Bet 2) is a specific instantiation
- [[ollie-crowe]] — author, driving the conversion narrative
- [[2026-04-16-tom-rogers-underwriting-ai]] — Tom Rogers' actuarial template already tracks development patterns
- [[tco-value-statement-process]] — Matt Lees' TCO process references claims modelling
