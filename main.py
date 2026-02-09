from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Log Analyzer")

app.include_router(router)
