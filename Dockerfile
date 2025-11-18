FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Preload rembg models during build
COPY preload_models.py .
RUN python preload_models.py || echo "Model preload failed, will download on first request"

# Copy application code
COPY api/ ./api/

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0", "--port", "8000"]

