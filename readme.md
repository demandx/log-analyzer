AI-Powered Cloud Log Analyzer

An AI-powered backend service that analyzes Linux system logs and generates human-readable insights such as summaries, severity levels, and possible causes. The application is built using FastAPI, containerized with Docker, and deployed on AWS EC2, demonstrating real-world backend, cloud, and DevOps workflows.

Features

Reads real Linux system logs (/var/log/syslog)

Analyzes logs using OpenAI APIs to generate summaries, severity levels, and possible causes

Exposes RESTful APIs using FastAPI

Interactive API documentation via Swagger UI

Fully containerized using Docker

Deployable on cloud infrastructure (AWS EC2)

Tech Stack

Programming Language: Python

Backend Framework: FastAPI

Operating System: Linux (Ubuntu)

AI Integration: OpenAI API

Containerization: Docker

Cloud Platform: AWS EC2

API Documentation: OpenAPI / Swagger

Tools: Git, SSH, Bash

Project Structure
log-analyzer/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── log_reader.py
│   ├── ai_service.py
│   └── __init__.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .env.example
└── README.md

Setup Instructions (Local)
Clone the repository
git clone https://github.com/<your-username>/ai-cloud-log-analyzer.git
cd ai-cloud-log-analyzer

Create virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Configure environment variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key

Run the application
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

Docker Setup
Build Docker image
docker build -t log-analyzer .

Run Docker container
docker run -d -p 8000:8000 log-analyzer


Access API documentation:

http://localhost:8000/docs

Cloud Deployment (AWS EC2)

Deployed on AWS EC2 (Ubuntu Free Tier)

Docker installed and configured on the EC2 instance

Application runs as a Docker container

Exposed via public IPv4 address

Example:

http://<EC2_PUBLIC_IP>:8000/docs

API Endpoints
Health Check
GET /health

Log Analysis
POST /logs/analyze?lines=50


Returns:

Log summary

Severity level

Possible causes

Security Notes

.env file is never committed to version control

API keys are managed using environment variables

.env.example is provided for reference

What This Project Demonstrates

Backend API development with FastAPI

Linux system-level log handling

Practical AI integration using OpenAI APIs

Docker-based containerization

Cloud deployment on AWS EC2

Secure handling of secrets and environment variables

Limitations

Designed for demonstration and learning purposes

Not intended for real-time or large-scale log monitoring

AI analysis depends on OpenAI API availability

License

This project is intended for educational and portfolio use.

Contact

For recruiter access to the private repository or a live demo, please contact me.
