FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn
COPY tool_server.py .
EXPOSE 8001
CMD ["uvicorn", "tool_server:app", "--host", "0.0.0.0", "--port", "8001"]
