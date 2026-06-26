---
title: "AI-141: Flock O'Clock — set up Planning Slack channel and run trial"
created: 2026-06-24
updated: 2026-06-24
domain: ai-enablement
type: issue
status: in-progress
priority: high
origin: "[[2026-06-24-ai-phoebe]]"
tags: [phoebe-woodman, rakhee, eraaz-ali, flock-o-clock, slack]
---

Design and trial the Flock O'Clock automation flow:
1. Two-column spreadsheet (contributor name + content slot)
2. Claude in a dedicated Slack channel (`#flock-o-clock-planning`) pings each contributor in their own thread
3. Contributors reply with bullet points or a slide link
4. Claude validates quality against Ed's comms playbook, gives feedback
5. Claude writes approved content back to column B
6. Skill rebuilds the deck automatically each time a contributor submits
7. Phoebe gets a live view and can catch anyone wildly off-track in real time

First step: trial with Phoebe + Tom + Rakhee + Eraaz where Tom plays himself and Rakhee/Eraaz play contributors.

## Actions

- [ ] Tom: set up `#flock-o-clock-planning` Slack channel; add and configure Claude
- [ ] [[phoebe-woodman]]: clean up the run sheet spreadsheet (coordinate with Ed and Rakhee)
- [ ] Run trial: Tom, Rakhee, Eraaz as test contributors
- [ ] Iterate based on trial feedback
- [ ] Aim to have something working before next Flock O'Clock (16 July)
