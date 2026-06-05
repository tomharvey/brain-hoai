# Workshop Facilitation Plan — Sales Shared Brain

> **Status: STRAWMAN.** Two sessions: a **technical pre-workshop** (de-risk the plumbing)
> and the **main workshop** (the sales team flesh out what only they can). Companion to the
> ontology / schema / observability / stack-decision artifacts.

## The governing principle

**Spend the team's time only on what the team alone can answer.** Everything resolvable by
one technical person should be resolved *before* the room, and arrive as a recommendation —
not an open question. The pre-workshop exists to make that true.

Two things only the domain experts can give us, and both become the workshop's spine:

- **Representational fit** — does the schema *hold* how they actually work? → "Trace a live deal."
- **Query fit** — does it *answer* what they actually ask? → "Question storm."

**Dogfood from minute one:** every decision in either session is captured live as a draft
**Decision (MADR)** row. The brain's meta layer starts filling before the brain exists.

---

## Session 1 — Technical pre-workshop (Tom ± technical teammate, ~2h)

**Goal:** resolve the plumbing, arrive at the main workshop with a one-page
*decided / recommend / needs-the-group* sheet, and prep the materials the exercises need.

| # | Topic | Decide / produce | Why pre, not main |
|---|---|---|---|
| 1 | **Identity & join keys** (#9, top risk) | domain (Account) + email (Person) as keys; who owns the master record Notion-vs-HubSpot; the dedupe-on-write rule | The thing most likely to corrupt a dual-store model; non-technical team can't adjudicate it |
| 2 | **Search: federate vs derived index** (#4) | ship **federation** v1; define the trigger to build the **AWS index** (OpenSearch + Bedrock) | Mechanism choice; team only supplies the *queries* (Session 2) that judge "good enough" |
| 3 | **HubSpot integration mechanics** (A+C) | which objects sync which direction; read-through now / write-back later; the graduation *mechanism* (team picks the *threshold*) | Plumbing; avoid dual-write conflicts before they exist |
| 4 | **Thin MCP shape & hosting** | tool surface (the lint-enforcement list = the build spec); where it runs; auth; stateless; **bus-factor** plan | Pure engineering |
| 5 | **Telemetry** | CloudWatch log-event schema; retention window; **intent-text PII/governance**; who may read it | Engineering + a governance flag to raise to group |
| 6 | **Rule representation** | data-shaped config file now (seam for ontology-as-data later) | Implementation detail of decision #7 |
| 7 | **Migration mechanics** | sequence (Accounts→People→Opps→Convos→Hyps→Signals); lint-as-QA + Claude-assisted extraction + quarantine view; **Notion inventory** to size it | Method; the team validates the *plan* and *timeline*, not the mechanics |

**Pre-workshop outputs (the inputs Session 2 needs):**
- A clean object-model diagram to **react to** (reacting beats inventing for non-technical folks).
- The strawman vocab lists, printed, ready to be challenged.
- **2–3 real messy Notion records** pulled for the migration exercise.
- Notion inventory (DB count + rough row counts) to right-size the migration conversation.
- The one-pager: what's **decided**, what we **recommend**, what genuinely **needs the group**.

**The handoff list — what the pre-workshop deliberately kicks to the group:** HubSpot
graduation threshold · the controlled vocabularies · the real queries · write/read workflow
& gate strictness · intent-text governance comfort.

---

## Session 2 — Main workshop (sales team + Tom, ~3.5h with breaks)

**Definition of done:** a validated object model, locked vocabularies, a ranked query list
(our acceptance tests), an agreed write workflow, a HubSpot threshold, and a migration plan
with an owner and a freeze date — all captured as draft Decision rows.

| # | Block | Time | Method | Output |
|---|---|---|---|---|
| 0 | **Frame** | 10m | What a shared brain is; what we decide today; **what's already settled** (don't relitigate plumbing) | shared frame |
| 1 | **Trace a live deal** | 40m | Pick a real recent account; walk every fact through the strawman objects/edges. Every fact must have a home; homeless facts → revise the schema | validated/edited object model |
| 2 | **Question storm** | 35m | Everyone writes the questions they *wish* they could ask the data; cluster; rank by value × frequency | ranked query list = acceptance tests; drives search & edges |
| — | *break* | 10m | | |
| 3 | **Lock the vocabularies** | 35m | Challenge every enum value: real or aspirational? Stages, roles, statuses, angles | frozen controlled vocab |
| 4 | **Workflow & the gate** | 30m | Who writes what; capture-to-inbox vs direct write; walk real friction examples to set which rules **block** vs **warn** | write model + gate strictness |
| 5 | **HubSpot threshold** | 20m | What *event* promotes a prospect into a HubSpot deal? (first meeting? SQL?) | the graduation rule |
| 6 | **Migration as design, not data-entry** | 25m | Show the 2–3 messy records; decide their target shape together; agree **"won't fit = a signal to revise," not a problem to force**; set owner + freeze date | migration plan + the right mindset |
| 7 | **Decisions & owners** | 15m | Review the live decision log; assign owners + dates; name the parking lot | committed next steps |

### Facilitation notes
- **Roles:** a facilitator who guards time and doesn't dominate; a scribe who turns each
  call into a Decision row; Tom as the domain↔technical translator.
- **React, don't invent.** Always put a strawman on the wall for them to push against —
  far higher yield with non-technical participants than a blank page.
- **Two exercises carry the session.** Blocks 1 and 2 *are* the representational-fit and
  query-fit gates run live. If time slips, protect those two and compress 5–6.
- **Parking lot** for anything that turns into engineering or can't be closed in the room —
  it routes back to a follow-up, not a stall.
- **Watch the migration framing (block 6).** If the team treats "this record won't fit" as
  something to force through rather than feed back into the schema, the whole test is lost.
  Make "quarantine + revise" an explicitly *valued* outcome before they start.

---

## After the workshops

1. Fold every Decision row + schema edit back into the strawman artifacts (live docs).
2. Pre-workshop owns: finalise search v1, identity rules, MCP build spec, migration runbook.
3. The ranked query list (Block 2) becomes the **acceptance test** the brain is measured against.
4. Migration begins as the ontology's representational-fit test (stack register #7) — with
   the feedback loop into the schema switched on.
