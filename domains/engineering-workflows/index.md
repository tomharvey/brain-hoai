---
title: Domain — Engineering Workflows
created: 2026-05-08
updated: 2026-05-08
domain: engineering-workflows
type: reference
tags: [domain, strategy, engineering, sdlc, agents]
---

# Engineering Workflows

**What this domain is trying to achieve:** Engineers shift from mechanical coding to architectural thinking. AI generates draft PRs from tickets; humans review and teach. Agents are first-class production services — monitored, costed, deployed to platform standards. The question is not "how do we go faster?" but "what does a software engineer look like in 2027?"

---

## What we currently believe is true

- **The frame is "better, not faster."** 10x better, more robust, more tested, more documented. Speed is a side-effect of quality. Engineers who resist AI adoption often respond better to the quality argument than the velocity argument.
- **Javi's pilot is the live experiment.** Linear ticket → draft PR → engineer reviews + teaches. Month-long, scoped to Acquisition AI PoC. It's early but it's running. This is the reference case for the whole domain.
- **Architecture docs are the prerequisite for everything else.** Chris (Head of Architecture) is working on docs and skills to teach Claude the company's coding standards. Without this, AI-generated code doesn't fit the platform. The productionised agent framework, the code review automation — both wait on Chris.
- **Vercel is the go-to TypeScript agent framework.** Decided when Ishmael migrated the safety agent from Strands. Chris approved. This is settled.
- **Jemima + Ishmael's working pattern is the target.** Shifted from PRD→handoff to close back-and-forth co-prompting. Sharing code and DB structure files to refine requirements together. This is what PM↔engineering looks like when both sides use AI fluently.
- **AI code quality is a live problem, not a future one.** Chris flagged in March: AI-generated code is degrading PR standards. Multiple review iterations needed. Engineers are shipping AI code now. PR comment mining into coding standards is the fix.
- **The coding standards approach is now concrete.** GitHub review comments → individual standard files (one file per rule, frontmatter with backlinks to originating comment). Each standard cites its source; the agent code-reviews against the index. Functions as a hyper-linter. ESLint rules are the deterministic layer once standards mature. Chris building the super repo (dev environment harness) to hold these.
- **The super repo pattern is the cross-repo context solution.** Single parent repo with individual service repos nested inside a `source/` folder. Claude Code runs at top level; GitHub Actions clone both and move the target repo into position. Local and CI behaviour are identical.
- **Token spend anxiety extends to engineering.** Despite unlimited AI budget, Ishmael was on Sonnet not Opus. Jordi's $200 Cursor overage is a rounding error on headcount cost, not a problem. The cultural permission to spend needs active management from Tom and Jordi.

## What we're uncertain about

- Whether Javi's pilot will produce evidence that quality improves (not just speed). The "slow month" expectation needs managing with Fergus and the team.
- Where agent services sit in the platform architecture. Chris/Jordi decision outstanding.
- Whether platform-architecture docs will be completed at the pace the agent framework needs.
- How to bring Rob, Javier, Jacob, and Sami into the SDLC-of-the-future conversation without it feeling like a distraction from OKR delivery.
- Whether the AI code review initiative (proposed) can be scoped as a Later candidate without causing confusion about priority.
- Where the coding standards hyper-linter ends and principled architecture begins — Chris sees these as distinct; the hyper-linter is the first step. Whether the two artifacts (human-readable principles doc + AI-readable backlinks) stay separate or merge over time.
- How to bring the wider engineering team into the coding standards repo without it becoming AI slop at scale — when to open it up vs curate it longer.

---

## Active initiatives

| Initiative | Status | Owner | Notes |
|---|---|---|---|
| [[ai-native-engineering]] | active | Javi / Tom | Month-long pilot live on Acquisition AI squad |
| [[agent-framework]] | active | Tom | Blocked on architecture docs + infra decisions |
| [[platform-architecture-docs]] | active | Chris | Prerequisite for everything else in this domain |
| [[engine-room-triage-automation]] | active | — | Status unclear — needs check |
| [[ai-code-review]] | proposed | — | Later candidate; depends on architecture docs maturity |

## Key decisions

- Vercel is the TypeScript agent framework (Chris approved, Apr 2026)
- Local-first harness is the right starting point — "if I'm off, it's off"

## Key people

- [[chris]] — Head of Architecture; owns platform-architecture-docs; coding standards
- [[jordi]] — Engineering lead; owns engineering culture and team AI adoption
- [[javier]] — Pilot engineer; building the harness; month of not-coding
- [[ishmael]] — Most AI-native engineer; safety agent reference implementation
- [[ollie-crowe]] — Product anchor for Station B; ticket quality is half the harness quality
