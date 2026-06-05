# Strawman: Sales Team Shared Brain — Ontology & Tooling

> **Status: STRAWMAN for the workshop.** Built to be argued with, not adopted as-is.
> Every "Decision" callout is a thing we resolve in the room. Nothing here is final.

This describes a shared, Claude-native "brain" for a 4-person, non-technical sales team.
It reuses the architecture proven in the Rosenfeld vault (typed objects + typed edges +
a gated, lint-validated write path) but with **sales-first-class objects** and a
**Notion + HubSpot + thin-MCP** stack instead of git/markdown.

---

## 0. The spine: where does each object live?

We have three candidate stores, each good at different things:

- **HubSpot** — transactional CRM. Great at deals, stages, forecasting, email/activity
  logging, seat-based access. Already in use. Rigid; bad at qualitative knowledge and
  flexible graph structure.
- **Notion** — flexible docs + databases. Great at narrative, hypotheses, relations,
  non-technical UI, AI/keyword search. Already in use *as a mess*. Weak at custom
  invariants.
- **Thin MCP** — our own small service. The single front door for Claude. Joins across
  HubSpot + Notion, presents one ontology, and **gates every write through lint** so the
  graph can't rot no matter who contributes.

The whole design reduces to: **draw the system-of-record (SoR) line between HubSpot and
Notion, and let the thin MCP unify them.**

---

## 1. HubSpot strategy — three options

> **Decision 1 (biggest one): which of these do we adopt?**

### Option A — Dual SoR, joined by the thin MCP *(recommended starting point)*
HubSpot owns the **transactional layer** (Accounts, Contacts, Deals, stages, activities).
Notion owns the **knowledge/graph layer** (Hypotheses, Signals, Conversations, Playbooks,
ICPs, and the qualitative relationships). The thin MCP reads both, presents one ontology,
and gates writes.
- ✅ Each store does what it's best at; nothing rebuilt; keeps revenue data where finance/ops expect it.
- ⚠️ **Identity problem**: the same Account/Person exists in both → need a stable join key
  (domain for accounts, email for people) and a rule for who owns identity. This is the
  crux — see Decision 2.

### Option B — HubSpot fully behind the thin MCP
Claude never talks to HubSpot directly; the MCP mediates *everything*, applying lint to
HubSpot writes too.
- ✅ Single governance point; one front door; lint covers HubSpot too.
- ⚠️ You're proxying HubSpot's surface — more to build/maintain, and you fight HubSpot's
  own model where it's opinionated.

### Option C — Notion-first, HubSpot as a "graduation" target
Top-of-funnel + all knowledge live in Notion. A target is **promoted into HubSpot only
when it crosses a qualification threshold** (e.g. first meeting booked / becomes an SQL).
- ✅ Simplest day one; keeps HubSpot clean (only real deals, fewer wasted seats); defers
  integration work; Notion is the wide exploration space.
- ⚠️ Two homes for "Account"; need a clean promotion/sync step; risk of drift after promotion.

**Strawman pick:** start at **A**, but adopt **C's threshold idea** as the rule for *when*
a Notion prospect earns a HubSpot Deal record. i.e. Notion is SoR for everything until
qualification; HubSpot becomes SoR for the deal/forecast layer at qualification; the thin
MCP keeps them joined. We can collapse to pure-C if HubSpot integration proves heavy.

---

## 2. First-class objects

| Object | Purpose | Proposed SoR | Replaces (Rosenfeld analog) |
|---|---|---|---|
| **Account** | The company we're selling to (the "sales target") | HubSpot (post-qual) / Notion (pre-qual) | Company |
| **Person** | An individual at an account (champion, buyer, blocker) | HubSpot (Contact) + Notion overlay | Contact |
| **Opportunity** | A specific revenue pursuit at an account | HubSpot (Deal) | — (new) |
| **Conversation** | A meeting/call/email — narrative + transcript | Notion | Conversation |
| **Hypothesis** | A testable sales belief ("X segment buys because Y") | Notion | Hypothesis (was "initiative") |
| **Signal** | An atomic piece of evidence for/against a hypothesis | Notion | Feedback |
| **ICP / Segment** | Definition of an ideal-customer segment | Notion | ICP |
| **Playbook / Asset** | Reusable messaging, case study, objection handling | Notion | reference/messaging |

