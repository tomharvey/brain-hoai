---
title: Tom Rogers — Underwriting & AI benefit conversation
created: 2026-04-16
updated: 2026-04-16
domain: operational-tooling
type: meeting
tags: [underwriting, claims-analysis, excel, pricing, darren, hib, pipeline]
---

# Tom Rogers — Underwriting & AI benefit conversation

Originally scheduled as Jordi/Billy — Tom Rogers joined instead (Billy didn't dial in). First substantive conversation with the core motor underwriting side of the org after weeks of ops-side discovery. Tom reached out via Jordi and came with a concrete, well-articulated ask.

## Attendees

- [[jordi|Jordi Pallares]]
- Tom Rogers (Head of Motor Underwriting)
- Tom Harvey (me)

---

## The ask — claims analysis automation

Tom's primary AI opportunity: the manual spreadsheet analysis underwriters do on claims listings when pricing a risk. This is *the* repetitive high-skill task in his team.

### Typical workflow today
1. Claims listings arrive as **PDFs** (HubSpot + G Drive) — occasionally Excel
2. Underwriter unlocks/reformats PDF → Google Sheet (high-friction, often garbled)
3. Pivot tables + manual analysis across hundreds to thousands of claim lines
4. Summary tables fed into pricing discussions

### What he's looking for in the analysis
- **Driver trends** — multiple accidents on same driver across 3–5 years
- **Date/time correlation** — accidents clustered in specific months, days, seasons
- **Causation trends** — e.g. historical theft problem → what mitigation has been put in place?
- **Days-to-report** — where can the Flock effect move the number?
- **Peril split** — own damage vs third party (own damage is where excess changes bite)
- **Excess modelling** — `MAX()` formula applying a £1k/£2k/£5k additional excess to each own-damage claim, roll up to new total incurred

### The "what do we need to believe" lens
On risks where commercial pressure pulls the price below the technical rate, the team models Flock advantages against the gap:
- Faster third-party claims settlement (e.g. −10%)
- Reduced days-to-report (e.g. 30 → lower)
- Model new loss ratio → justify a lower premium

This is both a **pricing** exercise (can we reach the rate?) and a **value-led pitch** exercise (what do we tell the broker?).

### The >£500k actuarial format
Separate standard template Milan/Michael fill in for large risks: development pattern tables, claims summary tables, variable assumptions. "What do we need to believe" block at the end. Tom is "pretty sure a lot of this is manual" but doesn't want to speak for the actuarial team. Milan catch-up incoming — worth a peek before that.

Small cases currently get less of this treatment because premium-vs-time-spent doesn't justify it. **If AI collapses the time cost, the same analysis could be applied to smaller cases too.**

---

## Team & AI posture

- Team usage is **"amateur level"** — everyone understands the potential, no one is deep
- ChatGPT mainly — Tom has **lost trust in it for complex Excel work** (returns have been wrong, misaligned rows when unlocking PDFs)
- Gemini used for internal meeting summaries (not client calls — those are phone, too quick)
- Looker: Tom is a **power user** — queries custom tables directly, not just standard dashboards. Strong SQL-ish comfort from a past life with MS Access.
- HubSpot: "makes him sad" but admits it's good for pipeline management — big improvement over paper on his desk
- Tom averages **64 calls/day**. Wants to stay in Excel / G Drive / pricing model. Every minute outside those three is friction.
- Tom does use AI at home and personally ("uses it as much as I can for quick things") — including loading 5–6 years of historical claims to analyse settlement vs reserve patterns (used to challenge a DCL/Admiral over-reserving).

### Darren McCauley's AI use (data point)
Tom confirms Darren is **definitely using AI** — screenshots summarising broker performance (Amazon specifically), triangulating telemetry/loss-rate data. Tom: *"I think he's using it more than he's letting on"* — aligned with my own read. Slides/presentations the one exception.

---

## Strategic framing — what freed capacity unlocks

I asked the planted question: if AI frees up UW assistants' time, what would you have them do?

Tom's answer (unprompted, clearly thought about):
- **Train them up into underwriters.** Scale to £400M requires more UW resource.
- Wants to grow internally, not hire externally — new hires arrive with biases from previous teams
- Assistants trained internally learn "the Flock way" without contamination
- Quote: *"they get a basis of the Flock. They know the Flock follow up before anything else... they've got this naivety that actually helps"*

This is the reframe you'd hope to hear. Tom is already there — no selling needed.

---

## HIB haulage campaign (side project)

Tom has a pipeline-generation project he'd like help with (wants to pair with Jemima):
- Old list: ~£150M of fleet contact from his previous life (6 years old)
- Wants to correlate **old customer names ↔ current operator licenses** to find still-live fleets
- Then enrich: Companies House, publicly-available contact info
- Output: **outbound campaign list for HIB partnership**

Flagged as: *"I wouldn't be confident doing that myself"* — he'd give it a go but wants help. Good PoC candidate, scoped, clear output.

---

## Key decisions / signals

- Tom is **actively seeking** AI help — not defensive, not sceptical. The "underwriters are defensive" pattern flagged elsewhere does not apply to Tom himself.
- His trust in AI is gated by **past bad experiences with ChatGPT on complex Excel** — Claude + structured extraction will need to clear that bar visibly
- HubSpot data quality: Tom is relatively content — *"I can't knock it, it feeds into Looker and Looker works"* — not a blocker from his seat
- "Don't send me on a mad chase" — he wants concrete, small, valuable wins. Not a vision pitch.

---

## Actions

- [ ] **Tom Rogers**: Share links in Slack to client folders showing small / medium / large cases and the various PDF claim-listing formats
- [ ] **Tom Harvey**: Before Milan catch-up, look at the >£500k actuarial template and identify where AI could compress the manual work
- [ ] **Tom Harvey**: Prototype claims-listing → Google Sheet extraction + trend analysis on one of Tom's shared examples (Claude, not ChatGPT — rebuild trust visibly)
- [ ] **Tom Harvey**: Connect Tom Rogers with [[mima|Jemima]] on the HIB haulage pipeline project — scope as a proper PoC
- [ ] **Tom Harvey**: Don't get him to write the list of trends himself — generate it from AI output when we have a working prototype
- [ ] **Tom Harvey**: Share relevant tools/tips with Tom (he'll push to the team) — move them off ChatGPT for work tasks

---

## Follow-ups to chase elsewhere

- **Billy Bone**: still the originally-interested party. Billy didn't make this call — need to loop back.
- **Darren**: Tom's confirmation that Darren is using AI more than he lets on is new signal. Strengthens case for a direct Darren discovery conversation.
- **Milan/Michael (actuarial)**: Tom hinted they "may be using AI to some degree" on the >£500k template — worth asking directly.
- **AI Breakfast**: Tom said "appreciate them and do that" but no commitment to attending — not pushed in the call, revisit after a concrete win lands.

---

Full transcript: [[2026-04-16-tom-rogers-underwriting-ai-transcript]]
