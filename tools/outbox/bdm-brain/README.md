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

Session logs are written to a local `logs/` directory, not Notion.
This requires the filesystem MCP server in Claude desktop.

In Claude desktop settings → MCP servers, add:

```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/path/to/bdm-brain/logs"
    ]
  }
}
```

Replace `/path/to/bdm-brain/logs` with the actual path where logs should live.
All BDM projects on this machine share the same `logs/` root — subdirectories
are namespaced by BDM name (`logs/matt-lees/`, `logs/alex-dyball/`, etc.).

The filesystem server only needs read+write access to the `logs/` directory.
Do not give it access to broader paths.

---

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
- My Accounts (this BDM's page)
- My Commitments (this BDM's page)
- My Shortcuts (this BDM's page)
- My Development Focus (this BDM's page)

Note: Brain Health Log is no longer a Notion page — observability data lives
in local `logs/` files. See Step 1.5.

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
Session → /session-close → Brain Health Log entry
  (roles used, tool hits/misses, role alignment score, gap, improvement suggestion)

Weekly pulse (Monday) → brain-health deep mode →
  pattern detection across all sessions + BDMs →
  top 3 improvements with specific rewrites →
  Slack to Adam

Adam reviews Friday →
  accept / reject suggestions →
  apply accepted changes to skill files →
  re-upload to all projects
```

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

Layer 1 (shared teamspace — all BDMs access these):
- BDM Directory
- Shared Activity Log
- Broker Ownership
- Sales Playbook (may already exist)
- Broker Tiers (may already exist)

Observability: no Notion page needed — logs live in local `logs/` directory (Step 1.5)

Layer 2 (each BDM's own space — one set per person):
- My Accounts
- My Commitments
- My Shortcuts
- My Development Focus
