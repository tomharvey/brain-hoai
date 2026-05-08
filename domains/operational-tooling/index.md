---
title: Domain — Operational Tooling
created: 2026-05-08
updated: 2026-05-08
domain: operational-tooling
type: reference
tags: [domain, strategy, operations, automation, ops]
---

# Operational Tooling

**What this domain is trying to achieve:** Eliminate high-volume manual workflows that cost hours/day across ops, underwriting, and finance. Strategic goal: document and improve operations company-wide — not just local optimisation. Every department designs processes with AI from the start, not retrofitted.

---

## What we currently believe is true

- **Emily's team is already there.** They are the reference model: daily AI usage, Zapier automation, process-first thinking. The goal for this domain is to replicate that model across other operational functions — underwriting assistance, finance, renewals.
- **Shreya's NOC skill works end-to-end.** This is the flagship ops automation. Blocked on one thing: Emily needs to confirm whether address data is in Looker (unblocks full automation). Until that's confirmed, the skill handles most but not all cases.
- **The submissions pipeline is a data substrate, not an efficiency play.** Reframed by Ollie/Antton/Curtis: the real value is building structured data from unstructured submissions that enables three conversion bets — development factor analysis, submission scoring, driver-data payload. "10% faster quoting" undersells this. "Capabilities Flock has never had before" is the right frame.
- **Kirsty's Looker→Claude connection is the Finance AI story.** Self-started, already producing business decisions from AI-generated insights. Cloud MCP deployment (AI-010) will expand this to the wider Finance team and unlock the renewals automation.
- **Process documentation is a prerequisite for reliable automation.** You can't automate what you haven't mapped. "Load-bearing Google Sheets" risk is real — automating on top of fragile undocumented processes embeds the fragility.
- **The renewals process is mapped but blocked.** Four manual steps that should be one. Blocked on Looker MCP cloud deployment (AI-010). Once that's deployed, this can move.
- **Installments has three distinct layers that need separate plans.** (1) Today's manual process — just needs managing reliably. (2) A more palatable interim version that codifies existing business logic out of spreadsheets. (3) A 3–5 year first-class loan management platform. Conflating these causes confusion. Fergus's view: if installments blocks a deal, swallow the manual cost; question is scalability, not correctness.
- **Finance AI adoption is a forcing-function problem, not a capability problem.** Jade's team (Kirsty, Christian) are capable but not making time. The intervention is a structured session that creates immediate wins, not more demos or self-directed learning.

## What we're uncertain about

- Whether the development factor is testable with the data Milan already has. This is Bet 1 from Ollie's conversion framing — the biggest prize, but requires Milan discovery first (Mon 11 May).
- Who owns the submissions pipeline long-term. Currently Fergus built it, Jacob is wiring it into Iceberg, Javier has overlapping classification skills. No single owner assigned.
- When Looker MCP cloud deployment (AI-010) will land — overdue since Apr 18, blocking renewals and expanding Finance AI access.
- How far the operational tooling model extends. Finance (Jade discovery Mon 11 May) and other functions still being assessed.
- Whether process documentation can happen systematically (PostHog/DOM analysis via Geran) or remains manual case-by-case.
- **Geran data quality risk:** Geran is pulling from Snowflake, the data lake, and platform DB without a clear understanding of which sources are clean. Telemetry quality has stabilised, so errors are now detectable in isolation — but Geran's cross-source assumptions may mix reliable and unreliable data silently (Fergus: "hospital pass").
- What the FinOps automation programme looks like in Q3 — Jade's paper has a laundry list; the question is what to address in Q3 vs Q4, and what gets traded off if finance work is pulled ahead.

---

## Active initiatives

| Initiative | Status | Owner | Notes |
|---|---|---|---|
| [[underwriting-assistance-ai]] | active | Emily | NOC end-to-end working; renewals blocked on AI-010 |
| [[submissions-automation]] | active | unassigned | Pipeline live (Fergus); reframed as conversion bet substrate |
| [[posthog-workflow-analysis]] | proposed | Geran | Process documentation shortcut via DOM analysis |
| [[process-documentation]] | proposed | — | Prerequisite for reliable automation at scale |

## Key decisions

- **001**: Holistic approach to submissions — address after discovery, not piecemeal intervention
- Submissions pipeline reframed as data substrate for conversion bets (Apr 2026, Ollie/Antton/Curtis)
- Looker MCP server: googleapis/mcp-toolbox selected over Ultrathink (**004**)

## Key people

- [[emily]] — ops lead; owns underwriting assistance; reference model
- [[shreya-chowta]] — most advanced ops AI user; built NOC automation
- [[kirsty]] — Finance power user; Looker→Claude MCP
- [[ollie-crowe]] — conversion bets framing; submissions narrative owner
- [[fergus]] — built the submissions pipeline; 9,000 submissions processed
- [[jade-mounir]] — Finance VP; AI discovery follow-up Mon 11 May
