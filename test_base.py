import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_index_route():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        # Use .text instead of await response.text
        assert "Hello" in response.text