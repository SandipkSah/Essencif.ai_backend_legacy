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
async def test_get_links_with_valid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/links/personal?tippgeber_id={VALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "documents" in data

@pytest.mark.asyncio
async def test_get_links_with_invalid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/links/personal?tippgeber_id={INVALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "documents" in data

@pytest.mark.asyncio
async def test_get_links_missing_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/links/personal')
        assert response.status_code == 400
        assert response.json() == {"error": "userID is required"}

@pytest.mark.asyncio
async def test_get_all_links():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/links/all')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "documents" in data

@pytest.mark.asyncio
async def test_add_link():
    async with httpx.AsyncClient(timeout=300.0) as client:
        payload = {
            "url": "http://example.com",
            "title": "Example",
            "type": "article",
            "user": {
                "id": VALID_USER_ID,
                "name": "Test User"
            }
        }
        response = await client.post(f'{BASE_URL}/api/links', json=payload)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)

# @pytest.mark.asyncio
# async def test_update_link():
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         payload = {
#             "title": "Updated Title"
#         }
#         response = await client.put(f'{BASE_URL}/api/links?id=valid_id', json=payload)
#         assert response.status_code == 200
#         data = response.json()
#         assert isinstance(data, dict)
#         assert "point_id" in data

# @pytest.mark.asyncio
# async def test_delete_link():
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         response = await client.delete(f'{BASE_URL}/api/links?id=valid_id')
#         assert response.status_code == 200
#         data = response.json()
#         assert isinstance(data, dict)