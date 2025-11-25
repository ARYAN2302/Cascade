FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY benchmarks/ ./benchmarks/

# Create logs directory
RUN mkdir -p logs

# Set working directory for src imports
WORKDIR /app/src

# Default: run the CLI
CMD ["python", "main.py"]
