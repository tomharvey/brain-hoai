"""Ollama embedding client with model-aware prefixes."""

import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/embed"


class OllamaUnavailable(Exception):
    pass


def _call_ollama(payload: dict) -> dict:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:500]
        raise RuntimeError(f"Ollama API error {e.code}: {body}") from e
    except (urllib.error.URLError, ConnectionError, OSError) as e:
        raise OllamaUnavailable(
            f"Cannot reach Ollama at {OLLAMA_URL}: {e}\n"
            "Start Ollama and pull the required model."
        ) from e


def _truncate(text: str, max_tokens: int) -> str:
    """Truncate text to fit within model context window.

    Nomic's tokenizer can go below 1 char/token for markdown with many
    special characters, timestamps, and URLs (measured ~0.88 on transcripts).
    We use 0.75 chars/token to guarantee safety for all content types.
    """
    max_chars = int(max_tokens * 0.75)
    if len(text) > max_chars:
        return text[:max_chars]
    return text


def embed_texts(texts: list[str], model_config: dict) -> list[list[float]]:
    """Embed document texts one at a time.

    Ollama's /api/embed sums token counts across all inputs in a batch,
    so we must send each text individually to avoid exceeding the context
    window on long documents.
    """
    if not texts:
        return []
    prefix = model_config["doc_prefix"]
    max_tokens = model_config["context_tokens"]
    prefix_budget = len(prefix) // 4 + 50
    content_budget = max_tokens - prefix_budget

    results = []
    for t in texts:
        truncated = _truncate(t, content_budget)
        resp = _call_ollama({
            "model": model_config["ollama_name"],
            "input": [prefix + truncated],
        })
        results.append(resp["embeddings"][0])
    return results


def embed_query(text: str, model_config: dict) -> list[float]:
    """Embed a single query with the appropriate prefix."""
    prefix = model_config["query_prefix"]
    resp = _call_ollama({
        "model": model_config["ollama_name"],
        "input": [prefix + text],
    })
    return resp["embeddings"][0]
