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

### Step 1.5 — Configure filesystem MCP server

Session logs live in a `logs/` directory **inside the project folder on Google Drive**.
Google Drive for Desktop syncs this to each BDM's machine as a local path, so the
filesystem MCP server reads and writes it like any local directory — but every BDM's
logs are visible from every machine. This is what makes cross-BDM aggregation work
in the weekly pulse without any extra infrastructure.

**Structure:**
```
Google Drive / BDM Brain /         ← the shared project folder
├── logs/
│   ├── matt-lees/                 ← BDM-namespaced subdirectories
│   │   └── 2026-06-16-0800-morning-brief.md
│   ├── alex-dyball/
│   │   └── 2026-06-16-0800-morning-brief.md
│   └── weekly-summary-2026-W25.md
├── skills/                        ← skill files (same ones in project knowledge)
└── project-instructions.md
```

**Find your synced path:**

| OS | Typical path |
|----|-------------|
| macOS (Drive for Desktop) | `~/Library/CloudStorage/GoogleDrive-[email]/My Drive/BDM Brain` |
| macOS (older Backup & Sync) | `~/Google Drive/BDM Brain` |
| Windows | `G:\My Drive\BDM Brain` (or whichever letter Drive mounts on) |

In Claude desktop settings → MCP servers, add:

```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/path/to/Google Drive/BDM Brain/logs"
    ]
  }
}
```

Replace the path with your actual synced Drive path from the table above.
The filesystem server only needs access to the `logs/` subdirectory — scope it tightly.

**One config per machine.** Each BDM sets this up once on their own machine, pointing at
the same Google Drive path. Because Drive sync keeps the folder in sync, the weekly pulse
deep mode can glob `logs/**/*.md` and see every BDM's session logs — not just its own.

---

### Step 2 — Add project instructions

Copy `project-instructions.md` into the project instructions field.
Replace every `[BDM_NAME]`, `[SLACK_HANDLE]`, `[EMAIL]` placeholder.

### Step 3 — Add project knowledge

Upload every file in `skills/` to project knowledge.
Skill files must be named exactly as they appear here — the project instructions
reference them by name.

Also add the following Notion pages to project knowledge (paste links):
- BDM Directory (read dynamically via MCP — do not snapshot, it must stay live)
- Shared Activity Log
- Sales Playbook
- Broker Tiers
- OKRs (current quarter)
- My Accounts (this BDM's page)
- My Commitments (this BDM's page)
- My Shortcuts (this BDM's page)
- My Development Focus (this BDM's page)

Notes:
- BDM Directory must be read via Notion MCP at session time, not as a static file —
  it needs to reflect additions (new BDM joins) without requiring project re-setup.
- Broker Ownership is not needed — HubSpot is the ownership oracle.
  If a broker isn't in HubSpot, the EOD nudge flags it for the BDM to add.
- Observability logs live in Google Drive / BDM Brain / logs/ — see Step 1.5.

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

## Observability — the self-improving loop

Every session ends with `/session-close`. The agent writes a structured entry to the
Brain Health Log in Notion. The Monday weekly pulse reads all entries from the week,
detects patterns, generates ranked improvement suggestions with specific skill file
rewrites, and Slacks Adam.

```
Session → /session-close → logs/[bdm-name]/YYYY-MM-DD-HHMM-[type].md
  written to Google Drive / BDM Brain / logs/
  Drive sync pushes to all machines automatically

Weekly pulse (Monday, any BDM's project) → brain-health deep mode →
  reads logs/**/*.md via filesystem MCP (Drive-synced, sees all BDMs) →
  pattern detection across all sessions + BDMs →
  top 3 improvements with specific rewrites →
  writes logs/weekly-summary-YYYY-WNN.md →
  Slacks Adam

Adam reviews Friday →
  opens logs/weekly-summary-YYYY-WNN.md →
  accepts / rejects suggestions →
  updates status: in session log files →
  accepted → Tom applies to skill files → re-uploads to all projects
```

Drive sync is the only infrastructure required for cross-BDM aggregation.
No admin project, no shared server, no extra tooling.

**Log directory layout:**

```
logs/
├── matt-lees/
│   ├── 2026-06-16-0800-morning-brief.md
│   ├── 2026-06-16-1430-granola.md
│   └── 2026-06-16-1745-eod-nudge.md
├── alex-dyball/
│   └── 2026-06-16-0800-morning-brief.md
└── weekly-summary-2026-W25.md
```

Each session log is a markdown file with YAML frontmatter (date, bdm, session_type,
scores, gap_type, improvement_applies_to, status) and a structured body.
Weekly summaries aggregate across all BDMs.

**Requires:** filesystem MCP server configured in Claude desktop, pointed at the
`logs/` directory (or its parent). See Step 1.5 in setup below.

**What Adam looks for on Friday:**
- Open `logs/weekly-summary-YYYY-WNN.md` — the ranked improvements are there
- Accept or reject each suggestion; update `status:` in the relevant session log file
- Any data gaps (broker missing from HubSpot, stale Notion page) — assign to fix
- Any "Tom to decide" suggestions — flag for next session

**What Tom looks for monthly:**
- Accepted suggestions: have they been applied to skill files and re-uploaded to projects?
- Recurring improvement types: same gap category persisting after fixes = deeper design issue
- Role distribution across session logs: unused roles may be undiscoverable or genuinely unneeded

---

## Updating

- **New BDM joins**: add to BDM Directory Notion page. All projects pick it up on next run.
- **Improving a skill**: edit the skill file here and re-upload to all projects.
- **Project instructions change**: update `project-instructions.md` and re-paste for each BDM.
- **Brain Health suggestions**: reviewed by Adam weekly (Fridays). Tom reviews monthly.

---

## Notion pages to create before setup

Layer 1 (shared Notion teamspace — all BDMs access these):
- BDM Directory
- Shared Activity Log
- Sales Playbook (may already exist)
- Broker Tiers (may already exist)

Not needed:
- Broker Ownership — HubSpot is the ownership oracle; this page is redundant
- Brain Health Log — observability lives in Google Drive / BDM Brain / logs/ (Step 1.5)

Layer 2 (each BDM's own space — one set per person):
- My Accounts
- My Commitments
- My Shortcuts
- My Development Focus
