#!/usr/bin/env bash
# MOSS Month-End MCP Server — macOS installer
#
# Usage:
#   bash install.sh
#
# What it does:
#   1. Ensures Python 3 and pip are available (installs via Homebrew if not)
#   2. Creates a hidden venv at ~/.moss-month-end/
#   3. Installs dependencies and copies server.py into it
#   4. Prints the JSON block to add to your Claude Desktop config

set -euo pipefail

INSTALL_DIR="$HOME/.moss-month-end"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

info()  { printf "\033[1;34m→\033[0m %s\n" "$1"; }
ok()    { printf "\033[1;32m✓\033[0m %s\n" "$1"; }
fail()  { printf "\033[1;31m✗\033[0m %s\n" "$1" >&2; exit 1; }

# ── Step 1: Python 3 ─────────────────────────────────────────────────────

if command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
    ok "Python 3 found: $PYTHON ($(python3 --version 2>&1))"
else
    fail "Python 3 not found. Download and install it from:
    https://www.python.org/ftp/python/3.13.14/python-3.13.14-macos11.pkg
Then re-run this script."
fi

# Verify pip is available
if ! "$PYTHON" -m pip --version >/dev/null 2>&1; then
    info "pip not found — installing..."
    "$PYTHON" -m ensurepip --upgrade
    ok "pip installed"
fi

# ── Step 2: Create venv and install deps ──────────────────────────────────

FIRST_INSTALL=false
if [[ -d "$INSTALL_DIR/venv" ]]; then
    info "Existing installation found — updating..."
else
    FIRST_INSTALL=true
    info "Creating venv at $INSTALL_DIR/venv..."
    mkdir -p "$INSTALL_DIR"
    "$PYTHON" -m venv "$INSTALL_DIR/venv"
    ok "venv created"
fi

info "Installing dependencies..."
"$INSTALL_DIR/venv/bin/pip" install --quiet --upgrade pip
"$INSTALL_DIR/venv/bin/pip" install --quiet -r "$SCRIPT_DIR/requirements.txt"
ok "Dependencies installed"

# ── Step 3: Copy server.py ────────────────────────────────────────────────

cp "$SCRIPT_DIR/server.py" "$INSTALL_DIR/server.py"
ok "server.py installed to $INSTALL_DIR/server.py"

# ── Step 4: Output config (first install only) ───────────────────────────

VENV_PYTHON="$INSTALL_DIR/venv/bin/python"
SERVER_PATH="$INSTALL_DIR/server.py"

if [[ "$FIRST_INSTALL" == "true" ]]; then
    cat <<EOF

────────────────────────────────────────────────────────────
  Add the following to your Claude Desktop config:

    macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

  Paste this inside the "mcpServers" object:
────────────────────────────────────────────────────────────

    "moss": {
      "command": "$VENV_PYTHON",
      "args": ["$SERVER_PATH"],
      "env": {
        "MOSS_API_PUBLIC_KEY": "kid_YOUR_KEY_ID_HERE",
        "MOSS_API_SECRET_KEY": "sk_YOUR_SECRET_KEY_HERE"
      }
    }

────────────────────────────────────────────────────────────
  Replace the key values with your MOSS API keys.
  Generate them at: MOSS → Settings → Company Settings → API Keys
  (set scope to read-only)

  Then restart Claude Desktop.
────────────────────────────────────────────────────────────
EOF
else
    ok "Updated. Restart Claude Desktop to pick up changes."
fi
