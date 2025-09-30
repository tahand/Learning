FROM python:3.10-slim

WORKDIR /app

# Install system deps (optional, helps with pandas, numpy, sklearn, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install JupyterLab so you can run notebooks
RUN pip install jupyterlab
