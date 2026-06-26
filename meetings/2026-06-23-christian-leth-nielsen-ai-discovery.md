---
title: "AI discovery — Christian Leth Nielsen"
created: 2026-06-23
updated: 2026-06-23
domain: ai-enablement
type: meeting
tags: [christian-leth-nielsen, finance, cfo, ai-discovery, looker, netsuite, semantic-layer]
---

## Attendees

- Christian Leth Nielsen (CFO)
- Tom Harvey

Full transcript: [[2026-06-23-christian-leth-nielsen-ai-discovery-transcript]]

---

## Key themes

### AI use cases — impressive breadth

**SPA vendor obligation extraction**
- Iterative self-checking loop: ran 10–11 times until output was stable and self-consistent
- Would have cost thousands in legal fees externally
- Output includes source references (line numbers in the original document)

**GWP budget analysis — without touching a spreadsheet**
- Data from FP&A cube (Looker) and Excel budget model; Kirsty has since loaded all budget data into the cube
- ~15 prompts to get output exactly right; faster iteration than working with Dave Pilley
- Claude debugged its own number mismatches when fed the correct version
- Calculated values (growth rates, variances) are simple enough to spot-check

**Distribution cost analysis vs Jade's analyst output**
- Same question answered in Claude: cleaner layout, better modelling (fixed vs. variable cost split for GoCardless/Grace)
- Clear conclusion: "this workflow is now the default; old input-sheet-to-analysis-schedule flow is obsolete"

**Budget model improvement (Cowork, during due diligence)**
- Fed Claude the full model; produced forecasts for 2026–28 with correct dimensions
- Built improved spreadsheet version retaining driver visibility, added scenario analysis
- Also handled model roll-forward (switching actuals/forecast split by month) — historically labour-intensive
- Jade taking on more forecasting; Christian holding back Claude outputs so she gets there herself

### Data quality, governance, and architecture

- Core risk: end users can't sense-check outputs the way Christian can because they don't know the numbers
  - Adam Smith example: building a trading pack without knowing which GWP figures to use
  - Open question: what role should Finance/Kirsty play in auditing end-user-generated outputs?
- Looker MCP (Google-provided) has auth problems + no semantic layer — strong case for replacing with a custom server
- NetSuite MCP installed but hitting API rate limits on document access; needs engineering fix
- Semantic layer debate: skills work for a small number of well-defined objects; the full ontology is hundreds of objects — that's where a semantic layer earns its keep
- Looker MCP can in theory create dashboards — useful for auditing calculations Adam is making

### Maturity shift needed

- Q3 shift: from "experiment freely" to "this is production-level, be robust"
- Key governance prompts everyone needs: cite source line, preserve driver visibility, flag when outputs differ
- Two value levers from AI in Finance:
  1. Expense saving: fewer analysts needed for routine analysis
  2. New insight generation: analyses like LTV:CAC that haven't been run in 2 years because too labour-intensive
  3. Ongoing monitoring (e.g. expense anomaly detection): run continuously, alert only on change

---

## Actions

- [ ] Tom: fix Drata MCP rate limit issue and deploy to all computers by 24 June → [[AI-137]]
- [ ] Tom: organise Finance team AI workshop (Tom in office in ~2 weeks; use Christian's examples to drive AI-first thinking) → [[AI-137]]
