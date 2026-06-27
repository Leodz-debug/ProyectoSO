# Proyecto SO - Despliegue de IA en AWS con Podman

## 📌 Descripción
Este proyecto implementa un sistema de inteligencia artificial desplegado en la nube utilizando AWS EC2, Podman, Ollama y Open WebUI. Permite ejecutar modelos de lenguaje de forma local en un servidor remoto accesible vía web.

---

## 🧠 Arquitectura del sistema

Usuario
↓
Open WebUI (Puerto 3000)
↓
Ollama (Puerto 11434)
↓
Modelo LLM (llama3.2 / tinyllama)

---

## ☁️ Infraestructura utilizada

- AWS EC2 (Ubuntu 24.04)
- Instancia: t3.small
- IP pública
- Security Groups configurados

---

## 🐳 Tecnologías

- Podman (contenedores)
- Ollama (modelos de IA)
- Open WebUI (interfaz web)
- Git + GitHub

---

## ⚙️ Instalación y despliegue

### 1. Clonar repositorio
```bash
git clone https://github.com/Leodz-debug/ProyectoSO.git
cd ProyectoSO

