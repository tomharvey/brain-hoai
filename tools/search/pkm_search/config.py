"""Config file management and model selection logic."""

import os
from datetime import date
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "pkm.conf"
DB_PATH = Path(__file__).resolve().parents[1] / "pkm.db"

MODELS = {
    "nomic": {
        "ollama_name": "nomic-embed-text",
        "dimensions": 768,
        "context_tokens": 8192,
        "doc_prefix": "search_document: ",
        "query_prefix": "search_query: ",
    },
    "qwen3": {
        "ollama_name": "qwen3-embedding:0.6b",
        "dimensions": 1024,
        "context_tokens": 32768,
        "doc_prefix": "Instruct: Represent this document for retrieval\n",
        "query_prefix": "Instruct: Given a search query, retrieve relevant documents\nQuery: ",
    },
}

LONG_FILE_THRESHOLD = 6000  # tokens
LONG_FILE_PCT_THRESHOLD = 10  # percent


def estimate_tokens(text: str) -> int:
    """Rough token estimate: word count * 1.3."""
    return int(len(text.split()) * 1.3)


def read_config() -> dict | None:
    """Read config file. Returns None if it doesn't exist."""
    if not CONFIG_PATH.exists():
        return None
    conf = {}
    for line in CONFIG_PATH.read_text().splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, val = line.split("=", 1)
            conf[key.strip()] = val.strip()
    return conf


def write_config(model: str, vault_path: str, files_analysed: int,
                 long_files: int, long_file_pct: float) -> None:
    """Write config file."""
    m = MODELS[model]
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(
        f"model={model}\n"
        f"dimensions={m['dimensions']}\n"
        f"vault_path={vault_path}\n"
        f"created={date.today().isoformat()}\n"
        f"files_analysed={files_analysed}\n"
        f"long_files={long_files}\n"
        f"long_file_pct={long_file_pct:.1f}\n"
    )


def select_model(file_texts: list[str]) -> tuple[str, int, int, float]:
    """Analyse file lengths and pick a model.

    Returns (model_name, files_analysed, long_files, long_file_pct).
    """
    total = len(file_texts)
    long = sum(1 for t in file_texts if estimate_tokens(t) > LONG_FILE_THRESHOLD)
    pct = (long / total * 100) if total > 0 else 0

    if pct >= LONG_FILE_PCT_THRESHOLD:
        model = "qwen3"
    else:
        model = "nomic"

    return model, total, long, pct


def get_model_config(conf: dict | None = None) -> dict:
    """Get the active model config dict from MODELS.

    Reads from config file if conf not provided.
    """
    if conf is None:
        conf = read_config()
    model_name = conf["model"] if conf else "nomic"
    return MODELS[model_name]
