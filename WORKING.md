# Working

## Current task

BDM brain co:work implementation design complete. W22 meetings need ingesting. Commit pending.

## W21 summary (what was done)

- **13 meetings ingested** (June 1–4):
  - 2026-06-01: Anneliese / Thomas, Jake / Thomas AI UW, Ollie / Tom Weekly
  - 2026-06-02: People Team AI Workshop, Tom <> Jordi Weekly, Matt Price 1:1
  - 2026-06-03: AI Culture Group Session (Jacob/Aleks/Stephen), 2W Prodtech Demo, Fred / Thomas AI Catch-up
  - 2026-06-04: AI Engineering Group Therapy (Rob/Ismael/Javier), Granola / Flockcover, Fergus <> Tom Weekly, Cloud Code check-in

- **People file created**: phoebe-woodman.md

- **Issues created**: AI-086 through AI-096 (11 new issues):
  - AI-086: AI culture group sessions — next cohorts
  - AI-087: AI better-not-faster narrative
  - AI-088: Conversion improvement coordination workshop
  - AI-089: Flock O'Clock automation — Phoebe (People Team)
  - AI-090: Notion workflow sidebar — Rakhee (People Team)
  - AI-091: Engagement survey automation — Rakhee (due end-June)
  - AI-092: AI Workshop June 16 logistics (due 2026-06-16)
  - AI-093: Expansion team freelancer candidates (Jordi)
  - AI-094: Confirm Granola Teams plan subscription
  - AI-095: London visit — half-day workshop with Fergus (due ~2026-07-13)
  - AI-096: MCP read/write governance — define approach for core systems

- **Synthesis pass**: domains/ai-enablement, domains/engineering-workflows, domains/product-ai updated; initiatives/bdm-ai-multiplayer updated

- **MANIFEST rebuilt** to include all 96 issues, all meetings through 2026-06-04

## Unresolved name flag

In the Jordi 1:1 transcript (2026-06-02), "Christian" appears in a garbled passage: *"I spoke the other day with Ismail and Christian with me that now with my mother they are working"* — "my mother" = Mima (known substitution), but "Christian" has no match in people files. Could be garbling of Javier, Ivan, or a real person named Christian. The meeting note was written without this reference as the passage is too garbled to use. Flagged here for awareness.

## Current state

**Inbox**: 2 items still pending triage:
- `inbox/ProdTech Roadmaps Q2 2026.pdf`
- `inbox/ai-workshop-2026-04-21.pdf`

**Priority open issues**:
- AI-092: AI Workshop June 16 logistics — due 2026-06-16
- AI-079: AI June engineering sprint — due 2026-06-30
- AI-072: BDM team AI workshop — due 2026-06-13
- AI-091: Engagement survey automation — due end-June
- AI-096: MCP read/write governance (high priority)
- AI-088: Conversion improvement coordination workshop
- AI-095: London visit week after Cardiff (~2026-07-13)
- AI-094: Granola Teams plan quote incoming

## BDM brain — co:work project built (2026-06-10)

Full project at `tools/outbox/bdm-brain/`. Ready to deploy to Matt Lees as pilot.
Open architectural decisions documented below — deep dive scheduled for next session.



Phase 1 delivery is co:work, not thin MCP. Build sheet: `reference/shared-brain/cowork-implementation.md`.

Key elements:
- **BDM Directory** in Notion — names, Slack handles, HubSpot owner IDs (Adam maintains)
- **HubSpot as ownership oracle** — query company owner at write time, map to BDM Directory
- **Granola skill** — sales template + BDM mention scan + Activity Log write + cross-BDM Slack DM
- **4 scheduled tasks**: 8am brief, 30-min pre-meeting, 5:30pm EOD nudge, Monday pulse
- **Caretaker/Apprentice**: weekly pulse writes to Brain Health Log; Adam reviews Fridays
- **Next step**: pilot with Matt Lees — Adam confirmed he's the right first person

Adam 1:1 key outputs: trading pack data quality is urgent blocker; wants proactivity; new BDM joining 2026-07-21.

## Open architectural decisions (BDM brain — deep dive next session)

1. **Scheduling mechanism** — does co:work scheduled tasks fire server-side (app closed)
   or client-side (app must be open)? If client-side, fallback needed: n8n vs GitHub
   Actions vs EventBridge. Gating question for the whole scheduled task design.

2. **Agentic vs reactive** — is co:work actually running an agent loop, or is it
   reactive tool-calling? The pre-meeting brief polls GCal every 15 min and fires
   unprompted. The weekly pulse reads 30+ files and makes decisions. At what point
   does this become a proper agent? Does that matter for what we can build in Phase 1?

3. **HubSpot as join key / name matching** — company search by broker name is fragile.
   Brown & Brown vs Brown and Brown vs B&B all fail. What's the fallback when search
   returns 0 or 3 results? Do we need a canonical name field? Does the domain (email
   domain as join key, from the ontology strawman) solve this?

4. **Skill reliability in scheduled context** — scheduled tasks invoke multi-step skill
   logic by reading a project knowledge file and following it. How reliable is this in
   practice? Does the agent consistently complete all steps, or does it collapse steps
   under time/context pressure? This affects how prescriptive skill files need to be.

5. **Phase 1 → Phase 2 trigger** — at what point does co:work get replaced by the
   thin MCP? What's the specific signal: number of active BDMs, query volume, a
   capability the co:work architecture can't deliver, or does it just stay as-is?
   This shapes how much to invest in the current implementation vs. treating it as
   a prototype.

## Next actions

- [ ] **Next session: BDM brain architecture deep dive** — work through the 5 questions above
- [ ] Ingest W22 meetings (Matt Price 1:1, Ollie weekly, Rakhee AI Workshops, group therapy session 3, Adam BDM brain)
- [ ] Create Adam BDM brain meeting note (transcript fetched: meeting ID 39bb1471)
- [ ] Set up co:work pilot with Matt Lees — use `tools/outbox/bdm-brain/` (README has setup steps)
- [ ] Triage inbox PDFs (AI workshop and ProdTech roadmaps)
- [ ] Confirm Granola Teams plan quote from Will (AI-094)
- [ ] AI Workshop June 16 — confirm logistics and invite (AI-092, **due in 6 days**)
- [ ] BDM workshop with team — Oli Crowe alignment done; schedule team session (AI-072)
- [ ] AI June sprint — coordinate with Rob/engineering team (AI-079)
- [ ] MCP read/write governance — quick answer on HubSpot deletes (AI-096)
