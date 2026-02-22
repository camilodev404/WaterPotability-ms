#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)
SOURCE_DIR="$ROOT_DIR/WaterPotability/notebooks/mlruns/1/models/m-1ccb4a99340344b4a23ab8657794666a/artifacts"
TARGET_DIR="$ROOT_DIR/WaterPotability-ms/models/water_potability_model"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Model source not found: $SOURCE_DIR"
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp -r "$SOURCE_DIR"/* "$TARGET_DIR"/

echo "Model artifacts copied to: $TARGET_DIR"
