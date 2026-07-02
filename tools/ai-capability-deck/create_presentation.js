const path = require("path");
const PptxGenJS = require("pptxgenjs");

const ASSETS = "/workspaces/pkm/.claude/skills/flock-deck-builder/assets";
const OUT = "/workspaces/pkm/outbox/ai-capability-where-flock-stands-2026-07-02.pptx";

const DARK = "19282D", YELLOW = "F6F404", WHITE = "FFFFFF", GREY = "E4E3DD", CHARCOAL = "3B484C", MID = "BCBBB8";

const pptx = new PptxGenJS();
pptx.layout = "LAYOUT_16x9";

function logoTop(slide) {
  slide.addImage({ path: path.join(ASSETS, "flock-logo-yellow.png"), x: 9.2, y: 0.16, w: 0.65, h: 0.110 });
}
function baseSlide() {
  const s = pptx.addSlide();
  s.background = { color: DARK };
  logoTop(s);
  return s;
}
function addTitle(slide, text, size = 17) {
  slide.addText(text, {
    x: 0.276, y: 0.28, w: 8.7, h: 0.85,
    fontFace: "Roboto Condensed", fontSize: size, bold: true,
    color: WHITE, align: "left", valign: "top", charSpacing: 2, margin: 0,
  });
}

// ---------- Slide 1 - Cover ----------
{
  const s = pptx.addSlide();
  s.background = { color: DARK };
  s.addText("JUL 2026", { x: 0.276, y: 0.236, w: 3, h: 0.3, fontFace: "Roboto Mono", fontSize: 8, color: GREY, margin: 0 });
  s.addText("AI CAPABILITY -\nWHERE FLOCK STANDS", {
    x: 0.276, y: 2.0, w: 5.745, h: 1.5,
    fontFace: "Roboto Condensed", fontSize: 35, bold: true,
    color: WHITE, align: "left", valign: "middle", charSpacing: 2, margin: 0,
  });
  s.addText("THE CAPABILITY BENCHMARK | 50 OF 57 PEOPLE SCORED", {
    x: 0.276, y: 3.6, w: 6.5, h: 0.3,
    fontFace: "Roboto Condensed", fontSize: 12, color: YELLOW, align: "left", charSpacing: 2, margin: 0,
  });
  s.addImage({ path: path.join(ASSETS, "flock-logo-yellow.png"), x: 0.378, y: 4.908, w: 1.48, h: 0.251 });
  s.addText("CONFIDENTIAL | FLOCKCOVER.COM", { x: 0.276, y: 5.28, w: 5, h: 0.25, fontFace: "Roboto", fontSize: 8, color: MID, align: "left", margin: 0 });
  s.addNotes("Deck source: reference/ai-capability-deck-2026-07.md (v3, data as at 2026-07-02). Story in titles: fluency is the centre of gravity - we score behaviour, not talk - almost everyone is past first contact - half the company builds its own tools - BDM and Prodtech lead, Finance and UW are the focus - every team has a champion - the at-risk list is blocked, not unwilling - Q3: unblock, propagate, deputise.");
}

