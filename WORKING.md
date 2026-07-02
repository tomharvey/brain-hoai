# Working

## Current task

AI Capability deck for Ed — iterating. Source of truth: `reference/ai-capability-deck-2026-07.md`. Rendered pptx: `outbox/ai-capability-where-flock-stands-2026-07-02.pptx` (gitignored — regenerate with `node tools/ai-capability-deck/create_presentation.js`; needs `npm i pptxgenjs` + assets in `.claude/skills/flock-deck-builder/assets`).

## State as of 2026-07-02 (end of session, machine move pending)

### Deck (v4)
- 8 statement-titled slides + cover; Ed's verbatim framework wording on slide 2; P80 (interpolated floats) range chart; teams re-cut Jul 2: Prodtech (15), Distribution (5), People (3), Underwriting (5), Pricing (4, split out — inverted pyramid story), Operations (7, claims folded in), Finance (10). Ed + Tom outside team view.
- Company: n=50 of 57 scope; 1:3 · 2:15 · 3:19 · 4:13; min 1 · median 3 · p80 4.0 · max 4; builders 50%/70%/30%.
- Champions: one row per team; Finance = Ivan (Christian → exec-sponsor bench).
- OPEN deck edits from Ed morning call: slide 8 needs the quantified targets (100% ≥ Stage 3, majority Stage 4, Stage 5 = eng stretch) and the "Ghostbusters" label removed (Tom disowned it live). Optional: plainer "Stage-4 vanguard" wording, per-stage example names in slide 2 notes.
- Upload destination NOT decided (auto-mode blocked shared-drive upload — personnel-sensitive content; Tom to choose: private My Drive vs shared).
- AI-154: send slides to Eraaz for review BEFORE the Ed update.

### Scores (people/ frontmatter = source of truth)
- Jul 2 changes: David Pilley 1→3, Anneliese 1→2→1, Queency 2→1 (challenged to 0 — refused on evidence, reasoning in chat/deck notes), Adam Sandle upheld 2, Kaylee (new, people/kaylee.md, surname TBC) scored 1.
- Still open: Kirsty context-scoped 2 vs Stage-4 Looker evidence; Geran frontmatter 4 vs body 3; Darren Nightingale unassessed (tentative 0–1, second-hand only — do NOT score without direct evidence).

### Q3 plan (from Jul 2 Ed + Eraaz meetings)
- Targets: 100% Stage 3+, majority 4, end of Q3; not a company OKR (Ed/Tom/Rakhee).
- Issues AI-152..156: operationalise w/ Rakhee + Ed 10-min (152, due Jul 3), Prodtech Stage-5 push + CEO demo (153, London wk), deck fixes + Eraaz review (154), JD AI content — Eraaz (155), PGR tooling trial — Eraaz+Rakhee Mon Jul 6 (156).
- Slide-8 operationalisation map: `reference/q3-slide8-operationalisation-map.md` (what Eraaz covered vs gaps — item 5 "own the quality" is the orphan; proposal: deputy responsibility).

## Next session
1. Apply the two open deck edits (slide 8 targets + Ghostbusters), regenerate pptx, send to Eraaz (AI-154).
2. Decide Drive upload destination.
3. Book Rakhee operationalisation + Ed 10-min (AI-152).
4. London week prep: AI-150/151/153.
5. SECURITY: `datadog-secrets.txt` untracked in repo root — travels with any docker image copy. Delete or move out before imaging.
6. ~15 Jun 22–25 meeting notes still unwritten (transcripts exist).
