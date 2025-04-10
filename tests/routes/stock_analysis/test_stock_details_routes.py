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
async def test_swot_analysis_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:  # Increase timeout
        response = await client.get(f'{BASE_URL}/api/swot_analysis/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "swot_analysis" in data

@pytest.mark.asyncio
async def test_swot_analysis_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:  # Increase timeout
        response = await client.get(f'{BASE_URL}/api/swot_analysis/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 200  # Adjust based on actual response
        data = response.json()
        assert "swot_analysis" in data

