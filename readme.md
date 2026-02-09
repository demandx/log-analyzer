AI Cloud Log Analyzer

A backend service that analyzes Linux system logs and generates human-readable insights using AI. Built with FastAPI, containerized using Docker, and deployed on AWS EC2.

What It Does

Reads Linux system logs

Summarizes log activity using OpenAI APIs

Identifies severity and possible causes

Exposes REST APIs with FastAPI

Runs as a Docker container on AWS EC2

Tech Stack

Python, FastAPI, Linux (Ubuntu), Docker, AWS EC2, OpenAI API, REST APIs

API Endpoints

GET /health — Service health check

POST /logs/analyze?lines=50 — Analyze recent log entries

Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload


Open: http://127.0.0.1:8000/docs

Run with Docker
docker build -t log-analyzer .
docker run -p 8000:8000 log-analyzer

Cloud Deployment

Deployed on AWS EC2 (Ubuntu Free Tier) using Docker and accessed via public IP.

Security

API keys managed via environment variables

.env is excluded from version control

Purpose

Built as a portfolio project to demonstrate backend development, cloud deployment, Dockerization, and practical AI integration.
