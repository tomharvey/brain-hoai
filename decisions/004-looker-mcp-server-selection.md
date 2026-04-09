---
title: "Looker MCP server selection: googleapis/mcp-toolbox over Ultrathink"
created: 2026-04-09
updated: 2026-04-09
domain: operational-tooling
type: decision
status: active
tags: [looker, mcp, infrastructure, architecture]
---

## Context

Kirsty Alexandre has a working Looker→Claude connection via MCP running locally. To scale this to 20+ users we need a production multi-user deployment. Two Looker MCP servers were evaluated.

## Decision

**Use [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) with the `looker` prebuilt.**

## Options considered

### Option 1: googleapis/mcp-toolbox (chosen)

- `looker` prebuilt: 18 tools covering the full analytical workflow (model exploration, querying, Looks, dashboards, embedding)
- `looker-dev` prebuilt: 23 tools for LookML development (optional, not needed for business users)
- `looker-conversational-analytics` prebuilt: 3 tools for natural language queries via Gemini (optional)
- Multi-user via `use_client_oauth=true` — per-request OAuth token forwarding
- Maintained by Google (Looker's parent company)

### Option 2: Ultrathink-Solutions/looker-mcp-server (rejected)

- 98 tools across 10 groups (explore, query, schema, content, board, folder, modeling, git, admin)
- Multi-user via admin sudo or OAuth pass-through
- Third-party, very new (April 2026, 1 star)

## Why googleapis wins

### The 98 vs 18 tool gap is misleading

| Category | Ultrathink tools | Relevant? |
|----------|-----------------|-----------|
| Admin (users, roles, permissions, groups) | 36 (37% of total) | No — Looker admin, not analytics |
| CRUD variants (update/delete on existing tools) | ~15 | Minor |
| Overlap with googleapis looker-dev | ~15 | No — googleapis does it better |
| Folders + Boards | 22 | Maybe — only if deep folder browsing needed |
| Genuinely new analytical tools | ~5 | Marginal — content search, scheduled delivery |

### googleapis is better for the analytical use case

1. **Explore handling** — dedicated `get_filters` and `get_parameters` tools that Ultrathink lacks. These surface LookML filter-only fields and dynamic parameters. Critical given Kirsty's curated explores are key to good results.
2. **LLM-optimised tool descriptions** — explicitly explains the Looker data model, helping Claude navigate model → explore → fields → query.
3. **Fewer tools = better tool selection** — 18 focused tools means Claude picks the right one more often. 98 tools pollutes the context and increases wrong-tool selection.
4. **Maintained by Google** vs a 1-star third-party project.
5. **Conversational analytics** — optional Gemini-powered natural language queries. Ultrathink has no equivalent.
6. **Already in use** — Kirsty runs this today. No migration, no retraining.

## Consequences

- Deploy googleapis/mcp-toolbox in HTTP mode with `use_client_oauth=true`
- Need an auth gateway in front to handle OAuth token exchange
- If we later need folder browsing, boards, or scheduled delivery, we can add custom tool definitions in YAML — the toolbox supports this without switching servers

## Links

- [[AI-010-looker-mcp-cloud-deployment]]
- [[2026-04-09-kirsty-ai-discovery]]
- [[kirsty]]
