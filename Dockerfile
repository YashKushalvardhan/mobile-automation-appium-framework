# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Simple pytest run for now.
# Allure reporting will be added later once we integrate it properly
# (in the Jenkins CI/CD phase).
CMD ["python", "-m", "pytest", "-v"]