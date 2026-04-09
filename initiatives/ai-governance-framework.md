---
title: AI governance framework
created: 2026-03-27
updated: 2026-03-27
domain: ai-enablement
type: initiative
status: active
origin: proposed
owner: tom
tags: [governance, risk, compliance, guidelines]
---

## Summary

The company is adopting AI fast but has no guardrails, guidelines, or risk framework. Sam's analogy: "riding a power bike at 200 mph as an amateur." Need company-wide AI guidelines covering risk awareness, prevention, and response protocols.

## Goal

A published AI governance framework that every department understands. Covers: acceptable use, risk scenarios, mitigation strategies, incident response.

## Current state

- No formal governance framework exists yet, but **practical governance is emerging through engineering**:
  - Mima's eval testing group: 111 test cases (red team/security, golden dataset, PromptFoo plugins) — see [[2026-04-08-eval-testing-regroup]]
  - Paul asked to review test suite for compliance gaps (ASAP)
  - `/create-test-cases` skill: stakeholders describe tests conversationally → skill generates PromptFoo config. Non-technical people contributing to technical governance.
  - Datadog observability being connected to agent framework (Ismael, demo with Datadog architect Fri/Mon)
  - S3 storage for all agent outputs under investigation — security, compliance, and analytics
  - Jordi investigating third-party security audit for AI features before launch
- Prompting workshops are beginner-level only
- Sam has PhD research in this area and wants to contribute
- Paul (Head of Compliance) identified as key collaborator
- Risk scenarios identified: data deletion, prompt manipulation, data exposure

## Dependencies

- Sam's availability and research
- Paul's buy-in
- Cross-functional workshop scheduling

## Risks

- Deprioritised indefinitely in favour of shipping
- Regulatory exposure if an incident occurs before framework exists

## Next actions

- [ ] Park formal framework for later in Q2 — but practical governance is no longer waiting (eval suite, observability, security audit)
- [ ] Sam to share AiCore industry report in #ai Slack
- [ ] Schedule business continuity workshop when timing is right (Sam + Paul + cross-functional)
- [ ] Document nightmare scenarios from discovery conversations
- [ ] Follow up on Paul's compliance review of eval test suite — bridge into broader governance requirements
- [ ] Connect Sam's governance research to Mima's practical eval work — avoid parallel tracks

## Log

### 2026-03-27

- Sam raised in 1:1 (Mar 25)
- Tom decision: important but not urgent, defer to later Q2

### 2026-04-08

- Eval testing regroup (Mima-led, Tom absent). Practical governance materialising through engineering:
  - 111 test cases covering security, red team, compliance in PromptFoo
  - Decision: test against production data, on-demand before major changes
  - Auth/user-isolation testing scoped for Playwright (user A can't access customer B's data)
  - Paul asked to review for compliance gaps
  - Datadog observability pipeline being connected (Ismael). S3 agent output storage under investigation.
  - Jordi raised third-party security audit question — checking with Chris/Fergus
  - See [[2026-04-08-eval-testing-regroup]]
