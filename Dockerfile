# Multi-stage Dockerfile: Builds React frontend, sets up Python backend, and serves all on port 8000
FROM node:20-alpine AS frontend-builder
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app

# Install git for repository cloning
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

# Install backend Python dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Copy backend application code
COPY backend/ ./backend/

# Copy built frontend assets from builder stage
COPY --from=frontend-builder /frontend/dist ./frontend/dist

# Copy sample repo and demo zip
COPY sample-repo/ ./sample-repo/
COPY sample-ecommerce-backend.zip ./

# Create data directories
RUN mkdir -p ./backend/data/chroma ./backend/data/repos

WORKDIR /app/backend

ENV PORT=8000
EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
