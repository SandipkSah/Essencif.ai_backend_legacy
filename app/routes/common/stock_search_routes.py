from quart import Blueprint, jsonify
import pandas as pd
import json
import os

stock_search_blueprint = Blueprint('stock_search', __name__)

# Get the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(project_root, "project root directory")

# Construct the path to the CSV file
csv_file_path = os.path.join(project_root, '../updated_stocks_list.csv')
print(csv_file_path, "just checking")


try:
    stocks_df = pd.read_csv(csv_file_path, delimiter=";", encoding='MacRoman')
except FileNotFoundError:
    stocks_df = pd.DataFrame()  # Create an empty DataFrame or handle the error as needed

@stock_search_blueprint.route('/api/search_stocks/<search_query>', methods=['GET'])
def stock_search(search_query):
    if stocks_df.empty:
        return jsonify({"error": "Stocks data not available"}), 500

    search_query_lower = search_query.lower()

    # Handle the case where ISIN might be NaN
    results = stocks_df[
        stocks_df['Name'].str.lower().str.contains(search_query_lower) |
        stocks_df['ISIN'].fillna('').str.lower().str.contains(search_query_lower)
    ]
    results = results[results['ISIN'].notna() & (results['ISIN'] != '')]
    stringified_json = json.dumps(results.to_dict(orient='records'))
    res = json.loads(stringified_json)
    return jsonify(res)