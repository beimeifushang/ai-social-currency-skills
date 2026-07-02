#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$TARGET_DIR"
cp -R "$ROOT_DIR"/skills/* "$TARGET_DIR"/

echo "Installed skills into $TARGET_DIR"
