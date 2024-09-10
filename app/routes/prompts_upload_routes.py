from flask import Blueprint, request, jsonify
import base64
import io
import pandas as pd
from openpyxl import load_workbook

prompt_upload_blueprint = Blueprint('prompts_upload', __name__)

@prompt_upload_blueprint.route('/api/prompts_upload', methods=['POST'])
def prompts_upload():
    # Assuming JSON data is sent with a base64-encoded Excel file
    data = request.get_json()

    if not data or 'excel_file' not in data:
        return jsonify({"error": "Invalid JSON data or no file provided"}), 400

    try:
        # Decode the base64-encoded file content
        file_content = base64.b64decode(data['excel_file'])
        input_file = io.BytesIO(file_content)

        # Read the existing workbook
        existing_wb = load_workbook('Chat GPT.xlsx')
        
        # List of sheets to update
        sheets_to_update = ['Context', 'Parameter', 'Prompts']

        # Dictionary to store updated dataframes
        updated_dfs = {}

        for sheet in sheets_to_update:
            try:
                # Read the uploaded Excel file (from input_file) for each sheet
                input_df = pd.read_excel(input_file, sheet_name=sheet, engine='openpyxl')
                print(input_df, f"This is the uploaded '{sheet}' data")

                # Load the existing sheet into a DataFrame
                if sheet in existing_wb.sheetnames:
                    existing_df = pd.read_excel('Chat GPT.xlsx', sheet_name=sheet, engine='openpyxl')
                    print(existing_df, f"This is the existing '{sheet}' data")
                else:
                    existing_df = pd.DataFrame()  # Create an empty DataFrame if the sheet does not exist

                # Append the new rows from the uploaded file to the existing dataframe
                updated_df = pd.concat([existing_df, input_df], ignore_index=True)
                updated_dfs[sheet] = updated_df

            except ValueError:
                # If the sheet does not exist in the uploaded file, skip it
                print(f"No data for '{sheet}' in the uploaded file")
                continue

        # Write the updated dataframes to the existing workbook
        with pd.ExcelWriter('Chat GPT.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            for sheet, df in updated_dfs.items():
                df.to_excel(writer, sheet_name=sheet, index=False)

        return jsonify({"message": "Files processed and data merged successfully"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
