#!/bin/bash
set -e

# Activate venv
if [ -d ".venv" ]; then
  source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
else
  echo "No .venv found, creating one..."
  python -m venv .venv
  source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
fi

# Switch mode
case "$1" in
  dev)
    echo "Installing dev requirements..."
    pip install -r dev-requirements.txt
    ;;
  prod)
    echo "Installing prod requirements..."
    pip install -r requirements.txt
    ;;
  run)
    echo "Running Ngahere-OS backend..."
    uvicorn backend.main:app --reload --port 8000
    ;;
  *)
    echo "Usage: ./ngahere_os.sh [dev|prod|run]"
    ;;
esac
