---
name: flock-deck-builder
description: >
  Creates a branded Flock presentation (.pptx) and saves it to Google Drive (Flock / Presentations folder).
  Use this skill whenever the user wants to create a presentation, deck, slides, or pitch — especially for
  Flock internal or customer-facing decks. Trigger on: "create a presentation", "make slides", "build a deck",
  "put together a pitch", "make a [topic] presentation", "create slides for [audience]", "safety review slides",
  "broker deck", "board update". The skill handles everything: clarifying the brief, building the slides in
  Flock brand style, and uploading to Google Drive. Do NOT use for presentations being built in other tools
  (Google Slides, Canva, etc.) — this skill outputs .pptx files only.
---

# Flock Presentation Creator

Creates polished, on-brand Flock presentations. Dark backgrounds, sharp yellow accents,
bold all-caps typography. Every deck looks like it came from Flock's design team.

**Audience guides in `references/`:**
- `references/audience-broker.md` — broker / MGA decks
- `references/audience-fleet-customer.md` — customer safety reviews and fleet pitches
- `references/audience-board.md` — board, exec team, investor updates
- `references/brand.md` — colours, fonts, logo placement, slide code templates

---

## Step 1 — Clarify the Brief

Before writing any code, gather everything needed. Use `AskUserQuestion` for a structured
experience. Do NOT ask for things already provided in the user's message. Aim to resolve
everything within 1–2 rounds of questions.

**Information needed:**

1. **Audience type** — broker, fleet customer (safety review or pitch), board/exec, or other?
2. **Topic & purpose** — what is this presentation about and what should it achieve?
3. **Key data / messages** — any specific stats, claims, or facts to include?
4. **Rough length** — how many slides? (suggest 8–12 if unsure)

**Once you know the audience type, read the matching guide:**

```
Broker:         Read: references/audience-broker.md
Fleet customer: Read: references/audience-fleet-customer.md
Board:          Read: references/audience-board.md
```

The audience guide contains: the right tone, a recommended slide structure, key messages
to land, data to request, and things to watch out for. Use it to inform Step 2.

---

## Step 2 — Present the Brief and Get Confirmation

**REQUIRED. Do not skip or merge with Step 3.**

Show the user a structured brief before writing a single line of code. This is their
chance to correct anything before you commit.

Present in this exact format:

---
**📋 PRESENTATION BRIEF**

**Title:** [proposed deck title in ALLCAPS style]
**Audience:** [who will see this — be specific, e.g. "Fleet manager at Midlands Couriers"]
**Goal:** [what it needs to achieve — one sentence]
**Tone:** [e.g. "direct and data-led" / "partnership-focused, commercially sharp"]

**Slide plan:**
| # | Slide type | Title | What it will contain |
|---|-----------|-------|----------------------|
| 1 | Cover | [TITLE] | Client/topic name, date, "CONFIDENTIAL \| FLOCKCOVER.COM" |
| 2 | ... | ... | ... |

**Copy & data I'll use:**
- [List each specific claim, stat, or fact — e.g. "Urban speeding rate: 8.3%"]
- [Confirm real data provided by the user]
- [Flag any assumptions or placeholders — e.g. "⚠️ Placeholder: no claims data provided, will use illustrative figures"]

**Things to be aware of:**
- [Caveats — e.g. "Replace illustrative figures with actual data before sending to customer"]
- [Any missing data the user should supply]

---

End with: *"Does this look right? Let me know if you want to change anything before I build it."*

Wait for explicit confirmation ("yes", "looks good", "go ahead") before proceeding.
If changes are requested, update the brief and confirm again before building.

---

## Step 3 — Build the Presentation

### Setup

Read the PptxGenJS guide before writing any code:
```bash
# Check if pptxgenjs guide exists in the skills directory:
ls .claude/skills/pptx/pptxgenjs.md 2>/dev/null || echo "No local guide — refer to PptxGenJS npm docs"
```

Also read brand guidelines for exact positions, font sizes, and copy-paste slide code:
```
Read: references/brand.md
```

