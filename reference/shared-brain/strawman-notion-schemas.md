# Strawman: Notion Database Schemas (Sales Shared Brain)

> **Status: STRAWMAN companion to `strawman-sales-ontology.md`.** Property-level detail for
> a working session. Notion-specific: property names, Notion property *types*, select
> options, relation wiring, rollups, and — critically — what the **thin MCP enforces that
> Notion cannot.**

## Legend

- Notion property types used: `Title`, `Text`, `Number`, `Select`, `Status`,
  `Multi-select`, `Date`, `Email`, `URL`, `Relation`, `Rollup`, `Formula`,
  `Created by`, `Last edited by`, `Last edited time`.
- **Req** = required. Notion can't truly require most fields → the **MCP gate** enforces
  these on write.
- **🔒 MCP-only** marks a rule Notion cannot express; the thin MCP enforces it.
- Attribution (`updated-by`, `updated`) is **free** via Notion `Created by` /
  `Last edited by` / `Last edited time` — no custom fields needed.

---

## Layer 1 — Sales graph (own teamspace)

### DB: Accounts
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Domain | Text | | ✓ | **Join key.** 🔒 MCP enforces uniqueness + format |
| Website | URL | | | |
| Industry | Select | | | |
| Employees | Number | | | |
| HQ | Text | | | |
| Segment | Relation | → ICPs | | |
| Stage | Status | researching / target / engaged / qualified / opportunity / customer / disqualified | ✓ | Status type gives kanban for free |
| Engagement-angle | Select | product / consulting / both / partner | | |
| Source | Select | inbound / outbound / referral / event | | |
| Warm-path | Relation | → People | | who can intro us |
| HubSpot-ID | Text | | | set at graduation (Option C) |
| Champion (rollup) | Rollup | via Opportunities → champion status | | see Rollups |

### DB: People
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Email | Email | | ✓ | **Join key.** 🔒 MCP enforces uniqueness |
| Account | Relation | → Accounts | ✓ | works-at |
| Title | Text | | | |
| Role-in-deal | Select | champion / economic-buyer / technical-buyer / influencer / blocker / unknown | | |
| Person-status | Select | active / dormant / departed / do-not-contact | ✓ | drives the headline query |
| LinkedIn | URL | | | |
| Introduced-by | Relation | → People (self) | | referred-by |
| HubSpot-ID | Text | | | |

### DB: Opportunities
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Account | Relation | → Accounts | ✓ | 🔒 exactly one |
| Stage | Status | discovery / demo / proposal / negotiation / won / lost | ✓ | |
| Value | Number | (£) | | |
| Close-date | Date | | | |
| Champion | Relation | → People | | 🔒 WARN if empty |
| Hypotheses | Relation | → Hypotheses | | which bets this deal tests |
| Champion-status | Rollup | Champion → Person-status | | for the headline query |
| Has-active-hyp | Rollup | Hypotheses → Hyp-status (contains "active") | | for the headline query |
| HubSpot-Deal-ID | Text | | | |

### DB: Conversations
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | e.g. `2026-06-10 — Acme — discovery` |
| Date | Date | | ✓ | |
| Account | Relation | → Accounts | ✓ | 🔒 ≥1 |
| People | Relation | → People | ✓ | 🔒 ≥1 attendee |
| Channel | Select | call / meeting / email / dm | ✓ | |
| Hypotheses-tested | Relation | → Hypotheses | | |
| Summary | Text | | | AI summary, verbatim |
| Transcript | Text | | | (or file attachment) |

### DB: Hypotheses
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Hyp-status | Status | active / validated / invalidated / decomposed | ✓ | |
| Segments | Relation | → ICPs | | |
| Engagement-angle | Select | product / consulting / both / partner | | |
| Current-assessment | Text | | | |
| Last-signal | Rollup | Signals → Observed-date (max) | | 🔒 WARN if active & >30d stale |
| Signal-count | Rollup | Signals (count) | | |

### DB: Signals
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | the observation, one line |
| Source | Relation | → Conversations | ✓ | 🔒 must have a source |
| Supports | Relation | → Hypotheses | | 🔒 Supports OR Contradicts non-empty |
| Contradicts | Relation | → Hypotheses | | |
| Account | Relation | → Accounts | | |
| Person | Relation | → People | | who said/showed it |
| Observed-date | Date | | ✓ | |
| Body | Text | | | verbatim, don't sanitise |

### DB: ICPs / Segments
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Definition | Text | | ✓ | |
| Active-hypotheses | Rollup | via Hypotheses.Segments | | |

### DB: Playbooks / Assets
| Property | Type | Options / Target | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | |
| Asset-type | Select | messaging / case-study / objection / sequence | ✓ | |
| Applies-to-segment | Relation | → ICPs | | |
| Applies-to-stage | Multi-select | (Account or Opportunity stages) | | |
| Body | Text | | | |

---

## Relation wiring (two-way names)

Notion relations are bidirectional — name both ends so each DB reads naturally:

| From | Property | → To | Back-property on target |
|---|---|---|---|
| People | Account | Accounts | People |
| Opportunities | Account | Accounts | Opportunities |
| Opportunities | Champion | People | Champion-of |
| Opportunities | Hypotheses | Hypotheses | Opportunities |
| Conversations | Account | Accounts | Conversations |
| Conversations | People | People | Conversations |
| Conversations | Hypotheses-tested | Hypotheses | Tested-in |
| Signals | Source | Conversations | Signals |
| Signals | Supports | Hypotheses | Supporting-signals |
| Signals | Contradicts | Hypotheses | Contradicting-signals |
| People | Introduced-by | People (self) | Introduced |

## Rollups that make the headline query native

