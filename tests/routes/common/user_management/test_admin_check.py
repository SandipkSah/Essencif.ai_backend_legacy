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
async def test_is_admin_with_valid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/admin_check?user_id={VALID_USER_ID}')
        assert response.status_code == 200
        assert response.text == "true"

@pytest.mark.asyncio
async def test_is_admin_with_invalid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/admin_check?user_id={INVALID_USER_ID}')
        assert response.status_code == 200
        assert response.text == "false"

@pytest.mark.asyncio
async def test_is_admin_missing_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/admin_check')
        assert response.status_code == 400
        assert response.json() == {"error": "Missing 'user_id' parameter"}