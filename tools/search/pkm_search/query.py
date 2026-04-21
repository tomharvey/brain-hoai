"""Query CLI: semantic, keyword, hybrid (RRF), and structured modes."""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

from .config import DB_PATH, get_model_config, read_config
from .schema import connect


def _check_db() -> sqlite3.Connection:
    if not DB_PATH.exists():
        print("ERROR: No index found. Run: python -m pkm_search.build", file=sys.stderr)
        sys.exit(1)
    return connect(str(DB_PATH))


def _has_embeddings(conn: sqlite3.Connection) -> bool:
    count = conn.execute("SELECT COUNT(*) FROM chunks_vec").fetchone()[0]
    return count > 0


# --- Semantic search ---

def search_semantic(conn: sqlite3.Connection, query: str, limit: int = 10) -> list[tuple[str, float]]:
    """Semantic vector search. Returns list of (path, score) tuples."""
    if not _has_embeddings(conn):
        return []

    conf = read_config()
    model_conf = get_model_config(conf)
    from .embed import embed_query

    vec = embed_query(query, model_conf)
    rows = conn.execute(
        """
        SELECT f.path, cv.distance
        FROM chunks_vec cv
        JOIN chunks c ON c.id = cv.chunk_id
        JOIN files f ON f.id = c.file_id
        WHERE embedding MATCH ?
        AND k = ?
        ORDER BY distance
        """,
        (json.dumps(vec), limit * 3),  # fetch extra to deduplicate by file
    ).fetchall()

    # Deduplicate by file path, keep best score
    seen = {}
    for path, distance in rows:
        score = 1 - distance
        if path not in seen or score > seen[path]:
            seen[path] = score

    ranked = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:limit]
    return ranked


def search_semantic_detailed(conn: sqlite3.Connection, query: str, limit: int = 10) -> str:
    """Semantic search with full output formatting."""
    if not _has_embeddings(conn):
        return "ERROR: No embeddings in index. Rebuild with Ollama running: python -m pkm_search.build"

    conf = read_config()
    model_conf = get_model_config(conf)
    from .embed import embed_query

    vec = embed_query(query, model_conf)
    rows = conn.execute(
        """
        SELECT cv.distance, c.content, c.heading, c.start_line, f.*
        FROM chunks_vec cv
        JOIN chunks c ON c.id = cv.chunk_id
        JOIN files f ON f.id = c.file_id
        WHERE embedding MATCH ?
        AND k = ?
        ORDER BY distance
        """,
        (json.dumps(vec), limit),
    ).fetchall()

    if not rows:
        return "No results found."

    cols = ["distance", "chunk_content", "heading", "start_line",
            "id", "path", "title", "type", "domain", "status", "owner",
            "created", "updated", "tags", "content", "file_hash", "token_count", "indexed_at"]

    output = [f"## Semantic Search Results ({len(rows)} matches)\n"]
    for i, row in enumerate(rows, 1):
        d = dict(zip(cols, row))
        score = 1 - d["distance"]
        heading_ctx = f" (§ {d['heading']})" if d["heading"] else ""
        output.append(f"### {i}. {d['path']}:{d['start_line']}{heading_ctx} (score: {score:.3f})")
        meta = []
        if d.get("title"):
            meta.append(f"Title: {d['title']}")
        if d.get("type"):
            meta.append(f"Type: {d['type']}")
        if d.get("domain"):
            meta.append(f"Domain: {d['domain']}")
        if d.get("status"):
            meta.append(f"Status: {d['status']}")
        if meta:
            output.append(" | ".join(meta))
        excerpt = d["chunk_content"][:500]
        output.append(f"\n> {excerpt}...\n")

    return "\n".join(output)


# --- Keyword search (FTS5) ---

