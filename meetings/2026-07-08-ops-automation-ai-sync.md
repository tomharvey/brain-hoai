---
title: Monthly Operations Automation & AI Sync
created: 2026-07-08
updated: 2026-07-09
domain: operational-tooling
type: meeting
tags: [ops, automation, cowork, renewals, hubspot, looker]
---

# Monthly Operations Automation & AI Sync — 2026-07-08

**Attendees**: Tom Harvey, [[shreya-chowta|Shreya Chowta]], [[emily|Emily Staton]], [[anna|Anna Spriggs]], [[jonny-smith|Jonny Smith]], [[fred-bush|Fred Bush]]

Transcript: [[2026-07-08-ops-automation-ai-sync-transcript]]

## Themes

### Jonny — connectivity workflow automation (co:work)
- Following the co:work session Tom ran a couple of weeks ago, Jonny built a Claude/co:work connector for his daily connectivity spreadsheet: downloads his Looker look, creates a new Excel tab, runs the VLOOKUPs against yesterday's data, and highlights policies over 35 connects or that dropped since yesterday.
- Tested twice, worked both times. Saves ~5–10 min/day. File currently lives in the co:work folder because local Documents and OneDrive access both failed — he'd prefer somewhere remotely accessible.
- Next phase: HubSpot connectors to action the daily filtered task list (e.g. send telematics-form chasers). Expects this to be painful — Zapier + HubSpot was "a bit of a pain" previously — and explicitly asked for Tom's help when he gets there.
- Longer term: fleet clinic list and other daily outputs generated off the same sheet.

### Emily — renewal process automation vision
- Current state: Anna's Zapier zap creates the HubSpot renewal deal 6 weeks out from the underwriters' Google Sheet, but leaves nearly everything blank — no company info, winning broker, or expected premium. Manual trips to the portal, Retool, Looker, and elsewhere to fill it in.
- Target state: HubSpot deal fully populated untouched; CCE generated (internal + external) from Looker; telemetry and speeding reports pulled; G Drive folder created with required files; broker email drafted; Retool/portal logging as a stretch.
- External sources needed: Experian (business credit / CCJ report — Tom confirmed an API exists, doable), Looker (telemetry, speeding, CCE), claims listings (Andy's daily emails + Admiral bordereau — searchable from email).
- Scale: renewals average 20–30 min each, up to 4–6/day in busy periods. Automating even the front half is a significant win.
- Proof point: Emily already upgraded the transfer-of-agency process with Claude — old Zapier version posted a bare alert; the Claude version pulls everything from HubSpot, drafts the channel post, pulls the BDM, and checks Companies House directors against the document. "If we've been able to do that for the TOA, we can definitely do it for renewals."
- Tom's framing: don't automate A→Z in one go — extract standalone sub-processes (e.g. Experian pull into HubSpot) that run independently of the big renewal flow.
- Fred's suggestion (adopted): paste the renewal process doc into Claude and ask "how much of this can you do? What should we tackle first?"

### Shreya — CC generator and new business team creator
- CC/CCE generator working: given a client name it goes into Looker CPE data, captures the information, and populates the CCE template. Output "was okay" — needed presentation/format tweaks, and the capture process is slow.
- New business team creator: refining for accuracy at volume — under load it "has its own mind and skips steps"; plan is batching (e.g. 10 at a time) so it runs reliably.

### Strategic context
- Potential trade risks binding authority on the horizon (rumour, nothing decided) — would materially increase the automation need.
- October submission targets from the OKR session (Jul 7) flagged as the forcing function: "there's going to be a lot of work coming our way, so we definitely need to get some of this sorted."
- Claude laptop logistics: Jonny currently on the Claude laptop, setting up his new laptop and bringing the Claude machine into the office Jul 9 for a setup session with Tom (log into all systems, configure Claude access). Tom in the office until Friday morning.
- Tom's AI workshop plugged; Jake (Wood) reportedly rallying the troops; ops folk invited to attend.

## Actions

- [ ] **Jonny**: bring the Claude laptop into the office (Jul 9), grab time with Tom to set it up — log into all relevant systems and configure Claude access.
- [ ] **Emily**: paste the renewal process document into Claude and ask what it can automate and which steps to tackle first.
- [ ] **Emily**: go through the renewal process doc and identify the easy-to-automate steps (HubSpot deal population, G Drive creation, broker email draft) as the first slice.
- [ ] **Jonny**: continue expanding connectivity automation; pull in Tom when the HubSpot actions phase starts.
- [ ] **Shreya**: harden the new business team creator for volume (batching approach).
- [ ] **Tom**: support Jonny's laptop setup session; advise on Experian API access when renewal automation starts.

## Transcription notes

- "Thom" → Tom; "Freda" → Fred; "Andrea" → Shreya; "claud"/"clawed"/"claw" → Claude; "experience" → Experian (in renewal context); "zappy" → Zapier.
- Unresolved: "Josh" (in Tom's line "What was that story, Josh?"), "Jake" (likely [[jake-wood|Jake Wood]], unconfirmed), "Curtis" ("Curtis is there... he'll be keen" re: workshop), "seato" (Jonny's laptop setup — possibly "IT" or a name).
