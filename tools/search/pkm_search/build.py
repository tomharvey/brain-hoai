"""Index builder: walk vault, parse, embed, write to SQLite.

Supports incremental indexing — only new/changed files are re-embedded.
"""

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from .config import (
    CONFIG_PATH,
    DB_PATH,
    MODELS,
    estimate_tokens,
    get_model_config,
    read_config,
    select_model,
    write_config,
)
from .embed import OllamaUnavailable, embed_texts
from .parse import FileData, chunk_file, parse_file
from .schema import connect, create_schema, drop_vector_table

VAULT_ROOT = Path(__file__).resolve().parents[3]

SKIP_DIRS = {".git", ".claude", ".devcontainer", ".obsidian", "tools", "node_modules"}
SKIP_FILES = {"CLAUDE.md", "AGENTS.md", "WORKING.md", "MANIFEST.md", "BOOTSTRAP.md", "README.md"}

BATCH_SIZE = 32


def find_files(vault: Path) -> list[Path]:
    """Walk the vault and return all indexable markdown files."""
    files = []
    for root, dirs, filenames in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = Path(root).relative_to(vault)
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            if rel_root == Path(".") and name in SKIP_FILES:
                continue
            files.append(Path(root) / name)
    return files


def _file_hash(path: Path) -> str:
    """MD5 hash of file content for change detection."""
    return hashlib.md5(path.read_bytes()).hexdigest()


def _resolve_model(args, conf: dict | None, vault: Path) -> tuple[str, bool]:
    """Determine which model to use and whether a full reindex is needed.

    Returns (model_name, needs_full_reindex).
    """
    if conf and args.model and args.model != conf["model"]:
        # Model override requested
        if not args.force:
            print(f"WARNING: Changing model from {conf['model']} to {args.model} requires a full reindex.")
            print("Run with --force to confirm, or remove --model to keep the current model.")
            sys.exit(1)
        print(f"Model change: {conf['model']} → {args.model} (full reindex)")
        return args.model, True

    if conf:
        return conf["model"], False

    # First run — auto-select
    if args.model:
        return args.model, False

    print("First run: analysing vault to select embedding model...")
    md_files = find_files(vault)
    texts = []
    for p in md_files:
        try:
            texts.append(p.read_text(encoding="utf-8"))
        except Exception:
            pass

    model, total, long, pct = select_model(texts)
    print(f"Model selection: {model} ({long}/{total} files exceed 6000 tokens, {pct:.1f}%)")
    return model, False