Install PptxGenJS if needed:
```bash
npm install -g pptxgenjs 2>/dev/null
```

Write the Node.js script to: `/tmp/create_presentation.js`

Output the .pptx to: the `outbox/` folder in the repo root, e.g. `outbox/midlands-couriers-safety-review-2026-03-05.pptx`
(kebab-case title, date-suffixed)


### Logo asset path

Set at the top of every script:

```javascript
const path = require('path');
const ASSETS = path.resolve(__dirname, '../../.claude/skills/flock-deck-builder/assets');
// Fallback: find the repo root from git
// const ASSETS = require('child_process').execSync('git rev-parse --show-toplevel').toString().trim() + '/.claude/skills/flock-deck-builder/assets';
```

Confirm logo present before running:
```bash
ls .claude/skills/flock-deck-builder/assets/
```

### Non-negotiable slide rules (apply to EVERY slide)

1. `pptx.layout = 'LAYOUT_16x9'` — set this BEFORE adding any slides. All coordinates assume 10"×5.625". `LAYOUT_WIDE` (13.333"×7.5") will make content look cramped in the top-left corner.
2. `slide.background = { color: "19282D" }` — dark background, no exceptions
3. Logo on every slide — **flock-logo-yellow.png is 444×75px (5.92:1 ratio), use exact dimensions below or it will distort:**
   - Cover → bottom-left `(x:0.378, y:4.908, w:1.48, h:0.251)`
   - All others → top-right `(x:9.2, y:0.16, w:0.65, h:0.110)`
4. ALL CAPS — every title, heading, and label
5. Fonts: Roboto Condensed (headings), Roboto (body), Roboto Mono (numbers/dates only)
6. Hero stat numbers: `F6F404` yellow **ALWAYS** — never red, never green
7. LEFT-ALIGN everything — `align: "left"`, starting at `x: 0.276`
8. Never use `#` prefix on hex colour values (breaks PptxGenJS)

See `references/brand.md` for complete slide templates with copy-paste code.

### Run the script

```bash
node /tmp/create_presentation.js
```

---

## Step 4 — QA the Slides

### Text check
```bash
python -m markitdown /path/to/output.pptx
```
Verify: all content present, no placeholder text, correct slide order.

### Visual check
Convert to images and inspect each slide:

```bash
# Convert to PDF for visual review (requires LibreOffice):
libreoffice --headless --convert-to pdf /path/to/output.pptx --outdir /tmp/ 2>/dev/null
rm -f /tmp/slide-*.jpg
pdftoppm -jpeg -r 150 /tmp/output.pdf /tmp/slide
ls /tmp/slide-*.jpg
```

Check every slide for:
- Text overflow or cutoff
- Overlapping elements
- Missing logo
- Stats numbers in wrong colour (must be yellow `F6F404`, not red/green)
- Currency values (£) wrapping to two lines — if so, reduce font size or increase box width
- Centred titles (must be left-aligned at x=0.276)
- Any leftover placeholder text

Fix all issues before uploading.

---

## Step 5 — Upload to Google Drive

Use the browser tools to upload the finished file.

1. Navigate to: `https://drive.google.com`
2. Find the `Flock / Presentations` folder (check left sidebar or search)
3. Click `+ New` → `File upload` → select the .pptx file
4. Wait for upload to complete
5. Confirm to the user: file saved to Google Drive, provide the filename

> **If Google Drive is not accessible:** provide a `computer://` link to the local file
> so the user can open it directly, and note they can upload manually.

---

## Quality Bar

Flock presentations are shown to customers, brokers, and boards. Standards are high:

- **Confident** — bold statements, not hedged language
- **Data-led** — every claim backed by a number
- **Concise** — one key idea per slide; split rather than cram
- **Premium** — design signals quality; sloppy layouts are not acceptable

If the content feels thin or generic, ask the user for specifics. A 8-slide deck
with strong content beats a 15-slide deck with filler.
