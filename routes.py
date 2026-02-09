from fastapi import APIRouter
from app.log_reader import read_syslog

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "service": "log-analyzer"}

@router.post("/logs/analyze")
def analyze_logs(lines: int = 100):
    logs = read_syslog(lines=lines)

    return {
        "source": "/var/log/syslog",
        "lines_read": lines,
        "logs_preview": logs[:1000]  # prevent huge response
    }
