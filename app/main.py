# FastAPI entrypoint + LangGraph integration
from fastapi import FastAPI

app = FastAPI(title="Personal Assistant", version="0.1.0")

@app.get("/health")
async def health():
    return {"status": "ok", "message": "Assistant container is running"}
