---
title: "Jay AI security / prompt injection audit"
id: AI-022
created: 2026-04-28
updated: 2026-04-28
domain: product-ai
type: issue
status: in-progress
priority: medium
assignee: jordi
origin: "[[2026-04-28-jordi-1-1]]"
tags: [security, jay, audit, prompt-injection]
---

## Description

Third-party security audit of Jay focusing on AI-specific attack vectors (prompt injection, data exposure, etc.). Jordi raised with Fergus who agreed — not a launch blocker, but needed before wider rollout.

## Vendor status

| Vendor | Status | Notes |
|--------|--------|-------|
| Samurai Security | Done | Below expectations — not recommended |
| Pen Test Partners | To contact | Via Jordi's former colleague |
| Thread Spike | To contact | Via Jordi's former colleague |
| Unknown (cold inbound) | Call Thu 2026-05-01 | Tom attending — AI + cybersecurity company |

## Acceptance criteria

- [ ] At least 2 vendors contacted and scoped
- [ ] Vendor selected and engagement started
- [ ] Audit completed with findings report

## Notes

- Ishmael involved in the evaluation process
- Existing quality governance: 111 PromptFoo test cases (red team, security, golden dataset) from [[2026-04-08-eval-testing-regroup]]
- Not a launch blocker — Jay expected to ship to test group this week

## Links

- [[2026-04-28-jordi-1-1]]
- [[ai-governance-framework]]
