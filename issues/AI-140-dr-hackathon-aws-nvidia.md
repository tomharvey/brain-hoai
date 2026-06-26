---
title: "AI-140: DR hackathon — spin up AWS with Nvidia, expose local model endpoint"
created: 2026-06-24
updated: 2026-06-24
domain: engineering-workflows
type: issue
status: todo
priority: medium
origin: "[[2026-06-24-ai-group-therapy]]"
tags: [ishmael, javier, chris, disaster-recovery, aws, bedrock]
---

Recent Anthropic/OpenAI outages (~3 hours down) prompted a DR planning discussion. Consensus: run a hackathon-style experiment to validate fallback options.

**Option 1 (preferred for experiment)**: Spin up AWS instance with Nvidia GPU, install an open-source model, expose an OpenAI-compatible endpoint. ~£10k for a Mac Mini (less than monthly Anthropic spend) but limited to ~4 engineers. AWS scales better.

**Option 2**: Bedrock as fallback. Top-tier privacy and pricing but Claude Desktop doesn't work through it. Potential: build a chat interface on top of a Bedrock API endpoint.

Also: Tom thought something was wired to Bedrock but hasn't confirmed. Check separately → [[AI-143]].

## Actions

- [ ] Agree on hackathon date with Javier, Ishmael, Chris
- [ ] Spin up AWS instance with Nvidia GPU
- [ ] Install and test open-source model (e.g. llama, mistral)
- [ ] Expose OpenAI-compatible endpoint for team testing
- [ ] Evaluate viability as production fallback
