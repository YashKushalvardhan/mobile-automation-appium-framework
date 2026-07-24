# Dockerfile
# Base image with Python already installed
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (Docker layer caching optimization —
# dependencies only reinstall if requirements.txt changes)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container
COPY . .

# Default command when the container starts
CMD ["pytest", "-v", "--alluredir=reports/allure-results"]