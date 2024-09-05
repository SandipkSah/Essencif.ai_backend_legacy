## Overview
This Flask application serves as the backend for a stock information web application. It provides various endpoints to fetch stock-related data such as current prices, financial statements, analyst sentiments, recent news, and SWOT analysis. The application integrates multiple APIs including Finnhub, Alpha Vantage, and Yahoo Finance to gather the required data.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Pip (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/khadkauj/FinanceBackendFlask.git
   cd FinanceBackendFlask
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Ensure you have the following API keys set in your environment:
   - `ALPHA_VANTAGE_API_KEY`
   - `FINNHUB_API_KEY`
   - `OPENAI_API_KEY`

### Running the Application
```bash
python3  app.py 
```
OR 
```bash
flask  run 
```

The application will start on `http://localhost:5000`.

## API Documentation

### 1. Index
- **URL:** `/`
- **Description:** Check if the server is running.

### 2. Search Stocks
- **URL:** `/api/search_stocks/<search_query>`
- **Description:** Search for stocks by name or ISIN.

### 3. Get Ticker by ISIN
- **URL:** `/api/get_ticker/<isin>`
- **Description:** Retrieve the stock ticker symbol for a given ISIN.

### 4. Current Price
- **URL:** `/api/current_price/<ticker>`
- **Description:** Get the current price of a stock and generate a summary.

### 5. Recent News
- **URL:** `/api/recent_news/<ticker>`
- **Description:** Get the top 3 recent news articles for a stock and generate a summary.

### 6. Financial Statements
- **URL:** `/api/financial_statements/<ticker>`
- **Description:** Get financial statements for a stock and generate a summary.

### 7. Analyst Sentiments
- **URL:** `/api/analyst_sentiments/<ticker>`
- **Description:** Get analyst sentiments for a stock and generate a summary.

### 8. Business Model
- **URL:** `/api/business_model/<ticker>`
- **Description:** Get the business model for a stock and generate a summary.

### 9. Time Series
- **URL:** `/api/time_series/<ticker>`
- **Description:** Get time series data (historical data) for a stock.

### 10. SWOT Analysis
- **URL:** `/api/swot_analysis/<ticker>`
- **Description:** Get SWOT analysis for a stock and generate a summary.

### 11. Summary Generation
- **URL:** Used internally by other endpoints.
- **Description:** Uses OpenAI's API to generate summaries for the data fetched from other endpoints.

### Notes
1. The application was initially hosted on Heroku, but due to the associated costs, it has been moved to [Koyeb](https://www.koyeb.com/) for free hosting. The current server link is accessible in the ReactJS application.

### Further Improvements

1. The `app.py` is using APIs from Finnhub, YFinance, and Alpha Vantage. There is a requirement to have an option to make all requests via the API of a selected API only at a time.
2. Each API request should be placed within a function and called only when necessary.