The "champion left + hypothesis still open" query is partly answerable **inside Notion**
via rollups + a filtered view:

- `Opportunities.Champion-status` = rollup over `Champion` → `Person-status`
- `Opportunities.Has-active-hyp` = rollup over `Hypotheses` → `Hyp-status`, "contains active"
- **View filter:** `Champion-status = departed` AND `Has-active-hyp = true`

→ Rollups get you this *specific, pre-modelled* query for free. **Ad-hoc / multi-hop /
not-pre-built** queries still need the thin MCP — which is the general argument for it.

## What the thin MCP enforces (Notion can't)

1. **Required fields** (the ✓ column) — Notion can't truly require a property.
2. **Uniqueness** — `Account.Domain`, `Person.Email`. Notion allows dupes.
3. **Cardinality** — "Opportunity → exactly one Account", "Conversation → ≥1 Person".
4. **Cross-field invariants** — "Signal.Supports OR Signal.Contradicts is non-empty".
5. **Referential type-safety** beyond what relations give (e.g. don't let a Signal's
   Person belong to a different Account than the Signal).
6. **Identity / dedupe across HubSpot ↔ Notion** on the join keys.
7. **Vocabulary as data** — read allowed Select values from the meta layer (below), so
   the team evolves vocab without editing code.

---

## Layer 2 — Meta / "the brain's brain" (separate teamspace, excluded from sales lint)

> Answers the question: *where does the knowledge about how the brain is built live?*
> **In-store, but partitioned.** These DBs are excluded from sales-graph queries and from
> the sales lint. The thin MCP **reads its own rules from here** — vocab and invariants as
> data, so non-technical teammates evolve structure by editing rows.
>
> **Graduated formality.** The meta layer is **loose by default** — it's where humans (and
> the self-inspection task) think out loud, so heavy validation would add friction exactly
> where you want fluidity. Specific object types then **tighten to the level they need**:
> a Decision must be a complete MADR before it's `accepted`; an Improvement Suggestion can
> be a one-liner. Formality is per-object, not blanket.
>
> Observability + self-improvement live here too — see
> `strawman-observability-self-improvement.md`. Raw telemetry stays in a cheap event store;
> only the *distilled* Usage Insights + Improvement Suggestions land in Notion.

### DB: Decisions (MADR)
| Property | Type | Options | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | `001 — HubSpot as graduation target` |
| Status | Status | proposed / accepted / superseded | ✓ | |
| Date | Date | | ✓ | |
| Context | Text | | ✓ | the forces at play |
| Decision | Text | | ✓ | what we chose |
| Consequences | Text | | | trade-offs accepted |
| Supersedes | Relation | → Decisions (self) | | |
| Source | Relation | → Build Log | | the raw exploration it came from |
| From-suggestion | Relation | → Improvement Suggestions | | when a usage insight prompted it |

> 🔒 **MADR tightening:** the MCP requires `Context`, `Decision` and `Consequences` to be
> non-empty before `Status` can move to `accepted`. Loose while `proposed`.

### DB: Conventions / Schema-defs (the ontology *as data*)
| Property | Type | Options | Req | Notes |
|---|---|---|---|---|
| Name | Title | | ✓ | object or field name |
| Kind | Select | object / field / edge / vocabulary / lint-rule | ✓ | |
| Applies-to | Text | | | which DB/property |
| Allowed-values | Multi-select | | | for `vocabulary` rows — the MCP reads these |
| Rule | Text | | | for `lint-rule` rows — human-readable invariant |
| Severity | Select | error / warn / flag | | |
| Rationale | Relation | → Decisions | | why it's this way |

### DB: Build Log (raw exploration archive — pointers, not clutter)
| Property | Type | Options | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | `2026-06-02 — shared-brain design chat` |
| Date | Date | | ✓ | |
| Type | Select | conversation / workshop / spike | | |
| Link | URL | | | raw transcript in git / Drive — kept *out* of the live store |
| Distilled-into | Relation | → Decisions | | what we extracted |

**Rule of thumb:** raw conversations live as a *link* in Build Log; their value is
extracted into Decisions and Conventions. The live brain stays signal-dense; the "why"
is queryable; the long transcripts don't pollute search.

---

## Layer 3 — Observability & self-improvement (distilled telemetry)

> Full design in `strawman-observability-self-improvement.md`. Raw interaction events live
> in a cheap append-only event store (**not Notion**); only the distilled output below
> lands here. Loose formality — these are working notes, not gated records.

### DB: Usage Insights
| Property | Type | Options | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | `2026-W24 — "departed champion" query asked 9×` |
| Period | Text | | | the window analysed |
| Insight-type | Select | hot-query / empty-search / frequent-rejection / unused-field / co-access / missing-capability | | matches the self-inspection signals |
| Evidence | Text | | | counts / patterns from the raw log |
| Suggestion | Relation | → Improvement Suggestions | | what it prompted |

### DB: Improvement Suggestions
| Property | Type | Options | Req | Notes |
|---|---|---|---|---|
| Title | Title | | ✓ | `Add "evaluator" to Role-in-deal` |
| Status | Status | new / triaged / accepted / rejected / applied | ✓ | |
| Change-type | Select | add-field / add-vocab-value / loosen-rule / add-relation / deprecate / new-capability | | drives the auto-apply threshold |
| Risk | Select | low / structural | | low may bypass MADR; structural never does |
| Evidence | Relation | → Usage Insights | | why we'd do it |
| Becomes | Relation | → Decisions | | the MADR it's promoted into |

> The **Interaction Log** itself is intentionally *not* a Notion DB — it's the raw event
> store. Schema for one event is in the observability artifact (§1).