def search_keyword(conn: sqlite3.Connection, query: str, limit: int = 10) -> list[tuple[str, float]]:
    """FTS5 keyword search. Returns list of (path, bm25_score) tuples."""
    rows = conn.execute(
        """
        SELECT f.path, files_fts.rank
        FROM files_fts
        JOIN files f ON f.id = files_fts.rowid
        WHERE files_fts MATCH ?
        ORDER BY files_fts.rank
        LIMIT ?
        """,
        (query, limit),
    ).fetchall()

    # FTS5 rank is negative (lower = better), convert to positive score
    return [(path, -rank) for path, rank in rows]


def search_keyword_detailed(conn: sqlite3.Connection, query: str, limit: int = 10,
                            show_content: bool = False) -> str:
    """FTS5 keyword search with full output formatting."""
    rows = conn.execute(
        """
        SELECT f.path, f.title, f.type, f.status, f.domain, f.content,
               files_fts.rank, snippet(files_fts, 1, '**', '**', '...', 40) as snippet
        FROM files_fts
        JOIN files f ON f.id = files_fts.rowid
        WHERE files_fts MATCH ?
        ORDER BY files_fts.rank
        LIMIT ?
        """,
        (query, limit),
    ).fetchall()

    if not rows:
        return "No results found."

    output = [f"## Keyword Search Results ({len(rows)} matches)\n"]
    for i, (path, title, ftype, status, domain, content, rank, snippet) in enumerate(rows, 1):
        score = -rank
        meta_parts = [x for x in [ftype, status] if x]
        meta = f" ({', '.join(meta_parts)})" if meta_parts else ""
        output.append(f"[{score:.3f}] {path} — {title or '(no title)'}{meta}")
        if snippet:
            output.append(f"> {snippet}")
        if show_content and content:
            output.append(f"\n{content[:500]}...\n")
        output.append("")

    return "\n".join(output)


# --- Hybrid search (RRF) ---

def search_hybrid(conn: sqlite3.Connection, query: str, limit: int = 10,
                  show_content: bool = False) -> str:
    """Hybrid search: FTS5 + vector, merged with Reciprocal Rank Fusion."""
    RRF_K = 60

    # Get keyword results
    keyword_results = search_keyword(conn, query, limit=limit * 2)

    # Get semantic results
    semantic_results = search_semantic(conn, query, limit=limit * 2)

    if not keyword_results and not semantic_results:
        return "No results found."

    # Build RRF scores
    rrf_scores: dict[str, float] = {}

    for rank, (path, _score) in enumerate(keyword_results, 1):
        rrf_scores[path] = rrf_scores.get(path, 0) + 1 / (RRF_K + rank)

    for rank, (path, _score) in enumerate(semantic_results, 1):
        rrf_scores[path] = rrf_scores.get(path, 0) + 1 / (RRF_K + rank)

    # Sort by RRF score
    ranked = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:limit]

    # Determine which lists each result appeared in
    keyword_paths = {p for p, _ in keyword_results}
    semantic_paths = {p for p, _ in semantic_results}

    # Fetch metadata for results
    output = [f"## Hybrid Search Results ({len(ranked)} matches)\n"]
    for i, (path, rrf_score) in enumerate(ranked, 1):
        row = conn.execute(
            "SELECT id, title, type, domain, status, content FROM files WHERE path = ?",
            (path,),
        ).fetchone()
        if not row:
            continue

        fid, title, ftype, domain, status, content = row

        # Source indicators
        sources = []
        if path in keyword_paths:
            sources.append("K")
        if path in semantic_paths:
            sources.append("S")
        source_str = "+".join(sources)

        meta_parts = [x for x in [ftype, status] if x]
        meta = f" ({', '.join(meta_parts)})" if meta_parts else ""
        output.append(f"### {i}. [{source_str}] {path} — {title or '(no title)'}{meta} (rrf: {rrf_score:.4f})")

        if domain:
            output.append(f"Domain: {domain}")

        if show_content and content:
            output.append(f"\n> {content[:500]}...\n")

        # Graph context: incoming links
        incoming = conn.execute("""
            SELECT DISTINCT f2.path FROM links l
            JOIN files f2 ON f2.id = l.source_id
            WHERE l.target_name IN (
                SELECT REPLACE(REPLACE(?, '.md', ''), '/', '-')
                UNION SELECT REPLACE(?, '.md', '')
            )
            AND f2.id != ?
            LIMIT 5
        """, (path, path.split("/")[-1], fid)).fetchall()
        if incoming:
            output.append(f"Linked from: {', '.join(r[0] for r in incoming)}")

        # Open actions count
        action_count = conn.execute(
            "SELECT COUNT(*) FROM actions WHERE file_id = ? AND done = 0", (fid,)
        ).fetchone()[0]
        if action_count:
            output.append(f"Open actions: {action_count}")

        output.append("")

    return "\n".join(output)


