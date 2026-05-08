---
title: Fergus <> Tom — Weekly
created: 2026-05-08
updated: 2026-05-08
domain: ai-enablement
type: meeting
tags: [weekly, fergus, leadership, admiral-business, finance, transcript-substrate, coding-standards, matt-price]
---

## Attendees

- [[fergus|Fergus Doyle]]
- Tom Harvey

## Key themes

### Admiral Business workshop — joint session opportunity

- Tom visiting London in a couple of weeks — that date is a potential for the AI workshop
- Admiral Business (not Pioneer umbrella — separate business unit, same Pioneer employees including Alex and Ed Hill) further along on AI agentification of dev workflows
- Fergus: hook Tom up with Alex or Ed Hill; explore co-presenting. Possible hackathon element
- Workshop rough shape: fortnightly product demo (9am, Hopper + Brunel), then fourth floor for the day
- Topics Fergus has in mind: claims/third party capture, shared experiences, general AI products, social (instadoc, as both teams working on it)
- **What Tom wants**: someone building a multi-source personal dashboard live — Looker + HubSpot + calendar in Claude. Not just Looker alone

### Finance team — forcing function

- Finance team not making time for AI ("too busy for the shortcut"). Tom: they have the capability, just not making the space
- Fergus screenshotted a finance discrepancy conversation — two large data sets with unexplained differences, being handed back to Chris to fix rather than structured as a programme of work. Classic "too busy to think" pattern
- **Jade's Mon 3–4 session with Fergus and Jordi** — prep for Q3 FinOps automation requirements. Fergus invited Tom to join or invite himself (speak to Jade at 11:30 first)
- Tom's plan: force the finance team into a room (blame Tom), get Kirsty in, spend two hours doing it together

Finance team context: Christian doing what Kirsty points him at (not self-directing); Geran doing things from scratch for Matt (finance) instead of teaching independence. Both are capable — problem is dependency, not skill.

### Installments business logic — where does it live?

- Net load (loan management platform) was removed without a replacement conversation. SAP was mentioned historically but not committed
- Fergus's view: installments is really a loan management concern; business logic exists across spreadsheets and people's heads — that complexity is already in the business
- Concern: if Admiral goes to raise finance to support installments capital, that changes requirements
- For now: take the business logic out of spreadsheets and put it somewhere sensible. Don't try to platform-100% everything

### Geran data quality risk — hospital pass

Fergus flagged a specific risk: **Geran making assumptions about data sources** — pulling from Snowflake, the data lake, platform DB inconsistently. Telemetry data quality has stabilised, so errors are now visible; Geran's approach may mix clean and dirty sources without knowing.

Fergus: "that's actually where I think [Geran's] approach to supporting that is most dangerous." Tom can help with some of those shoots.

### Transcript / data substrate — medallion architecture

Extended discussion on company-wide transcript strategy:
- **Medallion model**: bronze (raw transcript) → silver (structured extraction, entity tagging) → gold (domain-specific insights)
- Jemima has been building vector encoding in her personal OS — running into organisation problems (which folder? which structure?)
- Francesco's transcript service already exists (built on Granola) — not starting from zero
- Current state: BDMs (Ben, Daisy) have loose ability to query team transcripts; others (Sophie, Adam, Alex, Matt) do not
- **RBAC is the hard problem**: SLT meeting transcripts vs broker call transcripts need different access policies
- Underwriting gap: underwriters mostly on phones or in person — can't capture transcripts the same way; class imbalance vs BDMs
- The insight Tom demonstrated live: this transcript will be ingested through multiple lenses (AI uplift initiative, SDLC initiative, etc.) and produce different summaries. That capability requires transcript access

Fergus framing: **post-processing value** — not just storing the transcript, but tagging it. Like ProductBoard markup — annotate sections as relating to specific problem spaces. Small Haiku-level agents (HubSpot contact update from conversation, product feedback tagging) running on the raw transcript.

Agreed: not "more tickets in Linear" — better to validate/invalidate existing tickets or find the right project to comment on. The PM as human-in-the-loop to begin with, then let it run.

### Coding standards / GitHub comment approach

Fergus validated the GitHub comment → coding standard approach Tom and Chris had discussed that morning:
- Two artifacts: (1) human-readable principles doc (hundreds of rules, file-per-rule with frontmatter + backlinks), (2) AI-readable backlink index of GitHub comments
- The "write everything down" reframe: get Claude Code to write it based on high-level guidance
- Javier (Javier) used as Fergus's example from yesterday — "give me the 10 best Telemetry features for pricing" from a one-line prompt. Plan is wrong in some ways; you then chat it to correctness. If you don't do that step, errors compound

### Matt Price — background processing request

At close: Fergus flagged he's having a difficult time with [[matt|Matt Price]]. "Excellent diplomat, but struggling to get strong opinions from him." Struggling to get clear direction independent of the broader PM group.

Asked Tom to think on this as a background task — is there a superpower that needs dialling up, or is Fergus inadvertently blocking him from running with things?

Tom: "That resonates. I'll use my actual brain on that one."

### AI breakfast

- Matt Lees showed his second brain
- Jemima presented — flagging an organisation problem (transcript folder structure)
- Tom's observation: others are "reading their markdown files" while Tom treats his vault as unreadable binary — as long as the AI can read it, that's sufficient. Accuracy/eyeballing matters more for plans that drive actions, less for context that gets synthesised
- Looker/Telemetry login issues — Telemetry times out after 15 minutes (Lambda); Looker also needs fixing

## Actions

- [ ] Tom: invite self to Jade's Mon 3–4 session with Fergus and Jordi (or speak to Jade before then at 11:30)
- [ ] Tom: plan and run a dedicated finance team AI session (2 hours, bring Kirsty) 
- [ ] Tom: connect with Alex (Admiral Business) re: joint AI workshop / hackathon — Fergus to make intro
- [ ] Tom: think through Matt Price coaching angle for Fergus — what superpowers to dial up, and whether Fergus is inadvertently blocking
- [ ] Tom: address Looker login session timeout (Lambda, 15-min expiry)
- [ ] Fergus: send intro to Alex / Ed Hill (Admiral Business) for workshop co-planning

## Notes

The transcript infrastructure conversation is the clearest articulation yet of what the data substrate could become. The medallion model (bronze/silver/gold) is the right framing — it sets expectations about what each layer provides and what work it requires.

The Matt Price question from Fergus is sensitive — "you're my safe space" framing. Tom should think carefully before saying anything back. What Fergus is probably describing: Matt is diplomatic to a fault (avoids conflict with PMs), making it hard to get the kind of decisive PM leadership that would help Fergus drive product strategy. The question of whether Fergus is inadvertently creating this dynamic is important.

Full transcript: [[2026-05-08-fergus-tom-weekly-transcript]]
