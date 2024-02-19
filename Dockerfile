# syntax=docker/dockerfile:1
FROM python:3.11.4-slim-bullseye AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1

# Install OS dependencies required for Chrome and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gconf-service  \
    libasound2  \
    libatk1.0-0  \
    libcairo2  \
    libcups2  \
    libfontconfig1  \
    libgdk-pixbuf2.0-0  \
    libgtk-3-0  \
    libnspr4  \
    libpango-1.0-0  \
    libxss1  \
    fonts-liberation  \
    libappindicator1  \
    libnss3  \
    lsb-release  \
    xdg-utils

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Set the working directory in the container
WORKDIR /app

# Copying only the dependencies file at first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies including dev dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy your application code to the container
COPY . /app

# Ensure WebDriver has executable permissions
RUN chmod +x /app/resources/webdrivers/chromedriver_linux

# The command to run tests
ENTRYPOINT ["python3", "-m", "pytest", "-s"]
CMD ["--env", "QA", "PROD"]
