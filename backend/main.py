from fastapi import FastAPI
from app.database import engine, Base
from app.models import crypto
from app.routes.crypto_routes import router as crypto_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Crypto Dashboard API", version="1.0.0")

app.include_router(crypto_router)

@app.get("/")
async def root():
    return {"message": "Crypto Dashboard API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}