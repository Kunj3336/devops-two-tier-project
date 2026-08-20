# Automated CI/CD Two-Tier Web Application on AWS EC2

An end-to-end DevOps project featuring a containerized two-tier Flask and MySQL application, orchestrated with Docker Compose, and deployed via an automated Jenkins CI/CD pipeline triggered by GitHub Webhooks on an AWS EC2 instance.

---

## Architecture Overview

```text
Developer Workstation (Git Push)
           │
           ▼
     GitHub Repository
           │
           ▼ (GitHub Webhook / Port 8080)
    AWS EC2 (Ubuntu 24.04 LTS)
           │
           ▼
    Jenkins CI/CD Pipeline
     ├── Stage 1: Checkout SCM
     ├── Stage 2: Build Images (Docker)
     ├── Stage 3: Test Configuration (Docker Compose)
     └── Stage 4: Deploy (Docker Compose)
           │
           ▼
    Docker Bridge Network
     ├── Frontend / API: Flask App Container (Port 5000:5000)
     └── Backend / Data: MySQL 8.0 Container (Port 3306)
           └── Named Volume: mysql_data (Data Persistence)

---

## Tech Stack & Tools
Application Tier: Python 3.12, Flask, Jinja2 Templates, mysql-connector-python

Database Tier: MySQL 8.0 with automated entrypoint schema initialization (init.sql)

Containerization: Docker, Docker Compose v2, Named Volumes, Bridge Networking

CI/CD Automation: Jenkins (Declarative Pipeline), GitHub Webhooks

Cloud Infrastructure: AWS EC2 (t3.small, Ubuntu 24.04 LTS), Custom Security Groups

Security & Configuration: Environment variable isolation (.env), non-root database users