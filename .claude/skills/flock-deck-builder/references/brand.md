# Flock Brand Guidelines for Presentations

> These guidelines are derived from Flock's actual master presentations. Follow them exactly.

---

## Colour Palette

| Name              | Hex       | Usage                                                       |
|-------------------|-----------|-------------------------------------------------------------|
| Flock Dark        | `19282D`  | **Slide background** — every slide, no exceptions          |
| Flock Yellow      | `F6F404`  | **Primary accent** — hero stats, agenda numbers, logo      |
| White             | `FFFFFF`  | Headings, body text on dark background                      |
| Light Grey        | `E4E3DD`  | Secondary body text, stat labels, subtle UI elements        |
| Charcoal          | `3B484C`  | Card/panel backgrounds (raised panels on dark bg)           |
| Mid Grey          | `BCBBB8`  | Captions, footnotes, footer text                            |
| Green             | `19A84F`  | Positive directional signals ONLY ("▲ -15%")               |
| Red               | `F43D26`  | Risk badges and negative directional signals ONLY           |
| Orange            | `FF922E`  | Caution/warning signals only                                |

### ⚠️ CRITICAL: Stats Colour Rule

**Large hero numbers on stats slides = `F6F404` (yellow) or `FFFFFF` (white). NEVER red or green.**

Red/green/orange are signal colours only. They belong on small directional badges below stat labels,
not on the large primary number itself. If your slide shows:

```
47          +18%          £245K
CLAIMS      YoY INC       TOTAL LOSSES
```

All three hero numbers use `F6F404` yellow. To convey direction, add a small red badge below the
label — e.g. `▲ ABOVE TARGET` in red. Do not colour the number itself.

---

## Logo

Two logo variants are bundled in `assets/`:

| File | Use when |
|------|----------|
| `assets/flock-logo-yellow.png` | On dark backgrounds (`19282D`) — all slides |
| `assets/flock-logo-dark.png` | On light backgrounds (not used in standard decks) |

### Logo placement — exact positions from master file

**Cover slide** — logo at bottom-left, near footer:
```javascript
slide.addImage({
  path: path.join(ASSETS, 'flock-logo-yellow.png'),
  x: 0.378, y: 4.908, w: 1.48, h: 0.251
});
```

**Every other slide** — logo, top-right corner:
```javascript
// flock-logo-yellow.png is 444×75px → aspect ratio 5.92:1
// w=0.65", h=0.65/5.92=0.110" — correct proportions
slide.addImage({
  path: path.join(ASSETS, 'flock-logo-yellow.png'),
  x: 9.2, y: 0.16, w: 0.65, h: 0.110
});
```

**The logo must appear on every single slide. Do not skip it.**

Setup at the top of your script:
```javascript
const path = require('path');
const ASSETS = path.resolve(__dirname, 'assets');
// Use path.join(ASSETS, 'flock-logo-yellow.png') for every addImage call

// ⚠️ CRITICAL: Set layout BEFORE adding slides. All coordinates below assume 10" × 5.625".
// LAYOUT_16x9 = 10" × 5.625"  ← USE THIS
// LAYOUT_WIDE = 13.333" × 7.5" ← DO NOT USE — different scale, everything will look off
const pptx = new PptxGenJS();
pptx.layout = 'LAYOUT_16x9'; // 10" × 5.625"
```

---

## Typography

