# Strawman: Stack & Storage Decision Register

> **Status: STRAWMAN.** A deliberate re-check of every tooling/storage assumption before
> the workshop. Each row is **HOLD** (still right), **REFINE** (right direction, detail
> changed), or **REVISIT** (genuinely reconsider). Honesty over tidiness.

## A useful mental model: three planes

The stack has stopped being "a few tools" and become three planes. Naming them keeps the
sprawl legible:

| Plane | Holds | Tools |
|---|---|---|
| **Source-of-truth + UX** | the actual data, and where humans touch it | Notion, HubSpot |
| **Control plane** | the single API to the brain: federation, write-gate, capture | **Thin MCP** |
| **Derived-data + compute** | everything rebuildable: telemetry, search index | AWS (CloudWatch, S3/Athena, ?OpenSearch/Bedrock) |

Rule that falls out of this: **source-of-truth never lives in the derived plane.** Lose
all of AWS and you lose dashboards and search speed, not a single fact.

## The register

| # | Decision | Status | Note |
|---|---|---|---|
| 1 | Notion = knowledge/graph SoT + non-technical UX | **HOLD** | Conflict-free, already owned, native UI. Still the right home for the soft layer. |
| 2 | HubSpot = transactional SoT (A + C hybrid) | **HOLD** | Graduation threshold still open. AWS/telemetry changes nothing here. |
| 3 | Thin MCP = single front door + write-gate + federation + capture | **HOLD** | The keystone — but now also a single point of failure (see Complexity). Keep it thin & stateless. |
| 4 | **Search**: Notion-native + MCP for structural | **REVISIT** | Notion search can't see HubSpot. "Day-one quality" + cross-store + AWS commitment now push toward a **derived index on AWS**. See below. |
| 5 | Telemetry store | **REFINE** | Was a vague "SQLite/cloud table" → now **CloudWatch Logs** (+ S3/Athena for deep mining). Reuses existing AWS/Athena muscle. |
| 6 | Self-improvement loop | **REFINE** | Concept holds; **sequencing** changes — capture day 1, inspect/suggest phase 2. No fuel until there's usage. |
| 7 | Ontology-as-data (vocab/rules in Notion, MCP reads them) | **REFINE** | Deferring the *mechanism*, not the schema. See #7 in detail. |
| 8 | Git/markdown for the team brain | **HOLD** | Dropped (non-technical team). Optional read-only export mirror only. |
| 9 | Identity / join keys (domain, email) across Notion↔HubSpot | **HOLD — top risk** | Still the most likely thing to sink the dual-store model. Unresolved. |

## #4 in detail — the search reconsideration

This is the one I'd genuinely reopen. Earlier we leaned "Notion-native search is enough day
one." Two facts have since hardened:

- **Search must span both stores** — "everything about Acme" = HubSpot deals/activity **+**
  Notion conversations/signals. Notion search only sees Notion.
- **You're committing to AWS anyway** — so the cost of a derived index just dropped.

Two ways to give the MCP a unified search:

- **(a) Federate** — MCP fans out to Notion search + HubSpot search and merges. No index,
  simple, but weak ranking and no real semantic recall. Fine for "find about X."
- **(b) Derived index on AWS** — OpenSearch + Bedrock embeddings over both stores, rebuilt
  from source. Hybrid lexical+semantic+graph, genuinely good day one. More infra, but it
  lands in the plane you're already standing up.

**Lean (b)** given the day-one-quality bar and the structural queries — but ship **(a)** as
the v1 so search exists before the index does. Decision for the workshop.

## #7 in detail — ontology *content* vs. ontology-*as-data*

"Ontology" hides two things; only the second is deferred:

- **(A) The schema** — objects, fields, edges, vocab, invariants. **Day one, non-negotiable.**
  You can't migrate a mess into "no schema"; the migration *target* is the ontology and the
  lint gate *is* the ontology enforced.
- **(B) Ontology-as-data** — rules stored as editable Notion rows the MCP reads at runtime,
  so non-technical people can evolve them. **This** is what's deferred — for runtime
  coupling/bootstrap reasons and because there's no non-technical audience editing rules yet,
  not mainly "to gather data."

**Migration is the schema's first and best test.** The existing Notion mess is the test set:
forcing real historical records into the proposed schema proves **representational fit**
(can it *hold* the data) — a different, earlier gate than the **query/workflow fit** that
live usage proves later. So treat migration as an explicit ontology-hardening phase with a
feedback loop into the design. You go live with a schema already battle-tested — a *better*
day-one ontology, not a deferred one.

Counterintuitively, migration is also an argument to keep **(B)** deferred *through* that
window: the schema churns fastest during migration, and data-driven indirection is friction
exactly when you're iterating. Resolution: make the rule representation **data-shaped from
day one** (a declarative file, same shape as the future meta rows) but keep the **authoring
surface as a config file Tom owns**. Graduating to (B) then becomes a data-move + flip of the
read source, not a rewrite.

**Graduate (B) when:** schema survived migration **+** ~N weeks live without structural
change **+** a non-Tom person needs to edit a rule. (Likely late Phase 2, not Phase 3.)

## Complexity check — is this too much for 4 users + 1 maintainer?

The honest risk: Notion + HubSpot + AWS (CloudWatch/S3/Athena/?OpenSearch) + a bespoke MCP
is a lot of surface for a team where **Tom is the only technical maintainer**. Two guards:

1. **Each store earns its place and isn't substitutable** — Notion (human UX), HubSpot
   (existing CRM/forecasting), AWS (telemetry/compute/search). The MCP is the only bespoke
   code, and durability lives in the managed stores, not in it.
2. **Phasing, so complexity arrives only as it's justified:**

   - **Phase 1 — the brain works.** Notion (clean DBs) + thin MCP (gated writes + federated
     search **a**) + HubSpot read-through. Migrate the Notion mess. **Switch telemetry
     capture on (CloudWatch) from day one** — it's cheap and you'll want the data later.
   - **Phase 2 — the brain searches well.** Add the AWS derived index (**b**) if federation
     isn't enough.
   - **Phase 3 — the brain improves itself.** Self-inspection task + Improvement Suggestions
     once there's real usage to mine, and ontology-as-data once the rules have stabilised.

   Capture is the only Phase-3 thing pulled forward to Phase 1, because you can't
   retroactively observe usage you didn't log.

## Net verdict

Still happy — with three honest amendments: **CloudWatch settles the telemetry store**,
**search (#4) deserves a real reopen** toward an AWS derived index, and **the self-improvement
loop is Phase 3, not day one** (but its *capture* is Phase 1). The identity/join problem (#9)
remains the highest unresolved risk and should get real airtime in the workshop.
