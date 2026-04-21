#!/usr/bin/env bash
# Install vault search dependencies (run after container rebuild)
set -euo pipefail

echo "=== Vault Search: Install ==="

# 1. System deps
echo "Installing system dependencies..."
sudo apt-get update -qq
sudo apt-get install -y -qq zstd

# 2. Python deps
echo "Installing Python dependencies..."
pip install --quiet sqlite-vec pyyaml

# 3. Ollama
if command -v ollama &>/dev/null; then
    echo "Ollama already installed: $(ollama --version 2>&1 | tail -1)"
else
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# 4. Start Ollama if not running
if ! curl -s http://localhost:11434/api/tags &>/dev/null; then
    echo "Starting Ollama server..."
    ollama serve > /tmp/ollama.log 2>&1 &
    sleep 3
fi

# 5. Pull embedding model
echo "Pulling nomic-embed-text model..."
ollama pull nomic-embed-text

echo ""
echo "=== Install complete ==="
echo "To build the index: cd tools/search && python -m pkm_search.build /workspaces/pkm"