// ---------- Slide 2 - Headline ----------
{
  const s = baseSlide();
  addTitle(s, "THE CENTRE OF GRAVITY IS FLUENCY;\nA QUARTER ALREADY HANDS OFF WHOLE TASKS", 17);
  s.addText([
    { text: "50 of 57 in-scope people scored (88% coverage)", options: { bullet: true, breakLine: true } },
    { text: "The median person is at Stage 3 - argues with output, thinks with the model", options: { bullet: true, breakLine: true } },
    { text: "13 people at Stage 4 (delegation) - nobody yet at Stage 5", options: { bullet: true, breakLine: true } },
    { text: "Only three people sit at Stage 1 - one brand-new starter, two blocked; none unwilling", options: { bullet: true } },
  ], { x: 0.276, y: 1.35, w: 5.0, h: 2.0, fontFace: "Roboto", fontSize: 13, color: GREY, align: "left", valign: "top" });
  s.addShape(pptx.ShapeType.rect, { x: 0.276, y: 3.55, w: 4.6, h: 0.03, fill: { color: YELLOW }, line: { width: 0 } });
  s.addText("50/57", { x: 0.276, y: 3.75, w: 2.6, h: 0.9, fontFace: "Roboto Mono", fontSize: 44, bold: true, color: YELLOW, align: "left", valign: "middle", margin: 0 });
  s.addText("PEOPLE SCORED ON\nONE COMPANY-WIDE RUBRIC", { x: 3.0, y: 3.85, w: 3.0, h: 0.75, fontFace: "Roboto Condensed", fontSize: 11, color: GREY, align: "left", charSpacing: 2, valign: "middle", margin: 0 });
  // right card - the story in titles
  s.addShape(pptx.ShapeType.rect, { x: 5.55, y: 1.35, w: 4.15, h: 3.9, fill: { color: CHARCOAL }, line: { width: 0 } });
  s.addText("THE STORY IN ONE PASS", { x: 5.75, y: 1.5, w: 3.8, h: 0.35, fontFace: "Roboto Condensed", fontSize: 11, bold: true, color: YELLOW, align: "left", charSpacing: 2, margin: 0 });
  const story = [
    "We score behaviour, not talk",
    "Almost everyone is past first contact",
    "Half the company builds its own tools",
    "BDM + Prodtech lead; Finance + UW are the focus",
    "Every team has a champion",
    "The at-risk list is blocked, not unwilling",
    "Q3: unblock, propagate, deputise",
  ];
  story.forEach((t, i) => {
    const y = 1.95 + i * 0.46;
    s.addText("-", { x: 5.75, y, w: 0.3, h: 0.4, fontFace: "Roboto Mono", fontSize: 10, color: YELLOW, align: "left", margin: 0 });
    s.addText(t, { x: 6.07, y, w: 3.5, h: 0.4, fontFace: "Roboto", fontSize: 10.5, color: GREY, align: "left", margin: 0 });
  });
  s.addNotes("Activation framing deliberately removed pending definition alignment with Ed - his verbal shorthand for activated (Jun 24: building tools, bringing in the data) maps to Stage 2-3, not the framework's Stage-1-exit threshold; the definitions give very different numbers (84% vs 57-65% of scope). Realign with Ed before reintroducing. The 7 unscored: 5 underwriting ICs (holiday/paternity/deliberate deferral), Pavel (finance, no signal), Antton (CCO, no 1:1 yet). Denominator caveat: ai-activation-map.md uses ~63 in scope; this deck uses the 56-person June assessment scope - reconcile before Ed forwards numbers to Admiral Pioneer. Do NOT reuse the Jun 24 verbal numbers (90% activated, 75% building tools, 50% at top end) - see slide 4 notes for the honest bridge. Playbook timeline note: three iterations compressed into Jul 2, not skipped.");
}

