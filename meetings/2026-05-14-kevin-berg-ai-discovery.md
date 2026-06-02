---
title: Kevin / Thomas — AI discovery (May 14)
created: 2026-05-14
updated: 2026-05-14
domain: operational-tooling
type: meeting
tags: [operational-tooling, finance, ai-discovery, netsuite, excel]
---

# Kevin / Thomas — AI discovery (May 14)

**Attendees:** Tom Harvey, Kevin Berg (fractional CFO contractor)

Full transcript: [[2026-05-14-kevin-berg-ai-discovery-transcript]]

---

## Key themes

### Kevin's background and role
- Fractional CFO contractor at Flock for 3+ years (2 days/week)
- Also works with other insurtech scale-ups; does FP&A at Flock (unusual for his contracting pattern)
- Three-month contract extended indefinitely — "no one ever gets rid of me"

### AI tool stack and evolution
- Stack: Claude (primarily), Whisper, Granola
- Journey: Chat → Co-work → Code (moved to Code due to bandwidth/continuation issues with Co-work)
- Excel and PowerPoint Claude plugins: "phenomenal"; now interconnected — tables in presentations linked to data packs

### Current AI applications
- **Data analysis and commentary**: flags unusual items in reports, writes first-pass commentary
- **Automated trading pack commentary**: Google Apps Script that reads the weekly table and generates commentary in Kevin's style
- **Formula assistance**: complex budget restructuring 4 hours → 20 minutes; issue: Claude writes complex nested IFs instead of auditable simple formulas
- **Proof and reconciliation automation**: critical for accounting accuracy; enabled share options project within 2-day/week constraint
- **Predictive model building**: personal exploration of data science; found and corrected a data leakage issue

### Integration challenges
- **Xero**: limited MCP integration, "garbage" functionality
- **NetSuite**: manual report extraction; no automation path found yet
- **Junior staff**: lack automation mindset; senior staff too time-pressed to systematise

### Key insight: the corrective feedback loop
- Kevin has been "gritting teeth" through bad Claude formula choices instead of correcting it
- Tom's suggestion: go back and be like "take lessons from everything I've corrected you on; encode it in a skill"
- The commentary from Kevin's packs IS data for future packs — but Claude overfits past explanations (lazy)
- Solution: provide all underlying data cuts plus the questions Kevin would ask; make Claude go deeper

### Transition from single-player to team-shared AI workflows
- All Kevin's AI work is proprietary to him — can't share it yet; needs to become a "product"
- Matt Dipré doing similar things; Kevin + Ivan + Matt could cross-pollinate
- Finance team general issue: "too busy to take the shortcut"

---

## Actions

- [ ] Tom: NetSuite integration exploration for next month (→ AI-079 or new issue)
- [ ] Tom: Schedule Monday/Tuesday session with Kevin for deeper AI discovery (done — May 19 Finance Workshop)
- [ ] Kevin: Encode correction patterns for formula style preferences and analysis methodology into skills
- [ ] Kevin: Feed all underlying data cuts and questions into trading pack commentary prompt
