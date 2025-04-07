from quart import Blueprint, request, jsonify
import base64
import io
import pandas as pd
from openpyxl import load_workbook
import os
from app.utils.uploadPrompts import insert_prompts, insert_contexts, insert_parameters

prompt_upload_blueprint = Blueprint('prompts_upload', __name__)


@prompt_upload_blueprint.route('/api/prompts_upload', methods=['POST'])
async def  prompts_upload():
    # Assuming JSON data is sent with a base64-encoded Excel file
    # data = request.get_json()
    data = await request.get_json()  #  Correct


    if not data or 'excel_file' not in data:
        return jsonify({"error": "Invalid JSON data or no file provided"}), 400

    try:
        # Decode the base64-encoded file content
        # owner = data['owner']
        file_content = base64.b64decode(data['excel_file'])
        replace_prompt = data.get('replace_prompt', False)
        input_file = io.BytesIO(file_content)

        # # Load the uploaded Excel file directly into a new workbook object
        # uploaded_wb = load_workbook(input_file)

       

        # # Extract the data from the uploaded workbook
        # prompts = pd.read_excel(uploaded_wb, sheet_name='Prompts')
        # contexts = pd.read_excel(uploaded_wb, sheet_name='Context')
        # parameters = pd.read_excel(uploaded_wb, sheet_name='Parameter')

        # Read Excel directly from BytesIO without openpyxl
        prompts = pd.read_excel(input_file, sheet_name='prompt').to_dict(orient='records')
        contexts = pd.read_excel(input_file, sheet_name='context').to_dict(orient='records')
        parameters = pd.read_excel(input_file, sheet_name='parameter').to_dict(orient='records')


        try:
            # Upload the prompts, contexts, and parameters to the database
            await insert_contexts(contexts, replace_prompt)
            await insert_prompts(prompts, replace_prompt)
            await insert_parameters(parameters, replace_prompt)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        return jsonify({"message": "Uploaded file replaced the existing file successfully"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
