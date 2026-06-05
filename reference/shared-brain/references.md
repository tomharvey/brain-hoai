# References & Prior Art

> Sources that informed this strawman set, captured so the design is **auditable** — the
> same discipline the Rosenfeld vault applies (decisions link to evidence; carousels ship a
> `CONTEXT.md`). Some links are stable top-level docs rather than deep paths; verify version
> specifics at build time.

## Prior art — internal (the patterns this reuses)

The whole approach is the Rosenfeld vault's architecture re-pointed at sales objects:

- `CLAUDE.md` — the project-OS framing and conventions.
- `reference/ontology.md` — typed entity-and-edge schema (model for the sales ontology).
- `tools/vaultdb.py` — the deterministic query layer + `lint` gate (model for the thin MCP's
  enforcement role).
- Skills `/improve-skill` and `/review` — the model for the self-inspection / self-improving
  loop.
- `/linkedin-carousel`'s `CONTEXT.md` habit — the model for *this* references file.

## Platforms & storage

- **Notion for Developers** — https://www.notion.com/product/dev · API:
  https://developers.notion.com — knowledge/graph store + non-technical UX; databases =
  objects, properties = fields, relations = edges.
- **Official Notion MCP server** — Notion's hosted MCP; how Claude reads/writes Notion
  natively (see Notion developer docs above).
- **Airtable** — https://airtable.com · API:
  https://airtable.com/developers/web/api/introduction — the stricter-schema alternative
  weighed against Notion for a pure CRM.
- **HubSpot Developers** — https://developers.hubspot.com — existing CRM; transactional SoT
  in the A+C hybrid; has its own MCP already wired to Claude.
- **AWS — derived-data + compute plane:**
  - CloudWatch (Logs, Logs Insights, EMF/Metrics, alarms) —
    https://docs.aws.amazon.com/AmazonCloudWatch/ — telemetry store.
  - Athena — https://aws.amazon.com/athena/ — deep log mining over S3 (reuses existing
    Rosenfeld competency).
  - Amazon S3 — https://aws.amazon.com/s3/ — log archive / Athena source.
  - OpenSearch Service — https://aws.amazon.com/opensearch-service/ — candidate derived
    search index (search decision #4, option b).
  - Amazon Bedrock — https://aws.amazon.com/bedrock/ — candidate embeddings for hybrid
    semantic search.

## MCP & skills

- **Model Context Protocol** — https://modelcontextprotocol.io — the control-plane standard
  the thin MCP implements.
- **MCP Prompts primitive** — https://modelcontextprotocol.io/docs/concepts/prompts —
  the *supported-today* way to deliver guided, parameterized workflows ("skills") through a
  server. (Verify client-surface support — solid in Claude Code; confirm for claude.ai
  connectors.)
- **Anthropic Agent Skills** (`SKILL.md`) — the format used by the vault's `.claude/skills/`;
  supported on Claude Code and claude.ai today.
- **Skills Over MCP — Working Group (experimental, NOT ratified):**
  - Charter — https://modelcontextprotocol.io/community/skills-over-mcp/charter
  - `experimental-ext-skills` repo —
    https://github.com/modelcontextprotocol/experimental-ext-skills
  - **SEP-2640 — Skills Extension** (Extensions Track, draft) —
    https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2640 — the signal to
    watch before adopting skills-over-MCP as the distribution mechanism.
  - Interest-group notes (Feb 2026) —
    https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2316

## How references map to decisions

| Reference | Informs |
|---|---|
| Notion API / MCP, Airtable | Store choice (stack register #1) |
| HubSpot Developers | HubSpot strategy A+C (#2), identity/join keys (#9) |
| CloudWatch / Athena / S3 | Telemetry store (#5), self-improving loop |
| OpenSearch / Bedrock | Search: derived index (#4, option b) |
| MCP Prompts / Agent Skills / SEP-2640 | Delivering skills to the team (Prompts now → Skills Extension later) |
| vaultdb / ontology.md / `/improve-skill` | The entire reused architecture |
