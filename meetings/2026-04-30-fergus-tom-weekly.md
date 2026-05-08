---
title: Fergus <> Tom — Weekly
created: 2026-04-30
updated: 2026-04-30
domain: ai-enablement
type: meeting
tags: [weekly, fergus, leadership, ai-adoption, token-spend, capability-cohorts, looker, admiral]
---

## Attendees

- [[fergus|Fergus Doyle]]
- Tom Harvey

## Key themes

### Ollie & Javier AI adoption — ongoing friction

- [[ollie-crowe|Ollie]] and [[javier|Javier]] hardest to get on board — developers are currently the least engaged cohort
- Anton continuously "ravages" Ollie when he presents work — makes momentum hard to build. Fergus: the acquisition team's real problem is not moving fast enough, it's not being clear about what they're solving for
- Javier upgraded to premium Claude seat but not maxing it out — still on Sonnet; Fergus pushed the "if you're not maxing out premium, you're under-utilising" framing
- Tom's framing: speed isn't the message to land right now while Anton pressure is high; "it doesn't have to be faster"

### Anton/Darren doom loop — acquisition team

- Ongoing SLT debate between Anton and Darren on acquisition team direction. Ollie caught in the middle
- Fergus: in SLT yesterday, unclear what the acquisition team is even focused on — two SLT members asking for conflicting things
- Ollie incorporating conflicting feedback into a "Frankenstein" rather than reconciling and pushing back
- Fergus: needs to provide more air cover here

### Submissions pipeline / protect review demo

- Protect review Wednesday — Jordi's forcing function: "what are we going to show?"
- Jemima (Mima) referenced as fully engaged — "cloud coding his way through life" (i.e. not writing a line manually)
- Alex flagged as potentially picking up Jacob/Fergus support for submission output ahead of Wednesday — but hadn't communicated directly, which Fergus noted as a pattern problem
- [[mima|Jemima Pitceathly]] and [[ishmael|Ismael Jebril]] got Datadog skills — enables iteration loop on J product ("naima" in transcript = Mima, speech-to-text drops the "Ji")
- PostHog gap in submissions world noted — J team uses Datadog, not PostHog. MTA failures would have been caught earlier if PostHog alerts existed

### Token spend mindset — spend, don't limit

- Matt Lees burning highest token usage by far — "burning the average up massively". Fergus: "make it cost more, burn them"
- Submissions pipeline: ~50p/submission with Sonnet+Opus (unoptimised). If that leads to 1% conversion improvement, Anton would be delighted
- Key message: don't limit when nobody's using; limit only when it's clearly too much. Current state = not even close to too much
- Jemima's team extrapolated token costs from early J users — got to ~$2,400/month at scale and panicked. Tom: that's a celebration, not a concern

### Capability cohorts — 4 types

Tom's working framework:
1. **Non-users** — very few now
2. **Consumers** — using others' output
3. **Dabblers** — building their own things, contributing back
4. **Advanced builders** — like Matt Lees

Goal: move type-1 to type-2, type-2 to type-3. Not everyone needs to write skills — but everyone should be able to edit the skill they're using.

### Dotwork demo

- Dotwork = John Cutler's AI "second brain for companies". Engagement starts at $75k/year.
- Too process-heavy and too expensive for Flock right now — SLT can't even agree on KPIs
- Good inspiration for outcome-focused metrics / north stars persistent beyond a quarter. "A graph in Streamlit, management consultants, and a nice UI."

### Looker MCP — imminent

- Hours away from Looker MCP being live (auth-zero dependency remaining)
- Billy and Thom (underwriting team) asked for Looker access after seeing Jemima's J demo — now connected
- Permissions schema not configured properly: "I either have not enough or too much [access]". Assuming Kirsty's permissions model underlies it — to be checked
- Fergus: important to understand MCP permissioning at org level, especially HubSpot (licensing tiers = deal access or not)

### Admiral enterprise Anthropic terms

- Big Admiral has an enterprise deal with Anthropic. Pioneer (including Flock) benefits from the same terms, maintaining their own contracts. Same terms available post-close
- Fergus happy for Tom to run point on that conversation with Alex

### Admiral Haven compliance offboarding

- Compliance task due end of May: offboarding Haven from Admiral. Requires HubSpot automation
- Likely to run via on-device assistance but may need help. Fergus may ask Tom

### MTA failure post-mortem framing

- MTA failure was a UX failure (confusing new flow), not a technical failure. Invoice error was an incorrect calc on broker commission (additive not subtractive)
- Fergus: "we've been a bit relaxed about what we consider core user journeys that need coverage"
- Tom: "it was a miss not to have PostHog sending a daily summary to [the team]" — this would have caught it
- Not about being more careful before releasing — about observability and coverage of core journeys

## Actions

- [ ] Tom: check Looker permissions for Billy/Thom (what they actually have access to; Kirsty's permissions model)
- [ ] Tom: speak to Alex about Admiral enterprise Anthropic terms — Fergus to connect
- [ ] Tom: find out what monitoring/observability Ollie is using for the acquisition product (PostHog gap)
- [ ] Fergus: provide more air cover for Ollie vs Anton pressures

## Notes

The "spend the money" token mindset is a message to repeat. The pattern of people panicking at projected token costs before real usage exists is consistent. Matt Lees as the benchmark: he's not a cautionary tale, he's the standard to aim for.

The acquisition team doom loop (Ollie caught between Anton and Darren) is a real structural problem. Tom needs to flag when Ollie is getting contradictory direction, not just coach Ollie to handle it.

Full transcript: [[2026-04-30-fergus-tom-weekly-transcript]]