| Element               | Font              | Size     | Style              | Colour         |
|-----------------------|-------------------|----------|--------------------|----------------|
| Slide title           | Roboto Condensed  | 20–28pt  | BOLD, ALL CAPS     | `FFFFFF`       |
| Section break title   | Roboto Condensed  | 40–52pt  | BOLD, ALL CAPS     | `FFFFFF` + `F6F404` for punchline |
| Section header        | Roboto Condensed  | 20–24pt  | BOLD, ALL CAPS     | `FFFFFF`        |
| Body text             | Roboto            | 11–13pt  | Regular            | `E4E3DD`       |
| Stat / large number   | Roboto Mono       | 44–64pt  | BOLD               | `F6F404` — always yellow |
| Stat label            | Roboto Condensed  | 11pt     | Regular, ALL CAPS  | `E4E3DD`        |
| Date / small label    | Roboto Mono       | 8–9pt    | Regular            | `E4E3DD`        |
| Caption / footnote    | Roboto            | 9–10pt   | Regular            | `BCBBB8`        |
| Agenda number         | Roboto Mono       | 20pt     | Bold               | `F6F404`        |
| Agenda item           | Roboto Condensed  | 20pt     | Bold, ALL CAPS     | `FFFFFF`        |
| Footer                | Roboto            | 8pt      | Regular            | `BCBBB8`        |

### Font rules
- **ALL CAPS for all headings, titles, labels** — no sentence case, no title case
- Use `charSpacing: 2` on all ALL CAPS text
- Roboto Condensed = headings, labels, titles
- Roboto = body paragraphs, descriptions
- Roboto Mono = numbers, dates, data metrics only — not for body text
- Fallback: Arial (but Roboto is strongly preferred)

---

## Slide Templates

### 1. Cover Slide

**The title is LEFT-ALIGNED and occupies the left ~60% of the slide.** The right 40% is dark
breathing space — this creates a premium, editorial feel. Do NOT centre the title.

```
Slide dimensions: 10" × 5.625"

y=0.236  x=0.276  "MAR 2026"  — Roboto Mono, 8pt, E4E3DD
y=2.148  x=0.276  [TITLE]     — Roboto Condensed, 35pt, BOLD, FFFFFF, w=5.745"
y=4.908  x=0.378  [LOGO]      — flock-logo-yellow.png, 1.48" wide
y=5.28   x=0.276  "CONFIDENTIAL | FLOCKCOVER.COM" — Roboto, 8pt, BCBBB8
```

```javascript
slide.background = { color: "19282D" };

// Date
slide.addText("MAR 2026", {
  x: 0.276, y: 0.236, w: 3, h: 0.3,
  fontFace: "Roboto Mono", fontSize: 8, color: "E4E3DD", margin: 0
});

// Title — LEFT aligned, NOT centred, stays within left 5.745"
slide.addText("IMPROVING FLEET SAFETY\nTO REDUCE TOTAL COSTS", {
  x: 0.276, y: 2.148, w: 5.745, h: 1.065,
  fontFace: "Roboto Condensed", fontSize: 35, bold: true,
  color: "FFFFFF", align: "left", valign: "middle", charSpacing: 2, margin: 0
});

// Logo — bottom left
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 0.378, y: 4.908, w: 1.48, h: 0.251 });

// Footer
slide.addText("CONFIDENTIAL | FLOCKCOVER.COM", {
  x: 0.276, y: 5.28, w: 5, h: 0.25,
  fontFace: "Roboto", fontSize: 8, color: "BCBBB8", align: "left", margin: 0
});
```

---

### 2. Agenda Slide

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

