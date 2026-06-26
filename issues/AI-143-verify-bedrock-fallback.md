---
title: "AI-143: Verify Bedrock wiring as a fallback"
created: 2026-06-25
updated: 2026-06-25
domain: engineering-workflows
type: issue
status: todo
priority: medium
origin: "[[2026-06-25-fergus-tom-weekly]]"
tags: [fergus, bedrock, disaster-recovery]
---

Tom thought something was wired to Bedrock as a fallback but hasn't confirmed. Need to check and test before assuming there's any DR coverage.

Context: Bedrock offers top-tier privacy and pricing but Claude Desktop doesn't work through it. The DR hackathon (→ [[AI-140]]) may supersede this if AWS is a better option, but Bedrock is worth checking as a quick win.

## Actions

- [ ] Check what (if anything) is currently wired to Bedrock
- [ ] Test Bedrock connectivity and model availability
- [ ] Confirm whether Claude Code can be redirected through Bedrock
- [ ] Report findings to Fergus
