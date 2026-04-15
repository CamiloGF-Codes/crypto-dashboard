from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    crypto_id = Column(Integer, ForeignKey("cryptos.id"), nullable=False)
    price_usd = Column(Float, nullable=False)
    recorded_at = Column(DateTime, server_default=func.now())

    crypto = relationship("Crypto", back_populates="price_history")