> **Decision 3: Signal as its own object vs. a section inside Conversation.**
> Splitting it out is what makes the hard graph queries cheap (a Signal links *both* to its
> source Conversation *and* to the Hypothesis it moves). Strawman keeps it separate.

> **Decision 4: do we need Opportunity distinct from Account day one,** or is a status field
> on Account enough until volume justifies deals? (Ties to HubSpot Option C threshold.)

---

## 3. Object fields (strawman)

Common to all: `id`, `title/name`, `created`, `updated`, `updated-by`, `status`, `owner`.

**Account**
- `domain` (join key), `website`, `industry`, `employees`, `hq`, `segment` (→ ICP)
- `stage` (controlled vocab below), `engagement-angle`, `source`, `warm-path` (→ Person)
- `hubspot-id` (set at graduation), `notion-id`

**Person**
- `email` (join key), `linkedin-url`, `account` (→ Account), `title`
- `role-in-deal` (controlled vocab), `person-status` (controlled vocab — incl. `departed`)
- `introduced-by` (→ Person), `hubspot-id`, `notion-id`

**Opportunity**
- `account` (→ Account), `stage`, `value`, `close-date`, `champion` (→ Person)
- `hypotheses` (→ Hypothesis list), `hubspot-deal-id`

**Conversation**
- `account` (→ Account), `people` (→ Person list), `channel` (call/meeting/email/dm)
- `hypotheses-tested` (→ Hypothesis list), `date`, transcript/summary body

**Hypothesis**
- `hyp-status` (active/validated/invalidated/decomposed), `segments` (→ ICP list)
- `engagement-angle`, current-assessment body

**Signal**
- `source` (→ Conversation), `supports` (→ Hypothesis list), `contradicts` (→ Hypothesis list)
- `account` (→ Account), `person` (→ Person), `observed-date`, verbatim body

**ICP / Segment** — definition body, `active-hypotheses` (→ Hypothesis list)

**Playbook / Asset** — `asset-type`, `applies-to-segment` (→ ICP), `applies-to-stage`

---

## 4. Controlled vocabularies (the enums lint enforces)

> **Decision 5: lock these lists.** Notion select-properties enforce membership; the thin
> MCP enforces "this field must come from this list" on write.

- **Account.stage**: `researching` → `target` → `engaged` → `qualified` → `opportunity` → `customer` → `disqualified`
- **Opportunity.stage**: `discovery` → `demo` → `proposal` → `negotiation` → `won` / `lost`
- **Person.role-in-deal**: `champion`, `economic-buyer`, `technical-buyer`, `influencer`, `blocker`, `unknown`
- **Person.person-status**: `active`, `dormant`, `departed`, `do-not-contact`
- **engagement-angle**: `product`, `consulting`, `both`, `partner`
- **Hypothesis.hyp-status**: `active`, `validated`, `invalidated`, `decomposed`

---

## 5. Typed edges (the graph)

| Edge field | Source → Target | Meaning |
|---|---|---|
| `account` | Person → Account | works-at |
| `account` | Opportunity / Conversation / Signal → Account | concerns |
| `champion` | Opportunity → Person | championed-by |
| `role-in-deal` | Person → (qualifies their link to Opportunity) | plays-role |
| `introduced-by` | Person → Person | referred-by |
| `warm-path` | Account → Person | introduced-via |
| `people` | Conversation → Person (list) | attended-by |
| `hypotheses-tested` | Conversation → Hypothesis (list) | tests |
| `supports` / `contradicts` | Signal → Hypothesis (list) | moves |
| `source` | Signal → Conversation | evidenced-by |
| `segments` | Hypothesis → ICP (list) | applies-to |

Body links stay free-form; **promote a relationship to a field the moment a query needs it.**

---

## 6. Invariants the gate enforces (lint rules)

These are *why* we need the thin MCP rather than raw Notion. Errors block the write;
warnings flag for review.

