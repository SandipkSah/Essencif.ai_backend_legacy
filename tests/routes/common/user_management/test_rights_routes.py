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
async def test_get_user_roles_with_valid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rights?user_id={VALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            assert "project" in item
            assert "role" in item
            assert "project_id" in item

@pytest.mark.asyncio
async def test_get_user_roles_with_invalid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rights?user_id={INVALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1  # Assuming no roles for invalid user ID

@pytest.mark.asyncio
async def test_get_user_roles_missing_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rights')
        assert response.status_code == 400
        assert response.json() == {"error": "userID is required"}