# --- Structured queries ---

def query_open_actions(conn: sqlite3.Connection) -> str:
    rows = conn.execute("""
        SELECT a.text, a.line_number, a.owner, f.path, f.title
        FROM actions a
        JOIN files f ON f.id = a.file_id
        WHERE a.done = 0
        ORDER BY f.path, a.line_number
    """).fetchall()

    if not rows:
        return "No open actions found."

    output = [f"## Open Actions ({len(rows)} total)\n"]
    current_path = None
    for text, line, owner, path, title in rows:
        if path != current_path:
            current_path = path
            output.append(f"\n### {path}")
            if title:
                output.append(f"*{title}*\n")
        owner_str = f" [{owner}]" if owner else ""
        output.append(f"- [ ] {text}{owner_str} (line {line})")

    return "\n".join(output)


def query_actions_for(conn: sqlite3.Connection, person: str) -> str:
    rows = conn.execute("""
        SELECT a.text, a.line_number, f.path, f.title
        FROM actions a
        JOIN files f ON f.id = a.file_id
        WHERE a.done = 0 AND a.owner = ?
        ORDER BY f.path, a.line_number
    """, (person.lower(),)).fetchall()

    if not rows:
        return f"No open actions found for '{person}'."

    output = [f"## Open Actions for {person} ({len(rows)} total)\n"]
    for text, line, path, title in rows:
        output.append(f"- [ ] {text}\n  {path}:{line}")

    return "\n".join(output)


def query_links_to(conn: sqlite3.Connection, name: str) -> str:
    rows = conn.execute("""
        SELECT DISTINCT f.path, f.title, f.type, l.line_number
        FROM links l
        JOIN files f ON f.id = l.source_id
        WHERE l.target_name = ?
        ORDER BY f.path
    """, (name,)).fetchall()

    if not rows:
        return f"No files link to '{name}'."

    output = [f"## Files linking to '{name}' ({len(rows)} files)\n"]
    for path, title, ftype, line in rows:
        output.append(f"- {path}:{line} — {title or '(no title)'} [{ftype or '?'}]")

    return "\n".join(output)


def query_links_from(conn: sqlite3.Connection, name: str) -> str:
    rows = conn.execute("""
        SELECT l.target_name, l.display, l.line_number
        FROM links l
        JOIN files f ON f.id = l.source_id
        WHERE f.path LIKE ?
        ORDER BY l.line_number
    """, (f"%{name}%",)).fetchall()

    if not rows:
        return f"No outgoing links found from files matching '{name}'."

    output = [f"## Outgoing links from '{name}' ({len(rows)} links)\n"]
    for target, display, line in rows:
        display_str = f" ({display})" if display else ""
        output.append(f"- [[{target}]]{display_str} (line {line})")

    return "\n".join(output)


