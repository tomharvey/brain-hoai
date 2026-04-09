---
title: Jemima Pitceathly
created: 2026-03-27
updated: 2026-03-27
type: person
role: Product Manager
team: Product
tags: [product, skills, ai-champion]
---

## Role

Product Manager

## Team

Product (reports to [[matt]])

## Relationship

Reports to Matt. AI skills champion.

## Working style notes

- Built the Flock deck builder skill — brand-consistent presentations
- Has markdown-based workflow in VS Code (similar to Tom)
- Maintains personal notes on stakeholders and how to communicate with them
- Proactive AI adopter — referenced positively in multiple conversations

## 1:1 Log

### 2026-04-08 — Eval testing regroup (Tom absent)

- Led the eval testing regroup. 111 test cases now in Notion + GitHub (`redteam-evals` branch)
- Golden dataset (53), red team/security (49), PromptFoo plugins (9)
- Built `/create-test-cases` skill: stakeholders describe tests via conversation → skill formats into PromptFoo config. Strong example of skills-as-scaling-mechanism.
- Key decisions: test against prod data (not synthetic), on-demand runs not CI/CD, auth testing in Playwright not PromptFoo
- Driving E2E testing discussion (Playwright, auth/isolation) with Ismael
- Connecting with Paul for compliance test case requirements
- Ismael connecting agent framework to Datadog (demo with Datadog architect Fri/Mon), investigating S3 storage for all agent outputs
- Jordi raised third-party security audit question — checking with Chris/Fergus
- See [[2026-04-08-eval-testing-regroup]]

### 2026-04-08 — Value Statement automation workshop (with Matt Lees, Tom absent)

- Discussed automating the Flock Value Statement / TCO document for new business
- Preferred approach: Claude + HubSpot MCP replacing Lovable-to-PDF pipeline
- Goal: document appears automatically in submission folder without Matt's involvement (~80% automated)
- Assessing best path forward and locking in output format before building
- See [[2026-04-08-value-statement-automation]]
