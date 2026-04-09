---
title: Eval testing regroup
created: 2026-04-08
updated: 2026-04-09
domain: engineering-workflows
type: meeting
tags: [evals, testing, promptfoo, redteam, security, datadog, observability]
---

## Attendees

- [[mima|Jemima Pitceathly]] (led)
- [[jordi|Jordi Pallares Roset]]
- Ismael Jebril
- Javi
- Tom Harvey (unable to attend)

## Summary

Full test suite now in Notion and GitHub for review. 111 test cases across three areas on the `redteam-evals` branch of `platform-ai`.

### Test coverage

| Area | Count | Scope |
|---|---|---|
| Golden dataset | 53 | Fleet queries, charts, claims, date handling, memory, data formatting, deterministic validation |
| Red team / security | 49 | Policy isolation (P0), prompt injection, data manipulation, claims boundaries, write guardrails, score definitions |
| PromptFoo built-in plugins | 9 | PII, GDPR, hijacking |

### Artefacts

- **Notion**: test plan for compliance review
- **GitHub**: configs + skill on `redteam-evals` branch (`agents/` directory in `platform-ai`)
- **New skill**: `/create-test-cases` — stakeholders describe what they need to test via conversation, skill formats output into PromptFoo config

## Decisions

- **Non-technical staff don't need PromptFoo locally** — techies run it centrally
- **Testing against production data**, not synthetic — full CI/CD automation is not the goal; on-demand runs before major changes are the target cadence
- **Auth/user-isolation testing** (user A can't query customer B's data) is in scope but belongs in **Playwright**, not PromptFoo
- **Test users in production** will need to be created and associated with real customer policies for E2E testing

## Testing approach

- PromptFoo as the framework — strong, reusable suite run before significant agent changes
- **Workflow**: compliance/domain stakeholders have a conversation via the `/create-test-cases` skill → skill formats output into PromptFoo config → techies ingest and run
- Key coverage areas: safety score calculations, high-risk speeding definitions, data retrieval accuracy per vehicle/policy, cross-customer data isolation
- Acknowledged: not all tests will pass cleanly given real production data — **consistency of the suite matters more than 100% pass rate**

## Observability & logging

- Ismael connecting agent framework to **Datadog** — demo call with Datadog architect scheduled (this Friday or Monday)
- Datadog to surface per-tool traces, outputs, latency metrics (first token vs full response — exact capabilities TBC at demo)
- Investigating storing all agent outputs in **S3** (organised by user or policy) for security, compliance, and analytics
- Longer-term: agents analysing stored conversations to extract higher-level insights

## Security & external scanning

- Jordi raised whether new AI features should go through a pen test or security audit before launch
- Flock may have a contracted third-party scanner for web properties — ownership unclear; Chris to be asked
- Anthropic's Project Glass Wing noted as relevant: Claude used to find vulnerabilities (including 20-year-old bugs) in partnership with AWS, Cisco — potentially worth exploring for Flock's codebase

## Actions

- [ ] [[mima|Mima]]: draft initial test cases (using Granola notes from red team kickoff + scoring/calc definitions) — share to group channel by EOD or next day
- [ ] [[mima|Mima]]: turn test case creation process into a skill ✅ (done — `/create-test-cases`)
- [ ] [[mima|Mima]]: have conversation with [[paul|Paul]] to capture compliance test case requirements
- [ ] Ismael: invite Mima to Datadog LLM observability demo call (Fri or Mon)
- [ ] Ismael: investigate automating ingestion of test cases into PromptFoo config
- [ ] [[mima|Mima]] + Ismael: scope user journey / E2E testing (Playwright, auth/isolation, test user setup)
- [ ] Check with Chris whether third-party security scanning is still active — if so, what testing they recommend for new AI features
- [ ] [[jordi|Jordi]]: investigate third-party security audit (check with Chris and Fergus)
- [ ] [[paul|Paul O'Neill]]: review Notion doc for compliance gaps / missing scenarios (ASAP)
- [ ] Javi + Ismael: review test plan, decide if more cases needed, try `/create-test-cases` skill

## Notes

- Tom was unable to attend. Summary via Mima's Slack post + Granola meeting summary (2026-04-09).
- This is significant progress on the evals work that Sam was redirected toward on Mar 30 — but Mima's group has been driving it independently. Reinforces Mima's "we're already doing this" position.
- Paul's compliance review here is directly relevant to the [[ai-governance-framework]] initiative.
- The `/create-test-cases` skill workflow (stakeholder conversation → PromptFoo config) is a strong example of the "skills as scaling mechanism" thesis from [[skills-distribution]].
- Datadog + S3 observability work is the first concrete step toward production-grade agent monitoring.