slide.addText("AGENDA", {
  x: 0.276, y: 0.35, w: 9, h: 0.55,
  fontFace: "Roboto Condensed", fontSize: 24, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// Items — stacked rows starting y=1.1, each ~0.7" tall
const agendaItems = ["THE TOTAL COST OF RUNNING A FLEET", "THE BUSINESS CASE FOR IMPROVING SAFETY", "THE IMPACT OF SAFETY ON COST"];
agendaItems.forEach((item, i) => {
  const rowY = 1.1 + (i * 0.75);
  // Number
  slide.addText(String(i + 1), {
    x: 0.276, y: rowY, w: 0.6, h: 0.55,
    fontFace: "Roboto Mono", fontSize: 20, bold: true, color: "F6F404", align: "left", margin: 0
  });
  // Item text
  slide.addText(item, {
    x: 1.0, y: rowY, w: 8.5, h: 0.55,
    fontFace: "Roboto Condensed", fontSize: 20, bold: true,
    color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
  });
});
```

---

### 3. Section Break Slide

Bold statement slide between major sections. Key phrase on last line in yellow.

⚠️ **Control line breaks explicitly with `\n` inside the text strings.** At 48pt, long phrases will wrap unpredictably — e.g. "TELEMATICS IS HOW YOU STAY AHEAD." breaks so "AHEAD." sits alone on a third line. Force breaks where you want them: `"TELEMATICS IS HOW\nYOU STAY AHEAD."`.

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

slide.addText([
  { text: "WHEN SAFETY IMPROVES,\n", options: { color: "FFFFFF" } },
  { text: "FLEET COSTS FALL.", options: { color: "F6F404" } }
], {
  x: 0.276, y: 1.2, w: 9.4, h: 3.4,
  fontFace: "Roboto Condensed", fontSize: 48, bold: true,
  align: "left", valign: "middle", charSpacing: 2
});
```

---

### 4. Content Slide

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

// Title — left aligned, ALL CAPS, 20pt
slide.addText("SLIDE TITLE IN ALL CAPS", {
  x: 0.276, y: 0.35, w: 9, h: 0.55,
  fontFace: "Roboto Condensed", fontSize: 20, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// Body text — Roboto, E4E3DD, 12pt, left aligned
slide.addText([
  { text: "First bullet point", options: { bullet: true, breakLine: true } },
  { text: "Second bullet point", options: { bullet: true, breakLine: true } },
  { text: "Third bullet point", options: { bullet: true } }
], {
  x: 0.276, y: 1.1, w: 9.4, h: 4.0,
  fontFace: "Roboto", fontSize: 12, color: "E4E3DD", align: "left"
});
```

**Two-column variant — full pattern:**

⚠️ **Left column dead space is a common mistake.** Two paragraphs of 12pt body text only fills ~1.2" of a 3.5" tall text box. Always anchor the bottom of the left column with a yellow rule + stat or pull quote. The right card should run the full content height.

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

slide.addText("SLIDE TITLE IN ALL CAPS", {
  x: 0.276, y: 0.35, w: 9, h: 0.55,
  fontFace: "Roboto Condensed", fontSize: 20, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// LEFT column — body text (13pt fills space better than 12pt)
slide.addText("Body text goes here. Use 13pt to fill the column more naturally.", {
  x: 0.276, y: 1.0, w: 4.6, h: 2.0,
  fontFace: "Roboto", fontSize: 13, color: "E4E3DD",
  align: "left", valign: "top"
});

// Yellow rule — anchors the left column visually
slide.addShape(pptx.ShapeType.rect, {
  x: 0.276, y: 3.2, w: 4.6, h: 0.03,
  fill: { color: "F6F404" }, line: { width: 0 }
});

// Stat anchor — bottom-left (prevents dead space below body text)
slide.addText("352", {
  x: 0.276, y: 3.35, w: 1.3, h: 0.9,
  fontFace: "Roboto Mono", fontSize: 52, bold: true,
  color: "F6F404", align: "left", valign: "middle", margin: 0
});
slide.addText("ACTIVE FLOCK\nFLEETS TRACKED TODAY", {
  x: 1.65, y: 3.45, w: 3.1, h: 0.75,
  fontFace: "Roboto Condensed", fontSize: 11,
  color: "E4E3DD", align: "left", charSpacing: 2, valign: "middle", margin: 0
});

// RIGHT column — charcoal card, full content height (y=1.0 to y=5.25)
slide.addShape(pptx.ShapeType.rect, {
  x: 5.3, y: 1.0, w: 4.4, h: 4.25,
  fill: { color: "3B484C" }, line: { width: 0 }
});

// Card header in yellow
slide.addText("CARD HEADING", {
  x: 5.5, y: 1.15, w: 4.0, h: 0.4,
  fontFace: "Roboto Condensed", fontSize: 11, bold: true,
  color: "F6F404", align: "left", charSpacing: 2, margin: 0
});

// Card rows — 6 items at 0.58" spacing fits full card height
const items = [["LABEL", "Description text"]]; // extend as needed
items.forEach(([label, desc], i) => {
  const y = 1.65 + (i * 0.58);
  slide.addText("—", { x: 5.5, y, w: 0.3, h: 0.4, fontFace: "Roboto Mono", fontSize: 10, color: "F6F404", align: "left", margin: 0 });
  slide.addText(label, { x: 5.82, y, w: 1.5, h: 0.4, fontFace: "Roboto Condensed", fontSize: 10, bold: true, color: "FFFFFF", align: "left", margin: 0 });
  slide.addText(desc, { x: 7.35, y, w: 2.15, h: 0.4, fontFace: "Roboto", fontSize: 10, color: "E4E3DD", align: "left", margin: 0 });
});
```

**Column positions summary:**
```
Left (text + anchor):  x=0.276, w=4.6
Right (card):          x=5.3,   w=4.4, y=1.0, h=4.25
```

---

### 5. Stats / Proof Points Slide

**TEXT BOX WIDTH IS CRITICAL.** Numbers with currency symbols or % signs wrap onto new lines
if the box is too narrow. Choose font size based on value length:

| Value type | Example | Font size | Min box width |
|-----------|---------|-----------|---------------|
| Short number | `47` | 64pt | 2.8" |
| Percentage  | `+18%` | 56pt | 3.0" |
| Short currency | `£245K` | 52pt | 3.2" |
| Long currency | `£1.25M` | 44pt | 3.2" |

Use a helper function to ensure consistency:

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

slide.addText("CLAIMS FREQUENCY: CURRENT STATE", {
  x: 0.276, y: 0.35, w: 9, h: 0.55,
  fontFace: "Roboto Condensed", fontSize: 20, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// Stat block helper — call once per stat
// Block is vertically centred between title (y≈0.9) and footnote (y≈5.18)
// Padding above ≈0.6", padding below ≈0.68" — equal visual weight top and bottom
function addStat(slide, x, value, label, fontSize) {
  const NUM_Y  = 1.5;   // centred: pushed down from 1.1
  const LBL_Y  = 3.6;   // tight below number box
  const W      = 3.2;

  slide.addText(value, {
    x, y: NUM_Y, w: W, h: 2.0,
    fontFace: "Roboto Mono", fontSize, bold: true,
    color: "F6F404",      // ← ALWAYS yellow. Never red, never green.
    align: "center", valign: "middle", margin: 0
  });
  slide.addText(label, {
    x, y: LBL_Y, w: W, h: 0.9,
    fontFace: "Roboto Condensed", fontSize: 11, bold: false,
    color: "E4E3DD", align: "center", charSpacing: 2, margin: 0
  });
}

// 3-stat grid (x positions: 0.3, 3.5, 6.7)
addStat(slide, 0.3, "47",     "CLAIMS THIS YEAR",  64);
addStat(slide, 3.5, "+18%",   "YoY INCREASE",      56);
addStat(slide, 6.7, "£245K",  "TOTAL LOSSES",      52);  // 52pt — NOT 64 — for currency values
```

---

### 6. Table / Data Slide

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

// Header row: yellow background, dark text
// Body rows: alternating 3B484C / 19282D, light text
// Positive values: 19A84F, Negative: F43D26, Key highlight: F6F404
```

---

### 7. CTA / Close Slide

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

slide.addText("WHAT HAPPENS NEXT", {
  x: 0.276, y: 0.35, w: 9, h: 0.55,
  fontFace: "Roboto Condensed", fontSize: 28, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// 3 numbered steps
const steps = [
  ["PILOT", "We connect your telematics and establish a baseline safety score."],
  ["MEASURE & REVIEW", "Monthly safety reviews show exactly which drivers and routes to focus on."],
  ["FULL ROLLOUT", "Once results are proven, we scale across your full fleet."]
];

steps.forEach(([heading, desc], i) => {
  const rowY = 1.3 + (i * 1.15);
  slide.addText(String(i + 1), {
    x: 0.276, y: rowY, w: 0.6, h: 0.9,
    fontFace: "Roboto Mono", fontSize: 32, bold: true, color: "F6F404", align: "center", valign: "middle", margin: 0
  });
  slide.addText(heading, {
    x: 1.1, y: rowY, w: 8.4, h: 0.35,
    fontFace: "Roboto Condensed", fontSize: 15, bold: true,
    color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
  });
  slide.addText(desc, {
    x: 1.1, y: rowY + 0.38, w: 8.4, h: 0.5,
    fontFace: "Roboto", fontSize: 12, color: "E4E3DD", align: "left", margin: 0
  });
});

// Footer
slide.addText("FLOCKCOVER.COM", {
  x: 0.276, y: 5.3, w: 5, h: 0.25,
  fontFace: "Roboto", fontSize: 9, color: "BCBBB8", align: "left", margin: 0
});
```

---

### 8. Initiative / Detail Slide

Use for roadmap, feature, or initiative breakdowns. Counter badge top-left, two-column layout: problem + hypothesis on the left, data signal + opportunity in a charcoal card on the right.

```javascript
slide.background = { color: "19282D" };
slide.addImage({ path: path.join(ASSETS, 'flock-logo-yellow.png'), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });

// Counter + category label
slide.addText("INITIATIVE 1 OF 5", {
  x: 0.276, y: 0.22, w: 2.5, h: 0.25,
  fontFace: "Roboto Mono", fontSize: 8, color: "F6F404", align: "left", margin: 0
});
slide.addText("TIME IS CRITICAL", {  // or "GROWTH"
  x: 3.0, y: 0.22, w: 3.5, h: 0.25,
  fontFace: "Roboto Condensed", fontSize: 8, color: "BCBBB8",
  align: "left", charSpacing: 2, margin: 0
});

// Slide title
slide.addText("1. INITIATIVE TITLE IN ALL CAPS", {
  x: 0.276, y: 0.55, w: 9.0, h: 0.6,
  fontFace: "Roboto Condensed", fontSize: 20, bold: true,
  color: "FFFFFF", align: "left", charSpacing: 2, margin: 0
});

// LEFT — customer problem
slide.addText("CUSTOMER PROBLEM", {
  x: 0.276, y: 1.35, w: 4.6, h: 0.25,
  fontFace: "Roboto Condensed", fontSize: 8, bold: true,
  color: "F6F404", align: "left", charSpacing: 2, margin: 0
});
slide.addText("One sentence framing the customer pain this initiative solves.", {
  x: 0.276, y: 1.65, w: 4.6, h: 0.55,
  fontFace: "Roboto", fontSize: 11, color: "E4E3DD",
  align: "left", valign: "top", margin: 0
});

// Divider
slide.addShape(pptx.ShapeType.rect, {
  x: 0.276, y: 2.3, w: 4.6, h: 0.025,
  fill: { color: "3B484C" }, line: { width: 0 }
});

// LEFT — hypothesis
slide.addText("HYPOTHESIS", {
  x: 0.276, y: 2.42, w: 4.6, h: 0.25,
  fontFace: "Roboto Condensed", fontSize: 8, bold: true,
  color: "F6F404", align: "left", charSpacing: 2, margin: 0
});
slide.addText("The hypothesis — what we believe, why we believe it, what success looks like.", {
  x: 0.276, y: 2.72, w: 4.6, h: 2.45,
  fontFace: "Roboto", fontSize: 11, color: "E4E3DD",
  align: "left", valign: "top", margin: 0
});

// RIGHT — charcoal card
slide.addShape(pptx.ShapeType.rect, {
  x: 5.2, y: 1.35, w: 4.5, h: 3.82,
  fill: { color: "3B484C" }, line: { width: 0 }
});

// DATA SIGNAL (omit section if no signal available)
slide.addText("DATA SIGNAL", {
  x: 5.4, y: 1.55, w: 4.1, h: 0.25,
  fontFace: "Roboto Condensed", fontSize: 8, bold: true,
  color: "F6F404", align: "left", charSpacing: 2, margin: 0
});
slide.addText("Quantitative evidence supporting the hypothesis.", {
  x: 5.4, y: 1.85, w: 4.1, h: 0.9,
  fontFace: "Roboto", fontSize: 11, color: "E4E3DD",
  align: "left", valign: "top", margin: 0
});

// Separator
slide.addShape(pptx.ShapeType.rect, {
  x: 5.4, y: 2.9, w: 4.1, h: 0.025,
  fill: { color: "19282D" }, line: { width: 0 }
});

// OPPORTUNITY
slide.addText("OPPORTUNITY", {
  x: 5.4, y: 3.05, w: 4.1, h: 0.25,
  fontFace: "Roboto Condensed", fontSize: 8, bold: true,
  color: "F6F404", align: "left", charSpacing: 2, margin: 0
});
slide.addText("What we unlock if the hypothesis is correct.", {
  x: 5.4, y: 3.35, w: 4.1, h: 1.7,
  fontFace: "Roboto", fontSize: 11, color: "E4E3DD",
  align: "left", valign: "top", margin: 0
});
```

**If no data signal exists**, remove that section and expand OPPORTUNITY to fill the card from `y: 1.55` downward.

---

## Design Principles

1. **LEFT-ALIGN everything** — titles, headings, body. Flock does not centre content.
2. **One idea per slide** — split rather than cram
3. **Stats are the hero** — make numbers giant and yellow
4. **Yellow is a spotlight** — one yellow focal point per slide. More = noise.
5. **ALL CAPS for every heading and label** — always, without exception
6. **No decorative lines under titles** — use whitespace
7. **Dark background always** — `19282D` on every slide
8. **Logo on every slide** — bottom-left on cover, top-right on all others
9. **Never centre body copy** — left-align paragraphs and bullet points

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Red/green hero stat numbers | `F6F404` yellow always for large numbers |
| "£245K" wrapping to two lines | Use 52pt (not 64pt) for currency; ensure w≥3.2" |
| Centred slide titles | `align: "left"`, start at `x=0.276` |
| Logo missing on a slide | Add to every single slide — cover: bottom-left, others: top-right |
| Logo distorted / squashed | Use exact ratio: `w:0.65, h:0.110` (top-right) or `w:1.48, h:0.251` (cover). Logo PNG is 444×75px = 5.92:1 — never use square-ish dimensions |
| Sentence-case headings | ALL CAPS — always |
| Wrong layout constant | Use `LAYOUT_16x9` (10"×5.625"). `LAYOUT_WIDE` is 13.333"×7.5" — content will look cramped in top-left of slide |
| Left column dead space on two-column slides | Two paragraphs of 13pt body only fills ~1.2". Add a yellow rule + stat anchor at the bottom; extend the right card to h=4.25 to fill full slide height |
| Section break text wrapping badly | At 48pt, long phrases wrap unpredictably. Always insert explicit `\n` where you want line breaks — never let PptxGenJS decide |
| Stats block floating in top half | Vertically centre the block: numbers at `y:1.5 h:2.0`, labels at `y:3.6 h:0.9`. Equal padding above (~0.6") and below (~0.68") relative to title and footnote |
| `#` prefix on hex colours | Never use `#` — PptxGenJS will corrupt the file |
| 8-char hex for shadows | Use `opacity` property: `shadow: { color: "000000", opacity: 0.15 }` |
| Reusing options objects | Use factory: `const makeShadow = () => ({ type: "outer", ... })` |
