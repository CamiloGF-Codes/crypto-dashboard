from contextlib import asynccontextmanager
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import engine, Base, SessionLocal
from app.models import crypto
from app.models import price_history
from app.routes.crypto_routes import router as crypto_router
from app.services.crypto_service import sync_crypto_prices
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

scheduler = AsyncIOScheduler()

async def scheduled_sync():
    db = SessionLocal()
    try:
        await sync_crypto_prices(db)
        print("Sync completado")
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.add_job(scheduled_sync, "interval", minutes=5)
    scheduler.start()
    print("Scheduler iniciado")
    yield
    scheduler.shutdown()
    print("Scheduler apagado")

app = FastAPI(title="Crypto Dashboard API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(crypto_router)

@app.get("/")
async def root():
    return {"message": "Crypto Dashboard API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}