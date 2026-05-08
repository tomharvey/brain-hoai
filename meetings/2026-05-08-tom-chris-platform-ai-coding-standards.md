---
title: Tom <> Chris — Platform AI + Coding Standards
created: 2026-05-08
updated: 2026-05-08
domain: engineering-workflows
type: meeting
tags: [chris, coding-standards, super-repo, github-comments, cicd, david-zamora, ai-native-engineering]
---

## Attendees

- Tom Harvey
- [[chris|Chris Fothergill]]
- [[david|David Zamora]] (expected but didn't join)

## Key themes

### Context architecture hierarchy

Chris has been designing an information hierarchy for platform context:

1. **Principles** — overall context (probably not a skill file — just context)
2. **Patterns / architectures** — context + skills (e.g. how to write a command, a query)
3. **Libraries** — mostly skills
4. **Services** — a bit of context + specific skills

Problem with the previous approach: one monolithic skill with everything bundled in. No structure, no reuse across services.

David Zamora has already written up documentation against this structure. Chris is reviewing it. When agreed, they'll start filling it in properly.

### GitHub comment mining → organic coding standards

Tom's proposed approach — feed from the other direction:

- Take GitHub review comments → write a coding standard file around each comment
- **Backlink the standard to the originating comment** — auditability and citation
- Before writing a new standard: check existing index. If already present → reinforce. If close but needs update → update + note why. If conflicting → surface the conflict to the user
- Each standard = a single file with frontmatter (which comment created it, comments that validate/conflict/updated it, which repos it applies to / doesn't apply to)
- Index file lets the code review agent scan standards before reviewing code
- Works as a **hyper-linter** (structural/linting patterns) more than a principled architecture tool — that distinction is important

Chris: this will drive more review comments in GitHub naturally, and engineers will start thinking "put it in GitHub" rather than just Slacking something.

Tom: sourcing citations reduces hallucination — agent can't fabricate standards it can't cite.

### ESLint as the deterministic layer

Once AI-generated standards reach the point of being producible as ESLint rules, switch to running ESLint instead of running an agent. Agent writes the ESLint rule / custom rule; ESLint enforces it deterministically.

"There's only so loud you can shout" — once AI stops adhering to a prompt, wrap it in something programmatic.

Chris's first concrete use case: "you can't import this file from this random folder" — a front-end import structure rule that he's already writing comments about repeatedly.

### Super repo / dev environment harness

Tom's existing setup: a single repo with individual service repos nested inside a `source/` folder. Claude Code runs at the top level, can reach into any child repo.

- Top-level repo holds: context files, skills, cross-repo documentation
- Each child repo is an independent git repo (greyed out in status, not tracked by parent)
- Enables: making changes to platform-frontend and services simultaneously, with cross-repo awareness

**CI/CD challenge:** pipeline only runs on the individual repo, not the parent. 
**Solution agreed:** clone both the target repo and the super repo in the GitHub Action; move the target repo into the expected nested position; run the review from the top level. Same structure locally and in CI.

Chris to create the super repo on GitHub. Incremental approach: build up context, validate locally first before pushing as a CI action.

### Incremental approach — critical

- Don't dump data and call it done. No way to measure whether it's helping or hurting.
- Code review bot is probably a month away. First: build the context, run locally, verify it makes a difference.
- If pushed as a CI action too soon and it spews garbage, "we'll just lose people"

### Installments sidebar

Brief discussion at start: installments is not a calculation problem, it's a capital/risk problem. Brokers and carriers want money upfront; no one is currently taking on the risk for deferred payments. Geran could write a Streamlit app to manage the manual process, but that's not the real fix.

## Actions

- [ ] Chris: create the super repo on GitHub — add initial structure (principles, patterns, libraries, services)
- [ ] Chris + Tom: check in every couple of days on progress — add a few context files, iterate
- [ ] Tom: share example of coding standard with frontmatter + backlinks structure for Chris to use as template
- [ ] David Zamora: finalise documentation write-up for Chris to review and agree structure

## Notes

The GitHub comment → coding standard workflow is a genuine behaviour change: engineers naturally create GitHub comments when reviewing anyway. Wiring those into a standards file gives the work compound value — it doesn't just improve this PR, it improves every future review. The key unlock is backlinks; without them, it's just more AI-generated text.

Full transcript: [[2026-05-08-tom-chris-platform-ai-coding-standards-transcript]]
