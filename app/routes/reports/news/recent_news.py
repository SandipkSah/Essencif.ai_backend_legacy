from quart import Blueprint, jsonify
import requests
from datetime import datetime, timedelta
import yfinance as yf
import os
import traceback


recent_news_blueprint = Blueprint('recent_news', __name__)

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY')


@recent_news_blueprint.route('/api/recent_news/<ticker>', methods=['GET'])
def get_recent_news(ticker):
    try:
        current_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')
        url = f'https://finnhub.io/api/v1/company-news?symbol={ticker}&from={start_date}&to={current_date}&token={FINNHUB_API_KEY}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return jsonify(data[:10])  # Return only the first 10 news articles
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
