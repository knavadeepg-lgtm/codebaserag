#!/usr/bin/env bash
set -e

echo "=========================================="
echo " Starting CodeLens Codebase RAG Assistant "
echo "=========================================="

# Build frontend if dist doesn't exist
if [ ! -d "frontend/dist" ]; then
  echo "Building frontend..."
  cd frontend
  npm install
  npm run build
  cd ..
fi

cd backend

# Install Python requirements if needed
if [ ! -d "venv" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
else
  source venv/bin/activate
fi

export PORT=${PORT:-8000}
echo "Starting server on port $PORT..."
exec python -m uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
