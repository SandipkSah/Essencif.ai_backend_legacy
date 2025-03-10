from quart import Blueprint, jsonify
import requests
from datetime import datetime, timedelta
import yfinance as yf
import os
import traceback


financial_data_blueprint = Blueprint('financial_data', __name__)

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY')

@financial_data_blueprint.route('/api/current_price/<ticker>', methods=['GET'])
def get_current_price(ticker):
    try:
        url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={FINNHUB_API_KEY}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@financial_data_blueprint.route('/api/financial_statements/<ticker>', methods=['GET'])
def get_financial_statements(ticker):
    try:
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "Error Message" in data:
            return jsonify({"error": data["Error Message"]}), 404
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/analyst_sentiments/<ticker>', methods=['GET'])
def get_analyst_sentiments(ticker):
    try:
        url = f'https://finnhub.io/api/v1/stock/recommendation?symbol={ticker}&token={FINNHUB_API_KEY}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/business_model/<ticker>', methods=['GET'])
def get_business_model(ticker):
    try:
        url = f'https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={FINNHUB_API_KEY}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # If empty response, it usually means the ticker wasn't found
        if not data:
            return jsonify({"error": f"No data found for ticker {ticker}"}), 404
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/time_series/<ticker>', methods=['GET'])
def get_time_series(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1y")  # Fetch 1 year of historical data
        if data.empty:
            return jsonify({"error": f"No historical data found for ticker {ticker}"}), 404
        data = data.reset_index().to_dict(orient='records')
        return jsonify({"data": data})
    except ImportError as e:
        return jsonify({"error": "yfinance module not installed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/total_revenue/<ticker>', methods=['GET'])
def total_revenue(ticker):
    """Retrieves total revenue for a given ticker."""
    try:
        yf_ticker = yf.Ticker(ticker)
        financials = yf_ticker.financials.T
        if financials.empty:
            return jsonify({"error": f"No financial data found for ticker {ticker}"}), 404
        if "Total Revenue" not in financials.columns:
            return jsonify({"error": "Total Revenue data not available"}), 404
        total_revenue = financials["Total Revenue"]
        json_data = total_revenue.to_json(orient='index')
        return json_data
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/ebitda/<ticker>', methods=['GET'])
def ebitda(ticker):
    """Retrieves EBITDA for a given ticker."""
    try:
        yf_ticker = yf.Ticker(ticker)
        financials = yf_ticker.financials.T
        if financials.empty:
            return jsonify({"error": f"No financial data found for ticker {ticker}"}), 404
        if "EBITDA" not in financials.columns:
            return jsonify({"error": "EBITDA data not available"}), 404
        ebitda = financials["EBITDA"]
        json_data = ebitda.to_json(orient='index')
        return json_data
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@financial_data_blueprint.route('/api/balance_sheet/<ticker>', methods=['GET'])
def balance_sheet(ticker):
    """Retrieves balance sheet data for a given ticker."""
    try:
        yf_ticker = yf.Ticker(ticker)
        balance_sheet_table = yf_ticker.balancesheet
        if balance_sheet_table.empty:
            return jsonify({"error": f"No balance sheet data found for ticker {ticker}"}), 404
        json_data = balance_sheet_table.to_json(orient='index')
        return json_data
    except Exception as e:
        return jsonify({"error": str(e)}), 500