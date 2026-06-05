---
title: "2W: Prodtech Demo — Submissions Pipeline, E2E Testing, J Connectivity"
created: 2026-06-03
updated: 2026-06-03
domain: product-ai
type: meeting
tags: [prodtech, submissions, testing, j, connectivity, underwriting, conversion]
---

# 2W: Prodtech Demo

**Date:** 2026-06-03 10:00 AM  
**Full transcript:** [[2026-06-03-2w-prodtech-demo-transcript]]

## Attendees

- [[jordi|Jordi Pallares]] (Engineering lead)
- [[rob|Rob Grice]] (Submission pipeline — presenting)
- [[ivan-boix|Ivan Boix]] (J / connectivity — presenting)
- [[ed|Ed Leon Klinger]] (CEO)
- [[jonny-smith|Jonny Smith]]
- [[alex-smith|Alex Smith]] (e2e testing — presenting; leaving team ~one month from now)
- Anton (flyflock.io — strategic/product stakeholder; no people/ file)
- [[nathan-simkiss|Nathan Simkiss]] (Admiral Group; Chief of Staff; observing)
- Tom Harvey

---

## Presentations

### 1. Submission Data Pipeline (Rob Grice)

**What it does:** Automated extraction of 70–100 fields per submission from CCEs and claims listings. JSON output feeds the data lake for rapid querying. Granola identified ~10,000 historic submissions for backfill.

**Strategic pivot:** Started as underwriting automation (submission → quote). UW feedback revealed too much special logic to automate reliably. Shifted to a **submission intelligence layer** — useful to multiple teams: pricing, BDMs, broker pulse.

**Technical blockers ahead:**
- Data reconciliation when multiple values surface for the same field from different documents
- Expanding beyond CCEs/claims to other document types
- Google Drive vs HubSpot discrepancies — some docs only in Drive, auto-matching in HubSpot not 100% accurate

**Actions:**
- [ ] Rob: Resolve multi-value field reconciliation approach (downstream process, not extraction-phase)
- [ ] Rob: Run historic backfill job (~10,000 submissions)
- [ ] Rob/team: Expand document type coverage beyond CCEs/claims
- [ ] Investigate Google Drive as supplementary source for historic backfill; assess discrepancy scope

### 2. Strategic Discussion — Underwriting Automation (Ed Leon Klinger)

Ed opened a broader question: commercial motor underwriting has historically been too complex to automate. That assumption may no longer hold with LLMs.

**Two improvement paths identified:**
1. Make current decisions **faster/cheaper** (efficiency)
2. Make **better decisions** using enhanced data (effectiveness)

Rob's pivot from automation to data insights was questioned — not as wrong, but as potentially too conservative. Ed's view: experiments to test automation boundary are worth running, not just data structuring.

Parallel drawn to **Lama tree pipeline**: structuring data in high-utility format first unlocked significant downstream value. Submission data quality is prerequisite for effective LLM output.

### 3. Resource Allocation / Conversion Mission (Anton)

Anton raised concern: the team's stated mission is conversion improvement, but the link from submission pipeline to conversion is unclear. He identified three parallel efforts (manual UW process, existing pricing model with DCL CCE discounting, new extraction pipeline) with no coordination mechanism.

**Anton's ask:** A workshop and roadmap for conversion improvement experiments — stack rank by impact, decide what's good enough, resource accordingly. Current experimental approach may not address the immediate commercial challenge.

- [ ] Tom Rogers / Darren: Convene conversion improvement coordination workshop (Anton's explicit request)

### 4. End-to-End Testing Framework ([[alex-smith|Alex Smith]])

**Problem it solves:** Product configs drive the entire insurance lifecycle. A broken config breaks the product — underwriters can't bind, customers can't make MTAs. Existing unit tests don't touch live services; integration failures only appear in production.

**What was built:** Declarative end-to-end test suites that drive deployed configs through the real insurance lifecycle via platform services.

**Structure:**
- `QuoteToBind` suite: create quote → apply changes (field updates, vehicle add/remove) → price confirm → bind
- `StandardMTA` suite: adjustments against a bound policy
- Suites compose — model any real customer journey by stacking blocks
- Shared `liveContext` keeps current quote/risk/policy state available to all assertions
- Reusable helpers: common assertions (200s, price settling) baked into framework

**Current coverage:** Haulage, taxi, courier products.

**Benefits:** Ship with confidence, fewer production incidents, faster product development, less manual QA.

**Next steps:**
- [ ] [[alex-smith|Alex]]: Extend to billing, document generation, mid integration testing
- [ ] [[alex-smith|Alex]]/team: Simulate policy year (MTAs over time) to assert correct bills
- [ ] Team practice: add e2e test coverage as part of bug fix process, not just new features (before Alex leaves)

### 5. J Connectivity Skill (Ivan Boix)

**What it solves:** Customers ask connectivity questions (which vehicles are at risk? why is my rebate not applying?). J previously had no connectivity tools — it was inferring from trips data, which is wrong. Connectivity at Flock is measured by GPS points, not trips.

**Implementation:**
- 4 new API endpoints in Safety API exposing connectivity data from data lake (snapshot + historic, per vehicle + per policy) — built with [[jacob-holland|Jacob Holland]] and [[chris|Chris]]
- 4 MCP tools mirroring the API endpoints
- Connectivity skill embedded into J's context

**Connectivity definitions in skill:**
| Status | Definition |
|--------|-----------|
| Connected | Data received today |
| Recent | Data within last 7 days |
| At risk | 7–14 days since last data |
| Disconnected | >14 days no data |

**Also covers:** 75% threshold for rebate eligibility; Matrix vs non-Matrix device paths; workflow guidance; key rules to prevent J recommending disciplinary action.

**Status:** In pilot with select customers. Also applicable to portal connectivity page if needed — same endpoints.

---

## Cross-cutting themes

- **Coordination gap:** Three teams working on conversion-adjacent problems (manual UW, pricing model, submission pipeline) without a shared roadmap. Anton's frustration is legitimate — needs facilitating, not just more experiments.
- **Data quality first:** Lama tree parallel reinforces: structure the data well, and downstream AI quality follows. Submission pipeline is laying the right substrate.
- **J skills pattern:** Skills load on demand from system context — reduces base prompt size while enabling deep topic coverage. Now 7 skills: claims, connectivity, data accuracy, fatigue, portal navigation, safety scores, trip investigation.

---

## Notes

- Rob did his first Prodtech demo — acknowledged by Jonny.
- Ivan ran over time; agreed to be first presenter next time.
- Nathan Simkiss (Admiral Group) was observing — no active contribution in transcript.
