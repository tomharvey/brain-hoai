---
title: Submissions automation
created: 2026-03-27
updated: 2026-06-03
domain: operational-tooling
type: initiative
status: active
origin: self-started
owner: unassigned
tags: [submissions, coordination, underwriting]
---

## Summary

Three independent groups are working on automating the insurance submission process. Needs consolidation into a single coordinated effort.

## Goal

A unified approach to submission processing that reduces manual effort while maintaining accuracy. Human-in-the-loop rather than full automation — submissions are too varied for 100% accuracy.

## Current state

- Abs built CC extraction tool (leaving in a few weeks — handover needed)
- David doing separate submissions work
- Chris flagged at least three groups tackling this independently
- No shared approach or architecture
- Abs and Chris both suggested chat interface with human-in-the-loop as the right direction
- **Fergus built a working pipeline**: 9,000 submissions processed, S3 architecture, Lambda orchestration
- **Jacob**: wiring results into Iceberg table for querying
- **Javier**: building document classification skills — potential convergence point
- Two paths emerging: submission analytics vs quote-centric. Intermediate JSON format could bridge both.

## Dependencies

- Abs handover before departure
- Process documentation for how submissions actually work today
- Coordination decision: who leads this after Abs leaves?

## Risks

- Abs leaving without adequate handover
- Continued fragmentation if not consolidated
- Building on top of existing complexity instead of rethinking (vehicle resolution pattern)

## Next actions

- [ ] Complete discovery round before intervening
- [ ] Identify single owner post-Abs
- [ ] Map the three current efforts and their overlap
- [ ] Document the actual submission process end-to-end

## Log

### 2026-03-27

- Identified as fragmented across 3+ groups from Chris AI and Abs AI conversations
- Decision: address holistically after discovery round, not piecemeal

### 2026-04-20

- **Fergus's pipeline is operational**: ~9,000 submissions processed at ~50p each (~£40 total)
- Architecture: three S3 buckets (raw docs → OCR/JSON intermediary → final partitioned by date)
- Pipeline: documents from HubSpot tickets → Bedrock OCR → JSON extraction → Lambda combines all ticket docs → AI fills submission schema → JSON results
- Only 6/9,000 submissions too long for single context window
- Jacob wiring results into Iceberg table for querying — 5 minutes from query to results
- **Data source tension**: HubSpot tickets (initial email only, includes disqualified) vs Google Drive (manually curated, more complete, messy, reused across years). Google Drive is source of truth for complete submissions.
- **Schema**: Fergus let Claude define it from submissions (unbiased) rather than from existing quote requirements
- **Convergence with Javier's work**: Javier building document classification skills (TRS, CC detection) with assembler pattern. Could point to Fergus's result docs. Two paths: submission analytics (Fergus) vs quote-centric (Javier). Not mutually exclusive — intermediate "submission JSON" could feed both.
- **Future questions**: automated trigger point, Google Drive dependency, production deployment. No automated triggers yet.
- Tom's note: "Why didn't Javier or Rob do what Fergus has done? Javier has been close."
- Rob (week 1 acquisition squad) and wider tech-team attended alignment session
- See [[2026-04-20-submission-processing-pipeline]]

### 2026-04-27

- **Narrative reframe via Ollie Crowe** (relaying Antton + Curtis conversations): pipeline is no longer framed as "extract → pricing model → conversion" but as the **substrate enabling multiple conversion bets**.
- Antton: pricing sophistication lever has low confidence. Wants five ranked conversion bets grounded in data.
- Curtis (underwriting floor): real pricing gap is 30-40%, UWs override model by 40%+, adding rating factors won't move conversion.
- **Development factor is the hero bet**: Flock applies ~30% uplift to current-year claims ("development factor") that Curtis believes no other insurer applies. Legacy from the Andi book. Every submission ingested brings 2+ years of claims history — structuring that across carriers enables a market-wide benchmark. This is a data problem the pipeline directly enables.
- **Submission scoring (Bet 2)**: once pipeline is ingesting + #underwriting-losses channel is structured, score submissions by conversion likelihood. Convergence point with Adam's pipelining ask.
- Milan's driver-data payload still next but no longer leading the story.
- Sprint plan unchanged: Ingestion + Extraction + Presentation, 30 April.
- See [[ollie-conversion-bets-2026-04-27]]

### 2026-04-28

- **Matt Price 1:1**: Matt and Tom aligned on the data substrate framing. The real value isn't faster quotes or reducing UW assistant time — it's building a structured data layer from unstructured submission data that enables market analysis capabilities Flock has never had. Same work, same output, different justification.
- **Token spend culture problem**: Fergus runs submissions on *all* submissions. Others are afraid to spend tokens. Ishmael was on Sonnet instead of Opus despite unlimited AI budget. Ollie doing "some" submissions — should be doing all of them. Stop optimising for cost, optimise for getting people to use it.
- **Instrumentation gap**: no PostHog equivalent for submissions work. Unclear where Ollie's feedback data lives. Need the "bonnet open" feedback loop that made driver claims and referrals successful. Tom to follow up with Ollie.
- **Matt's steer to Ollie**: log the opportunities in Linear as slices of the same underlying piece of work, then start pulling data. "Build the data substrate first" message hasn't reached Ollie yet.
- See [[2026-04-28-matt-price-1-1]], [[2026-04-28-jordi-1-1]]
