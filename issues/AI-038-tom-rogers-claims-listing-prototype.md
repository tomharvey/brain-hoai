---
title: Prototype claims listing analysis for Tom Rogers (Motor Underwriting)
created: 2026-05-11
updated: 2026-06-03
domain: operational-tooling
type: issue
status: todo
priority: high
origin: "[[2026-04-16-tom-rogers-underwriting-ai]]"
tags: [underwriting, claims, pdf, prototype, tom-rogers]
---

## What

Build a working prototype that takes a motor insurance claims listing (PDF or Excel, as received from broker via HubSpot/G Drive) and outputs structured trend analysis matching what Tom Rogers does manually today.

## Why

Tom Rogers is actively seeking help and not defensive. His trust in AI is broken by past ChatGPT failures on complex Excel — a working Claude prototype is the unlock. If we clear the bar visibly, he'll push adoption to the whole underwriting team and the pattern scales to smaller cases currently skipped on cost grounds.

## Output the prototype must produce

From a raw claims listing:
- Driver trends (multiple accidents on same driver, 3–5 year window)
- Date/time correlation (accidents clustered by month, day, season)
- Causation trends (e.g. historical theft problem — what mitigation exists?)
- Days-to-report analysis (where does the Flock effect show?)
- Peril split (own damage vs third party)
- Excess modelling — apply £1k / £2k / £5k additional excess to each own-damage claim, roll up to new total incurred (`MAX()` formula equivalent)

## Prerequisite

Tom Rogers was going to share client folder links (PDF claim formats) in Slack. Chase this first — the prototype needs real examples to work with.

## Next actions

- [ ] Chase Tom Rogers — did he share the Slack links to client folders?
- [ ] Get 1–2 real claims listing PDFs (small / medium case examples)
- [ ] Build extraction → Google Sheet equivalent → trend analysis prompt in Claude
- [ ] Show Tom the output side-by-side with what he'd do manually
- [ ] If it works: scope the >£500k actuarial template separately (→ AI-029 context)

## 2026-06-03 update

Tom Rogers was mentioned by Anton at the Prodtech demo as someone who should be in the conversion improvement coordination workshop ([[AI-088]]). Flagged as not yet having had an AI follow-up since April. Tom also surfaced as a candidate for AI culture group sessions. Worth combining the prototype check-in with a broader AI conversation — see people/tom-rogers.md.
