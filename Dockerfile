# Python 3.12 বেস ইমেজ ব্যবহার করা
FROM python:3.12-slim

# ওয়ার্কিং ডিরেক্টরি সেট করা
WORKDIR /app

# প্রয়োজনীয় ডিপেন্ডেন্সি ফাইল কপি করা এবং ইনস্টল করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# প্রজেক্টের সমস্ত ফাইল কন্টেইনারে কপি করা
COPY . .

# এপিআই সার্ভারের পোর্ট ওপেন করা
EXPOSE 8000

# কন্টেইনার রান করার সময় ফাস্টএপিআই সার্ভার স্টার্ট করা
CMD ["python", "trustflow_server.py"]
# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies & git if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements or project files into the container
COPY . /app/

# Set environment variables for Doha Sovereign Cluster
ENV PYTHONUNBUFFERED=1
ENV CLOUD_NODE_ENV=production
ENV SOVEREIGN_REGION=Doha-Cluster

# Expose secure port for real-time API webhooks & dashboards
EXPOSE 8080

# Execute the Master Telemetry Framework runner on container start
CMD ["python3", "HamadTamimMasterTelemetryFramework.py"]
version: '3.8'

services:
  hamad_tamim_telemetry_engine:
    build: .
    container_name: hamad_tamim_sovereign_node
    restart: always
    environment:
      - NODE_ENV=production
      - TARGET_REGION=Doha-Sovereign-Cluster
      - ENCRYPTION_STANDARD=AES-256-GCM
    ports:
      - "8080:8080"
    volumes:
      - ./logs:/app/logs
    networks:
      - sovereign_mesh

networks:
  sovereign_mesh:
    driver: bridge
