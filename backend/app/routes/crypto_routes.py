from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.crypto_repository import CryptoRepository

router = APIRouter(prefix="/cryptos", tags=["cryptos"])

@router.get("/")
def get_all_cryptos(db: Session = Depends(get_db)):
    repo = CryptoRepository(db)
    return repo.get_all()

@router.post("/")
def create_crypto(
    symbol: str,
    name: str,
    price_usd: float,
    market_cap: float,
    db: Session = Depends(get_db)
):
    repo = CryptoRepository(db)
    return repo.create(symbol, name, price_usd, market_cap)

@router.get("/{symbol}")
def get_crypto_by_symbol(symbol: str, db: Session = Depends(get_db)):
    repo = CryptoRepository(db)
    return repo.get_by_symbol(symbol)