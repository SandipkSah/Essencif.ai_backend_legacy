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
    payload = {
        "user_id": VALID_USER_ID,
        "email": f"test_{VALID_USER_ID}@example.com",
        "given_name": "Valid",
        "surname": "User",
        "company": "ValidCorp",
        "position": "Developer"
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/rights', json=payload)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            assert "project" in item
            assert "role" in item
            assert "project_id" in item

@pytest.mark.asyncio
async def test_get_user_roles_with_invalid_user_id():
    payload = {
        "user_id": INVALID_USER_ID
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/rights', json=payload)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1  # Only Essencif.AI default role

@pytest.mark.asyncio
async def test_get_user_roles_missing_user_id():
    payload = {}

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/rights', json=payload)
        # assert response.status_code == 400
        assert "error" in response.json() 

@pytest.mark.asyncio
async def test_get_user_roles_invalid_json():
    headers = {"Content-Type": "application/json"}

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/rights', content="not-a-json", headers=headers)
        # assert response.status_code == 400
        assert "error" in response.json()
