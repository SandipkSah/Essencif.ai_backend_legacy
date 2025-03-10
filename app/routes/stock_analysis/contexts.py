from quart import Blueprint, jsonify, request
from app.models.context import Context
from app.models.prompt import Prompt
from app.models.parameter import Parameter
from app.models.user_role import userRole  # Import the userRole model
from app.models.applicationAdmins import ApplicationAdmins  # Import ApplicationAdmins model
from app.models.solution_group import SolutionGroup  # Import SolutionGroup model

contexts_blueprint = Blueprint('contexts', __name__)

EssencifAI_ID = 1

@contexts_blueprint.route('/api/contexts', methods=['GET'])
async def get_contexts():
    """Retrieves context information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        # Check if the user is a global admin
        is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()
        if is_admin:
            # Provide access to all contexts with the role of admin
            contexts = await Context.all().prefetch_related('owner')
            context_data = [{
                "id": context.context_id,
                "owner": context.owner.name,  # Get owner's name instead of ID
                "contextname": context.context_name,
                "context": context.detailed_definition
            } for context in contexts]
            return jsonify({"contexts": context_data})
        
        # All users should have access to EssencifAI_ID contexts, plus additional ones if they belong to user groups
        solution_groups = [EssencifAI_ID]
        if user_id:
            solution_groups += await userRole.filter(user_id=user_id).values_list("solution_group_id", flat=True)
        
        # Fetch all contexts plus additional ones from user groups
        contexts = await Context.filter(owner_id__in=solution_groups).prefetch_related('owner')
        
        context_data = [{
            "id": context.context_id,
            "owner": context.owner.name,  # Get owner's name instead of ID
            "contextname": context.context_name,
            "context": context.detailed_definition
        } for context in contexts]
        
        return jsonify({"contexts": context_data})
    
    except Exception as e:
        print(f"Error occurred while retrieving contexts: {str(e)}")
        return jsonify({"error": f"Failed to get contexts. {str(e)}"}), 500



