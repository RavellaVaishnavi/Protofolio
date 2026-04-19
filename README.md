📌 Overview

This project demonstrates an end-to-end DevOps workflow by deploying a Flask web application using Docker containerization and Kubernetes orchestration. It showcases practical implementation of modern DevOps tools and deployment strategies.

🧱 Architecture
Flask Application (Backend with multiple routes)
Docker (Containerization)
Kubernetes (Orchestration with Deployment & Service)
NodePort Service (External access to application)
⚙️ Features

🐍 Flask Application

Routes: /projects, /skills, /education
Lightweight and modular structure

🐳 Docker

Containerized Flask application
Portable and consistent runtime environment
Built and tested locally

📦 Kubernetes

2-replica deployment for high availability
Self-healing pods
Declarative configuration using YAML

🌐 Service Exposure

NodePort service used to expose application externally
Traffic routed to Kubernetes pods
