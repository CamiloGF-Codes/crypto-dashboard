import httpx
import asyncio
from sqlalchemy.orm import Session
from app.repositories.crypto_repository import CryptoRepository

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

async def fetch_crypto_prices(symbols: list[str], max_retries: int = 3, delay: float = 1.0) -> dict:
    for attempt in range(1, max_retries + 1):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(COINGECKO_URL, params={
                    "ids": ",".join(symbols),
                    "vs_currencies": "usd",
                    "include_market_cap": "true"
                })

                if response.status_code != 200:
                    raise Exception(f"CoinGecko error: {response.status_code}")

                return response.json()

        except Exception as error:
            print(f"Intento {attempt}/{max_retries} falló: {error}")
            if attempt == max_retries:
                raise
            await asyncio.sleep(delay)

async def sync_crypto_prices(db: Session):
    data = await fetch_crypto_prices(["bitcoin", "ethereum", "solana"])

    repo = CryptoRepository(db)

    for coin_id, values in data.items():
        repo.upsert(
            symbol=coin_id.upper(),
            name=coin_id.capitalize(),
            price_usd=values["usd"],
            market_cap=values.get("usd_market_cap", 0)
        )

    return data