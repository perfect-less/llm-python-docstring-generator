#!/bin/sh
set -e

ollama serve &
sleep 3

# Ensure model is available
ollama pull phi3

# Optional: warm it up
ollama run phi3 || true

# Keep container running
tail -f /dev/null