def query_orphans(conn: sqlite3.Connection) -> str:
    rows = conn.execute("""
        SELECT f.path, f.title, f.type
        FROM files f
        WHERE f.id NOT IN (
            SELECT DISTINCT f2.id
            FROM files f2
            JOIN links l ON l.target_name = REPLACE(REPLACE(f2.path, '.md', ''), '/', '-')
            UNION
            SELECT DISTINCT f3.id
            FROM files f3
            JOIN links l2 ON f3.path LIKE '%/' || l2.target_name || '.md'
        )
        ORDER BY f.path
    """).fetchall()

    if not rows:
        return "No orphan files found."

    output = [f"## Orphan Files ({len(rows)} files with no incoming links)\n"]
    for path, title, ftype in rows:
        output.append(f"- {path} — {title or '(no title)'} [{ftype or '?'}]")

    return "\n".join(output)


def query_recent(conn: sqlite3.Connection, days: int = 7) -> str:
    rows = conn.execute("""
        SELECT path, title, type, domain, status, updated
        FROM files
        WHERE updated >= date('now', ?)
        ORDER BY updated DESC
    """, (f"-{days} days",)).fetchall()

    if not rows:
        return f"No files updated in the last {days} days."

    output = [f"## Recently Updated ({len(rows)} files in last {days} days)\n"]
    for path, title, ftype, domain, status, updated in rows:
        meta = " | ".join(filter(None, [ftype, domain, status]))
        output.append(f"- {path} — {title or '(no title)'} [{meta}] (updated: {updated})")

    return "\n".join(output)


def query_by_field(conn: sqlite3.Connection, field: str, value: str) -> str:
    valid_fields = {"status", "type", "domain", "owner"}
    if field not in valid_fields:
        return f"ERROR: Invalid field '{field}'. Use one of: {', '.join(valid_fields)}"

    rows = conn.execute(f"""
        SELECT path, title, type, domain, status, owner, updated
        FROM files
        WHERE {field} = ?
        ORDER BY updated DESC
    """, (value,)).fetchall()

    if not rows:
        return f"No files with {field} = '{value}'."

    output = [f"## Files where {field} = '{value}' ({len(rows)} files)\n"]
    for path, title, ftype, domain, status, owner, updated in rows:
        meta = " | ".join(filter(None, [ftype, domain, status, f"owner: {owner}" if owner else None]))
        output.append(f"- {path} — {title or '(no title)'} [{meta}]")

    return "\n".join(output)


def query_by_tag(conn: sqlite3.Connection, tag: str) -> str:
    rows = conn.execute("""
        SELECT f.path, f.title, f.type, f.domain, f.status
        FROM file_tags ft
        JOIN files f ON f.id = ft.file_id
        WHERE ft.tag = ?
        ORDER BY f.updated DESC
    """, (tag,)).fetchall()

    if not rows:
        return f"No files with tag '{tag}'."

    output = [f"## Files tagged '{tag}' ({len(rows)} files)\n"]
    for path, title, ftype, domain, status in rows:
        meta = " | ".join(filter(None, [ftype, domain, status]))
        output.append(f"- {path} — {title or '(no title)'} [{meta}]")

    return "\n".join(output)


def query_unlinked_meetings(conn: sqlite3.Connection) -> str:
    rows = conn.execute("""
        SELECT f.path, f.title, f.updated
        FROM files f
        WHERE f.type = 'meeting'
        AND f.id NOT IN (
            SELECT DISTINCT source_id FROM links
            WHERE target_name LIKE 'AI-%'
        )
        ORDER BY f.updated DESC
    """).fetchall()

    output = [f"## Meetings with no linked issues ({len(rows)} meetings)\n"]
    for path, title, updated in rows:
        output.append(f"- {path} — {title or '(no title)'} (updated: {updated})")

    return "\n".join(output)


