# syntax=docker/dockerfile:1

# Base image compatible with ARM64
FROM --platform=linux/arm64 python:3.11.4-slim-bullseye AS base
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1

# Install OS dependencies required for Chrome and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    firefox-esr \
    chromium \
    chromium-driver

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copying only the dependencies file at first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies including dev dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy your application code to the container
COPY . /app

# The command to run tests
ENTRYPOINT ["python3", "-m", "pytest", "-s"]
CMD ["--env", "QA", "PROD"]