# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv .venv

# Copy requirements file
COPY requirements.txt .

# Activate venv and install Python dependencies
RUN .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

# Copy prisma schema and generate client
COPY prisma ./prisma
RUN .venv/bin/prisma generate

# Copy application source code
COPY src ./src
COPY scripts ./scripts

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD [".venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
