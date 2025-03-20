import pytest
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")
VALID_USER_ID = os.getenv("VALID_USER_ID")
INVALID_USER_ID = os.getenv("INVALID_USER_ID")
VALID_DOCUMENT_ID = os.getenv("VALID_DOCUMENT_ID")

@pytest.mark.asyncio
async def test_create_or_update_rating_with_invalid_data():
    async with httpx.AsyncClient() as client:
        payload = {
            "user_id": VALID_USER_ID,
            "document_id": VALID_DOCUMENT_ID,
            "rating": 6  # Invalid rating
        }
        response = await client.post(f'{BASE_URL}/api/rating', json=payload)
        assert response.status_code == 400
        assert response.json() == {"error": "Rating must be a number between 1 and 5."}

@pytest.mark.asyncio
async def test_create_or_update_rating_missing_fields():
    async with httpx.AsyncClient() as client:
        payload = {
            "user_id": VALID_USER_ID,
            "rating": 4
        }
        response = await client.post(f'{BASE_URL}/api/rating', json=payload)
        assert response.status_code == 400
        assert response.json() == {"error": "Invalid JSON data or missing fields (document_id, rating, user_id)."}

@pytest.mark.asyncio
async def test_get_user_ratings_with_valid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rating?user_id={VALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            assert "document_id" in item
            assert "rating" in item

@pytest.mark.asyncio
async def test_get_user_ratings_with_invalid_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rating?user_id={INVALID_USER_ID}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0  # Assuming no ratings for invalid user ID

@pytest.mark.asyncio
async def test_get_user_ratings_missing_user_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{BASE_URL}/api/rating')
        assert response.status_code == 400
        assert response.json() == {"error": "user_id parameter is required"}
