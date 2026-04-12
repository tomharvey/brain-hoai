---
title: Javier — Acquisition AI Vision
created: 2026-04-10
updated: 2026-04-10
domain: product-ai
type: meeting
tags: [acquisition, api, integration, mcp, saaspocalypse, product-strategy]
---

# Javier — Acquisition AI Vision

Strategic conversation with [[javier]] (recently promoted) about his vision for Flock's AI-driven integration strategy. Javier's thesis: Flock needs to surface everywhere brokers work, not just through the traditional portal.

## Attendees

- [[javier]]
- Tom (me)

---

## The "SaaSpocalypse" framing

Javier's position: most SaaS workflow tools will be automated away. Only data sources and domain-specific knowledge providers survive.

My position: SaaS continues but becomes unrecognisable. Products become hyper-personalised rather than "fit into our box". The AI-era Shopify moment (a platform that lets you build personalised tools on top of a core product) hasn't happened yet. We're in a weird middle zone between 2010-era SaaS and building everything from scratch with AI.

### Where we agree
- HubSpot becomes a data backend, not a UI people interact with
- Matt/Adam don't need to buy a CRM — Claude builds one for them
- Domain expertise (insurance knowledge) is the real value, not the software wrapper
- Insurance is something you must buy from someone — AI can't replace the product itself

---

## Javier's vision: surface Flock everywhere

### The problem
Brokers will increasingly use AI agents to manage risk, find quotes, and process submissions. If Flock isn't easily accessible via API/MCP, we won't be in the conversation.

### The vision
- Be present in every platform brokers use: risk management tools, Claude workspaces, ChatGPT, whatever comes next
- Don't just optimise for AI SEO (though that matters too) — build an integration layer that makes connecting to Flock cheap and fast
- Analogy: Javier's wife's startup was nobody until they integrated with Salesforce. Same principle.

### How to get there
1. **Be API-first** — we're close but not fully there (auth/authz gaps)
2. **MCP server on our APIs** — Chris has already created one for the policy management API
3. **Proof of concept**: HubSpot → Claude → Flock quote creation
4. **Iterate**: fail on the first attempt, teach it the edge cases, then automate for small fleets without human in the loop

---

## Proof of concept — 2-week target

Javier committed to running an integration test within **2 weeks** (by ~2026-04-24):

### Decision to make first
- **Option A**: Automated quoting (HubSpot submission → Claude → Flock API → quote)
- **Option B**: Automated appetite checking (is this submission worth quoting?)
- Appetite check happens before quoting, so may be more valuable as a first step
- But appetite is tricky — it gets modified depending on the policy

### Test approach
- Use **disqualified HubSpot leads** as test data (safe — no impact on real pipeline)
- Chris's existing MCP server for the insurance service API is the starting point
- Connect HubSpot MCP + Flock MCP to Claude and see how far we get

### If quoting becomes cheap
Changes the appetite question entirely — if it costs nothing to generate a quote, you can quote everything and let price speak for itself.

---

## AI SEO

I'm asking [[liam]] (speaking to him next) to test: **does Claude/ChatGPT recommend Flock when asked about courier fleet insurance?** Basic but important to know. This is the surface-level version of Javier's deeper integration vision.

---

## Actions

- [ ] **Javier**: Decide first use case (quoting vs appetite check) and run integration test by ~2026-04-24
- [ ] **Tom**: Ask Chris about the existing policy management MCP server — what state is it in?
- [ ] **Tom**: Ask Liam to test AI SEO for Flock (does Claude recommend us for fleet insurance?)
- [ ] **Javier/Tom**: Share progress on integration experiments

---

Full transcript: [[2026-04-10-javier-acquisition-ai-vision-transcript]]
