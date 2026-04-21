---
title: Submissions automation
created: 2026-03-27
updated: 2026-04-20
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