// ---------- Slide 3 - Framework table ----------
{
  const s = baseSlide();
  addTitle(s, "WE SCORE SIX STAGES OF BEHAVIOUR:\nWHAT PEOPLE DO, NOT WHAT THEY UNDERSTAND", 17);
  const header = [
    { text: "STAGE", options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 10, align: "left" } },
    { text: "NAME", options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 10, align: "left" } },
    { text: "WHAT IT LOOKS LIKE", options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 10, align: "left" } },
    { text: "THE BEHAVIOURS WE CHECK FOR", options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 10, align: "left" } },
  ];
  const rows = [
    ["0", "SEARCH", "Single prompt, read answer, done", "No follow-up or correction; doesn't come back after \"fine but unremarkable\" output"],
    ["1", "FIRST WIN", "Pushes back, iterates, has a conversation", "Gets genuinely useful wins that become a default, not one-offs"],
    ["2", "CONTEXT+TOOLS", "Loads context, connects data sources, dresses the model", "CLAUDE.md / strategy docs / process maps; real systems connected (MCP, files, APIs)"],
    ["3", "FLUENCY", "Argues with output, thinks with the model, builds tools", "\"What are the failure modes?\"; builds on partial output; named, reusable artifacts"],
    ["4", "DELEGATION", "Hands off whole tasks, reviews at output level", "Trusts the agent within constraints; parallel sessions; catches errors via domain knowledge"],
    ["5", "ORCHESTRATION", "Directs systems, measures adherence", "Context quality judged by agent behaviour, not by reading it; composes human/agent/function"],
  ];
  const body = rows.map((r, i) => r.map((c, j) => ({
    text: c,
    options: {
      fill: { color: i % 2 === 0 ? CHARCOAL : DARK },
      color: j === 0 ? YELLOW : j === 1 ? WHITE : GREY,
      bold: j <= 1,
      fontFace: j === 0 ? "Roboto Mono" : j === 1 ? "Roboto Condensed" : "Roboto",
      fontSize: 9.5, align: "left", valign: "middle",
    },
  })));
  s.addTable([header, ...body], { x: 0.276, y: 1.3, w: 9.45, colW: [0.65, 1.5, 3.35, 3.95], border: { type: "none" }, rowH: 0.55, margin: 0.06 });
  s.addText("STAGE / NAME / WHAT-IT-LOOKS-LIKE ARE VERBATIM FROM THE TABLE SHARED 24 JUN", { x: 0.276, y: 5.15, w: 9, h: 0.25, fontFace: "Roboto", fontSize: 9, color: MID, align: "left", margin: 0 });
  s.addNotes("First three columns are verbatim the wording shared with Ed on Jun 24 (reference/framework-stages-shared-with-ed-2026-06-24.png) - he should recognise the table; the fourth column is the expansion. Builds tools sits inside Stage 3's description, so any Stage 3+ claim implies tool-building - see builder-audit caveats. BEHAVIOUR, NOT UNDERSTANDING: the framework scores what people do, not what they grasp - the CEO can score below a junior ops person; this is not a capability ranking - say this out loud before team numbers. Confidence tiers: low = gather more data (low-confidence scores in headline numbers: Michael Matthews, Ben Allen, Daisy Mae; Aleks medium with contested range). Ed's does-it-extend-to-6-7-8 question: Stage 5 is the ceiling and NOBODY currently sits there - Ismael recalibrated 5 to 4 on Jun 30 under sustained-practice standards; Stage 6 deliberately uncharacterised, Ismael is the person to define the frontier. External benchmark gap: Flock-native rubric, can't compare across companies; Ed's aipilled.com anchor ~40-50; AI-125 survey with Rakhee (due Jul 7) is the systematic answer.");
}