def build(vault: Path | None = None, args=None) -> None:
    """Build or incrementally update the index."""
    if vault is None:
        vault = VAULT_ROOT
    if args is None:
        args = argparse.Namespace(model=None, force=False)

    start_time = time.time()
    now = datetime.now(timezone.utc).isoformat()
    conf = read_config()

    # Determine model
    model_name, needs_full_reindex = _resolve_model(args, conf, vault)
    model_conf = MODELS[model_name]
    dimensions = model_conf["dimensions"]

    # Determine if DB exists and is usable
    db_exists = DB_PATH.exists()
    fresh_db = not db_exists or needs_full_reindex

    if needs_full_reindex and db_exists:
        DB_PATH.unlink()

    conn = connect(str(DB_PATH))
    if fresh_db:
        create_schema(conn, dimensions)
    elif not fresh_db:
        # Ensure schema is up to date (idempotent IF NOT EXISTS)
        create_schema(conn, dimensions)

    # Build a map of existing files and their hashes
    existing = {}
    if not fresh_db:
        rows = conn.execute("SELECT id, path, file_hash FROM files").fetchall()
        existing = {row[1]: (row[0], row[2]) for row in rows}

    # Walk vault
    md_files = find_files(vault)
    md_paths = set()
    files_indexed = 0
    files_skipped = 0
    files_truncated = 0

    for path in md_files:
        rel_path = str(path.relative_to(vault))
        md_paths.add(rel_path)
        fhash = _file_hash(path)

        # Skip unchanged files
        if rel_path in existing and existing[rel_path][1] == fhash:
            files_skipped += 1
            continue

        # Parse file
        try:
            fd = parse_file(path, vault)
        except Exception as e:
            print(f"  WARN: skipping {rel_path}: {e}", file=sys.stderr)
            continue

        fm = fd.frontmatter
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]

        content_text = fd.body
        token_count = estimate_tokens(content_text)

        # Check truncation
        if token_count > model_conf["context_tokens"]:
            files_truncated += 1
            print(f"  WARN: {rel_path} exceeds context window ({token_count} tokens), will truncate for embedding", file=sys.stderr)

        # Delete old data if updating an existing file
        if rel_path in existing:
            old_id = existing[rel_path][0]
            # FTS5 trigger handles deletion automatically
            conn.execute("DELETE FROM chunks_vec WHERE chunk_id IN (SELECT id FROM chunks WHERE file_id = ?)", (old_id,))
            conn.execute("DELETE FROM chunks WHERE file_id = ?", (old_id,))
            conn.execute("DELETE FROM links WHERE source_id = ?", (old_id,))
            conn.execute("DELETE FROM file_tags WHERE file_id = ?", (old_id,))
            conn.execute("DELETE FROM actions WHERE file_id = ?", (old_id,))
            conn.execute("DELETE FROM files WHERE id = ?", (old_id,))

        # Insert file
        created = fm.get("created")
        updated = fm.get("updated")
        conn.execute(
            """INSERT INTO files (path, title, type, domain, status, owner, created, updated, tags, content, file_hash, token_count, indexed_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                fd.path,
                fm.get("title"),
                fm.get("type"),
                fm.get("domain"),
                fm.get("status"),
                fm.get("owner") or fm.get("assignee"),
                str(created) if created else None,
                str(updated) if updated else None,
                json.dumps(tags),
                fd.body,
                fhash,
                token_count,
                now,
            ),
        )
        file_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        for tag in tags:
            conn.execute("INSERT OR IGNORE INTO file_tags (file_id, tag) VALUES (?, ?)", (file_id, tag))

        for link in fd.links:
            conn.execute(
                "INSERT INTO links (source_id, target_name, display, line_number) VALUES (?, ?, ?, ?)",
                (file_id, link.target, link.display, link.line_number),
            )

        for action in fd.actions:
            conn.execute(
                "INSERT INTO actions (file_id, text, done, line_number, owner) VALUES (?, ?, ?, ?, ?)",
                (file_id, action.text, int(action.done), action.line_number, action.owner),
            )

        # Chunk and prepare for embedding
        chunks = chunk_file(fd)
        for idx, chunk in enumerate(chunks):
            if not chunk.content.strip():
                continue
            conn.execute(
                "INSERT INTO chunks (file_id, heading, chunk_index, content, start_line) VALUES (?, ?, ?, ?, ?)",
                (file_id, chunk.heading, idx, chunk.content, chunk.start_line),
            )

        files_indexed += 1

    conn.commit()

    # Remove stale files (deleted from disk)
    stale_paths = set(existing.keys()) - md_paths
    files_removed = 0
    for stale_path in stale_paths:
        stale_id = existing[stale_path][0]
        conn.execute("DELETE FROM chunks_vec WHERE chunk_id IN (SELECT id FROM chunks WHERE file_id = ?)", (stale_id,))
        conn.execute("DELETE FROM chunks WHERE file_id = ?", (stale_id,))
        conn.execute("DELETE FROM links WHERE source_id = ?", (stale_id,))
        conn.execute("DELETE FROM file_tags WHERE file_id = ?", (stale_id,))
        conn.execute("DELETE FROM actions WHERE file_id = ?", (stale_id,))
        conn.execute("DELETE FROM files WHERE id = ?", (stale_id,))
        files_removed += 1
        print(f"  Removed: {stale_path}", file=sys.stderr)

    conn.commit()

    # Embed all chunks that don't have vectors yet
    unembedded = conn.execute("""
        SELECT c.id, c.content, c.file_id
        FROM chunks c
        LEFT JOIN chunks_vec cv ON cv.chunk_id = c.id
        WHERE cv.chunk_id IS NULL
    """).fetchall()

    embedded_count = 0
    try:
        chunk_ids = [row[0] for row in unembedded]
        chunk_texts = [row[1] for row in unembedded]

        # embed_texts handles truncation internally per-item
        for i in range(0, len(chunk_texts), BATCH_SIZE):
            batch_texts = chunk_texts[i : i + BATCH_SIZE]
            batch_ids = chunk_ids[i : i + BATCH_SIZE]
            embeddings = embed_texts(batch_texts, model_conf)
            for cid, emb in zip(batch_ids, embeddings):
                conn.execute(
                    "INSERT INTO chunks_vec (chunk_id, embedding) VALUES (?, ?)",
                    (cid, json.dumps(emb)),
                )
            embedded_count += len(batch_texts)
            print(f"  Embedded {embedded_count}/{len(chunk_texts)} chunks...", file=sys.stderr)

        conn.commit()
        semantic_status = f"{embedded_count} new embeddings"
    except OllamaUnavailable as e:
        print(f"\n  WARNING: {e}", file=sys.stderr)
        print("  Index built without embeddings. Semantic search disabled until Ollama is available.\n", file=sys.stderr)
        semantic_status = "DISABLED (Ollama unavailable)"

    # Write config (on first run or model change)
    if not conf or needs_full_reindex:
        file_count = conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
        long_count = conn.execute("SELECT COUNT(*) FROM files WHERE token_count > 6000").fetchone()[0]
        pct = (long_count / file_count * 100) if file_count > 0 else 0
        write_config(model_name, str(vault), file_count, long_count, pct)

    # Summary
    elapsed = time.time() - start_time
    total_files = conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    total_chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    total_links = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
    total_actions = conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0]
    total_tags = conn.execute("SELECT COUNT(DISTINCT tag) FROM file_tags").fetchone()[0]
    total_embeddings = conn.execute("SELECT COUNT(*) FROM chunks_vec").fetchone()[0]

    conn.close()

    print(f"\nIndex built: {DB_PATH}")
    print(f"  Model:      {model_name} ({model_conf['ollama_name']})")
    print(f"  Files:      {total_files} ({files_indexed} indexed, {files_skipped} unchanged, {files_removed} removed)")
    if files_truncated:
        print(f"  Truncated:  {files_truncated} files exceeded context window")
    print(f"  Chunks:     {total_chunks}")
    print(f"  Links:      {total_links}")
    print(f"  Actions:    {total_actions}")
    print(f"  Tags:       {total_tags}")
    print(f"  Embeddings: {total_embeddings} ({semantic_status})")
    print(f"  Time:       {elapsed:.1f}s")


def main():
    parser = argparse.ArgumentParser(description="Build PKM vault search index")
    parser.add_argument("vault", nargs="?", default=str(VAULT_ROOT), help="Vault root path")
    parser.add_argument("--model", choices=["nomic", "qwen3"], help="Override embedding model")
    parser.add_argument("--force", action="store_true", help="Force full reindex (required with --model change)")
    args = parser.parse_args()

    build(Path(args.vault), args)


if __name__ == "__main__":
    main()
