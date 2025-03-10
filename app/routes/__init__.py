# Import blueprints (same as before)
from app.routes.base_routes import base_blueprint

from app.routes.common.user_management.admin_check import admin_check_blueprint
from app.routes.common.user_management.rights_routes import rights_blueprint
from app.routes.common.user_management.implementation_routes import implementation_blueprint
from app.routes.common.stock_search_routes import stock_search_blueprint

from app.routes.reports.finance.financial_data_routes import financial_data_blueprint
# from app.routes.finance.current_price import current_price_blueprint
# from app.routes.finance.financial_statements import financial_statements_blueprint
# from app.routes.finance.analyst_sentiments import analyst_sentiments_blueprint
# from app.routes.finance.business_model import business_model_blueprint
# from app.routes.finance.time_series import time_series_blueprint
# from app.routes.finance.total_revenue import total_revenue_blueprint
# from app.routes.finance.ebitda import ebitda_blueprint
# from app.routes.finance.balance_sheet import balance_sheet_blueprint

from app.routes.reports.news.recent_news import recent_news_blueprint

from app.routes.stock_analysis.GPT_analysis_routes import GPT_analysis_blueprint
from app.routes.stock_analysis.contexts import contexts_blueprint
from app.routes.stock_analysis.prompts import prompts_blueprint
from app.routes.stock_analysis.parameters import parameters_blueprint
from app.routes.stock_analysis.prompts_upload_routes import prompt_upload_blueprint
from app.routes.stock_analysis.stock_details_routes import stock_details_blueprint

from app.routes.knowledge_management.queryQDrant import query_blueprint
from app.routes.knowledge_management.links import link_blueprint
from app.routes.knowledge_management.rating import rating_blueprint
from app.routes.knowledge_management.points import point_blueprint



def register_blueprint(app):
    # Register blueprints (same as before)

    # base route for base route for testing
    app.register_blueprint(base_blueprint)

    # routes for user context for authorization and so.
    app.register_blueprint(admin_check_blueprint)
    app.register_blueprint(rights_blueprint)
    app.register_blueprint(implementation_blueprint)


    # routes for portfolio_analysis
    # app.register_blueprint(context_prompt_blueprint)
    app.register_blueprint(stock_search_blueprint)
    app.register_blueprint(stock_details_blueprint)
    app.register_blueprint(contexts_blueprint)
    app.register_blueprint(prompts_blueprint)
    app.register_blueprint(parameters_blueprint)
    app.register_blueprint(GPT_analysis_blueprint)
    app.register_blueprint(prompt_upload_blueprint)
    


    # routes for knowledge management
    app.register_blueprint(query_blueprint)
    app.register_blueprint(link_blueprint)
    app.register_blueprint(rating_blueprint)
    app.register_blueprint(point_blueprint)
    
    

    # routes for the finance reports
    app.register_blueprint(financial_data_blueprint)
    # app.register_blueprint(current_price_blueprint)
    # app.register_blueprint(financial_statements_blueprint)
    # app.register_blueprint(analyst_sentiments_blueprint)
    # app.register_blueprint(business_model_blueprint)
    # app.register_blueprint(time_series_blueprint)
    # app.register_blueprint(total_revenue_blueprint)
    # app.register_blueprint(ebitda_blueprint)
    # app.register_blueprint(balance_sheet_blueprint)
    

    # routes for the news report
    app.register_blueprint(recent_news_blueprint)

