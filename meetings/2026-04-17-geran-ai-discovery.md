---
title: Tom <> Geran — AI Discovery
created: 2026-04-17
updated: 2026-04-17
domain: ai-enablement
type: meeting
tags: [discovery, geran, product, streamlit, snowflake, personal-os, team-dynamics]
---

## Attendees

- [[geran|Geran Butcher]]
- Tom Harvey

## Key themes

### Team situation

- Complete engineering turnover — new team is David (Zamora) and Sam. Alex left after Portugal remote request denied. Abs already gone.
- Sam struggling with startup dynamics — background in B2C with thousands of customers, wants documented requirements vs Flock's bias-for-learning culture. Conversation with Jordi ongoing.
- Harvey providing reassurance to wider team about small team effectiveness — "nah, it's fine, it used to just be me and Abs and we nailed it." Positive cultural influence.
- Company policy confirmed: no new international remote workers. Ishmael grandfathered but no new exceptions.

### AI tools and development work

- Built Streamlit apps for data analysis — Matt Dipre's haulage analysis tool is now a production process
- Architecture: Streamlit hosted on Snowflake, data in Glue via Snowflake proxy (for security/permissions)
- Code is copy-pasted directly into Snowflake — no Git integration. Single Python files with minimal abstractions.
- "Connect to Git" option exists but not used
- More visual/UI oriented than text-based — interested in personal OS concept but wants a UI for his "mind palace," not a markdown vault

### Personal OS interest

- Not currently running a personal OS like Tom/Mima/Ollie
- Uses Claude Desktop for non-coding, starting to double down on it
- Key insight: "I do want a UI for my mind palace. I want a framing of it that is specific to me."
- Interested in how a PM OS would look — PostHog integration, daily automated check-ins, joining context between Granola/Notion/data lake
- More interested in "how do I convert this into something useful for the engineers" than personal productivity
- The million-dollar question he named: "if an engineer has one and a product manager has one, how do those mind palaces talk to each other and how does that change the software development lifecycle?"

### Product strategy: unconnected fleets

- High priority on Admiral Pioneer roadmap
- Geran advocates regularly but faces pushback on focus ("is this a new distraction or a lens on current work?")
- Challenge: colouring it as an extension of current work rather than a new initiative
- Tom's read: Pioneer is very interested in unconnected fleets; pushback from Fergus is about focus discipline, not disagreement on value

## Actions

- [ ] Continue personal OS conversation — Geran wants to explore what a PM-specific OS looks like with UI elements — Tom
- [ ] Follow up on Sam's fit — Jordi already in conversation — observe, don't intervene

## Notes

The "million-dollar question" — how do personal OSes talk to each other across roles — is the same tension surfaced in Fergus's 1:1 (individual vs team augmentation). Geran framed it from the product angle: "if we can crack it, that's a blog post at least." Worth tracking as it connects to [[ai-native-engineering]] (developer side) and the team-vs-individual question from the offsite.

Full transcript: [[2026-04-17-geran-ai-discovery-transcript]]
