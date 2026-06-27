#!/bin/bash

echo "Iniciando Ollama..."

podman rm -f ollama 2>/dev/null

podman run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  docker.io/ollama/ollama


echo "Iniciando Open WebUI..."

podman rm -f open-webui 2>/dev/null

podman run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OLLAMA_BASE_URL=http://host.containers.internal:11434 \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main


echo "Despliegue terminado."
