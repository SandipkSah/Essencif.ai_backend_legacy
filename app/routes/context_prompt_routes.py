from quart import Blueprint, jsonify
from app.ormModels.context import Context
from app.ormModels.prompt import Prompt
from app.ormModels.parameter import Parameter

import pandas as pd
import os

context_prompt_blueprint = Blueprint('context_prompt', __name__)
# Read prompts from Excel
# current_env = os.getenv('CURRENT_QUART_ENV', "development")
# if (current_env == 'development'):
#     excel_file = 'Chat GPT.xlsx'
# else:
#     # for now it is this way, but it needs to be changed
#     #  depending on the location excel database file
#     excel_file = '/home/data/Chat GPT.xlsx'




@context_prompt_blueprint.route('/api/contexts', methods=['GET'])
async def get_contexts():
    """Retrieves context information from the database."""
    try:
        # Prefetch the related UserGroup data
        contexts = await Context.all().prefetch_related('owner')
        
        context_data = [{
            "id": context.id,
            "owner": context.owner.id,  # Or any other UserGroup fields you need
            "contextname": context.name,
            "context": context.detailed_definition
        } for context in contexts]

        return jsonify({"contexts": context_data})

    except Exception as e:
        print(f"Error occurred while retrieving contexts: {str(e)}")
        return jsonify({"error": f"Failed to get contexts.{str(e)}"}), 500
    
    # @context_prompt_blueprint.route('/api/contexts', methods=['GET'])
    # def get_contexts():
    #     """Retrieves context information from an Excel file."""
    #     try:
    #         df_context = pd.read_excel(excel_file, sheet_name="Context")

    #         # Convert DataFrame to JSON
    #         context_data = df_context.to_json(orient='records')

    #         return jsonify({"contexts": context_data})

    #     except Exception as e:
    #         print(f"Error occurred while retrieving contexts: {str(e)}")
    #         return jsonify({"error": f"Failed to get contexts.{str(e)}"}), 500



# @context_prompt_blueprint.route('/api/prompts', methods=['GET'])
# async def get_prompts():
#     """Retrieves prompt information from the database."""
#     try:
#         prompts = await Prompt.filter(owner='1')
#         prompt_data = [{"id": prompt.id, "owner": prompt.owner, "promptname": prompt.name, "prompt": prompt.detailed_definition} for prompt in prompts]

#         return jsonify({"prompts": prompt_data})

#     except Exception as e:
#         print(f"Error occurred while retrieving prompts: {str(e)}")
#         return jsonify({"error": f"Failed to get prompts.{str(e)}"}), 500

@context_prompt_blueprint.route('/api/prompts', methods=['GET'])
async def get_prompts():
    """Retrieves prompt information from the database."""
    try:
        # Prefetch the related owner data
        prompts = await Prompt.filter(owner__id='1').prefetch_related('owner')
        
        prompt_data = [{
            "id": prompt.id,
            "owner": prompt.owner.id,
            "promptname": prompt.name,
            "prompt": prompt.detailed_definition
        } for prompt in prompts]

        return jsonify({"prompts": prompt_data})

    except Exception as e:
        print(f"Error occurred while retrieving prompts: {str(e)}")
        return jsonify({"error": f"Failed to get prompts.{str(e)}"}), 500


# @context_prompt_blueprint.route('/api/parameters', methods=['GET'])
# async def get_parameters():
#     """Retrieves parameter information from the database."""
#     try:
#         parameters = await Parameter.filter(owner='Default')
#         parameter_data = [{"id": parameter.id, "owner": parameter.owner, "parameterset": parameter.parameter_set, "engine": parameter.engine, "max_tokens": parameter.max_tokens, "temperature": parameter.temperature, "top_p": parameter.top_p, "n": parameter.n, "stream": parameter.stream, "presence_penalty": parameter.presence_penalty, "frequency_penalty": parameter.frequency_penalty, "user": parameter.username} for parameter in parameters]

#         return jsonify({"parameters": parameter_data})

#     except Exception as e:
#         print(f"Error occurred while retrieving parameters: {str(e)}")
#         return jsonify({"error": f"Failed to get parameters.{str(e)}"}), 500
    
# @context_prompt_blueprint.route('/api/parameters', methods=['GET'])
# async def get_parameters():
#     """Retrieves parameter information from the database."""
#     try:
#         parameters = await Parameter.filter(owner='2').values(
#             'id',
#             'parameter_set',
#             'engine',
#             'max_tokens',
#             'temperature',
#             'top_p',
#             'n',
#             'stream',
#             'presence_penalty',
#             'frequency_penalty',
#             'username',
#             'owner'  # This is the UserGroup id
#         )
        
#         parameter_data = [{
#             "id": param['id'],
#             "owner": param['owner__id'],  # or param['owner__name']
#             "parameterset": param['parameter_set'],
#             "engine": param['engine'],
#             "max_tokens": param['max_tokens'],
#             "temperature": param['temperature'],
#             "top_p": param['top_p'],
#             "n": param['n'],
#             "stream": param['stream'],
#             "presence_penalty": param['presence_penalty'],
#             "frequency_penalty": param['frequency_penalty'],
#             "user": param['username']
#         } for param in parameters]

#         return jsonify({"parameters": parameter_data})

#     except Exception as e:
#         print(f"Error occurred while retrieving parameters: {str(e)}")
#         return jsonify({"error": f"Failed to get parameters.{str(e)}"}), 500

@context_prompt_blueprint.route('/api/parameters', methods=['GET'])
async def get_parameters():
    """Retrieves parameter information from the database."""
    try:
        parameters = await Parameter.filter(owner__id='2').values(
            'id',
            'parameter_set',
            'engine',
            'max_tokens',
            'temperature',
            'top_p',
            'n',
            'stream',
            'presence_penalty',
            'frequency_penalty',
            'username',
            'owner_id',
            'owner__name'  # Added to get the UserGroup name
        )
        
        parameter_data = [{
            "id": param['id'],
            "owner": param['owner_id'],
            "owner_name": param['owner__name'],  # Added owner name to response
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
        return jsonify({"error": f"Failed to get parameters.{str(e)}"}), 500