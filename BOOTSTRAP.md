# Bootstrap: Head of AI Operating System

This is a one-time setup prompt. Paste this into Claude Code in an empty git repo to scaffold the vault.

## What to build

Scaffold a markdown-native personal operating system for a Head of AI role. The CLAUDE.md file in this repo is the operating manual — read it first, then create everything it describes.

## Step 1: Folder structure

Create the following directories (with .gitkeep files so they survive git):

```
inbox/
domains/engineering-workflows/
domains/operational-tooling/
domains/product-ai/
domains/ai-enablement/
initiatives/
decisions/
meetings/
people/
reviews/
reference/templates/
.claude/skills/
.obsidian/
```

## Step 2: Root files

Create these files at the repo root:

### AGENTS.md
Compact version of CLAUDE.md for non-Claude agents (Copilot, Cursor, Codex, Windsurf). Include:
- One-paragraph summary of what this vault is
- The folder structure and what each directory contains
- The frontmatter conventions (fields, allowed values)
- Wikilink convention
- Pointer to WORKING.md as the starting point and MANIFEST.md for navigation

### WORKING.md
Session crash buffer. Initial content:
- Current task: "Vault just initialised"
- Context: "Scaffolded on [today's date]. No initiatives, decisions, or meetings captured yet."
- Next steps checklist: map existing AI initiatives, set up git remote, configure QMD for local search, first /morning brief after a few days of content

### MANIFEST.md
Auto-generated vault index. Initial content: section headers for each domain and each type (initiatives, decisions, meetings, reviews, people, reference) with "_No notes yet._" under each. Include a "Recent (last 7 days)" section. Add a note at the top: "Auto-generated. Rebuild with /manifest. Last updated: [today's date]."

### README.md
Brief repo README covering:
- What this is (one sentence)
- Quick start: open in Claude Code, available slash commands
- Design principles: markdown is truth, git is the database, AI is collaborator not dependency, structure follows need, link liberally
- Viewing options: VS Code + Foam (primary), Obsidian (mobile), Quartz (browser with auth)
- Tools: QMD for local search, Claude Code for agentic operations

### .gitignore
Ignore: .obsidian/workspace.json, .obsidian/workspace-mobile.json, .obsidian/graph.json, .DS_Store, Thumbs.db, .qmd/, node_modules/, .quartz-cache/, public/, *.swp, *.swo, *~

### .obsidian/app.json
Minimal Obsidian config: livePreview true, useMarkdownLinks false, newLinkFormat "shortest", showFrontmatter false.

## Step 3: Templates

Create these in `reference/templates/`:

### meeting.md
Frontmatter: title, created, updated, domain, type (meeting), tags, attendees. Body sections: Context (one sentence why), Notes, Decisions, Actions (checkboxes with owner and due date), Links.

### person.md
Frontmatter: title, created, updated, type (person), role, team, tags. Body sections: Role, Team, Relationship type (stakeholder/direct report/peer/skip-level/external), Working style notes, 1:1 Log (dated entries).

### initiative.md
Frontmatter: title, created, updated, domain, type (initiative), status, origin (self-started/directed/proposed), owner, tags. Body sections: Summary, Goal, Current state, Dependencies, Risks, Next actions (checkboxes), Log (dated entries).

### decision.md
MADR format. Frontmatter: title (with NNN prefix), created, updated, domain, type (decision), status (accepted/proposed/superseded), tags. Body sections: Context and problem statement, Decision drivers, Considered options (each with Good/Bad because), Decision outcome (chosen option with justification), Consequences, Links.

## Step 4: Skills

Create these in `.claude/skills/`:

### morning.md — /morning
Morning brief. Steps: read WORKING.md, list files modified in last 48h (git log or timestamps), count inbox items, scan active initiatives, check yesterday's meetings for open actions, check if weekly review is due. Output to terminal only (no file created). Format as a brief with sections: Interrupted work, Inbox count, Active initiatives summary, Open actions, Upcoming (review due yes/no).

### manifest.md — /manifest
Rebuild MANIFEST.md. Steps: walk all directories (skip .claude, .git, node_modules, .obsidian), parse frontmatter from each .md file, group by domain then by type, generate recent (last 7 days) section, write to MANIFEST.md with timestamp. Entry format: `- [[filename]] — title (status if applicable)`.

### decision.md — /decision
Create decision record. Steps: find next number by scanning decisions/ folder, ask for or infer title/context/drivers/options/outcome/consequences/domain, create file at decisions/NNN-kebab-title.md using the MADR template.

### initiative.md — /initiative
Create or update initiative. For new: ask for or infer title/owner/domain/status/origin/summary/goal/current-state/dependencies/risks/next-actions, create at initiatives/kebab-title.md. For update: open existing file, update relevant sections, bump updated date, add dated log entry.

### review.md — /review
Weekly review. Steps: determine current ISO week, scan this week's meetings, scan active initiatives for latest log entries, scan this week's decisions, count inbox items, create at reviews/YYYY-WNN.md. Template sections: Three wins (human fills), Domain progress (four subsections), Decisions made, Meetings this week, Open loops, Inbox backlog, Next week focus (human fills), Energy and effectiveness (human fills). Auto-populate what you can, leave reflective sections for the human.

### ingest.md — /ingest
Process inbox. Steps: list inbox files, read each and determine type/domain/destination, present triage plan as a list (source → destination with domain), ask for confirmation before moving, add/update frontmatter on moved files, update links if filenames changed. Rules: never delete, leave vague items with needs-context tag, split multi-topic notes, preserve original creation dates.

## Step 5: Initial commit

Initialise git (if not already), add all files, commit with message: `feat: scaffold head of ai operating system`

## Step 6: Confirm

After scaffolding, run /morning to verify the skills work and show the empty vault state. Then report what was created as a summary.
