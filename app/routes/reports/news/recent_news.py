from quart import Blueprint, jsonify
import httpx
from datetime import datetime, timedelta
import os
import traceback

recent_news_blueprint = Blueprint('recent_news', __name__)

FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY')

@recent_news_blueprint.route('/api/recent_news/<ticker>', methods=['GET'])
async def get_recent_news(ticker):
    try:
        if not FINNHUB_API_KEY:
            return jsonify({"error": "API key not configured"}), 500
            
        current_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')
        url = f'https://finnhub.io/api/v1/company-news?symbol={ticker}&from={start_date}&to={current_date}&token={FINNHUB_API_KEY}'
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=100.0)
            response.raise_for_status()
            data = response.json()
            
        return jsonify(data[:10])  # Return only the first 10 news articles
    except httpx.RequestError as e:
        print(f"Request error for {ticker}: {str(e)}")
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except httpx.HTTPStatusError as e:
        print(f"HTTP error for {ticker}: {str(e)}")
        return jsonify({"error": f"API error: {str(e)}"}), 500
    except ValueError as e:
        print(f"JSON error for {ticker}: {str(e)}")
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        print(f"Unexpected error for {ticker}: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500