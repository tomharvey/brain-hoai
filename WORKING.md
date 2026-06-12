# Working

## Current task

W22 session complete. All files committed.

## W22 summary (what was done)

- **9 meetings ingested** (June 9–11):
  - 2026-06-09: Matt Price 1:1, Ollie weekly, Rakhee AI Workshops
  - 2026-06-10: AI group therapy (Chris/Sam/Alex + Geran strategy split), Adam BDM brain, AI strategy Geran
  - 2026-06-11: BDM brain architecture deep-dive (Ollie), Fergus weekly

- **People files created**: sami.md, ben-allen.md, daisy-mae-baker.md, ivan-boix.md, kevin-berg.md (from earlier W22 work)

- **Issues created**: AI-097 through AI-109 (13 new issues)
  - AI-107: Share activation + adoption frameworks with Ed and Rakhee — **urgent, due 2026-06-30**
  - AI-109: Cancelled (public telemetry endpoint)
  - AI-099: Cancelled (workshop framing)
  - AI-088: Cancelled (conversion improvement coordination)

- **Key issue updates**:
  - AI-095 reframed: London visit → Ed update + wider company engagement (Jul 8, Antton + Christian away)
  - AI-068: Workshop agenda updated — intent first, incremental building, context over prompting

- **New reference doc**: `reference/ai-adoption-frameworks.md` — three frameworks: team role taxonomy, utility vs companion, implementer vs systems thinker

- **Activation map** (`reference/ai-activation-map.md`) — major update:
  - Added Underwriting and People columns
  - Distribution chart (Mermaid xychart-beta): ~36 assessed
  - Progression table: 8 movers with before/after evidence
  - Comprehensive "Not yet assessed" section with priority conversations list
  - Notes on Tom Rogers, Liam Thomson, Darren McCauley

- **Org chart updated**: Mollie removed (left), Emily now reports to Antton, Connie + Navani on maternity

- **Synthesis passes**: domains/ai-enablement, domains/engineering-workflows updated; initiatives/ai-native-engineering + bdm-ai-multiplayer updated

## Unresolved name flag

In the Jordi 1:1 transcript (2026-06-02), "Christian" appears in a garbled passage — unfixable. Flagged for awareness only.

## Current state

**Inbox**: 2 items still pending triage:
- `inbox/ProdTech Roadmaps Q2 2026.pdf`
- `inbox/ai-workshop-2026-04-21.pdf`

**Priority open issues**:
- AI-107: Share activation + adoption frameworks with Ed + Rakhee — **urgent, due 2026-06-30**
- AI-068: Company-wide workshop — **due 2026-06-16 (4 days)**
- AI-092: AI Workshop June 16 logistics — due 2026-06-16
- AI-072: BDM team AI workshop — due 2026-06-13
- AI-079: AI June engineering sprint — due 2026-06-30
- AI-091: Engagement survey automation — due end-June
- AI-096: MCP read/write governance (high priority)
- AI-094: Granola Teams plan quote incoming
- AI-095: London visit Jul 8 — Ed update + wider engagement

## BDM brain — co:work project built (2026-06-10)

Full project at `tools/outbox/bdm-brain/`. Ready to deploy to Matt Lees as pilot.

Phase 1 delivery is co:work, not thin MCP. Build sheet: `reference/shared-brain/cowork-implementation.md`.

Key elements:
- **BDM Directory** in Notion — names, Slack handles, HubSpot owner IDs (Adam maintains)
- **HubSpot as ownership oracle** — query company owner at write time, map to BDM Directory
- **Granola skill** — sales template + BDM mention scan + Activity Log write + cross-BDM Slack DM
- **4 scheduled tasks**: 8am brief, 30-min pre-meeting, 5:30pm EOD nudge, Monday pulse
- **Caretaker/Apprentice**: weekly pulse writes to Brain Health Log; Adam reviews Fridays
- **Next step**: pilot with Matt Lees — Adam confirmed he's the right first person

## BDM brain architectural decisions — RESOLVED (2026-06-11)

Full decision record: `decisions/005-bdm-brain-scheduling-architecture.md`

1. **Scheduling**: co:work scheduled tasks fire server-side (Anthropic infra). Server-side connectors only (Slack, HubSpot, Granola, Notion, GCal, Gmail). Filesystem MCP is interactive-only. **Validate in pilot**.

2. **HubSpot name matching**: capture company ID on first touch, store in My Accounts. Name search is fallback only.

3. **Phase 1 → Phase 2 trigger**: Notion Activity Log contention with 3+ active BDMs. Likely Q3 2026 if pilot succeeds.

## Next actions

- [ ] **Jun 16 workshop** — confirm demo owner (Matt Lees candidate), brief plants, write activity prompt (AI-068, AI-092, **4 days**)
- [ ] **AI-107** — share activation + adoption frameworks with Ed and Rakhee before Jun 30
- [ ] **BDM pilot** — set up Matt Lees co:work project using `tools/outbox/bdm-brain/`
- [ ] **BDM workshop** — Ollie alignment done; schedule team session (AI-072, due Jun 13)
- [ ] **AI June sprint** — coordinate with Rob/engineering (AI-079)
- [ ] **Evaluation gap** — priority 8 conversations: Antton, Darren McCauley, Darren Nightingale, Lawrence Tanner, Michael Matthews, Christian, Paul O'Neill, Sami
- [ ] Triage inbox PDFs (AI workshop and ProdTech roadmaps)
- [ ] Confirm Granola Teams plan quote from Will (AI-094)
- [ ] MCP read/write governance — quick answer on HubSpot deletes (AI-096)
