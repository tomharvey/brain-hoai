#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

PIP_ROOT_USER_ACTION=ignore pip install --quiet --disable-pip-version-check pyyaml sqlite-vec
