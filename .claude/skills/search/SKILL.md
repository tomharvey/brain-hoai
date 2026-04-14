---
name: search
description: Search across all vault notes using hybrid keyword + semantic search
---

# /search — Search the vault

Search across all vault notes using hybrid keyword + semantic search.

## When to use

When you need to find notes, trace cross-references, or answer questions about what's in the vault.

## How to use

Run from the `tools/search` directory:

### Hybrid search (default, best for most queries)
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.query "query" --mode hybrid
```

### Find conceptually related notes
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.query "query" --mode semantic
```

### Find exact phrases or names
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.query "query" --mode keyword
```

### Structured queries (graph and metadata)
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured open-actions
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "actions-for tom"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "links-to person-name"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "by-type initiative"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "by-domain product-ai"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "by-status active"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "by-tag icp"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured orphans
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured "recent 14"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured unlinked-meetings
```

### Filter by frontmatter fields (raw SQL)
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured --filter "type='initiative' AND status='active'"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured --filter "domain='product-ai'"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured --filter "tags LIKE '%icp%'"
cd /workspaces/pkm/tools/search && python -m pkm_search.query --mode structured --filter "token_count > 6000"
```

### Show content preview
Add `--show-content` to hybrid or keyword searches to see the first 500 chars of each result.

## Notes

- Hybrid mode combines keyword (FTS5) and semantic (vector) search using Reciprocal Rank Fusion. Use this by default.
- Results show `[K]` for keyword match, `[S]` for semantic match, `[K+S]` for both.
- Semantic search requires Ollama running with the configured embedding model.
- The embedding model was auto-selected at first index. Check `tools/search/pkm.conf` to see which model is active.
- The index lives at `tools/search/pkm.db`. Run `/reindex` after creating or editing files.
