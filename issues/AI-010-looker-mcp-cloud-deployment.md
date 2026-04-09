---
title: "Deploy Looker MCP to cloud infrastructure"
id: AI-010
created: 2026-04-09
updated: 2026-04-09
due: 2026-04-18
origin: "[[2026-04-09-kirsty-ai-discovery]]"
domain: operational-tooling
type: issue
status: todo
priority: high
assignee: tom
tags: [looker, mcp, cloud, infrastructure, kirsty]
---

## Description

Kirsty's Looker→Claude MCP connection currently runs on local machines (Kirsty + a handful of finance users). To scale company-wide, it needs to be deployed in multi-user mode on cloud infrastructure.

## Current setup (single-user, local)

Kirsty runs:
```bash
toolbox --stdio --prebuilt looker
```
With env vars: `LOOKER_BASE_URL`, `LOOKER_CLIENT_ID`, `LOOKER_CLIENT_SECRET`

This uses [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) with the `looker` prebuilt — 18 tools covering the full analytical workflow (model exploration, querying, Looks, dashboards, embedding). The client ID/secret are per-user Looker API3 keys (generated in Looker Admin > Users), so each local install authenticates as one Looker user.

Christian, Kevin, and David also have this running locally with their own API3 keys.

## Server decision

Evaluated googleapis/mcp-toolbox vs Ultrathink-Solutions/looker-mcp-server (98 tools). **Staying with googleapis.** See [[004-looker-mcp-server-selection]] for full rationale.

## Multi-user deployment

### How it works

The toolbox has a `use_client_oauth` mode. When enabled:
- Per-user API3 keys (`LOOKER_CLIENT_ID`/`LOOKER_CLIENT_SECRET`) are no longer needed
- Each request carries its own OAuth bearer token in a header
- Different users authenticate independently via their own Looker identity
- Looker permissions model is respected per-user

### Configuration

In the toolbox source config (or via env vars):

```yaml
sources:
  looker:
    kind: looker
    base_url: "${LOOKER_BASE_URL}"
    use_client_oauth: "true"   # enables per-request OAuth token forwarding
```

Or set `LOOKER_USE_CLIENT_OAUTH=true` as an env var.

### Target architecture

```
User (Claude) → Auth Gateway → mcp-toolbox (HTTP mode, use_client_oauth=true) → Looker API
                    │
                    └── Validates user, obtains Looker OAuth token,
                        passes as bearer token in request header
```

### Deployment steps

1. Deploy toolbox as HTTP server (not stdio): `toolbox --prebuilt looker --address 0.0.0.0:8080`
2. Set `LOOKER_BASE_URL` and `LOOKER_USE_CLIENT_OAUTH=true`
3. Put auth gateway in front that:
   - Authenticates the user (company SSO / OAuth)
   - Exchanges their identity for a Looker OAuth token
   - Forwards the token in the request header
4. Configure Claude clients to point at the gateway URL instead of running toolbox locally

### Open questions

- Is Flock's Looker self-hosted or Google Cloud Core? (affects OAuth token exchange mechanism)
- What auth gateway to use? (existing API gateway, OAuth proxy, or custom)
- Does the toolbox HTTP mode support streamable-http or just SSE? (need to check)

## Acceptance criteria

- [x] Get Notion page from Kirsty — https://www.notion.so/flockcover/How-to-Connect-Claude-to-Looker-2fee4b915259800d841dcc5fd0d27359
- [ ] Determine Looker hosting model (self-hosted vs Google Cloud Core)
- [ ] Test `use_client_oauth=true` mode locally
- [ ] Deploy toolbox in HTTP mode on cloud infrastructure
- [ ] Set up auth gateway with OAuth token exchange
- [ ] Verify bi-directional access works for multiple users with different Looker permissions
- [ ] At least one user who doesn't have local toolbox can access Looker via Claude

## Dependencies

- ~~Kirsty sharing Notion page~~ — done
- Clarity on Looker hosting model
- Auth gateway selection/setup

## Notes

- This is the #1 enabler for scaling Kirsty's work across the business
- Multiple business users already requesting access — demand is there
- Unblocks AI-007 (renewals Looker→HubSpot) at production scale
- Also unblocks Anton and Adam using the insights dashboard
- No migration needed — same toolbox Kirsty already uses, just deployed differently

## Links

- [[2026-04-09-kirsty-ai-discovery]]
- [[004-looker-mcp-server-selection]]
- [[kirsty]]
- Enables: [[AI-007-renewals-looker-hubspot]]
