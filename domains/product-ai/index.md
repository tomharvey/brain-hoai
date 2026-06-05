---
title: Domain — Product AI
created: 2026-05-08
updated: 2026-06-04
domain: product-ai
type: reference
tags: [domain, strategy, product, jay, submissions, conversion]
---

# Product AI

**What this domain is trying to achieve:** Shape and ship AI-driven products from the prodtech team. The customer-facing bet. Build the data substrate that enables conversion improvements Flock has never had before. What Web 2.0 did with input fields, agents will do with conversations.

---

## What we currently believe is true

- **Jay is the primary product bet — but the feedback loop is broken.** Jay needs instrumentation before it needs features. Datadog (not PostHog) is where the data lives; Mima doesn't have access by default; thumbs up/down buttons aren't wired up yet. A launch without a feedback loop is a launch that kills momentum. The offsite Station A work (Ishmael + Mima) produced a self-improving loop design — that's the path.
- **The real pricing gap is 30–40%, not 5–10%.** Curtis confirmed from the underwriting floor. Adding more rating factors to a model that UWs override 40%+ of the time won't move conversion. The system is fundamentally constrained elsewhere.
- **Development factor is the highest-value, most tractable bet.** Flock applies ~30% uplift to current-year claims that Curtis believes no competitor applies. If disprovable with structured submission data, that's a direct price lift at no loss-ratio cost. Submission pipeline directly enables this. Milan discovery (Mon 11 May) is the next gate.
- **The submission pipeline is now a substrate, not a feature.** Three conversion bets ride on it: (1) development factor analysis, (2) submission scoring by conversion likelihood, (3) driver-data payload. Antton confirmed pricing sophistication alone won't get there — data-led bets are the right framing. Updated 2026-06-03: Rob's pipeline has pivoted from automation to submission intelligence layer (multiple teams: pricing, BDMs, broker pulse). 10k historic submission backfill in progress. Key open question: data reconciliation for multi-value fields. ([[2026-06-03-2w-prodtech-demo]])
- **Safety agent memory pattern is generalisable.** Ishmael's implementation (Bedrock Agent Core, file-based skills, PromptFoo evals) is the reference implementation. The pattern applies to underwriting and submissions too — corrections make agents better, not just faster.
- **WhatsApp bot validated concept but is paused.** Deployed, tested with 1-2 fleets via Ben. If the proposition validates → WhatsApp becomes a platform service. Not the priority right now.

## What we're uncertain about

- Whether Jay's launch will get enough usage to generate signal. Matt Price's concern: launches to small group, gets 5 chats/week, luster fades. Tonic agency (already paid) running against Jay to roleplay fleet manager scenarios. 8 days since last GTM channel update as of 2026-05-12 — pace is concerning. Tom softening on J; Matt wants quiet GA now to iron out bugs rather than a delayed big launch. **Update 2026-06-04:** Digital engagement → retention correlation now statistically confirmed in Mima's stats pack. Hypothesis: generate enough timely insight per 24-hour period that there's value in coming back once a working day. Users at daily active status → higher policy retention at end of period (causal direction plausible, error bars large). The activation journey for J users mirrors the company AI framework: monthly → weekly → daily active. Moving users up that chain is the measurable goal. Waiting for Liam to return from the World Cup before wider push. Tom reconsidered broader push after Matt 1:1: "engagement is great but requires Ben to talk to them." → [[2026-06-02-matt-price-1-1]]
- **Haulage safety is a late-stage year-end risk.** If not addressed soon, Flock exits the year without a haulage safety proposition — more directly tied to retention than J. Immediate opportunity: 16% of submissions contain telematics data, TSB in 10%. Apply existing submission analysis before building new tools. ([[2026-05-12-matt-price-1-1]])
- Whether the development factor is testable with data Milan already has. Discovery call is the gate.
- Whether the conversion bets framing will break the Anton/Darren deadlock. Ollie is caught between conflicting SLT direction. Matt Price's view: show up with data, change the conversation. Anton raised explicitly at 2026-06-03 Prodtech demo: no workshop, no roadmap, no prioritised experiment list exists. Three parallel efforts (manual UW, existing pricing model, new extraction pipeline) are uncoordinated. → [[AI-088]]
- What the insight layer looks like as a first use case. Cloud MCP deployment needed first; no narrow anchor yet.
- Whether CC extraction tool handover is complete enough. Abs left; tool status unclear.

---

## Active initiatives

| Initiative | Status | Owner | Notes |
|---|---|---|---|
| [[safety-agent-memory]] | active | Ishmael | Production-ready; Datadog observability issues pending |
| [[cc-extraction-handover]] | active | Abs → ? | Abs departed; successor unclear |
| [[insight-layer]] | proposed | TBD | No narrow first use case anchored; depends on AI-010 |
| [[whatsapp-driver-reporting]] | paused | Ollie | Concept validated; not current priority |

## Key decisions

- Submissions framed as data substrate for conversion bets, not operational efficiency play (Apr 2026)
- Jay instrumentation is the priority before feature additions

## Key people

- [[matt]] — Matt Price; product lead; second brain advocate; conversion bets framing
- [[ollie-crowe]] — conversion bets author; Antton relationship; submissions narrative
- [[ishmael]] — Jay engineer; safety agent architect; Station A anchor
- [[mima]] — Jay product; `/create-test-cases` skill; co-prompting with Ishmael
- [[javier]] — submissions/quoting; Acquisition AI PoC
- Milan Chavda — [[milan-chavda]]; pricing intelligence; Bet 1 gate
