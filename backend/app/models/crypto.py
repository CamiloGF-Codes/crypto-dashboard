from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Crypto(Base):
    __tablename__ = "cryptos"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False,unique=True)
    name = Column(String, nullable=False)
    price_usd = Column(Float, nullable=False)
    market_cap = Column(Float)
    recorded_at = Column(DateTime, server_default=func.now())
    
    price_history = relationship("PriceHistory", back_populates="crypto")