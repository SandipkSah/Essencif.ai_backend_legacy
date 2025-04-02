from quart import Quart
from quart_cors import cors
from dotenv import load_dotenv
from tortoise import Tortoise


import config
from quart import current_app
import os
from app.routes import register_blueprint

app = Quart(__name__)
app.config.from_object(config)
app = cors(app, allow_origin="*")



load_dotenv(override=True)

# Database initialization function
async def init_tortoise():
    await Tortoise.init(
        db_url=os.getenv("DB_URL", "sqlite://essencifai"),
        modules={
            "models": [
                "app.models.applicationAdmins",
                "app.models.context",
                "app.models.dim_fact",
                "app.models.dim_object",
                "app.models.document",
                "app.models.fact",
                "app.models.implementation",
                "app.models.parameter",
                "app.models.user_point",
                "app.models.prompt", 
                "app.models.rating", 
                "app.models.result",
                "app.models.solution_group",
                "app.models.user_role",
                "app.models.user",
                "app.models.user_question_history", 
                ]
            },
    )
    # await Tortoise.generate_schemas(safe=True)
    

# Initialize the database (you should now await this in the main async function)
@app.before_serving
async def init():
    await init_tortoise()



register_blueprint(app)

# CORS header middleware
@app.after_request
async def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.getenv("PORT", 8080))  # Default to 8000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)