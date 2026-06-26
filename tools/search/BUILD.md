# Build: Vault Search with Ollama + SQLite

Build a local search system for a markdown vault. The vault contains 100+ markdown files with YAML frontmatter, wikilinks, and a folder hierarchy. The goal is hybrid search (keyword + semantic) and structured frontmatter queries, accessible via a Claude Code skill.

## Design decisions and rationale

**Why Ollama + SQLite, not QMD or a vector database:**
- QMD uses node-llama-cpp for embeddings, which fails to compile on ARM64 (our target is a Radxa Rock 5C). Ollama runs natively on ARM64 with no compilation issues.
- SQLite is a single file, zero-config, and provides both FTS5 (full-text search) and sqlite-vec (vector similarity) in one database. No separate vector DB daemon to run.
- A custom Python approach lets us index frontmatter as structured columns, which is critical — many vault queries are relational ("show me all active initiatives in the product-ai domain") not semantic.

**Embedding model selection — one-time decision at bootstrap:**

Two candidate models are available:

- **nomic-embed-text v1.5** (137M params, 274MB, 768 dimensions, 8192 token context): Best English retrieval quality per benchmark for short-to-medium content. Fastest to embed on CPU. Fully open (weights, training code, and training data all public).
- **qwen3-embedding:0.6b** (0.6B params, 639MB, 1024 dimensions, 32K token context): Instruction-aware, 32K context captures entire long transcripts without truncation. Slightly behind nomic on pure English retrieval benchmarks but the context length advantage is decisive for long documents.

Rather than picking per-file (which doubles query-time latency and adds schema complexity), the indexer analyses the vault once at first run, counts how many files exceed 6000 tokens, and picks one model for the entire vault:

- If **fewer than 10% of files** exceed 6000 tokens: use **nomic-embed-text** (better retrieval quality, faster, smaller)
- If **10% or more of files** exceed 6000 tokens: use **qwen3-embedding:0.6b** (captures full content of long files, handles short files adequately)

The chosen model is recorded in a config file (`~/.vault-search/[vault-name].conf`) so subsequent indexing runs use the same model without re-analysing. The model can be overridden manually by editing the config or passing `--model nomic` or `--model qwen3` to the indexer. Changing the model requires a full reindex (the script should handle this automatically — drop and recreate the vector table).

**Why hybrid search (FTS5 + vector), not just one:**
- Keyword search (FTS5) excels at exact matches — finding a specific person's name, a ticket number like ROS-38, or a phrase you remember writing. Semantic search misses these.
- Semantic search (vector similarity) excels at conceptual queries — "what have I written about vendor lock-in?" finds notes that discuss the concept without using those exact words. Keyword search misses these.
- Reciprocal Rank Fusion (RRF) merges both ranked result lists into a single ranking that's better than either alone.

**Why per-file embedding, not per-chunk:**
- At 100-500 files, most fit within at least one model's context window (8K or 32K).
- Per-file embedding preserves document coherence and makes attribution trivial — every search result is a file, not an anonymous chunk.
- If a file exceeds the selected model's context window, embed the first N tokens (where N is the model's limit). This should be rare — qwen3's 32K limit covers essentially any single document.

## Prerequisites

Assume Ollama is already installed and running on the machine with both models pulled:
```
ollama pull nomic-embed-text
ollama pull qwen3-embedding:0.6b
```

Assume Python 3.11+ is available. Use pip for dependencies.

## What to build

### 1. Database schema

Create a SQLite database. The per-vault DB path is derived from the vault root: `~/.vault-search/[vault-name].db` (e.g. `head-of-ai-os.db`, `rosenfeld.db`).

**`documents` table:**
- `id` INTEGER PRIMARY KEY
- `path` TEXT UNIQUE — relative path from vault root
- `title` TEXT — from frontmatter
- `doc_type` TEXT — from frontmatter `type` field
- `domain` TEXT — from frontmatter `domain` field
- `status` TEXT — from frontmatter `status` field
- `tags` TEXT — JSON array of tags from frontmatter
- `created` TEXT — from frontmatter
- `updated` TEXT — from frontmatter
- `content` TEXT — full raw markdown content (for display/context)
- `frontmatter_json` TEXT — full frontmatter as JSON (for arbitrary field queries)
- `token_count` INTEGER — approximate token count of the content
- `file_hash` TEXT — MD5 of file content for change detection
- `indexed_at` TEXT — timestamp of last indexing

