import httpx
from sqlalchemy.orm import Session
from app.repositories.crypto_repository import CryptoRepository

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

async def fetch_crypto_prices(symbols: list[str]) -> dict:
    params = {
        "ids": ",".join(symbols),
        "vs_currencies": "usd",
        "include_market_cap": "true"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(COINGECKO_URL, params=params)

        if not response.status_code == 200:
            raise Exception(f"CoinGecko error: {response.status_code}")

        return response.json()

async def sync_crypto_prices(db: Session):
    data = await fetch_crypto_prices(["bitcoin", "ethereum", "solana"])

    repo = CryptoRepository(db)

    for coin_id, values in data.items():
        repo.create(
            symbol=coin_id.upper(),
            name=coin_id.capitalize(),
            price_usd=values["usd"],
            market_cap=values.get("usd_market_cap", 0)
        )

    return data