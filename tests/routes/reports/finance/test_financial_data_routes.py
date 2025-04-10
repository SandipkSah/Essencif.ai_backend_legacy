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
async def test_get_current_price_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/current_price/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "c" in data  # Current price
        assert "h" in data  # High price of the day
        assert "l" in data  # Low price of the day

@pytest.mark.asyncio
async def test_get_current_price_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/current_price/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 200  # Adjust based on actual response
        data = response.json()
        assert "c" in data  # Current price
        assert "h" in data  # High price of the day
        assert "l" in data  # Low price of the day

@pytest.mark.asyncio
async def test_get_financial_statements_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/financial_statements/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "Symbol" in data
        assert "Name" in data

# @pytest.mark.asyncio
# async def test_get_financial_statements_with_invalid_ticker():
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         response = await client.get(f'{BASE_URL}/api/financial_statements/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
#         assert response.status_code == 404  # Adjust based on actual response
#         data = response.json()
#         assert "error" in data

@pytest.mark.asyncio
async def test_get_analyst_sentiments_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/analyst_sentiments/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_business_model_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/business_model/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "ticker" in data

@pytest.mark.asyncio
async def test_get_business_model_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/business_model/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 404  # Adjust based on actual response
        data = response.json()
        assert "error" in data

@pytest.mark.asyncio
async def test_get_time_series_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/time_series/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], list)

@pytest.mark.asyncio
async def test_get_time_series_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/time_series/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 404  # Adjust based on actual response
        data = response.json()
        assert "error" in data

@pytest.mark.asyncio
async def test_total_revenue_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/total_revenue/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)

@pytest.mark.asyncio
async def test_total_revenue_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/total_revenue/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 404  # Adjust based on actual response
        data = response.json()
        assert "error" in data

@pytest.mark.asyncio
async def test_ebitda_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/ebitda/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)

@pytest.mark.asyncio
async def test_ebitda_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/ebitda/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 404  # Adjust based on actual response
        data = response.json()
        assert "error" in data

@pytest.mark.asyncio
async def test_balance_sheet_with_valid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/balance_sheet/{VALID_TICKER}')
        # print(response.json())  # Print the response
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)

@pytest.mark.asyncio
async def test_balance_sheet_with_invalid_ticker():
    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.get(f'{BASE_URL}/api/balance_sheet/{INVALID_TICKER}')
        # print(response.status_code)  # Print the status code
        # print(response.json())  # Print the response
        assert response.status_code == 404  # Adjust based on actual response
        data = response.json()
        assert "error" in data