- **ERR** every Opportunity links to exactly one Account.
- **ERR** every Conversation links to ≥1 Person and ≥1 Account.
- **ERR** every Signal links to ≥1 Hypothesis (via supports/contradicts) and a source Conversation.
- **ERR** every relation target exists and is the right type (referential integrity).
- **ERR** controlled-vocab fields contain only allowed values.
- **WARN** every Opportunity has ≥1 Person with `role-in-deal: champion`.
- **WARN** an `active` Hypothesis with no Signal in the last 30 days → stale, needs review.
- **WARN** an Account at stage `opportunity`+ with no linked Opportunity record.
- **FLAG** (the headline query, as a standing rule) — any Opportunity whose `champion` has
  `person-status: departed` while a linked Hypothesis is still `active`.

---

## 7. Proof: the hard query traced through the model

> "Show me every target where the champion left and the hypothesis is still open."

1. `Person` where `person-status = departed`
2. → `Opportunity` where `champion = thatPerson`
3. → `Opportunity.hypotheses` where `hyp-status = active`
4. → return the `Account` (+ the at-risk hypothesis + last conversation)

Every hop is a typed edge or a controlled-vocab field. Notion's native search can't do
this multi-hop join; the thin MCP can, because the ontology made each hop explicit. This
is the single best argument for the thin-MCP layer and for promoting `role-in-deal` /
`person-status` to first-class fields.

---

## 8. Migrating the existing Notion mess

The mess is almost always *missing edges and inconsistent fields*, not missing content.

**Migration doubles as the ontology's first and best test.** Forcing real historical records
into the proposed schema proves *representational fit* (can it hold what we already have) —
an earlier, different gate than the *query/workflow fit* live usage proves later. Records
that won't fit cleanly are direct evidence the schema is wrong or thin → feed that back into
the design *before* go-live. This is why the **ontology content is day one** even though the
*ontology-as-data mechanism* is deferred (see stack register #7).

Plan:

1. **Define target ontology** (this doc) and create clean target databases.
2. **Audit** the existing Notion: inventory every database/page, classify each into a
   target object, mark the junk.
3. **Field-map** old → new; identify which old text fields become *relations*.
4. **Migrate in waves**, dependency order: Accounts → People → Opportunities →
   Conversations → Hypotheses → Signals. (Edges can only point at rows that already exist.)
5. **Run lint as a migration QA gate** — score each migrated record; quarantine
   incomplete ones into a "needs triage" view instead of letting them in dirty.
6. **Backfill edges** — the relationships are usually what the mess is missing.
7. **Freeze old**, redirect the team to the clean DBs.

**Claude does the heavy lifting here**: it reads each messy page, proposes a structured
row, and the gated-write path means a human only approves — drift can't sneak in. The
same lint that governs daily writes governs the migration.

---

## 9. Open decisions for the workshop

1. **HubSpot strategy** — A / B / C (§1). What's the graduation threshold?
2. **Identity / join keys** — domain for Accounts, email for People? Who owns identity
   when a record lives in both stores?
3. **Signal: separate object or section?** (§2, Decision 3)
4. **Opportunity distinct from Account day one?** (Decision 4)
5. **Lock the controlled vocabularies** (§4).
6. **Gate strictness** — which rules block vs. merely warn? (§6)
7. **Search depth** — is keyword + semantic (Notion native) enough, or do we need the
   thin MCP for structural/graph search from day one? (We think day one, per the queries.)
8. **Who can write vs. read** — all 4 write? Or capture-to-inbox + reviewer promotes?
9. **Where the thin MCP runs / who maintains it** (the one technical dependency).
10. **Migration sequencing & freeze date** for the old Notion.
11. **Telemetry**: raw event store + retention; intent-text governance; auto-apply
    threshold for self-generated suggestions. (See observability artifact.)

---

## 10. The brain improves itself

Because the thin MCP is the single front door, it logs every intent, tool call, and
outcome (writes capture the lint verdict). A weekly self-inspection task reads that
telemetry and writes evidence-backed **Improvement Suggestions** — "this rule is rejected
constantly," "this search keeps coming back empty," "these two objects are always queried
together." Suggestions route through human triage → MADR → the ontology-as-data, so the
schema evolves from real use without ever silently self-mutating.

This is the payoff of the meta layer: with non-technical users who can't tell you the
schema is wrong, their *usage* tells you instead. Full design in
`strawman-observability-self-improvement.md`.
