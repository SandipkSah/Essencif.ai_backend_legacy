from flask import Blueprint, jsonify
import pandas as pd

context_prompt_blueprint = Blueprint('context_prompt', __name__)

@context_prompt_blueprint.route('/api/contexts', methods=['GET'])
def get_contexts():
    """Retrieves context information from an Excel file."""

    try:
        # Read contexts from Excel
        excel_file = 'Chat GPT.xlsx'
        df_context = pd.read_excel(excel_file, sheet_name="Context")

        # Convert DataFrame to JSON
        context_data = df_context.to_json(orient='records')

        return jsonify({"contexts": context_data})

    except Exception as e:
        print(f"Error occurred while retrieving contexts: {str(e)}")
        return jsonify({"error": f"Failed to get contexts.{str(e)}"}), 500

@context_prompt_blueprint.route('/api/prompts', methods=['GET'])
def get_prompts():
    """Retrieves prompt information from an Excel file."""

    try:
        # Read prompts from Excel
        excel_file = 'Chat GPT.xlsx'
        df_prompt = pd.read_excel(excel_file, sheet_name="Prompts")
        df_prompt = df_prompt[df_prompt['Owner'] == 'Default']
        
        # Convert DataFrame to JSON
        prompt_data = df_prompt.to_json(orient='records')

        return jsonify({"prompts": prompt_data})

    except Exception as e:
        print(f"Error occurred while retrieving prompts: {str(e)}")
        return jsonify({"error": f"Failed to get prompts.{str(e)}"}), 500
