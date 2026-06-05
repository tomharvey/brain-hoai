# Strawman: Observability & the Self-Improving Brain

> **Status: STRAWMAN.** Companion to `strawman-sales-ontology.md` and
> `strawman-notion-schemas.md`. Describes how the brain observes its own use and proposes
> its own evolution.

The thin MCP is the **single front door** for every read and write. That makes it the
natural place to observe how the brain is *actually* used — and that observation is what
lets the brain evolve from real usage instead of our guesses. This is the Rosenfeld
`/improve-skill` and `/review` discipline applied to the whole knowledge base.

---

## The loop

```
   ┌──────────────────────────────────────────────────────────┐
   │                                                          │
   ▼                                                          │
 USE ──► CAPTURE ──► INSPECT ──► SUGGEST ──► DECIDE ──► EVOLVE ┘
(team)   (MCP logs   (nightly   (Improvement (human +   (Conventions/
         intent +    self-      Suggestion   MADR)      Schema-defs
         calls +     inspection  rows)                   updated →
         outcomes)   task)                               MCP reads
                                                         new rules)
```

Real use → telemetry → self-inspection → suggestion → decision → ontology-as-data change →
the MCP reads the new rules on its next call. Nothing mutates the schema without a human
accepting it.

---

## 1. Capture — what the MCP logs

Every MCP call emits one **Interaction** event:

| Field | Example |
|---|---|
| timestamp / user / session | `2026-06-10T14:03Z` · alice · sess_82f |
| **intent** | "which accounts have a departed champion?" (the NL request) |
| role *(derived)* | classified async during inspection — not captured at call time |
| operation | `query` · objects: `Opportunity`, `Person` |
| inputs | filters / query string / the proposed row (for writes) |
| **outcome** | `success` / `empty-result` / `lint-rejected` / `error` |
| response summary | result count, written record id, or the rejection reason |
| latency | 240ms |

**Writes capture the lint verdict** (pass, or which rule failed). Rejections are the
single richest signal — they're a feedback stream about your own ontology.

**Role classification is async** — derived during the inspection pass, not at call time. The `intent` field (the raw NL request) is the input; the inspection task infers which of the eight roles (`librarian`, `secretary`, `coach`, `forecaster`, `strategy-partner`, `sparring-partner`, `caretaker`, `apprentice`) the user was invoking, then annotates the log record. A single interaction may map to multiple roles. No latency cost on the MCP call path.

## 2. Store — raw vs. distilled (same principle as Build Log)

Raw events are high-volume → **not Notion** (rate limits, row bloat). The Notion meta layer
holds only the **distilled** output: Usage Insights + Improvement Suggestions. Same move as
"raw transcript → link, distilled → Decisions" — keep Notion signal-dense.

