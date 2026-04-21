"""Markdown parser: frontmatter, wikilinks, actions, sections."""

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Action:
    text: str
    done: bool
    line_number: int
    owner: str | None = None


@dataclass
class Link:
    target: str
    display: str | None
    line_number: int


@dataclass
class Section:
    heading: str | None
    content: str
    start_line: int


@dataclass
class FileData:
    path: str
    frontmatter: dict
    body: str
    body_start_line: int
    links: list[Link] = field(default_factory=list)
    actions: list[Action] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)


_WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
_ACTION_RE = re.compile(r"^- \[([ xX])\] (.+)$")
_HEADING_RE = re.compile(r"^## (.+)$")

# Patterns for extracting action owner: "Tom: do X", "[[tom]]: do X", "Tom to do X"
_OWNER_PATTERNS = [
    re.compile(r"^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]\s*[:—–-]\s*"),
    re.compile(r"^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]\s+to\s+", re.IGNORECASE),
    re.compile(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s*[:—–-]\s*"),
    re.compile(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+to\s+", re.IGNORECASE),
]


def _extract_owner(text: str) -> str | None:
    for pat in _OWNER_PATTERNS:
        m = pat.match(text)
        if m:
            return m.group(1).lower().strip()
    return None


def parse_frontmatter(content: str) -> tuple[dict, str, int]:
    """Extract YAML frontmatter. Returns (frontmatter_dict, body, body_start_line)."""
    if not content.startswith("---"):
        return {}, content, 1

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content, 1

    fm_text = content[3:end].strip()
    body_start = content.count("\n", 0, end + 4) + 1
    body = content[end + 4:].lstrip("\n")

    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}

    return fm, body, body_start


def parse_file(path: Path, vault_root: Path) -> FileData:
    """Parse a markdown file into structured data."""
    content = path.read_text(encoding="utf-8")
    rel_path = str(path.relative_to(vault_root))

    fm, body, body_start = parse_frontmatter(content)

    links: list[Link] = []
    actions: list[Action] = []
    sections: list[Section] = []

    current_heading = None
    current_lines: list[str] = []
    current_start = body_start

    for i, line in enumerate(body.split("\n"), start=body_start):
        # Wikilinks
        for m in _WIKILINK_RE.finditer(line):
            links.append(Link(target=m.group(1).strip(), display=m.group(2), line_number=i))

        # Actions
        am = _ACTION_RE.match(line.strip())
        if am:
            action_text = am.group(2)
            actions.append(Action(
                text=action_text,
                done=am.group(1).lower() == "x",
                line_number=i,
                owner=_extract_owner(action_text),
            ))

        # Section tracking
        hm = _HEADING_RE.match(line)
        if hm:
            if current_lines:
                sections.append(Section(
                    heading=current_heading,
                    content="\n".join(current_lines).strip(),
                    start_line=current_start,
                ))
            current_heading = hm.group(1).strip()
            current_lines = []
            current_start = i
        else:
            current_lines.append(line)

    # Final section
    if current_lines:
        sections.append(Section(
            heading=current_heading,
            content="\n".join(current_lines).strip(),
            start_line=current_start,
        ))

    return FileData(
        path=rel_path,
        frontmatter=fm,
        body=body,
        body_start_line=body_start,
        links=links,
        actions=actions,
        sections=sections,
    )


def chunk_file(file_data: FileData, max_lines: int = 300) -> list[Section]:
    """Decide chunking strategy and return chunks."""
    line_count = file_data.body.count("\n") + 1

    if line_count <= max_lines:
        # Small file: single chunk
        return [Section(
            heading=None,
            content=file_data.body.strip(),
            start_line=file_data.body_start_line,
        )]

    # Large file: use sections if available
    if len(file_data.sections) > 1:
        return file_data.sections

    # No sections: window-based chunking
    words = file_data.body.split()
    chunks = []
    window_size = 500
    overlap = 100
    start = 0
    chunk_idx = 0

    while start < len(words):
        end = min(start + window_size, len(words))
        chunk_text = " ".join(words[start:end])
        # Approximate line number
        approx_line = file_data.body_start_line + (start * line_count // max(len(words), 1))
        chunks.append(Section(
            heading=f"chunk-{chunk_idx}",
            content=chunk_text,
            start_line=approx_line,
        ))
        chunk_idx += 1
        start += window_size - overlap

    return chunks
