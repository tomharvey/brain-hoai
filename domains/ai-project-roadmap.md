---
title: AI project roadmap
created: 2026-04-22
updated: 2026-04-22
domain: ai-enablement
type: reference
status: active
tags: [roadmap, projects, now-next-later]
---

# AI Project Roadmap

1-month horizon. Stages represent commitment, not time. Projects always serve a Now initiative.

> Follows the ProdTech Now/Next/Later framework — see [[ProdTech Roadmaps Q2 2026.pdf]].
> Parent view: [[ai-initiative-roadmap]].

---

## NOW — Resourced, cracking on

| Project | Serves | Owner | Size | Status |
|---|---|---|---|---|
| Offsite AI session (AI-016) | AI capability uplift | Tom | S | Today. v4 locked, anchors briefed. |
| Complete discovery — underwriting (AI-003) | AI capability uplift | Tom | S | Darren/Billy remain. Nearly done. |
| Javier HubSpot→Claude→Flock PoC | AI-native engineering | Javier | M | Due ~Apr 24. Active build. |
| DataDog observability fix (AI-017) | AI-native engineering | Ishmael | M | Due Apr 25. Three blocking issues, chasing DD support. |
| CC extraction handover | Operational AI automation | Abs → TBD | M | Abs departing. Knowledge transfer before last day or it's orphaned. |
| Enterprise deal negotiation | Claude standardisation | Tom | S | Rate limits already a constraint. Matt Lees hit cap. |

---

## NEXT — Ready to go, measurable outcome defined

| Project | Serves | Owner | Size | What's needed to move to Now |
|---|---|---|---|---|
| Looker MCP cloud deploy (AI-010) | Operational AI automation | Tom | L | Fargate+ALB+OAuth architected. Needs build time. Unblocks renewals (AI-007) and multi-user access. |
| Access & permissions audit (AI-014, AI-015) | AI capability uplift | Tom | S | Matt Dipre blocked on Looker+HubSpot. Sophie on HubSpot AI. Admin tasks, not technical problems. |
| Submissions scoping (AI-009) | Operational AI automation | Tom | M | Three groups working independently. Need single owner post-Abs, scoped milestones. |
| Skills repo governance (AI-002) | Claude standardisation | Tom | M | Repo exists, ungoverned. Contribution guidelines + testing standards before distribution. |
| Shared context architecture (AI-018) | Claude standardisation | Tom | L | How teams share skills/knowledge without git conflicts or excluding non-devs. Options identified, no decision. |
| Platform architecture docs | AI-native engineering | Chris | M | Types done, architecture in progress. Foundation for AI code review. Needs Chris's headspace. |

---

## LATER — Enough to have the conversation

| Project | Serves | Why it matters |
|---|---|---|
| Renewals Looker→HubSpot (AI-007) | Operational AI automation | Eliminate PMT + Renewals Tracker spreadsheets. Blocked on AI-010. |
| Driver referral automation (AI-011) | Operational AI automation | 2.5–5 hrs/day savings. Process understood, owner pair identified (Fred + Shreya). |
| AI code review in CI | AI-native engineering | Claude in GitHub Actions, non-blocking PR comments. Depends on arch docs maturity. |
| Engine Room triage validation | AI-native engineering | Jordi's MVP exists (~2hrs invested). Does it produce useful triage? |
| Slack channel analysis agent (AI-020) | AI governance framework | Surface duplicated conversations and topic overlap across channels. |
| Ashby ATS evaluation (AI-019) | AI capability uplift | Same price as Lever, AI-native features. Low effort if someone picks it up. |

---

## Definition of Ready (from ProdTech framework)

- **Now**: Resourcing booked in so we can crack on and ship.
- **Next**: A measurable outcome tied to a strategic goal. Good understanding of what to build, plus a t-shirt size from light scoping.
- **Later**: A descriptive title and enough articulation of why to have the conversation. Expected to sit here for months.
