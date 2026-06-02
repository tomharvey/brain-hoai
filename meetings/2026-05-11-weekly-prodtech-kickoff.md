---
title: Weekly Product + Tech Kickoff (May 11)
created: 2026-05-11
updated: 2026-05-11
domain: engineering-workflows
type: meeting
tags: [engineering-workflows, product, five-sigma, claims, j-release, retention]
---

# Weekly Product + Tech Kickoff — May 11

**Attendees:** Tom Harvey, [[fergus|Fergus Doyle]], ProdTech leadership ([[matt|Matt Price]], [[jordi|Jordi Pallares]], [[ollie-crowe|Ollie Crowe]], [[mima|Jemima Pitceathly]], [[chris|Chris Fothergill]], others)

Full transcript: [[2026-05-11-weekly-prodtech-kickoff-transcript]]

---

## Key themes

### Expansion team — MTA adjustments and courier launch
- Adjustment hub ready for launch to existing clients
- Courier launch session today
- MDA simplification: breaking advanced flow into separate actions, reverting closer to previous system design

### Five Sigma claims project — kick-off week
- Second pre-brief done; project plan is large and extensive
- Technical approach: API access for vehicle coverage info + claims ingestion via API
- Admiral team more formal in approach vs. Flock tech company style
- Resourcing discussion pending: limited Flock involvement in implementation; may suit acquisition team
- Project channel: platform-claims for full plan

### Chief Vehicle Rentals integration — pause recommended
- Chief handling rental and credit hire for taxi claims; complex access issues
- Problem: Chief may also be an insured customer → can't show premium amounts
- Workaround in place: policy page broken for claims admins, redirected to portal; premium no longer shown prominently
- Documentation still contains other customers' premium data — can't be fully resolved
- Tom recommendation: **pause development** until comprehensive scoping; Chief's role may change with in-house claims management plans
- Risk: negating loss ratio benefits from Chief deployment

### Retention team — connectivity endpoints
- Building new data lake-driven API for J and portals
- Includes TSP information in consolidated endpoints; supports old and new system data
- Harsh completed pre-work; API implementation starting today
- J release: Anton wants July for marketing impact; Liam unavailable most of June

### J release tension
- Tom: earlier release → more learning → better July splash
- Risk: waiting until July is un-startup-like; Liam's calendar shouldn't block a release
- Blog series (3 parts) planned; Part 1 technical content can proceed before release

### Lunch and Learn — new format this Friday
- Tom, Som, and Chris presenting
- New format with multiple presenters; engineers encouraged to attend

---

## Actions

- [ ] Tom: Follow up on Five Sigma resourcing — whether acquisition team or elsewhere
- [ ] Ollie: Sequence Chief Vehicle Rentals work given scope uncertainty
- [ ] Tom: Push back on July-only J release; explore soft launch to existing customers first

---

## People without vault files
- Harsh — expansion team engineer; completed API pre-work for connectivity endpoints
- Som — engineer; presenting at Friday lunch and learn
- Liam — retention PM; mostly unavailable June; focusing on Amazon after
