from quart import Blueprint, request, jsonify
from app.ormModels.user_right import UserRight
from app.ormModels.applicationAdmins import ApplicationAdmins  # Import ApplicationAdmins model
from app.ormModels.user_group import UserGroup  # Import UserGroup model

rights_blueprint = Blueprint('rights', __name__)

EssencifAI_ID = 1

@rights_blueprint.route('/api/rights', methods=['GET'])
async def get_user_rights():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "userID is required"}), 400

    # Check if the user is a global admin
    is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()

    # Print the contents of the ApplicationAdmins table
    application_admins = await ApplicationAdmins.all()
    print(f"ApplicationAdmins table contents============================: {application_admins}")

    if is_admin:
        # Provide access to all projects with the role of admin
        user_groups = await UserGroup.all()
        print(user_groups, "why not all")
        rights_data = [{"project": ug.name, "role": "admin", "project_id": ug.id} for ug in user_groups]
        return jsonify(rights_data), 200

    user_rights = []
    user_groups = []  # Initialize user_groups with the default group

    if user_id:
        db_user_rights = await UserRight.filter(user_id=user_id).prefetch_related('user_group')
        if db_user_rights:
            user_groups += [ur.user_group.id for ur in db_user_rights]
            user_rights = [{"project": ur.user_group.name, "role": ur.role, "project_id": ur.user_group.id} for ur in db_user_rights]

        # Check if there is a user right for "Essencif.AI"
        if not any(right["project"] == "Essencif.AI" for right in user_rights):
            user_rights.append({"project": "Essencif.AI", "role": "member", "project_id": EssencifAI_ID})
    
    return jsonify(user_rights), 200