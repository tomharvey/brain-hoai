---
name: reindex
description: Reindex the vault for search after creating, editing, or deleting notes
---

# /reindex — Reindex the vault for search

Rebuild the search index after creating, editing, or deleting notes.

## When to use

Run this when search results feel stale, or after a session where you've created or edited multiple files. The indexer skips unchanged files (hash check), so it's fast to run frequently — only new or modified files are re-embedded.

## Steps

1. Run the indexer:
```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.build /workspaces/pkm
```

2. Review the summary output — it shows files indexed, skipped (unchanged), and removed.

## To change the embedding model

```bash
cd /workspaces/pkm/tools/search && python -m pkm_search.build /workspaces/pkm --model qwen3 --force
cd /workspaces/pkm/tools/search && python -m pkm_search.build /workspaces/pkm --model nomic --force
```

This triggers a full reindex with the new model.
