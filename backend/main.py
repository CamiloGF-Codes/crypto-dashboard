from fastapi import FastAPI

app = FastAPI(title="Crypto Dashboard API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Crypto Dashboard API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}