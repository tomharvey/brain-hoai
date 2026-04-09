---
title: Skills distribution and standardisation
created: 2026-03-27
updated: 2026-03-27
domain: ai-enablement
type: initiative
status: active
origin: self-started
owner: tom
tags: [skills, claude, distribution, tooling]
---

## Summary

A central skills directory exists but lacks ownership, governance, and visibility. Skills are being built across teams but good prompts disappear into private conversations. Tom taking ownership.

## Goal

A well-governed, discoverable catalogue of company skills that any team member — dev or non-dev — can find, use, and contribute to.

## Current state

- Central repo exists but ungoverned
- Skills in development: Flock deck builder (Mima), engine room review, renewals (Job/Anna), broker deck (Kirsty), platform frontend patterns (Sam), NPM library skills (Chris), Linear ticket creator
- Came up in 3 of 7 meetings this week
- Skills AI session (Mar 27) established shared vocabulary for dev and non-dev audiences
- Proposed: GitHub repo with automatic updates to Claude plugins
- **Jordi flagged (2026-03-30)**: Matt asked about sharing a skill company-wide — Jordi's response: "who tested this?" Need clear standards for:
  - Public vs private skills
  - Testing/review requirements before distribution
  - Who approves company-wide sharing

## Dependencies

- Tom getting access to and ownership of the existing repo
- Contribution guidelines
- Claude enterprise deal (for company-wide distribution)

## Risks

- Skills built without content validation lead to broken implementations
- Individual "superpowers" that don't scale
- Non-engineering teams left behind if distribution is too dev-centric

## Next actions

- [ ] Get access to existing skills repo
- [ ] Inventory what exists
- [ ] Define contribution and review process
- [ ] Communicate to engineering and non-engineering teams

## Log

### 2026-03-27

- Raised in engineering drop-in, Chris AI, and skills AI session
- Tom committed to taking ownership
- Tracked as AI-002

### 2026-03-30

- Jordi raised deployment standards in 1:1 — Matt asked to share a skill without testing
- Need public/private governance and review process before company-wide distribution

### 2026-04-02

- Matt Lees created a Claude skill for renewal documents (Flock Value Statement) — wanted to install at org level
- Jordi pushed back: org-level skills need validation and maintenance process. Share directly with users first, get feedback.
- Matt Lees accepted, keeping local. Good test case for whatever governance process we define.

### 2026-04-08

- Eval testing regroup (Mima-led, Tom absent): 111 test cases now in Notion + GitHub (`redteam-evals` branch). Golden dataset (53), red team/security (49), PromptFoo plugins (9). New `/create-test-cases` skill on the branch. Paul reviewing for compliance gaps. Jordi investigating third-party security audit. See [[2026-04-08-eval-testing-regroup]].