// ---------- Slide 4 - Distribution ----------
{
  const s = baseSlide();
  addTitle(s, "ALMOST EVERYONE IS PAST FIRST CONTACT; THE FEW\nAT STAGE 1 ARE NEW OR BLOCKED, NOT UNWILLING", 17);
  const dist = [["STAGE 0", 0], ["STAGE 1", 3], ["STAGE 2", 15], ["STAGE 3", 19], ["STAGE 4", 13], ["STAGE 5", 0]];
  const maxW = 5.4, maxN = 19;
  dist.forEach(([label, n], i) => {
    const y = 1.35 + i * 0.52;
    s.addText(label, { x: 0.276, y, w: 1.0, h: 0.36, fontFace: "Roboto Condensed", fontSize: 11, color: GREY, align: "left", charSpacing: 2, valign: "middle", margin: 0 });
    if (n > 0) {
      s.addShape(pptx.ShapeType.rect, { x: 1.4, y: y + 0.03, w: Math.max(0.12, (n / maxN) * maxW), h: 0.3, fill: { color: i === 3 ? YELLOW : CHARCOAL }, line: { width: 0 } });
    } else {
      s.addText("|", { x: 1.4, y, w: 0.3, h: 0.36, fontFace: "Roboto Mono", fontSize: 12, color: MID, align: "left", valign: "middle", margin: 0 });
    }
    s.addText(String(n), { x: 1.5 + (n / maxN) * maxW, y, w: 0.7, h: 0.36, fontFace: "Roboto Mono", fontSize: 12, bold: true, color: n > 0 ? YELLOW : MID, align: "left", valign: "middle", margin: 0 });
  });
  s.addText("MIN 1  |  MEDIAN 3  |  P80 4.0  |  MAX 4   (N=50 SCORED)", { x: 0.276, y: 4.6, w: 6.6, h: 0.3, fontFace: "Roboto Mono", fontSize: 11, bold: true, color: WHITE, align: "left", margin: 0 });
  s.addText("At Stage 1: Anneliese (install blocked - AI-149) | Queency (daily use, single-shot) | Kaylee (new in claims)", { x: 0.276, y: 4.95, w: 7.2, h: 0.3, fontFace: "Roboto", fontSize: 10, color: MID, align: "left", margin: 0 });
  // right stats
  s.addText("64%", { x: 7.55, y: 1.5, w: 2.1, h: 0.85, fontFace: "Roboto Mono", fontSize: 40, bold: true, color: YELLOW, align: "left", valign: "middle", margin: 0 });
  s.addText("FLUENT OR BETTER\nSTAGE 3+", { x: 7.55, y: 2.35, w: 2.35, h: 0.5, fontFace: "Roboto Condensed", fontSize: 10, color: GREY, align: "left", charSpacing: 2, margin: 0 });
  s.addText("26%", { x: 7.55, y: 3.05, w: 2.1, h: 0.85, fontFace: "Roboto Mono", fontSize: 40, bold: true, color: YELLOW, align: "left", valign: "middle", margin: 0 });
  s.addText("HANDING OFF WHOLE\nTASKS - STAGE 4", { x: 7.55, y: 3.9, w: 2.35, h: 0.5, fontFace: "Roboto Condensed", fontSize: 10, color: GREY, align: "left", charSpacing: 2, margin: 0 });
  s.addNotes("Top fifth = nearest-rank p80: the stage 80% of people sit at or below; company p80=4 means the top fifth is delegating. Jul 2 evidence challenges moved four scores: David Pilley 1 to 3 (Moss environment blocker separated from his Stage-3 dashboard practice); Anneliese briefly 1 to 2 then corrected back to 1 (Jun 1 connector setup was a guided session); Queency 2 to 1 (assisted install + single-shot pattern); Adam Sandle challenged and UPHELD at 2 (telemetry MCP + FNOL skill in real use). BRIDGE FROM JUN 24 CLAIMS: 50% at top end = actually 27% at Stage 4, zero at Stage 5. 90% activated = 96% of scored / 84% of scope; of the nine not counted, seven are unmeasured, two blocked. 75% building tools = 65% Stage 3+ proxy, 51% strict / 71% loose by artifact audit (next slide). Finance+UW lag confirmed (means 2.3/2.5): Finance genuinely broad (1-4), UW tightest cluster (all 2-3). 30% of UW past activation = Finance exactly 30% fluent+, UW actually 50% but zero at Stage 4. 90% there on benchmarking = 49/56 = 87.5%, holds as high-80s. BRIDGE FROM JUN 18 DOC: it said all Engineering+Product at Stage 4+; Jun 30 re-assessment applied sustained-practice-not-spikes standards, pulled 7 of 10 engineers down. The company didn't get worse; the measurement got honest - same standards for the company-wide survey.");
}

// ---------- Slide 5 - Builders ----------
{
  const s = baseSlide();
  addTitle(s, "HALF THE COMPANY BUILDS ITS OWN TOOLS -\nANOTHER FIFTH IS ONE COACHED REP AWAY", 17);
  function stat(x, value, label) {
    s.addText(value, { x, y: 1.45, w: 3.0, h: 1.5, fontFace: "Roboto Mono", fontSize: 56, bold: true, color: YELLOW, align: "center", valign: "middle", margin: 0 });
    s.addText(label, { x, y: 3.0, w: 3.0, h: 0.8, fontFace: "Roboto Condensed", fontSize: 11, color: GREY, align: "center", charSpacing: 2, valign: "top", margin: 0 });
  }
  stat(0.3, "50%", "BUILD INDEPENDENTLY -\nREUSABLE TOOLS IN LIVE USE");
  stat(3.5, "70%", "HAVE BUILT OR CO-BUILT\nAT LEAST ONE SKILL");
  stat(6.7, "30%", "NO ARTIFACT YET");
  s.addText([
    { text: "The middle rung (20%) built something with guidance - Fred's personalised referral skill, Phoebe's Netlify slides, Adam Sandle's FNOL reports", options: { bullet: true, breakLine: true } },
    { text: "Converting that rung to independent builders IS the Q3 enablement plan: coached reps, not more workshops", options: { bullet: true } },
  ], { x: 0.276, y: 4.15, w: 9.4, h: 1.1, fontFace: "Roboto", fontSize: 12, color: GREY, align: "left", valign: "top" });
  s.addNotes("Artifact-level audit, Jul 2: one agent per team verified every claim against people files + transcripts. Rubric: builder = named, reusable artifact they created with AI (skill, dashboard, automation, MCP workflow, app, pipeline) in repeated use. 25 verified / 10 assisted / 14 no-artifact of 49. This is the honest version of the Jun 24 75%-building-tools claim: roughly right under the loose definition (71%), ahead of the evidence under the strict one (51%) - say which definition you mean. The Stage 3+ proxy (65%) over- and under-counts both ways: e.g. Darren McCauley at Stage 3 with no artifact (Jun 22 transcript: pretty much a ChatGPT guy); Milan at Stage 2 with two corroborated skills. Full mismatch list in the builder-audit appendix of the source doc.");
}

