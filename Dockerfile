# syntax=docker/dockerfile:1

# Start from the official Python 3.11 image
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1

# Install OS dependencies required for Firefox
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry using pip to ensure it uses the correct version of Python
RUN python3 -m pip install "poetry==$POETRY_VERSION"

# Set Poetry configuration to not create a virtual env within the Docker container
RUN poetry config virtualenvs.create false

# Set the working directory in the container
WORKDIR /app

# Copying only the dependencies file at first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies including dev dependencies
RUN poetry install --no-root

# Copy your application code to the container
COPY . /app

# The command to run tests
ENTRYPOINT ["python3", "-m", "pytest", "-s"]
CMD ["--env", "QA", "PROD"]