**`documents_fts` virtual table (FTS5):**
- Full-text index over `title` and `content` columns from `documents` table
- Use `content=documents` and `content_rowid=id` to keep it sync'd

**`documents_vec` virtual table (sqlite-vec):**
- Vector dimensions depend on selected model: 768 for nomic, 1024 for qwen3
- Linked to `documents.id`

### 2. Config file

Store the model selection at `~/.vault-search/[vault-name].conf` as a simple key-value file:

```
model=nomic
dimensions=768
vault_path=/home/tom/head-of-ai-os
created=2026-04-10
files_analysed=142
long_files=3
long_file_pct=2.1
```

This is written once at first index and read on subsequent runs.

### 3. Token counting

Use a simple heuristic for token estimation: `len(text.split()) * 1.3`. This is rough but sufficient for the model selection threshold. No need to pull in a tokenizer library.

### 4. Indexer script: `vault_index.py`

A Python script that:

1. Accepts a vault root path as argument (default: current directory).
2. Derives the vault name from the directory name for DB and config file paths.
3. **First run (no config file exists):**
   - Walk all `.md` files, skipping `.git/`, `.claude/`, `.obsidian/`, `node_modules/`, and any file named `CLAUDE.md`, `AGENTS.md`, `WORKING.md`, `MANIFEST.md`.
   - Estimate token count for each file.
   - Count how many exceed 6000 tokens.
   - If fewer than 10% exceed 6000 tokens: select `nomic-embed-text` (768 dims).
   - If 10% or more exceed 6000 tokens: select `qwen3-embedding:0.6b` (1024 dims).
   - Print the decision: `"Model selection: [model] (N/M files exceed 6000 tokens, P%)"`
   - Write the config file.
   - Create the database with the appropriate vector dimensions.
   - Proceed to index all files.
4. **Subsequent runs (config file exists):**
   - Read model selection from config.
   - If `--model nomic` or `--model qwen3` is passed and differs from config, print a warning that this will trigger a full reindex, ask for confirmation (or accept `--force`), update config, drop and recreate the vector table, and reindex everything.
5. **Indexing each file:**
   - Parse YAML frontmatter (use `python-frontmatter` library).
   - Hash the content (MD5).
   - Check if the file already exists in the DB with the same hash — skip if unchanged.
   - Estimate token count.
   - Upsert the row into `documents`.
   - Update the FTS5 index.
   - Call Ollama's local API (`POST http://localhost:11434/api/embed`) with the configured model and the full file content as input.
     - For nomic: prefix content with `search_document: `
     - For qwen3: prefix content with `Instruct: Represent this document for retrieval\n`
   - If the file exceeds the model's context window (8192 for nomic, 32768 for qwen3), truncate to the limit before embedding. Log a warning for these files.
   - Store the embedding in `documents_vec`.
6. Remove any rows from the DB whose files no longer exist on disk.
7. Print a summary: model used, files indexed, files skipped (unchanged), files removed, files truncated (if any), time taken.

Dependencies: `python-frontmatter`, `sqlite-vec`, `requests`.

Install sqlite-vec via: `pip install sqlite-vec`

To load sqlite-vec in Python:
```python
import sqlite_vec
db = sqlite3.connect("vault.db")
db.enable_load_extension(True)
sqlite_vec.load(db)
```

### 5. Search script: `vault_search.py`

A Python script that accepts a query string and returns ranked results. It reads the config file to know which model and dimensions to use.

**`--mode semantic`**: Embed the query via Ollama with the configured model, then find the top-K nearest vectors in `documents_vec` using cosine distance.
- For nomic: prefix query with `search_query: `
- For qwen3: prefix query with `Instruct: Given a search query, retrieve relevant documents\nQuery: `

**`--mode keyword`**: Use FTS5 `MATCH` query against `documents_fts`. Return results ranked by BM25.

**`--mode hybrid`** (default): Run both semantic and keyword searches, then merge results using Reciprocal Rank Fusion:
```
RRF_score(doc) = sum(1 / (k + rank_in_list)) for each list the doc appears in
```
Use k=60 (standard RRF constant).

