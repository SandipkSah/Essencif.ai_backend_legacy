import pytest
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")
VALID_TICKER = os.getenv("VALID_TICKER")
INVALID_TICKER = os.getenv("INVALID_TICKER")

@pytest.mark.asyncio
async def test_get_recent_news_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/recent_news/{VALID_TICKER}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 10  # Ensure only the first 10 news articles are returned

@pytest.mark.asyncio
async def test_get_recent_news_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/recent_news/{INVALID_TICKER}')
        assert response.status_code == 200  # Adjust based on actual response
        data = response.json()
        assert data == []  # Expecting an empty list

