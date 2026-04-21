---
title: "Submission processing pipeline — alignment session"
created: 2026-04-20
updated: 2026-04-20
domain: operational-tooling
type: meeting
tags: [submissions, pipeline, architecture, acquisition]
---

# Submission processing pipeline — alignment session

## Attendees

- [[fergus|Fergus Doyle]]
- [[rob|Rob Grice]]
- Tom Harvey
- tech-team

## Key themes

### Fergus's pipeline is operational

~9,000 submissions processed at ~50p each (~£40 total). Three S3 buckets: raw docs → OCR/JSON intermediary → final partitioned output. Lambda orchestration. Only 6 out of 9,000 submissions too long for single context window.

### Data source tension

HubSpot tickets (initial email attachments only, includes disqualified deals) vs Google Drive (manually curated, more complete but messy, includes additional broker correspondence). Google Drive is the "source of truth" for complete submissions but has reuse/year overlap issues.

### Schema approach

Fergus let Claude define the schema from the submissions themselves (unbiased view) rather than starting from existing quote requirements. [[jacob-holland|Jacob]] wiring results into Iceberg table for querying.

### Convergence with Javier's work

Javier building document classification skills (TRS, CC detection) with an assembler pattern. Could point to Fergus's result documents instead of re-doing extraction. Two paths: submission analytics (Fergus) vs quote-centric (Javier/acquisition team). Not mutually exclusive — intermediate "submission JSON" format could feed both.

### Future architecture questions

Automated trigger point (when pipeline fires), Google Drive dependency, production deployment. No automated triggers yet — manual batch processing.

### Cost is not the constraint

Tom pushed: work out how to do it first, optimize later. Fergus agreed but cautioned against running full 9,000 reprocessing repeatedly. Multiple processing levels discussed (20p basic → 50p-£1 enhanced for subset).

## Tom's private notes

"Rewriting stuff from scratch in an AI developer world is easy. Why is that a benefit? Why didn't Javier or Rob do what Fergus has done? Javier has been close — why not this approach. Is Javier missing something or has Fergus missed something?"

## Actions

- [ ] **[[jacob-holland|Jacob]]**: Continue wiring Iceberg table for submission querying
- [ ] **[[fergus|Fergus]]**: Share architecture and code repo with wider team (rename from "spike")
- [ ] **Javier/[[fergus|Fergus]]**: Explore integration between document classification skills and pipeline results
- [ ] **Tom**: Facilitate alignment between Fergus's analytics path and Javier's quote-centric path

## Transcript

Full transcript: [[2026-04-20-submission-processing-pipeline-transcript]]
