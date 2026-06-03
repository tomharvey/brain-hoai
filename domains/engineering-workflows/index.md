---
title: Domain — Engineering Workflows
created: 2026-05-08
updated: 2026-06-02
domain: engineering-workflows
type: reference
tags: [domain, strategy, engineering, sdlc, agents]
---

# Engineering Workflows

**What this domain is trying to achieve:** Engineers shift from mechanical coding to architectural thinking. AI generates draft PRs from tickets; humans review and teach. Agents are first-class production services — monitored, costed, deployed to platform standards. The question is not "how do we go faster?" but "what does a software engineer look like in 2027?"

---

## What we currently believe is true

- **The frame is "better, not faster."** 10x better, more robust, more tested, more documented. Speed is a side-effect of quality. Engineers who resist AI adoption often respond better to the quality argument than the velocity argument. Confirmed in Dev AI Practices session (2026-05-18): Tom named it explicitly and no one pushed back. "For the first time in my career, no one's complaining about the team's shipping speed."
- **Javi's pilot is the live experiment.** Linear ticket → draft PR → engineer reviews + teaches. Month-long, scoped to Acquisition AI PoC. It's early but it's running. This is the reference case for the whole domain.
- **Architecture docs are the prerequisite for everything else.** Chris (Head of Architecture) is working on docs and skills to teach Claude the company's coding standards. Without this, AI-generated code doesn't fit the platform. The productionised agent framework, the code review automation — both wait on Chris.
- **Vercel is the go-to TypeScript agent framework.** Decided when Ishmael migrated the safety agent from Strands. Chris approved. This is settled.
- **Jemima + Ishmael's working pattern is the target.** Shifted from PRD→handoff to close back-and-forth co-prompting. Sharing code and DB structure files to refine requirements together. This is what PM↔engineering looks like when both sides use AI fluently.
- **AI code quality is a live problem, not a future one.** Chris flagged in March: AI-generated code is degrading PR standards. Multiple review iterations needed. Engineers are shipping AI code now. PR comment mining into coding standards is the fix.
- **Two fundamentally different modes of AI use — most engineers are in the wrong one.** Mode 1 (current): ask a question, wait for answer, repeat — still mentally in the loop. Mode 2 (target): sit outside the loop, let agent do the spade work, guide and repoint. Fergus named this clearly in Dev AI Practices (2026-05-18). [[stephen-millington|Stephen]]'s Databricks monitoring system (2026-05-19) is a concrete example of Mode 2: instead of coding anomaly detection algorithms, he passes the graph to Claude visually and trusts it to make the call. The gap between these modes is the adoption gap to close.
- **Tech debt cleanup is the right first agent target.** Making older services look like the gold standard (insurance service) is pure execution — no judgment required, high value, never gets done due to time pressure. Chris testing this on customers/broker services. Endorsements process is the first isolated end-to-end workflow pilot. ([[AI-053]])
- **The coding standards approach is now concrete.** GitHub review comments → individual standard files (one file per rule, frontmatter with backlinks to originating comment). Each standard cites its source; the agent code-reviews against the index. Functions as a hyper-linter. ESLint rules are the deterministic layer once standards mature. Chris building the super repo (dev environment harness) to hold these. Rob independently arrived at the same pattern while learning Flock conventions via Claude during the HubSpot ETL work — confirming the need is real and the form is intuitive. ([[2026-05-14-rob-hubspot-pipeline]])
- **The super repo pattern is the cross-repo context solution.** Single parent repo with individual service repos nested inside a `source/` folder. Claude Code runs at top level; GitHub Actions clone both and move the target repo into position. Local and CI behaviour are identical.
- **Token spend anxiety extends to engineering.** Despite unlimited AI budget, Ishmael was on Sonnet not Opus. Jordi's $200 Cursor overage is a rounding error on headcount cost, not a problem. The cultural permission to spend needs active management from Tom and Jordi.

- **The 5-stage activation pathway is being formalised.** Tom is building a structured framework and visualisation of where all teams and people sit. Jordi asked about the criteria (2026-05-26) — activation is about maturity of usage, not token spend. Stage 3–4 is the target for most engineers; Stage 5 for exceptions. Expect a Stage 6 to be needed by end of year. A common pathway to success is confirmed — Admiral Business data point corroborates the same progression across their team of five engineers. → [[2026-05-26-jordi-weekly]]
- **Incident management process is now a live priority.** Fergus raised an uptick in incidents over 4–5 weeks. Jordi can't answer "how many incidents in the last 4 weeks?" without thread-hunting. Lightweight AI-integrated process needed. → [[AI-061]]
- **Engineering AI adoption shows mixed signals: retention team is the bright spot, acquisition team is regressing.** Fergus confirmed (2026-05-14) that the retention team (Jacob included) has genuinely transitioned to "build the least possible" thinking — the right Mode 2 mindset. Harvey joining acquisition may import that mindset, but it could equally get beaten out of him. Engineering usage data shows zeros and declines in some individuals; Fergus attributes this partly to domain/team changes since Tom's departure as Eng lead. "AI June" proposed as a reset: a bounded two-week experiment the whole team engages in. → [[AI-077]] ([[2026-05-14-rob-grice-catchup]])
- **Knowledge hoarding is confirmed across engineering and product.** Multiple people (Javier, Ollie, Mima) are treating their AI context as job-security "special sauce." This is not new engineer behaviour — it's the same pattern as "I'm the only one who knows how this service works." The counter-argument that works: "It just makes you a bottleneck holding the can for the shit work you're bored of." ([[2026-05-19-jordi-weekly]], [[2026-05-19-matthew-price]])
- **Scheduling the slot creates the output.** Evidence from Jordi's team-by-team monitoring review: [[stephen-millington|Stephen]] built the Databricks monitoring system specifically because a slot was scheduled — the deadline was the forcing function. Regular cadence is more important than the agenda. ([[AI-058]], [[2026-05-19-jordi-weekly]])
- **CI/CD and testing are more critical than ever — not less.** Engineers in the AI culture session (2026-06-03) independently confirmed: PRs are less useful, but the pipeline they protect is more important. Non-deterministic agents still fall over against deterministic rails (column constraints, pricing service contracts). The harness around humans-and-AI is the core engineering problem. Coding standards buried in people's heads become the next blocker — PR comment mining into structured standards docs is the fix. ([[2026-06-03-ai]])

## What we're uncertain about

- Whether Javi's pilot will produce evidence that quality improves (not just speed). The "slow month" expectation needs managing with Fergus and the team. Fergus was in the Dev AI Practices session (2026-05-18) and endorsed the direction — the failure mode concern (harness engineering instead of shipping) was acknowledged and accepted as the lesser risk right now.
- Where agent services sit in the platform architecture. Chris/Jordi decision outstanding.
- Whether platform-architecture docs will be completed at the pace the agent framework needs.
- How to bring Rob, Javier, Jacob, and Sami into the SDLC-of-the-future conversation without it feeling like a distraction from OKR delivery. Rob specifically needs a different approach — tends to delegate everything to AI without architecture-first thinking. Targeted support plan needed. ([[AI-055]])
- Whether the AI code review initiative (proposed) can be scoped as a Later candidate without causing confusion about priority.
- **David goes on paternity leave ~2026-05-19.** His skills and context need capturing this week. Alex Smith (team) also leaving around the same time. Super repo creation is now time-sensitive. ([[2026-05-12-david-ai-engineering]])
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