**Store: AWS CloudWatch** (we're already AWS-native — Strands, Athena). Concretely:

- **CloudWatch Logs** — the MCP emits one structured-JSON log event per interaction. Cheap,
  managed, append-only, per-log-group **retention** set natively (e.g. 90 days). **Logs
  Insights** covers the short-window aggregate queries the self-inspection task needs
  ("lint rejections on field X this week").
- **EMF / CloudWatch Metrics + alarms** — emit metrics straight from those logs for a live
  usage dashboard and alerts (error-rate spike, write-rejection surge).
- **S3 + Athena for deep analysis** — a subscription filter streams logs to S3; the
  self-inspection task queries them with **Athena**, reusing the exact competency the
  energy product already runs on. Use this for the heavier multi-week pattern-mining;
  Logs Insights for the quick stuff.

This removes the earlier "bespoke event store" hand-wave — CloudWatch *is* the event store.

- **Governance:** intent text can contain sensitive sales detail → same trust boundary and
  access control as the brain itself; never ship to third parties.

## 3. Inspect — the self-inspection task

A scheduled, Claude-driven automation (the brain's own `/review`) runs nightly over the raw
log and hunts for patterns:

| Pattern in the log | What it suggests |
|---|---|
| Repeated lint rejections on the same field/rule | rule too strict, or users confused → loosen / re-word / add a write-time prompt |
| Searches that often return empty | missing data, a missing vocab value, or a gap the ontology can't answer |
| Frequent multi-hop queries that are slow/awkward | promote an edge or add a rollup |
| Two object types frequently accessed together | candidate new relation |
| Fields/objects never read or written | candidate to **deprecate** — keep the brain lean |
| Recurring intent with no matching tool/skill | candidate new capability |
| Free-text where a Select was expected | vocabulary needs a new value |
| Role distribution heavily skewed to one type | other roles may be undiscoverable or genuinely unneeded — validate with users before building |
| High volume of `role_confidence: ambiguous` | intent classification needs refinement, or the prompt surface isn't giving users clear affordances for each mode |
| Role inferred as X but response pattern matches Y | brain switching modes uninvited — evaluation failure, see §5 |
| A role with zero usage across N weeks | either the Phase isn't live yet, users don't know the capability exists, or the need doesn't actually arise — flag for the workshop |

Output: **Improvement Suggestion** rows, each linked to its evidence (the patterns +
counts) and proposing a *concrete* change — add field X, add vocab value Y, loosen rule Z,
add relation, deprecate W.

## 4. Evaluate — role-alignment scoring

Every interaction carries a `role` field. The evaluation task (runs alongside self-inspection) checks whether the brain's response matched the mode the user's intent implied. A librarian intent that gets a sparring-partner response is a failure; a strategy-partner request that gets a list of facts with no synthesis is also a failure.

Rubric per role:

| Role | Response should... | Failure looks like |
|------|--------------------|--------------------|
| **Librarian** | Return relevant records accurately | Empty result for a query that should match; hallucinated accounts or contacts |
| **Secretary** | Log the action *and* schedule a reminder | Action noted in the response text but not written to the knowledge graph |
| **Forecaster** | Surface a signal before the BDM asked | Signal only appears when directly queried — reactive, not proactive |
| **Coach** | Ground feedback in the user's own history | Generic advice unconnected to past interactions or patterns |
| **Strategy partner** | Synthesise context *and* recommend a direction | A list of facts with no recommendation — retrieval dressed up as synthesis |
| **Sparring partner** | Hold a counter-position and defend it | Agree with everything the user says; hedge every pushback into irrelevance |
| **Caretaker** | Apply lint rules correctly and consistently | Rule silently ignored, or fires incorrectly on valid input |
| **Apprentice** | Ground improvement suggestions in logged evidence | Suggestions not backed by usage data; speculation dressed up as analysis |

Evaluation outputs flow into the same Improvement Suggestion pipeline as inspection outputs. A pattern of strategy-partner requests getting librarian-quality responses is a capability gap, not a data gap — it routes to a prompt/skill change, not a schema change.

---

## 5. Decide — route into the existing pipeline

Improvement Suggestion → human triage → promoted to a proposed **Decision** (MADR) →
accepted → applied to **Conventions / Schema-defs** (the ontology-as-data) → MCP reads the
new rules on its next call.

- **Safety:** structural changes require an accepted Decision — no silent self-mutation.
- **Decision:** an **auto-apply threshold** — low-risk changes (e.g. adding a Select value)
  might bypass MADR; structural changes (new object/edge, changed cardinality) never do.

---

## Why this matters most with non-technical users

They can't tell you "the schema is wrong" — but **their usage will.** Lint rejections,
empty searches, and awkward queries are the brain reporting its own gaps in a language the
team doesn't have to speak. The self-inspection task turns that exhaust into a prioritised,
evidence-backed change list. The brain gets better the more it's used, which is exactly the
property you want from a shared asset four people lean on daily.

## Open decisions

1. ~~Raw event store technology~~ → **CloudWatch** (decided). Open: retention window.
2. Governance/privacy of captured intent text (intent fields may contain sensitive deal detail).
3. Auto-apply threshold — which suggestion types bypass the MADR step?
4. ~~Cadence of the self-inspection task~~ → **nightly** (decided). May also add a usage-volume trigger for burst periods.
5. Who triages Improvement Suggestions, and how they're prioritised.
6. ~~Role classification mechanism~~ → **async / inspection pass** (decided). Role derived from `intent` text during nightly inspection, not at call time. No real-time role dashboards, no latency cost.
