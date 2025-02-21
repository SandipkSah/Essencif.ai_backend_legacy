from quart import Blueprint, jsonify, request
from app.ormModels.context import Context
from app.ormModels.prompt import Prompt
from app.ormModels.parameter import Parameter
from app.ormModels.user_right import UserRight  # Import the UserRight model

context_prompt_blueprint = Blueprint('context_prompt', __name__)

DEFAULT_OWNER_ID = 1

@context_prompt_blueprint.route('/api/contexts', methods=['GET'])
async def get_contexts():
    """Retrieves context information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        # All users should have access to DEFAULT_OWNER_ID contexts, plus additional ones if they belong to user groups
        user_groups = [DEFAULT_OWNER_ID]
        if user_id:
            user_groups += await UserRight.filter(user_id=user_id).values_list("user_group_id", flat=True)
        
        # Fetch all contexts plus additional ones from user groups
        contexts = await Context.filter(owner_id__in=user_groups).prefetch_related('owner')
        
        context_data = [{
            "id": context.id,
            "owner": context.owner.name,  # Get owner's name instead of ID
            "contextname": context.name,
            "context": context.detailed_definition
        } for context in contexts]
        
        return jsonify({"contexts": context_data})
    
    except Exception as e:
        print(f"Error occurred while retrieving contexts: {str(e)}")
        return jsonify({"error": f"Failed to get contexts. {str(e)}"}), 500


@context_prompt_blueprint.route('/api/prompts', methods=['GET'])
async def get_prompts():
    """Retrieves prompt information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        user_groups = [DEFAULT_OWNER_ID]
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


@context_prompt_blueprint.route('/api/parameters', methods=['GET'])
async def get_parameters():
    """Retrieves parameter information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        user_groups = [DEFAULT_OWNER_ID]
        if user_id:
            user_groups += await UserRight.filter(user_id=user_id).values_list("user_group_id", flat=True)
        
        print(f"User ID: {user_id}, User Groups: {user_groups}")
        
        # Fetch all parameters plus additional ones from user groups
        parameters = await Parameter.filter(owner_id__in=user_groups).values(
            'id', 'parameter_set', 'engine', 'max_tokens', 'temperature', 'top_p', 'n',
            'stream', 'presence_penalty', 'frequency_penalty', 'username', 'owner_id', 'owner__name'
        )
        
        print(f"Retrieved parameters: {parameters}")
        
        parameter_data = [{
            "id": param['id'],
            "owner": param['owner__name'],  # Get owner's name instead of ID
            "parameterset": param['parameter_set'],
            "engine": param['engine'],
            "max_tokens": param['max_tokens'],
            "temperature": param['temperature'],
            "top_p": param['top_p'],
            "n": param['n'],
            "stream": param['stream'],
            "presence_penalty": param['presence_penalty'],
            "frequency_penalty": param['frequency_penalty'],
            "user": param['username']
        } for param in parameters]
        
        return jsonify({"parameters": parameter_data})
    
    except Exception as e:
        print(f"Error occurred while retrieving parameters: {str(e)}")
        return jsonify({"error": f"Failed to get parameters. {str(e)}"}), 500