def query_filter(conn: sqlite3.Connection, filter_expr: str) -> str:
    """Raw SQL filter against the files table."""
    # Whitelist allowed column names to prevent injection
    allowed_cols = {"title", "type", "domain", "status", "owner", "tags",
                    "created", "updated", "token_count", "path"}

    try:
        rows = conn.execute(f"""
            SELECT path, title, type, domain, status, owner, updated
            FROM files
            WHERE {filter_expr}
            ORDER BY updated DESC
        """).fetchall()
    except Exception as e:
        return f"ERROR: Invalid filter expression: {e}"

    if not rows:
        return f"No files matching: {filter_expr}"

    output = [f"## Filter: {filter_expr} ({len(rows)} files)\n"]
    for path, title, ftype, domain, status, owner, updated in rows:
        meta = " | ".join(filter(None, [ftype, domain, status, f"owner: {owner}" if owner else None]))
        output.append(f"- {path} — {title or '(no title)'} [{meta}]")

    return "\n".join(output)


# --- CLI dispatch ---

STRUCTURED_COMMANDS = {
    "open-actions": "List all unchecked action items",
    "links-to": "Find files linking to <name>",
    "links-from": "Find outgoing links from <name>",
    "orphans": "Find files with no incoming links",
    "recent": "Recently updated files (optional: number of days)",
    "by-status": "Filter files by status <value>",
    "by-type": "Filter files by type <value>",
    "by-domain": "Filter files by domain <value>",
    "by-owner": "Filter files by owner <value>",
    "by-tag": "Filter files by tag <value>",
    "actions-for": "Open actions assigned to <person>",
    "unlinked-meetings": "Meetings with no linked issues",
}


def run_structured(conn: sqlite3.Connection, query: str, filter_expr: str | None = None) -> str:
    if filter_expr:
        return query_filter(conn, filter_expr)

    parts = query.strip().split(maxsplit=1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else None

    if cmd == "open-actions":
        return query_open_actions(conn)
    elif cmd == "actions-for" and arg:
        return query_actions_for(conn, arg)
    elif cmd == "links-to" and arg:
        return query_links_to(conn, arg)
    elif cmd == "links-from" and arg:
        return query_links_from(conn, arg)
    elif cmd == "orphans":
        return query_orphans(conn)
    elif cmd == "recent":
        days = int(arg) if arg and arg.isdigit() else 7
        return query_recent(conn, days)
    elif cmd == "by-status" and arg:
        return query_by_field(conn, "status", arg)
    elif cmd == "by-type" and arg:
        return query_by_field(conn, "type", arg)
    elif cmd == "by-domain" and arg:
        return query_by_field(conn, "domain", arg)
    elif cmd == "by-owner" and arg:
        return query_by_field(conn, "owner", arg)
    elif cmd == "by-tag" and arg:
        return query_by_tag(conn, arg)
    elif cmd == "unlinked-meetings":
        return query_unlinked_meetings(conn)
    else:
        cmds = "\n".join(f"  {k:20s} {v}" for k, v in STRUCTURED_COMMANDS.items())
        return f"Unknown structured query: '{query}'\n\nAvailable commands:\n{cmds}"


def main():
    parser = argparse.ArgumentParser(description="PKM vault search")
    parser.add_argument("query", nargs="*", help="Search query or structured command")
    parser.add_argument("--mode", choices=["semantic", "keyword", "hybrid", "structured"], default="hybrid")
    parser.add_argument("--filter", dest="filter_expr", help="SQL filter expression for structured mode")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--show-content", action="store_true", help="Show first 500 chars of content")
    args = parser.parse_args()

    query = " ".join(args.query) if args.query else ""
    conn = _check_db()

    if args.mode == "structured":
        result = run_structured(conn, query, args.filter_expr)
    elif args.mode == "keyword":
        result = search_keyword_detailed(conn, query, args.limit, args.show_content)
    elif args.mode == "hybrid":
        result = search_hybrid(conn, query, args.limit, args.show_content)
    else:
        result = search_semantic_detailed(conn, query, args.limit)

    print(result)
    conn.close()


if __name__ == "__main__":
    main()
