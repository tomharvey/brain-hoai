"""SQLite schema creation with sqlite-vec and FTS5 support."""

import sqlite3
import sqlite_vec


def connect(db_path: str) -> sqlite3.Connection:
    """Create a connection with sqlite-vec loaded."""
    conn = sqlite3.connect(db_path)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def create_schema(conn: sqlite3.Connection, dimensions: int = 768) -> None:
    """Create all tables and indexes."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS files (
            id          INTEGER PRIMARY KEY,
            path        TEXT NOT NULL UNIQUE,
            title       TEXT,
            type        TEXT,
            domain      TEXT,
            status      TEXT,
            owner       TEXT,
            created     TEXT,
            updated     TEXT,
            tags        TEXT,
            content     TEXT,
            file_hash   TEXT,
            token_count INTEGER,
            indexed_at  TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS chunks (
            id          INTEGER PRIMARY KEY,
            file_id     INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
            heading     TEXT,
            chunk_index INTEGER NOT NULL,
            content     TEXT NOT NULL,
            start_line  INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS links (
            id          INTEGER PRIMARY KEY,
            source_id   INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
            target_name TEXT NOT NULL,
            display     TEXT,
            line_number INTEGER
        );

        CREATE TABLE IF NOT EXISTS file_tags (
            file_id     INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
            tag         TEXT NOT NULL,
            PRIMARY KEY (file_id, tag)
        );

        CREATE TABLE IF NOT EXISTS actions (
            id          INTEGER PRIMARY KEY,
            file_id     INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
            text        TEXT NOT NULL,
            done        INTEGER NOT NULL,
            line_number INTEGER NOT NULL,
            owner       TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_files_type ON files(type);
        CREATE INDEX IF NOT EXISTS idx_files_domain ON files(domain);
        CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
        CREATE INDEX IF NOT EXISTS idx_files_updated ON files(updated);
        CREATE INDEX IF NOT EXISTS idx_links_target ON links(target_name);
        CREATE INDEX IF NOT EXISTS idx_links_source ON links(source_id);
        CREATE INDEX IF NOT EXISTS idx_actions_done ON actions(done);
        CREATE INDEX IF NOT EXISTS idx_chunks_file ON chunks(file_id);
    """)

    # FTS5 full-text index over files
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(
            title, content, content=files, content_rowid=id
        )
    """)

    # FTS5 triggers to keep it in sync
    conn.executescript("""
        CREATE TRIGGER IF NOT EXISTS files_fts_insert AFTER INSERT ON files BEGIN
            INSERT INTO files_fts(rowid, title, content)
            VALUES (new.id, new.title, new.content);
        END;

        CREATE TRIGGER IF NOT EXISTS files_fts_delete AFTER DELETE ON files BEGIN
            INSERT INTO files_fts(files_fts, rowid, title, content)
            VALUES ('delete', old.id, old.title, old.content);
        END;

        CREATE TRIGGER IF NOT EXISTS files_fts_update AFTER UPDATE ON files BEGIN
            INSERT INTO files_fts(files_fts, rowid, title, content)
            VALUES ('delete', old.id, old.title, old.content);
            INSERT INTO files_fts(rowid, title, content)
            VALUES (new.id, new.title, new.content);
        END;
    """)

    # Vector table — dimensions depend on model
    conn.execute(f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_vec USING vec0(
            chunk_id INTEGER PRIMARY KEY,
            embedding FLOAT[{dimensions}]
        )
    """)

    conn.commit()


def drop_vector_table(conn: sqlite3.Connection) -> None:
    """Drop and allow recreation of the vector table (for model changes)."""
    conn.execute("DROP TABLE IF EXISTS chunks_vec")
    conn.commit()
