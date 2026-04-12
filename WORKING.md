# Working

## Current task

Board roadmap polish (AI-001) is the priority. Discovery round nearly complete — Sophie Dodds remaining. Week 16 starts Monday.

## Context

Week 3 as Head of AI. Discovery round nearly complete — 20+ calls across 3 weeks. Vault now has:
- 24 meeting notes + transcripts
- 25+ people files
- 14 initiatives tracked across 4 domains
- 12 issues (AI-001 to AI-012, AI-012 removed)
- 1 decision record (004 — Looker MCP server selection)
- Calendar skill and Granola ingestion workflows established
- gws CLI authenticated for calendar management
- Vector database added for fuzzy search across vault

**Key deadline: AI board roadmap for Pioneer board meeting 2026-04-20** (AI-001). 8 days out.

## Week 15 (W15) — completed

### Fri 10 Apr — 9 meetings ingested
- [x] AI Breakfast — Matt demo'd sales outreach pipeline (10 agents, 89% email accuracy, 549 accounts). Kirsty demo'd AI driver tree dashboard. Ollie postponed scheduled briefing demo.
- [x] Oli — acquisition strategy, team boundary with Jaren, 10x growth challenge, telematics as moat
- [x] Jemima — AI adoption segmentation, personal OS comparison, style guides promised
- [x] Paul O'Neill — compliance measurement gap thesis (can't deploy agents if data isn't captured), cultural metrics, delegated authority
- [x] AI Workshops steering group — confidence before automation, 3-layer approach (company workshop + dept workshops + 1:1 pairing), Oli to lead Co-Work/MCP workshop, potential Apr 23 town hall slot
- [x] Alex Dyball — pragmatic ChatGPT user, meeting self-scoring pattern, renewal nudge blocked by data quality
- [x] Jonny Smith — connectivity ops, GPS fix data quality issue in MCP, Zapier+Looker automation self-built, HubSpot contact staleness
- [x] Javier — acquisition AI vision, "surface everywhere" strategy, Flock API MCP exists (Chris built it), 2-week PoC target for HubSpot→Claude→Flock quoting
- [x] Liam Thomson — one-person marketing team, Artlist for video, Lovable for decks, Flock ranks first for "connected fleet insurance" in AI search

### Earlier in W15
- [x] Matt Lees Enterprise Engine 002 (Mon 7 Apr)
- [x] Fred AI discovery (Tue 8 Apr)
- [x] Kirsty AI discovery (Wed 9 Apr)
- [x] Looker MCP server research + Decision 004

## Cross-cutting themes from discovery round

1. **HubSpot data quality** — the single most repeated blocker. Contact staleness (Jonny, Alex), name mismatches (Jonny solved via deal IDs), stale deal owners, missing loss reasons. Affects Matt's pipeline, Jonny's automations, and any future agent work.
2. **Confidence > automation** — the workshops group agreed: building confidence is the April priority, not automating the right things. Kirsty's cool dashboard has value because of what it did to Kirsty, not just the insights.
3. **Telematics MCP needs domain education** — GPS fix thresholds, data quality indicators. Critical before customer-facing AI.
4. **Flock API as MCP** — Chris already built a policy management MCP. Javier's 2-week PoC could be a breakthrough for the "surface everywhere" vision.
5. **Insight loops** — dashboards that say the same thing every week become disengaging. Need insight-as-data feeding into future analysis.
6. **Paul's measurement gap** — can't measure compliance if data isn't captured. Underwriting referrals, policy readership, meeting attendance — none systematically measured.

## Monday 13 Apr

| CEST | UK | Who | Topic |
|------|----|-----|-------|
| 12:30-12:45 | 11:30-11:45 | Sophie Dodds | Discovery (distribution/broker management) |

## Open issues

| Issue | Priority | Status | Notes |
|-------|----------|--------|-------|
| **AI-001** Board roadmap | High | todo | **Due Apr 20. 8 days.** Draft in `ai-roadmap-draft.md` |
| **AI-010** Looker MCP cloud | High | todo | Notion page received. Next: test `use_client_oauth`, deploy |
| **AI-007** Renewals Looker→HubSpot | Medium | todo | Blocked on AI-010. Confirmed viable. |
| **AI-008** Shreya NOC follow-up | Medium | todo | **Overdue.** Ping her async. |
| **AI-009** Submissions scoping | Medium | todo | Not started |
| **AI-003** Discovery round | High | in-progress | Sophie Dodds remaining, then complete |
| **AI-011** Driver referral automation | Medium | backlog | Map HubSpot template, prototype |
| **AI-002** Skills repo ownership | Medium | todo | Not progressed |

## Waiting on

- [ ] Kirsty: HTML dashboard file (promised on call)
- [ ] Kirsty: ICP analysis results (testing Claude vs Adam's assumptions)
- [ ] Shreya: NOC template test results (AI-008)
- [ ] Matt Lees: HubSpot data structure alignment with Emily + Adam
- [ ] Jemima: Three communication style guides
- [ ] Rakhee: Apr 23 town hall slot confirmation for AI workshop
- [ ] Javier: PoC progress on HubSpot→Claude→Flock API quoting (~by Apr 24)

## Next session priorities

- [ ] Sophie Dodds discovery (Mon 13 Apr)
- [ ] Board roadmap polish — incorporate discovery round findings
- [ ] Ping Shreya re NOC test
- [ ] Ask Chris about policy management MCP server status
- [ ] Run `/manifest` and commit
