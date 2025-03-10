from quart import Blueprint, request, jsonify
from app.models.user_role import userRole
from app.models.applicationAdmins import ApplicationAdmins  # Import ApplicationAdmins model
from app.models.solution_group import SolutionGroup  # Import SolutionGroup model

rights_blueprint = Blueprint('rights', __name__)

EssencifAI_ID = 1

@rights_blueprint.route('/api/rights', methods=['GET'])
async def get_user_roles():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "userID is required"}), 400

    # Check if the user is a global admin
    is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()

    if is_admin:
        # Provide access to all projects with the role of admin
        solution_groups = await SolutionGroup.all()
        rights_data = [{"project": ug.name, "role": "admin", "project_id": ug.solution_group_id} for ug in solution_groups]
        return jsonify(rights_data), 200

    user_roles = []
    solution_groups = []  # Initialize solution_groups with the default group

    if user_id:
        db_user_roles = await userRole.filter(user_id=user_id).prefetch_related('solution_group')
        if db_user_roles:
            solution_groups += [ur.solution_group.id for ur in db_user_roles]
            user_roles = [{"project": ur.solution_group.name, "role": ur.role, "project_id": ur.solution_group.solution_group_id} for ur in db_user_roles]

        # Check if there is a user right for "Essencif.AI"
        if not any(right["project"] == "Essencif.AI" for right in user_roles):
            user_roles.append({"project": "Essencif.AI", "role": "member", "project_id": EssencifAI_ID})
    
    return jsonify(user_roles), 200