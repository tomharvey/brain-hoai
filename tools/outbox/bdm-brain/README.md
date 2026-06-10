# BDM Brain — co:work Project

A shared Claude brain for the Flock BDM/sales team, delivered via Claude co:work.

---

## What's in this folder

```
bdm-brain/
├── README.md                      ← you are here
├── project-instructions.md        ← paste into co:work project instructions
├── onboarding-questions.md        ← data file: the 7 questions + guidance
├── skills/
│   ├── onboarding.md              ← interactive setup: steps through questions one by one
│   ├── granola-summary.md         ← post-meeting Granola summary with BDM mention detection
│   ├── ghost-check.md             ← on-demand ghost account detection
│   └── brain-health.md            ← manual Caretaker review trigger
└── scheduled-tasks/
    ├── morning-brief.md           ← 8:00am weekdays
    ├── pre-meeting-brief.md       ← 30 min before external calendar events
    ├── eod-nudge.md               ← 5:30pm weekdays
    └── weekly-pulse.md            ← Monday 8:00am
```

---

## Setup — one project per BDM

Each BDM gets their own co:work project. The project instructions are personalised;
the skill files and Notion pages are shared.

### Step 1 — Create the project

In Claude co:work (desktop app): New project → name it "[Name]'s Brain".

### Step 2 — Add project instructions

Copy `project-instructions.md` into the project instructions field.
Replace every `[BDM_NAME]`, `[SLACK_HANDLE]`, `[EMAIL]` placeholder.

### Step 3 — Add project knowledge

Upload every file in `skills/` to project knowledge.
Skill files must be named exactly as they appear here — the project instructions
reference them by name.

Also add the following Notion pages to project knowledge (paste links):
- BDM Directory
- Shared Activity Log
- Broker Ownership
- Sales Playbook
- Broker Tiers
- OKRs (current quarter)
- Brain Health Log
- My Accounts (this BDM's page)
- My Commitments (this BDM's page)
- My Shortcuts (this BDM's page)
- My Development Focus (this BDM's page)

### Step 4 — Connect MCP tools

Ensure these MCP connectors are active in the project:
- Notion (read + write to the BDM's own pages; read-only for team pages)
- HubSpot (read + create/update; no delete)
- Slack (send to DMs only; not channels)
- Gmail (create_draft only — never send)
- Google Calendar (read-only)
- Granola (read-only)

### Step 5 — Run onboarding

In a new conversation in this project, type: `/onboarding`

The agent will step through 7 questions one at a time and build Layer 2
(My Shortcuts, My Development Focus, My Commitments seed).

### Step 6 — Set up scheduled tasks

In co:work project settings → Scheduled tasks:

| Task | Prompt | Schedule |
|------|--------|----------|
| Morning brief | (contents of `scheduled-tasks/morning-brief.md`) | 8:00am Mon–Fri |
| EOD nudge | (contents of `scheduled-tasks/eod-nudge.md`) | 5:30pm Mon–Fri |
| Weekly pulse | (contents of `scheduled-tasks/weekly-pulse.md`) | 8:00am Monday |
| Pre-meeting brief | (contents of `scheduled-tasks/pre-meeting-brief.md`) | Every 15 min, 7:30–18:00 Mon–Fri |

---

## Updating

- **New BDM joins**: add to BDM Directory Notion page. All projects pick it up on next run.
- **Improving a skill**: edit the skill file here and re-upload to all projects.
- **Project instructions change**: update `project-instructions.md` and re-paste for each BDM.
- **Brain Health suggestions**: reviewed by Adam weekly (Fridays). Tom reviews monthly.

---

## Notion pages to create before setup

Layer 1 (shared teamspace — all BDMs access these):
- BDM Directory
- Shared Activity Log
- Broker Ownership
- Brain Health Log
- Sales Playbook (may already exist)
- Broker Tiers (may already exist)

Layer 2 (each BDM's own space — one set per person):
- My Accounts
- My Commitments
- My Shortcuts
- My Development Focus
