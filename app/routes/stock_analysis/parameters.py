from quart import Blueprint, jsonify, request
from app.models.parameter import Parameter
from app.models.user_role import userRole  # Import the userRole model
from app.models.applicationAdmins import ApplicationAdmins  # Import ApplicationAdmins model
from app.models.solution_group import SolutionGroup  # Import SolutionGroup model

parameters_blueprint = Blueprint('parameters', __name__)

EssencifAI_ID = 1



@parameters_blueprint.route('/api/parameters', methods=['GET'])
async def get_parameters():
    """Retrieves parameter information from the database, ensuring all users have access."""
    try:
        user_id = request.args.get("user_id", type=int)
        
        # Check if the user is a global admin
        is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()
        if is_admin:
            # Provide access to all parameters with the role of admin
            parameters = await Parameter.all().values(
                'parameter_id', 'parameter_set', 'engine', 'max_tokens', 'temperature', 'top_p', 'n',
                'stream', 'presence_penalty', 'frequency_penalty', 'username', 'owner_id', 'owner__name'
            )
            parameter_data = [{
                "id": param['parameter_id'],
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
        
        solution_groups = [EssencifAI_ID]
        if user_id:
            solution_groups += await userRole.filter(user_id=user_id).values_list("solution_group_id", flat=True)
        
        print(f"User ID: {user_id}, User Groups: {solution_groups}")
        
        # Fetch all parameters plus additional ones from user groups
        parameters = await Parameter.filter(owner_id__in=solution_groups).values(
            'parameter_id', 'parameter_set', 'engine', 'max_tokens', 'temperature', 'top_p', 'n',
            'stream', 'presence_penalty', 'frequency_penalty', 'username', 'owner_id', 'owner__name'
        )
        
        # print(f"Retrieved parameters: {parameters}")
        
        parameter_data = [{
            "id": param['parameter_id'],
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