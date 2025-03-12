import pytest
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")
VALID_USER_ID = os.getenv("VALID_USER_ID")
INVALID_USER_ID = os.getenv("INVALID_USER_ID")
PROJECT_ID = os.getenv("PROJECT_ID")

@pytest.mark.asyncio
async def test_get_implementations_with_valid_projects():
    async with httpx.AsyncClient() as client:
        response = await client.post(f'{BASE_URL}/api/implementations', json={"projects": [PROJECT_ID]})
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for item in data:
            assert "implementation_id" in item
            assert "implementation" in item
            assert "owner" in item
            assert "route" in item
            assert "colours" in item
            assert isinstance(item["colours"], list)

@pytest.mark.asyncio
async def test_get_implementations_with_empty_projects():
    async with httpx.AsyncClient() as client:
        response = await client.post(f'{BASE_URL}/api/implementations', json={"projects": []})
        assert response.status_code == 400
        assert response.json() == {"error": "projects_list is required"}

@pytest.mark.asyncio
async def test_get_implementations_missing_projects():
    async with httpx.AsyncClient() as client:
        response = await client.post(f'{BASE_URL}/api/implementations', json={})
        assert response.status_code == 400
        assert response.json() == {"error": "projects_list is required"}

# @pytest.mark.asyncio
# async def test_get_implementations_internal_server_error(mocker):
#     mocker.patch('app.models.implementation.Implementation.filter', side_effect=Exception("Test exception"))
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f'{BASE_URL}/api/implementations', json={"projects": ["project1", "project2"]})
#         assert response.status_code == 500
#         assert response.json() == {"error": "An error occurred: Test exception", "status_code": 500}