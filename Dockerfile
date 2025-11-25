FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src/ ./src/
COPY benchmarks/ ./benchmarks/


RUN mkdir -p logs


WORKDIR /app/src


CMD ["python", "main.py"]
