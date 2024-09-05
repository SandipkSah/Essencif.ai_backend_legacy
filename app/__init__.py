from flask import Flask, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Import blueprints
from app.routes.base_routes import base_blueprint
from app.routes.stock_search_routes import stock_search_blueprint
from app.routes.stock_details_routes import stock_details_blueprint
from app.routes.financial_data_routes import financial_data_blueprint  # Import financial data routes
from app.routes.GPT_analysis_routes import GPT_analysis_blueprint  # Import document analysis routes
from app.routes.context_prompt_routes import context_prompt_blueprint  # Import context prompt routes

# Register blueprints
app.register_blueprint(base_blueprint)
app.register_blueprint(stock_search_blueprint)
app.register_blueprint(stock_details_blueprint)
app.register_blueprint(financial_data_blueprint)  # Register financial data routes
app.register_blueprint(GPT_analysis_blueprint)  # Register document analysis routes
app.register_blueprint(context_prompt_blueprint)  # Register context prompt routes

# Ensure CORS headers are applied to every response
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(debug=True)