// ---------- Slide 6 — Teams ----------
{
  const s = baseSlide();
  addTitle(s, "BDM AND PRODTECH LEAD; FINANCE AND UNDERWRITING\nARE THE Q3 FOCUS - FOR DIFFERENT REASONS", 17);
  const teams = [
    ["DISTRIBUTION (BDM)", 3, 4.0, 4],
    ["PRODTECH", 2, 4.0, 4],
    ["PEOPLE", 2, 3.2, 4],
    ["UNDERWRITING", 2, 3.0, 3],
    ["PRICING", 2, 3.0, 3],
    ["OPERATIONS", 1, 3.0, 4],
    ["FINANCE", 1, 3.0, 4],
  ]; // [name, min, p80 (linear interpolation), max]
  const X0 = 2.05, XW = 1.47, Y0 = 1.72, ROW = 0.51, BARH = 0.13, D = 0.22;
  const sx = (v) => X0 + v * XW;
  for (let v = 0; v <= 5; v++) {
    s.addShape(pptx.ShapeType.line, { x: sx(v), y: 1.5, w: 0, h: 3.62, line: { color: CHARCOAL, width: 0.75 } });
    s.addText("STAGE " + v, { x: sx(v) - 0.55, y: 5.16, w: 1.1, h: 0.22, fontFace: "Roboto Mono", fontSize: 8, color: MID, align: "center", margin: 0 });
  }
  // encoding legend
  s.addShape(pptx.ShapeType.roundRect, { x: 2.05, y: 1.2, w: 0.5, h: 0.11, rectRadius: 0.055, fill: { color: MID }, line: { width: 0 } });
  s.addText("RANGE: MIN TO MAX", { x: 2.65, y: 1.12, w: 1.9, h: 0.26, fontFace: "Roboto Condensed", fontSize: 9, color: MID, align: "left", charSpacing: 1, valign: "middle", margin: 0 });
  s.addShape(pptx.ShapeType.ellipse, { x: 4.75, y: 1.14, w: 0.2, h: 0.2, fill: { color: YELLOW }, line: { color: DARK, width: 2 } });
  s.addText("P80 - 80% OF TEAM AT OR BELOW", { x: 5.05, y: 1.12, w: 3.4, h: 0.26, fontFace: "Roboto Condensed", fontSize: 9, color: MID, align: "left", charSpacing: 1, valign: "middle", margin: 0 });
  teams.forEach(([name, mn, p80, mx], i) => {
    const yC = Y0 + i * ROW;
    s.addText(name, { x: 0.276, y: yC - 0.15, w: 1.72, h: 0.3, fontFace: "Roboto Condensed", fontSize: 10, bold: true, color: GREY, align: "left", charSpacing: 1, valign: "middle", margin: 0 });
    s.addShape(pptx.ShapeType.roundRect, { x: sx(mn), y: yC - BARH / 2, w: sx(mx) - sx(mn), h: BARH, rectRadius: BARH / 2, fill: { color: MID }, line: { width: 0 } });
    s.addShape(pptx.ShapeType.ellipse, { x: sx(p80) - D / 2, y: yC - D / 2, w: D, h: D, fill: { color: YELLOW }, line: { color: DARK, width: 2 } });
    s.addText(p80.toFixed(1), { x: sx(p80) - 0.3, y: yC - 0.37, w: 0.6, h: 0.2, fontFace: "Roboto Mono", fontSize: 8.5, bold: true, color: YELLOW, align: "center", margin: 0 });
  });
  s.addText("FINANCE AND OPERATIONS SPAN THE WHOLE LADDER | NEITHER UNDERWRITING NOR PRICING HAS ANYONE AT DELEGATION YET", { x: 0.276, y: 5.4, w: 9.4, h: 0.2, fontFace: "Roboto", fontSize: 9, color: MID, align: "left", margin: 0 });
  s.addNotes("Small-team caveat: People n=3, top-fifth = max; read the dots. Ed and Tom sit outside the team view by design (confirmed Jul 2); Ed counts in company stats only. Finance is infrastructure-gated: Moss MCP installs, Python-less machines, NetSuite/Looker access - not skill or will (Jun 29/30 meetings are the evidence; both Stage-1s sit here, each one unblock-plus-one-win from Stage 2). UW is propagation-gated: five genuine builders at Stage 3, zero at 4, practice staying private - Darren McCauley secretly all over it, not pushing down; Jake Wood is the bottom-up bridge to the 5 unassessed ICs and Darren Nightingale (number one cynic - do not approach yet). Prodtech: top fifth at 4 with min 2 - 8 of 15 at Stage 4 but a tail of 2s; middle recalibrated down amid craft-loss anxiety (Javier associate factory, Aleks I've learned nothing, Stephen pulling back); intervention = teaching capacity + shared quality infrastructure, not tooling. Antton (CCO) belongs to Operations but is unassessed - their coverage gap. Team labels are the July groupings (Prodtech = Engineering + Product + Fergus); several files still carry Leadership team tags, bucketed by function. Unassessed (not in stats): Darren Nightingale (tent. 0), Andrew Dodd, Curtis Bailey (holiday, 0-1), Billy Bone (paternity, 1), Matt Smith (1, went quiet), Pavel (0, no signal), Antton (1-2). Team shapes: Distribution - nobody below fluency, two agent systems in production. Prodtech - over half at delegation, deep vanguard with a fragile tail. Operations - one star, mixed middle. People - one star, two early. Underwriting - capped at fluency, no stars. Pricing - inverted pyramid, ICs ahead of their heads. Finance - widest spread. Operations - claims folded in Jul 2, incl. new starter Kaylee at 1. (n: Distribution 5, Prodtech 15, People 3, Underwriting 5, Pricing 4, Operations 7, Finance 10.)");
}

