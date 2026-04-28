---
title: AI governance framework
created: 2026-03-27
updated: 2026-04-22
domain: ai-enablement
type: initiative
status: active
origin: proposed
owner: tom
tags: [governance, risk, compliance, guidelines, sprawl-prevention]
---

## Summary

The company is adopting AI fast but has no guardrails, guidelines, or risk framework. Sam's analogy: "riding a power bike at 200 mph as an amateur." Need company-wide AI guidelines covering risk awareness, prevention, and response protocols — but also a coordination mechanism that prevents AI sprawl before it starts.

## Goal

A published AI governance framework that every department understands. Three pillars:

1. **Risk & compliance** (Sam + Paul) — acceptable use, risk scenarios, mitigation strategies, incident response
2. **Quality governance** (Mima + Tom) — eval suites, output quality standards, observability, security audits
3. **Sprawl prevention** (Tom) — coordination mechanisms that replace the natural friction AI removed. Registry, visibility, "check before you build"

## Current state

### Pillar 1 — Risk & compliance
- No formal framework yet — parked for later Q2
- Sam has PhD research in this area and wants to contribute
- Paul (Head of Compliance) identified as key collaborator
- Risk scenarios identified: data deletion, prompt manipulation, data exposure
- Prompting workshops are beginner-level only

### Pillar 2 — Quality governance (practical, already emerging)
- Mima's eval testing group: 111 test cases (red team/security, golden dataset, PromptFoo plugins) — see [[2026-04-08-eval-testing-regroup]]
- Paul asked to review test suite for compliance gaps (ASAP)
- `/create-test-cases` skill: stakeholders describe tests conversationally → skill generates PromptFoo config. Non-technical people contributing to technical governance.
- Datadog observability being connected to agent framework (Ismael, demo with Datadog architect Fri/Mon)
- S3 storage for all agent outputs under investigation — security, compliance, and analytics
- Jordi investigating third-party security audit for AI features before launch

### Pillar 3 — Sprawl prevention (new, critical)

**The Amazon lesson:** When building was expensive, the cost of creation *was* the coordination mechanism. Teams looked around first because building took weeks. Redundant tools died of natural causes because maintenance cost real budget. AI removed that immune system. Building is now free; knowing what already exists is not. The gap between those two costs is where sprawl lives.

Flock is small enough to build the immune system *now*, before it needs retrofitting. Early symptoms are already visible:

**Duplication:**
- **Submission extraction** — Fergus built a batch pipeline processing 9,000 submissions into structured JSON (analytics angle). Javier independently building document classification skills with an assembler pattern (quote-centric angle). Same source documents, different outputs, neither aware of the other's approach until the [[2026-04-20-submission-processing-pipeline|alignment session on 20 Apr]]. The intermediate "submission JSON" could feed both, but only because someone forced the conversation.
- **Skills in isolation** — Mima's `/create-test-cases` skill has been communicated many times but still only has 3 users. Skills are being built per-person without visibility of what exists. [[skills-distribution]] is the coordination response, but the pattern extends beyond skills to tools and automations.

**Coordination gaps:**
- **Personal operating systems** — Tom, Jemima, Harvey, Fergus, Jacob all building personal OSes independently ([[2026-04-21-codifying-context-retention-team]]). Geran's discovery question nails it: "how do personal OSes talk to each other?" Without a shared context protocol, each OS becomes a silo.
- **Slack channel overlap** — teams duplicating conversations across channels without visibility. AI-020 (Slack channel analysis agent) was created to find this overlap — which is itself an instance of the pattern (building a tool to find the duplication, exactly like Amazon's Clarity).

**Derived artifact risk (early stage):**
- Fergus's pipeline stores extracted submission JSON in S3. Javier's classification skills could produce overlapping structured output stored elsewhere. Two extraction pipelines from the same source documents = two sets of derived artifacts, governed separately, neither aware the other exists. If a source submission is corrected or retracted, which outputs update?

**The immune system we need:**
- **Registry:** a living catalog of AI tools, agents, skills, and automations across the company. Not a spreadsheet — something that's part of the workflow, not bolted on after.
- **"Check before you build" culture:** lightweight, not bureaucratic. Before starting an AI tool/skill/automation, check the registry. If something adjacent exists, talk to the owner first. This is a cultural norm, not an approval process.
- **Derived artifact awareness:** when an AI produces output (summaries, extractions, knowledge bases), where does it live and who governs it? Revoking access to a source document doesn't revoke the AI-generated summary three systems away.
- **Coordination through the capability uplift:** the [[ai-capability-uplift]] programme is the accelerator. This pillar is the steering. They must be coupled — every enablement session should include "here's what already exists" alongside "here's how to build."

Reference: [Amazon AI sprawl post by Peter Girnus](https://x.com/gothburz/status/2046575505160225010) — raw source in `inbox/`.

## Dependencies

- Sam's availability and research
- Paul's buy-in
- Cross-functional workshop scheduling

## Risks

- Deprioritised indefinitely in favour of shipping
- Regulatory exposure if an incident occurs before framework exists
- **Sprawl compounds silently.** By the time it's visible, the cost of untangling is 10x the cost of preventing. The Amazon post describes 247 tools in one division — that's what "too late" looks like. Flock's window to build the immune system is now, while the company is small and the Head of AI role has visibility across all initiatives.

## Next actions

### Pillar 1 — Risk & compliance
- [ ] Park formal framework for later in Q2 — but practical governance is no longer waiting (eval suite, observability, security audit)
- [ ] Sam to share AiCore industry report in #ai Slack
- [ ] Schedule business continuity workshop when timing is right (Sam + Paul + cross-functional)
- [ ] Document nightmare scenarios from discovery conversations

### Pillar 2 — Quality governance
- [ ] Follow up on Paul's compliance review of eval test suite — bridge into broader governance requirements
- [ ] Connect Sam's governance research to Mima's practical eval work — avoid parallel tracks

### Pillar 3 — Sprawl prevention
- [ ] Design an AI tools/skills/agents registry — lightweight, living, part of the workflow not separate from it
- [ ] Couple sprawl prevention to capability uplift: every enablement session includes "here's what already exists"
- [ ] Define derived artifact policy: when AI produces output, where does it live, who owns it, what happens when the source changes?
- [ ] Resolve Fergus/Javier submission extraction overlap as the first real test case
- [ ] Review [[skills-distribution]] as the coordination mechanism for skills specifically — extend the pattern to tools and automations

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

### 2026-04-22

- Added Pillar 3 (sprawl prevention) after reading Amazon AI Tools Governance post (Peter Girnus). Core insight: when building is free, the natural coordination mechanism (cost of creation) disappears. Governance must be designed in, not retrofitted.
- Early Flock symptoms identified: parallel submission extraction work (Fergus/Javier), siloed personal OS builds, skills built in isolation.
- Decision: build the immune system now while the company is small enough. Registry, "check before you build" culture, derived artifact awareness.
- Linked to [[ai-capability-uplift]] — the accelerator and the steering must be coupled.

### 2026-04-28

- **Pillar 2 — Security audit in motion**: Jordi engaging vendors for AI-specific security/prompt injection audit of Jay. Samurai Security call went poorly. Pen Test Partners and Thread Spike to be contacted this week. Tom has a cold inbound call Thursday with an AI + cybersecurity company. Not a launch blocker. → AI-022
- **Pillar 2 — Observability**: Mima and Ishmael both need Datadog API access for Jay feedback loop. Jay data is in Datadog not PostHog. Without access, no one can do the "bonnet open" daily usage review that made driver claims successful. → AI-021
- See [[2026-04-28-jordi-1-1]]
