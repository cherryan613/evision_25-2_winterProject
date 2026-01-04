FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y tcpdump && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir fastapi uvicorn requests
COPY agent_a.py .
EXPOSE 8000
CMD ["uvicorn", "agent_a:app", "--host", "0.0.0.0", "--port", "8000"]