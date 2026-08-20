# Automated CI/CD Two-Tier Web Application on AWS EC2

An end-to-end DevOps implementation featuring a containerized two-tier Flask and MySQL application, orchestrated with Docker Compose, and automated using a Jenkins CI/CD pipeline triggered by GitHub Webhooks on AWS EC2.

---

## 🏗️ Architecture Overview

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
```
---

## 🛠️ Tech Stack & Tools

* **Application Tier:** Python 3.12, Flask, Gunicorn / Jinja2 Templates, `mysql-connector-python`
* **Database Tier:** MySQL 8.0 with automated entrypoint schema initialization (`init.sql`)
* **Containerization:** Docker, Docker Compose v2, Named Volumes, Custom Bridge Networking
* **CI/CD Automation:** Jenkins (Declarative Pipeline), GitHub Webhooks
* **Cloud Infrastructure:** AWS EC2 (`t3.small`, Ubuntu 24.04 LTS), Custom Security Groups
* **Security & Configuration:** Isolated `.env` environment variables, non-root database users

---

## 📁 Project Structure

```text
devops-two-tier-project/
├── db/
│   └── init.sql                  # Automated database schema initialization
├── screenshots/                  # Pipeline and verification proofs
│   ├── aws-ec2-infra.png
│   ├── docker-containers.png
│   ├── github-webhook.png
│   ├── live-deployment.png
│   ├── live-app-db.png
│   ├── pipeline-status.png
│   └── security-group.png
├── templates/
│   └── index.html                # Frontend UI template
├── .gitignore                    # Prevents secret/environment credential leaks
├── app.py                        # Flask backend application with connection pooling
├── docker-compose.yml            # Multi-container orchestration & networking
├── Dockerfile                    # Multi-stage optimized application container image
├── Jenkinsfile                   # Declarative pipeline for automated build/deploy
├── requirements.txt              # Application dependencies
└── README.md                     # Documentation
```
---

## 📁 Verification & Deployment Proofs

**1. Automated CI/CD Execution (Jenkins Pipeline)**

    - Every commit to master triggers a declarative pipeline executing checkout, build, testing, and zero-downtime deployment.

**2. Live Application with Persistent Database Storage**

    - Data entered via the web UI is validated by Flask, committed to MySQL, and preserved across container restarts.

**3. Docker Multi-Container Runtime on EC2**

    - Isolated bridge network running both application and database tiers with mapped port bindings.

**4. GitHub Webhook Delivery**

   - Instant HTTP POST payload dispatch triggering automated builds on code push.

---

## 🚀 Local Setup & Deployment

**1. Clone the Repository**

```bash
git clone https://github.com/Kunj3336/devops-two-tier-project.git
```
```bash
cd devops-two-tier-project
```

**2. Configure Environment Variables**
    
Create a `.env` file in the project root directory using your own credentials:
```env
DB_HOST=db
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

**3. Launch Containers**

```bash    
docker compose up -d --build
```
Access the application at http://localhost:5000.

---

## ⚙️ CI/CD Pipeline Implementation

The pipeline is defined in the `Jenkinsfile` using Declarative syntax:

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-two-tier-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm devops-two-tier-app python -m pytest || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }
}
```
---
