# Sales Shared Brain — Strawman Design Set

> **Status: STRAWMAN, for a team workshop.** Everything here is built to be argued with,
> not adopted as-is. Each doc flags its own open **Decisions**; nothing is final until the
> workshop closes them.

## What this is

A design exploration for a **shared, Claude-native "brain"** for a 4-person, non-technical
sales team — somewhere they read from and contribute to through Claude, with powerful
search and a write path that keeps the knowledge clean. It reuses the architecture proven
in the Rosenfeld vault (typed objects + typed edges + a gated, lint-validated write path)
on a **Notion + HubSpot + thin-MCP + AWS** stack.

## The one-paragraph architecture

Three planes. **Source-of-truth + UX**: Notion (knowledge/graph) and HubSpot (deals). A
**control plane**: a thin MCP that is the single front door — it federates queries, gates
every write through lint, and captures telemetry. A **derived-data + compute plane** on
AWS: CloudWatch telemetry, and (later) a search index. Source-of-truth never lives in the
derived plane.

## Reading order

1. **`strawman-sales-ontology.md`** — start here. The conceptual model: first-class
   objects, typed edges, invariants, the HubSpot strategy, migration, and the
   self-improving loop. The "what and why."
2. **`strawman-notion-schemas.md`** — the build sheet. Property-level Notion schemas for
   every database (sales layer + meta layer), relation wiring, rollups, and exactly what
   the thin MCP enforces that Notion can't.
3. **`strawman-observability-self-improvement.md`** — how the brain observes its own use
   (CloudWatch) and proposes its own evolution. Capture day one; inspect/suggest later.
4. **`strawman-stack-decisions.md`** — the decision register. Every tooling/storage call
   with a **HOLD / REFINE / REVISIT** status, the three-plane model, the complexity check,
   and the content-vs-mechanism nuance on ontology-as-data.
5. **`strawman-workshop-plan.md`** — how we close all of the above: a technical
   pre-workshop and the main team workshop, with exercises, timings, and the
   decided/recommend/needs-the-group split.

**`references.md`** — sources and prior art behind the set (Notion/HubSpot/AWS/MCP docs,
the Skills-over-MCP charter + SEP-2640, and the internal vault patterns this reuses), so the
design is auditable.

## The decisions that gate everything else

Resolve these first — they unblock the rest (all expanded in the docs above):

- **Identity / join keys** across Notion ↔ HubSpot — the highest unresolved risk.
- **HubSpot graduation threshold** — what event promotes a prospect into a HubSpot deal.
- **Search: federate vs. AWS derived index** — ship federation v1; define the trigger.
- **Controlled vocabularies** — the team owns these.
- **Write workflow & gate strictness** — who writes what; which rules block vs. warn.

## Status legend used across the set

- **STRAWMAN** — a proposal to react to.
- **Decision** callouts — open questions for the workshop.
- Stack register: **HOLD** (still right) · **REFINE** (direction holds, detail changed) ·
  **REVISIT** (genuinely reconsider).
