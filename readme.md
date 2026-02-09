**AI Cloud Log Analyzer**
A backend service that analyzes Linux system logs and returns structured, human-readable insights. The application is built using FastAPI, designed for AI-powered analysis, containerized with Docker, and deployable on AWS EC2.

**Overview**

This project demonstrates how to design and deploy a cloud-ready backend system that processes real Linux system logs and produces analytical insights through an AI layer. The system architecture cleanly separates log ingestion, analysis, and API delivery.
For demonstration purposes, the AI analysis layer currently runs in mock mode. The application is fully designed to integrate with OpenAI APIs in production without changes to the API contract.

**Key Features**

1. Reads real Linux system logs (/var/log/syslog)

2. REST API built with FastAPI

3. Health check endpoint for service monitoring

4. Structured analysis output (summary, severity, causes)

5. Clean separation between log ingestion and analysis layers

6. Docker-ready and cloud-deployable architecture

7. Secure handling of configuration via environment variables

**Tech Stack**
Language: Python
Framework: FastAPI
Operating System: Linux (Ubuntu)
Containerization: Docker
Cloud Platform: AWS EC2
API Style: REST
Tools: Git, Bash, SSH

**API Endpoints
**
Health Check
GET /health


Response:

{ "status": "ok" }

Log Analysis
POST /logs/analyze?lines=50


Response (example):

{
  "lines_read": 50,
  "analysis": {
    "summary": "System logs indicate repeated AppArmor denials and kernel warnings.",
    "severity": "medium",
    "possible_causes": [
      "Restricted permissions for snap-based applications",
      "Access attempts to protected kernel files"
    ],
    "recommendation": "Review AppArmor profiles and verify expected behavior."
  }
}

Running Locally
pip install -r requirements.txt
uvicorn app.main:app --reload


Access:

http://127.0.0.1:8000/docs

Docker Usage
docker build -t log-analyzer .
docker run -p 8000:8000 log-analyzer


**AI Integration Note

The analysis layer is mocked for demonstration purposes due to API credit limitations.
In production, this layer is designed to call OpenAI APIs without requiring changes to routes, data flow, or response format.**

**What This Project Demonstrates
**

Backend API development using FastAPI
Linux system-level log processing
Clean service-layer abstraction
Docker-based application packaging
Cloud-ready backend architecture
Professional handling of external dependencies
