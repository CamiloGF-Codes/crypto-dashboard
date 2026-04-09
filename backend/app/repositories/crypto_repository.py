from sqlalchemy.orm import Session
from app.models.crypto import Crypto

class CryptoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, symbol: str, name: str, price_usd: float, market_cap: float):
        crypto = Crypto(
            symbol=symbol,
            name=name,
            price_usd=price_usd,
            market_cap=market_cap
        )
        self.db.add(crypto)
        self.db.commit()
        self.db.refresh(crypto)
        return crypto

    def get_all(self):
        return self.db.query(Crypto).all()

    def get_by_symbol(self, symbol: str):
        return self.db.query(Crypto).filter(Crypto.symbol == symbol).first()