// ---------- Slide 7 - Champions ----------
{
  const s = baseSlide();
  addTitle(s, "EVERY TEAM HAS A CHAMPION -\nTWO TEAMS ARE CHAMPIONS", 17);
  const th = (t, w) => ({ text: t, options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 9.5, align: "left" } });
  const header = [th("TEAM"), th("CHAMPION"), th("THE ONE-LINER")];
  const rows = [
    ["DISTRIBUTION (BDM)", "THE WHOLE TEAM", "Nobody below fluency; two agent systems in production - a 9-agent enterprise pipeline and the SLT trading review"],
    ["PRODTECH", "THE STAGE-4 VANGUARD", "8 of 15 delegating: parallel agents writing PRs (Ismael ~90% AI-generated code), test suites, the acquisition brain, production apps"],
    ["OPERATIONS", "SHREYA", "3 production tools built independently; now teaching the method"],
    ["FINANCE", "IVAN", "Daily credit-control skill running 2+ months (Slack nudge); broker-payment dashboard; co-built the NetSuite MCP"],
    ["UNDERWRITING", "JAKE WOOD", "Dashboard drove HubSpot notes 0 to 90%; the peer bridge into underwriting"],
    ["PRICING", "FRANCESCO", "MCP performance coach in weekly 1:1 use; claims-triangle skill; J feedback pipeline"],
    ["PEOPLE", "ERAAZ", "3x/day co:work optimisation system; builds prompts for his own team"],
  ];
  const body = rows.map((r, i) => r.map((c, j) => ({
    text: c,
    options: {
      fill: { color: i % 2 === 0 ? CHARCOAL : DARK },
      color: j === 1 ? (i < 2 ? YELLOW : WHITE) : j === 0 ? WHITE : GREY,
      bold: j === 1,
      fontFace: j === 2 ? "Roboto" : "Roboto Condensed",
      fontSize: 10, align: "left", valign: "middle",
    },
  })));
  s.addTable([header, ...body], { x: 0.276, y: 1.3, w: 9.45, colW: [1.85, 1.95, 5.65], border: { type: "none" }, rowH: 0.48, margin: 0.05 });
  s.addText("ONE NAMED INDIVIDUAL PER TEAM MAX; WHERE MOST OF A TEAM IS AT CHAMPION LEVEL, THE TEAM IS THE CHAMPION", { x: 0.276, y: 5.15, w: 9.4, h: 0.25, fontFace: "Roboto", fontSize: 9, color: MID, align: "left", margin: 0 });
  s.addNotes("Table rule: max one named individual per team; where most of a team is at champion level (BDM, Prodtech's vanguard), the team itself is the champion - the stronger story for Ed (whole teams get there, not just heroes). Full bench (promotion shortlist + deputy pool for the Q3 AI partnering team, AI-127): Jacob, David Z, Fergus, Mima, Ollie, Geran, Matt Price (Prodtech - Ed named Mima on Jun 24 as the promote-the-boundary-pushers example); Matt Lees, Adam Smith (BDM); Kevin (Finance, teaching David Pilley); Emily (Ops); Tom Rogers, Francesco (UW). WATCH FLAGS (over-trust, the company-wide failure mode): Adam Smith presented wrong Claude numbers to SLT (Jun 11), validation still not in place; Tom Rogers promised a customer an unconfirmed feature; David Pilley (Stage 3, Moss unblocked Jun 30) carries Kevin's thinks-it's-magic flag - his 3-to-4 path is review muscle, not more tools. Celebrate the output, install the guardrails.");
}

