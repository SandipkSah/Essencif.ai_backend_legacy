from quart import Blueprint, jsonify, request
from app.models.context import Context
from app.models.prompt import Prompt
from app.models.parameter import Parameter
from app.models.user_right import UserRight  # Import the UserRight model
from app.models.applicationAdmins import ApplicationAdmins  # Import ApplicationAdmins model
from app.models.user_group import UserGroup  # Import UserGroup model

prompts_blueprint = Blueprint('prompts', __name__)

EssencifAI_ID = 1


@prompts_blueprint.route('/api/prompts', methods=['GET'])
async def get_prompts():
    """Retrieves prompt information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        # Check if the user is a global admin
        is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()
        if is_admin:
            # Provide access to all prompts with the role of admin
            prompts = await Prompt.all().prefetch_related('owner')
            prompt_data = [{
                "id": prompt.id,
                "owner": prompt.owner.name,  # Get owner's name instead of ID
                "promptname": prompt.name,
                "prompt": prompt.detailed_definition
            } for prompt in prompts]
            return jsonify({"prompts": prompt_data})
        
        user_groups = [EssencifAI_ID]
        if user_id:
            user_groups += await UserRight.filter(user_id=user_id).values_list("user_group_id", flat=True)
        
        # Fetch all prompts plus additional ones from user groups
        prompts = await Prompt.filter(owner_id__in=user_groups).prefetch_related('owner')
        
        prompt_data = [{
            "id": prompt.id,
            "owner": prompt.owner.name,  # Get owner's name instead of ID
            "promptname": prompt.name,
            "prompt": prompt.detailed_definition
        } for prompt in prompts]
        
        return jsonify({"prompts": prompt_data})
    
    except Exception as e:
        print(f"Error occurred while retrieving prompts: {str(e)}")
        return jsonify({"error": f"Failed to get prompts. {str(e)}"}), 500