**`--mode structured`**: Accept a SQL-like filter expression and query the `documents` table directly. Examples:
- `--mode structured --filter "doc_type='initiative' AND status='active'"`
- `--mode structured --filter "domain='product-ai'"`
- `--mode structured --filter "tags LIKE '%icp%'"`
- `--mode structured --filter "token_count > 6000"` (find long documents)

All modes accept:
- `--top-k N` (default 10)
- `--vault PATH` (default current directory, used to resolve the DB and config location)
- `--show-content` flag to print the first 500 chars of each result's content

Output format for each result:
```
[score] path/to/file.md — Title (type, status)
```

### 6. Claude Code skill: `.claude/skills/search.md`

Create a skill file that teaches Claude Code how to use the search scripts:

```markdown
# /search — Search the vault

Search across all vault notes using hybrid keyword + semantic search.

## When to use

When you need to find notes, trace cross-references, or answer questions about what's in the vault.

## How to use

Run the search from the vault root:

### Hybrid search (default, best for most queries)
python ~/.vault-search/vault_search.py "query" --mode hybrid

### Find conceptually related notes
python ~/.vault-search/vault_search.py "query" --mode semantic

### Find exact phrases or names
python ~/.vault-search/vault_search.py "query" --mode keyword

### Find by frontmatter fields
python ~/.vault-search/vault_search.py --mode structured --filter "doc_type='initiative' AND status='active'"
python ~/.vault-search/vault_search.py --mode structured --filter "domain='engineering-workflows'"
python ~/.vault-search/vault_search.py --mode structured --filter "tags LIKE '%icp%'"

### Show content preview
Add --show-content to any search to see the first 500 chars of each result.

## Notes

- Hybrid mode combines keyword and semantic search using Reciprocal Rank Fusion. Use this by default.
- Semantic search requires Ollama running with the configured embedding model.
- The embedding model was selected automatically at first index based on vault content. Check ~/.vault-search/[vault-name].conf to see which model is active.
- The index lives at ~/.vault-search/[vault-name].db. Run /reindex after creating or editing files.
- Structured mode queries frontmatter fields directly — useful for filtering by type, status, domain, or tags.
```

### 7. Claude Code skill: `.claude/skills/reindex.md`

```markdown
# /reindex — Reindex the vault for search

Rebuild the search index after creating, editing, or deleting notes.

## When to use

Run this when search results feel stale, or after a session where you've created or edited multiple files. The indexer skips unchanged files (hash check), so it's fast to run frequently — only new or modified files are re-embedded.

## How to use

python ~/.vault-search/vault_index.py /path/to/vault

## To change the embedding model

python ~/.vault-search/vault_index.py /path/to/vault --model qwen3 --force
python ~/.vault-search/vault_index.py /path/to/vault --model nomic --force

This triggers a full reindex with the new model.
```

## File locations

- `~/.vault-search/vault_index.py` — indexer script
- `~/.vault-search/vault_search.py` — search script
- `~/.vault-search/[vault-name].db` — SQLite database (per-vault, auto-created)
- `~/.vault-search/[vault-name].conf` — model config (per-vault, auto-created)
- `.claude/skills/search.md` — Claude Code skill (in each vault that uses it)
- `.claude/skills/reindex.md` — Claude Code skill (in each vault that uses it)

## Testing

After building everything:

1. Run the indexer against a vault: `python ~/.vault-search/vault_index.py /path/to/vault`
2. Confirm it prints the model selection decision with file count breakdown.
3. Check the config file: `cat ~/.vault-search/[vault-name].conf`
4. Verify hybrid: `python ~/.vault-search/vault_search.py "ICP trading desk" --mode hybrid --top-k 5`
5. Verify structured: `python ~/.vault-search/vault_search.py --mode structured --filter "doc_type='contact'"`
6. Verify keyword: `python ~/.vault-search/vault_search.py "Gerard Reid" --mode keyword`
7. Verify semantic: `python ~/.vault-search/vault_search.py "vendor lock-in and model flexibility" --mode semantic`
8. Test model override: `python ~/.vault-search/vault_index.py /path/to/vault --model qwen3 --force` — confirm it reindexes everything and updates the config.