// ---------- Slide 8 - At-risk ----------
{
  const s = baseSlide();
  addTitle(s, "THE AT-RISK LIST IS BLOCKED OR UNMEASURED,\nNOT UNWILLING", 17);
  const th = (t) => ({ text: t, options: { fill: { color: YELLOW }, color: DARK, bold: true, fontFace: "Roboto Condensed", fontSize: 9.5, align: "left" } });
  const header = [th("TEAM"), th("WHO"), th("WHY")];
  const rows = [
    ["FINANCE", "ANNELIESE | QUEENCY", "Stage 1 - Anneliese: guided setup, install blocked (AI-149), one real win from Stage 2; Queency: daily file-feed use but single-shot, connected Moss unqueried in real work"],
    ["PRODTECH", "STEPHEN | ALEKS", "Recalibrated 4 to 2; pull-back and skill-displacement grief"],
    ["UNDERWRITING", "BEN | DAISY MAE", "Stage 2 on inference only - near-zero individual data (\"Chinese wall of a calendar\")"],
    ["PRICING", "MICHAEL M | MILAN", "Heads of function at Stage 2, \"still not ingrained\" - while their own ICs sit at Stage 3"],
    ["PEOPLE", "RAKHEE | PHOEBE", "Stage 2 - the people coordinating the AI programme trail it; both have live 2-to-3 paths (PGR prompt AI-144, Flock O'Clock AI-141)"],
    ["OPS", "JONNY | FRED | ADAM SANDLE | KAYLEE", "Stages 1-2; guided-only wins; Sandle on fortnightly coaching (AI-131); Kaylee new - heavy personal use, none at work yet"],
  ];
  const body = rows.map((r, i) => r.map((c, j) => ({
    text: c,
    options: {
      fill: { color: i % 2 === 0 ? CHARCOAL : DARK },
      color: j === 0 ? WHITE : j === 1 ? WHITE : GREY,
      bold: j === 0,
      fontFace: j === 2 ? "Roboto" : "Roboto Condensed",
      fontSize: 10, align: "left", valign: "middle",
    },
  })));
  s.addTable([header, ...body], { x: 0.276, y: 1.3, w: 9.45, colW: [1.4, 2.7, 5.35], border: { type: "none" }, rowH: 0.55, margin: 0.05 });
  s.addText("FOUR GROUPS, FOUR INTERVENTIONS: BLOCKED | UNMEASURED | PULLED BACK | HABIT NOT FORMED", { x: 0.276, y: 5.15, w: 9.4, h: 0.25, fontFace: "Roboto", fontSize: 9, color: MID, align: "left", margin: 0 });
  s.addNotes("Nobody on this list is refusing. Four groups, four interventions: BLOCKED (Anneliese - a Python install; Queency - a filtering bug), UNMEASURED (Ben, Daisy - assess before judging), PULLED BACK (Stephen, Aleks - the craft conversation, not pressure), HABIT NOT FORMED (Michael, Milan, Rakhee, Phoebe - coached reps on real work). A single level-up-or-else message would misfire on three of the four groups. Queency downgrade rationale (Jul 2, on Tom's challenge): connected Moss MCP was installed with support; working pattern is single-shot - when Moss returned wrong data she stopped rather than iterated; Stage 2 requires the behaviour, not the tool. Rakhee, checked against Jun 25 meetings: Claude is her primary tool (strategy thought partner, policy review, Alar daily, two Notion trackers) - genuine daily use, but no demonstrated arguing-with-output and every artifact is someone else's (Eraaz builds; she tested the PGR prompt). Hold at 2 high end; decisive test = AI-144 session Mon Jul 6 - if she builds rather than frames-while-Eraaz-builds, that's her 3. Rakhee/Phoebe sensitivity: Eraaz is the in-team fix; Rakhee is the benchmarking-survey partner - position as her programme skills + my practice coaching, not problem children. Open score conflicts (know, don't present): Kirsty 2 on Moss context vs Stage-4 Looker evidence remains valid; Geran frontmatter 4 vs body 3.");
}

