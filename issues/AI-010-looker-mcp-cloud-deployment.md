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
Claude Code → stdio proxy → HTTPS → ALB (TLS) → Fargate task → Looker API
                                          │
                                ┌─────────┴──────────┐
                                │  Sidecar (:8080)    │
                                │  Auth0 JWT → Looker │
                                │  token exchange     │
                                │  Proxy to :8081     │
                                ├─────────────────────┤
                                │  Toolbox (:8081)    │
                                │  use_client_oauth   │
                                │  --prebuilt looker  │
                                └─────────────────────┘
```

### Infrastructure decisions

- **Cloud**: AWS Fargate, `eu-west-2`
- **Looker**: Google Cloud Core
- **Auth**: Auth0 (existing company provider)
- **IaC**: AWS CDK (TypeScript) with CDK Pipelines
- **Sidecar**: TypeScript (Node.js)
- **Pattern**: Sidecar proxy in same Fargate task

### Sidecar proxy (TypeScript, ~100–200 lines)

1. Listen on `:8080` (ALB target)
2. Validate Auth0 JWT via JWKS (`jose` library)
3. Extract user identity (email/sub) from JWT
4. Look up user's Looker API3 creds from Secrets Manager (keyed by user)
5. Call Looker `/api/4.0/login` → access token
6. Cache token in-memory (keyed by user, TTL ~55 mins)
7. Set `Authorization: Bearer <looker-token>` header
8. Reverse proxy to Toolbox on `localhost:8081`

**Streamable HTTP only** (no legacy SSE). Toolbox POST responses are plain `application/json` — no streaming. Sidecar is pure request/response proxy. Preserve `Mcp-Session-Id` header. Can use plain `fetch` or `http-proxy` — no stream piping needed. Block `GET /mcp/sse` at the sidecar (return 404).

### CDK stack outline

```
LookerMcpStack
├── VPC (or import existing)
├── ECS Cluster
├── Fargate Task Definition
│   ├── Sidecar container (:8080) — ECR
│   └── Toolbox container (:8081) — ECR mirror
├── ECS Service (Fargate, desired=1)
├── ALB + HTTPS listener (ACM cert)
│   └── Target group → :8080
├── Secrets Manager (per-user Looker API3 creds)
├── IAM (task role: Secrets Manager read, ECR pull)
└── CDK Pipeline (self-mutating)
    └── Source → Build → Deploy
```

### Client-side

Thin stdio proxy script (TypeScript, distributable via npm) that:
1. Handles Auth0 device flow or cached token
2. Connects to Fargate endpoint via HTTPS
3. Bridges stdio ↔ HTTP for Claude MCP
4. Configured as MCP server in Claude settings

### Deployment steps

1. Mirror Toolbox image to ECR (eu-west-2)
2. Build sidecar container, push to ECR
3. CDK deploy: VPC/ALB/Fargate/Secrets Manager
4. Store per-user Looker API3 keys in Secrets Manager
5. Test end-to-end with one user
6. Write client setup docs
7. Roll out

### Open questions

- ~~Is Flock's Looker self-hosted or Google Cloud Core?~~ → **Google Cloud Core**
- ~~What auth gateway to use?~~ → **ALB + Auth0**
- Does Toolbox Docker image support arm64 (Graviton)? If not, use x86_64
- Does Toolbox HTTP mode use SSE or Streamable HTTP? Sidecar must handle whichever
- CDK Pipeline source: existing monorepo or new repo?
- Does Flock have a shared VPC / ECS cluster in eu-west-2, or greenfield?
- Client-side stdio proxy: build now, or start with manual token passing?

### Toolbox image details

- **Registry**: `us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox`
- **Pin to**: `v1.1.0` (released 2026-04-13). Do not use `latest`.
- **Architecture**: Multi-arch (amd64 + arm64) — **Graviton is a go**
- **Size**: ~30-60 MB compressed. Distroless base (`gcr.io/distroless/cc-debian12:nonroot`), single Go binary.
- **Security**: Runs as `nonroot` user by default.
- **Mirror to ECR** in eu-west-2 — avoids cross-cloud pull latency and Google outage dependency. Pin the version tag.

### Concerns

1. **Mirror Toolbox to ECR** — cross-cloud pull from Google Artifact Registry adds cold start latency and creates outage dependency. Mirror `v1.1.0` to ECR and update when upgrading.
2. ~~**Streaming responses**~~ — Resolved. Dropping legacy SSE, Streamable HTTP only. POST responses are plain JSON. Sidecar is pure request/response — no stream piping needed.
3. ~~**Graviton**~~ — confirmed multi-arch. Use Graviton (ARM64) for cost savings.
4. **Secrets Manager at scale** — one secret per user is fine at 30 users. At 200+ consider single secret with JSON map or DynamoDB.
5. **Looker token refresh** — API3 tokens expire ~60 mins. In-memory cache with TTL handles this; sidecar restart causes brief re-auth latency spike (acceptable).
6. **Client-side stdio proxy is the UX bottleneck** — server is clean, but users need a local bridge from Claude stdio to remote HTTP. Distribute as npm package for easy install.

## Alternative considered: Bedrock AgentCore Runtime

Researched 2026-04-16. Rejected in favour of Fargate+ALB+sidecar.

### Findings

- **Available in eu-west-2**: yes
- **Container support**: arbitrary Docker, must be ARM64, listen on `0.0.0.0:8000`, path `/mcp`
- **Protocol**: Streamable HTTP + SSE, both supported and production-ready
- **Auth0 flow maturity**: GA. OIDC discovery, RFC 6749 compliant. DCR support. Requires `audience` parameter (not just `resource`) to get JWT instead of opaque tokens
- **Cost**: per-CPU-second consumption billing, 128 MB minimum
- **Observability**: CloudWatch + OpenTelemetry built in

### Why not

1. **Does not eliminate the sidecar.** AgentCore validates the Auth0 JWT but does not exchange it for a Looker access token. We'd still need container code that looks up API3 credentials in Secrets Manager and calls Looker `/api/4.0/login`. The main hoped-for simplification is illusory.
2. **Claude client compatibility gap.** AgentCore's endpoint sits behind AWS WAF rules that reject requests without User-Agent headers. The MCP Python SDK doesn't set User-Agent by default — AWS's own docs recommend monkey-patching `httpx.Request.__init__`. We'd inherit this as permanent friction in the stdio client proxy that we ship to users.
3. **Endpoint URL is user-hostile.** `https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{ESCAPED_ARN}/invocations` — not a URL we can put in docs or give to users without a proxy in front.
4. **Cost advantage is marginal.** Per-CPU-second billing wins for bursty workloads. A steady low-volume gateway isn't bursty — negligible savings.
5. **Vendor lock-in.** Fargate+ALB runs in our VPC with our ALB/ACM/Route53. Container is portable. AgentCore adds AWS-specific runtime concepts (session isolation, 8-hour sessions) we don't currently need.

### What would trigger a revisit

- Claude Desktop/Code adds a native remote MCP client that handles AWS WAF conventions out of the box
- AgentCore adds native per-user secret mapping (Auth0 user → Secrets Manager secret) without container code — eliminating the sidecar
- We reach a scale where per-second CPU billing materially beats Fargate-hours (thousands of users, bursty access)
- AWS ships a friendlier endpoint (custom domain / vanity URL) for AgentCore Runtime

## Acceptance criteria

- [x] Get Notion page from Kirsty — https://www.notion.so/flockcover/How-to-Connect-Claude-to-Looker-2fee4b915259800d841dcc5fd0d27359
- [x] Determine Looker hosting model — **Google Cloud Core**
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
