Automated CI/CD Two-Tier Web Application on AWS EC2

An end-to-end DevOps project featuring a containerized two-tier Flask and MySQL application, orchestrated with Docker Compose, and deployed via an automated Jenkins CI/CD pipeline triggered by GitHub Webhooks on an AWS EC2 instance.

Architecture Overview
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

Tech Stack & Tools

Application Tier: Python 3.12, Flask, Jinja2 Templates, mysql-connector-python

Database Tier: MySQL 8.0 with automated entrypoint schema initialization (init.sql)

Containerization: Docker, Docker Compose v2, Named Volumes, Bridge Networking

CI/CD Automation: Jenkins (Declarative Pipeline), GitHub Webhooks

Cloud Infrastructure: AWS EC2 (t3.small, Ubuntu 24.04 LTS), Custom Security Groups

Security & Configuration: Environment variable isolation (.env), non-root database users

Project Structure
devops-two-tier-project/
├── db/
│   └── init.sql                  # Automated database schema initialization
├── screenshots/                  # Deployment & verification proofs
│   ├── aws-ec2-infra.png
│   ├── docker-containers.png
│   ├── github-webhook.png
│   ├── live-app-db.png
│   ├── pipeline-status.png
│   └── security-group.png
├── templates/
│   └── index.html                # Frontend UI template
├── .gitignore                    # Prevents secret/credential leaks
├── app.py                        # Flask backend application
├── docker-compose.yml            # Multi-container orchestration & networking
├── Dockerfile                    # Container image configuration
├── Jenkinsfile                   # Declarative pipeline script
├── requirements.txt              # Application Python dependencies
└── README.md                     # Project documentation

Verification & Deployment Proofs
1. Automated CI/CD Execution (Jenkins Pipeline)

Every commit to the master branch triggers the declarative pipeline executing checkout, build, testing, and deployment.

2. Live Application with Persistent Database Storage

Data entered through the web UI is processed by Flask, committed to MySQL, and preserved across container reloads.

3. Docker Multi-Container Runtime on EC2

Isolated bridge network running both application and database tiers with mapped port bindings.

4. GitHub Webhook Integration

Automated HTTP POST payload dispatch triggering builds immediately on code push.

Local Setup & Deployment
1. Clone the Repository
git clone https://github.com/Kunj3336/devops-two-tier-project.git
cd devops-two-tier-project

2. Configure Environment Variables

Create a .env file in the project root:

DB_HOST=db
DB_USER=devops_user
DB_PASSWORD=kunj@work
DB_NAME=devops_app

3. Launch Containers
docker compose up -d --build


Access the application at: http://localhost:5000

CI/CD Pipeline Implementation

The pipeline is defined in the Jenkinsfile using Declarative syntax:

pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            git branch: 'master', url: '[https://github.com/Kunj3336/devops-two-tier-project.git](https://github.com/Kunj3336/devops-two-tier-project.git)'
        }
    }
    stage('Build') {
        steps {
            sh 'docker compose build'
        }
    }
    stage('Test') {
        steps {
            sh 'docker compose config'
        }
    }
    stage('Deploy') {
        steps {
            sh 'docker compose up -d'
        }
    }
}
post {
    always {
        sh 'docker image prune -f'
    }
}
}