// ---------- Slide 9 - Q3 CTA ----------
{
  const s = baseSlide();
  addTitle(s, "Q3: UNBLOCK FINANCE, PROPAGATE UNDERWRITING,\nDEPUTISE THE CHAMPIONS", 17);
  const steps = [
    ["THE BASELINE EXISTS", "49 of 56 scored on one rubric; the remaining tail is 7 named people with dates and owners, not a programme."],
    ["FOCUS ON THE TWO GAP TEAMS", "Finance (unblock infrastructure) and UW (propagate via Jake + peer demos). Monthly team workshops continue; company-wide sessions don't scale."],
    ["DEPUTISE THE CHAMPIONS", "AI partnering team pilot for Q3 - the Ghostbusters model - drawn from the champions table."],
    ["MEASURE OUTCOMES, NOT TOOL USAGE", "Counting skills built is the wrong metric; the benchmarking survey (with Rakhee, this week) gives the baseline, then targets go on the rubric."],
    ["OWN THE QUALITY OF WHAT SHIPS", "The new failure mode is over-trust. Guardrails ship with delegation."],
  ];
  steps.forEach(([heading, desc], i) => {
    const rowY = 1.35 + i * 0.78;
    s.addText(String(i + 1), { x: 0.276, y: rowY, w: 0.5, h: 0.7, fontFace: "Roboto Mono", fontSize: 24, bold: true, color: YELLOW, align: "center", valign: "top", margin: 0 });
    s.addText(heading, { x: 1.0, y: rowY, w: 8.6, h: 0.3, fontFace: "Roboto Condensed", fontSize: 13, bold: true, color: WHITE, align: "left", charSpacing: 2, margin: 0 });
    s.addText(desc, { x: 1.0, y: rowY + 0.3, w: 8.6, h: 0.42, fontFace: "Roboto", fontSize: 10.5, color: GREY, align: "left", margin: 0 });
  });
  s.addText("FLOCKCOVER.COM", { x: 0.276, y: 5.3, w: 5, h: 0.25, fontFace: "Roboto", fontSize: 9, color: MID, align: "left", margin: 0 });
  s.addNotes("Near-term dated commitments (all open): benchmarking survey with Rakhee (AI-125, due Jul 7 - Ed committed this to Admiral Pioneer), new-hire assessment integration (AI-128, Jul 8), AI partnering pilot (AI-127, Jul 1, needs launch), Moss rollout completion (AI-148, Jul 6), Anneliese's Python fix (AI-149, Jul 3), London push on Rob & Javier to 100% AI-assisted (AI-150, Jul 10), Geran finance-metrics session (AI-151, Jul 9). Sweep the past-due items before Ed asks what's blocking finance: AI-045/046 Ed's own Cursor/MCP access from May, AI-056 NetSuite MCP, AI-014 Matt Dipre Looker access. Ed's Jun 24 provocations not answered by this deck (park explicitly if raised): company-wide intensive week, hiring bar (no Copilot-only engineers), firing implications, external speakers. The deck's line: benchmark first, then set the bar.");
}

pptx.writeFile({ fileName: OUT }).then(() => console.log("WROTE " + OUT));
