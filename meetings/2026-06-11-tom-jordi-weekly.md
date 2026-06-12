---
title: "Tom <> Jordi: Weekly 1:1"
created: 2026-06-11
updated: 2026-06-11
domain: engineering-workflows
type: meeting
tags: [jordi, engineering, finance-ai, claude-native-api, bdm-brain, stripe, scheduling]
---

# Tom <> Jordi: Weekly 1:1

**Date:** 2026-06-11
**Attendees:** [[jordi]], Tom

Full transcript: [[2026-06-11-tom-jordi-weekly-transcript]]

---

## Key themes

### London visit — July 8

Tom coming to London July 8, skipping Cardiff (passport tight; Cardiff low-value: prod tech day + town hall leaves little connection time). Prod tech day poll narrowly favours July 22 (Tom on holiday) — agreed to proceed without Tom or push to end of September.

### Freelance search

High volume of candidates via Spanish communities and Targo's network. Quality mixed — one candidate caught using AI live during interview to answer questions. Aiming to have someone confirmed by end of next week (Jordi). Two recruiters now also helping with senior engineering lead (started yesterday).

### MCP tool — Queenie's laptop

Kirsty tried remote installation with [[queency-gonsalves]] (Queenie) — too painful. Rob is out. Jordi to install the Python MCP tool (connects to Moss) at 1:30pm before all-hands. Python is installed; MCP JSON has a stale entry to remove but has auth env vars. Anneliese may also need it.

### Finance AI — data quality and architecture

Finance project ongoing: workshops to map workflows and identify tooling. Core challenge: no clear single source of truth. NetSuite targeted for deprecation for new policies, but migration timeline is long. Each policy is highly customised with few written rules, making AI context-feeding hard.

Jordi's view: finance is too critical for non-deterministic output. New billing system is the right place to design AI-native from day one — build with AI requirements baked in (clean data model, MCP-accessible, deterministic where needed).

Stripe announced AI agent in private beta at their conference: can create catalog items, issue invoices, give pricing/conversion insights via prompt. Per-resolution pricing model (incentive-aligned). Has own MCP. Relevant precedent.

### Claude-native API endpoint — key pattern shift

Chris is building an API endpoint specifically for Claude to wrap a finance workflow for Matt. **No frontend — Claude is the consumer.** Tom sees this as a meaningful pattern shift worth broadcasting: skip building screens, expose thin endpoints for agents to solve specific tasks. Matt (and others) stay in the loop to validate.

This pattern should extend: finance, underwriting assistance, other operational workflows. The endpoint is read-only now but Chris is open to write. → [[AI-098]]

### BDM co-pilot launch + Flock Launches channel

BDM brain launching Monday. Jordi suggested sharing in Flock Launches channel when BDMs start using it. Tom agreed — same for Matt's endpoint when shipped.

### Engineering AI 1:1s complete

Tom completed 1:1s with all engineers on AI usage:
- **Chris + Sam + Alex**: most technically confident, most resistant to fully delegating. Alex: interrogates the plan heavily upfront. Sam: intense line-by-line output review, treats Claude as a senior faster engineer. Chris: delegates junior tasks, moving toward peer.
- **Steve, Jacob, Alex group**: more anxiety, grief over losing craft.
- **Rob** (newest): no prior attachment, least friction.

Reshuffling groups and running the session again in a few weeks.

---

## Actions

- [x] Jordi to install Python MCP tool on Queenie's laptop at 1:30 (Jun 11, same day)
- [ ] **Jordi**: confirm freelance candidate by end of next week
- [ ] **Tom**: book July 8 London flights
- [ ] **Tom**: launch BDM co-pilot Monday; share in Flock Launches
- [ ] **Tom**: share Matt's Claude-native endpoint in Flock Launches when shipped → [[AI-098]]
- [ ] **Tom + Chris**: explore more Claude-native API endpoints for finance/underwriting tasks → [[AI-098]]
