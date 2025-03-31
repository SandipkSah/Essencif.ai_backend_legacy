import pytest
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")
VALID_USER_ID = os.getenv("VALID_USER_ID")
INVALID_USER_ID = os.getenv("INVALID_USER_ID")

@pytest.mark.asyncio
async def test_get_user_points_with_valid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/points?user_id={VALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "user_id" in data
        assert "points" in data
        assert "tier" in data

@pytest.mark.asyncio
async def test_get_user_points_with_invalid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/points?user_id={INVALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "user_id" in data
        assert "points" in data
        assert "tier" in data

@pytest.mark.asyncio
async def test_get_user_points_missing_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/points')
        assert response.status_code == 400
        assert response.json() == {"error": "userID is required"}
