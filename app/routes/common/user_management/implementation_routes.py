from quart import Blueprint, request, jsonify
from app.models.implementation import Implementation

implementation_blueprint = Blueprint('implementation', __name__)

@implementation_blueprint.route('/api/implementations', methods=['POST'])
async def get_implementations():
    data = await request.get_json()
    project_ids = data.get('projects')
    print("what are the projeeeeeeeeeee", project_ids)
    if not project_ids:
        return jsonify({"error": "projects_list is required"}), 400

    implementations = await Implementation.filter(owner_id__in=project_ids).all()
    implementations_data = [
        {
            "implementation_id": impl.implementation_id,
            "implementation": impl.implementation,
            "owner": impl.owner_id,
            "route": impl.route,
            "colours": [
                impl.colour_1, impl.colour_2, impl.colour_3,
                impl.colour_4, impl.colour_5, impl.colour_6, impl.colour_7
            ]
        }
        for impl in implementations
    ]
    # print("implementations_data", implementations_data)
    return jsonify(implementations_data), 200