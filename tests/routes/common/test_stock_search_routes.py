import pytest
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")

@pytest.mark.asyncio
async def test_stock_search_with_valid_query():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/search_stocks/apple')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            assert "Name" in item
            assert "ISIN" in item

@pytest.mark.asyncio
async def test_stock_search_with_invalid_query():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/search_stocks/invalidquery')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0  # Assuming no results for invalid query

