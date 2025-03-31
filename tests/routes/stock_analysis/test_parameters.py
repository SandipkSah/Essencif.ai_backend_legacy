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
async def test_get_parameters_with_valid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/parameters?user_id={VALID_USER_ID}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "parameters" in data
        assert isinstance(data["parameters"], list)

@pytest.mark.asyncio
async def test_get_parameters_with_invalid_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/parameters?user_id={INVALID_USER_ID}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 200  # Adjust based on actual response
        data = response.json()
        assert "parameters" in data
        assert isinstance(data["parameters"], list)

@pytest.mark.asyncio
async def test_get_parameters_missing_user_id():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/parameters')
        print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 200  # Adjust based on actual response
        data = response.json()
        assert "parameters" in data
        assert isinstance(data["parameters"], list)

