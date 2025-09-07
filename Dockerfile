FROM python:3.11-slim

WORKDIR /workspace

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps for builds & git
RUN apt-get update && apt-get install -y --no-install-recommends \    build-essential git curl \  && rm -rf /var/lib/apt/lists/*

# Install Python deps from requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create expected dirs (actual code mounted via volumes during dev)
RUN mkdir -p /workspace/app /workspace/goals /workspace/.assistant

EXPOSE 8000
