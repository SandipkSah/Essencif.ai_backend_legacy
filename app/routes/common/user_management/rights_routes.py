from quart import Blueprint, request, jsonify
from app.models.user_role import userRole
from app.models.applicationAdmins import ApplicationAdmins
from app.models.solution_group import SolutionGroup
from app.models.user import User  # Import User model
from tortoise.exceptions import DoesNotExist, IntegrityError, OperationalError

rights_blueprint = Blueprint('rights', __name__)

EssencifAI_ID = 1

@rights_blueprint.route('/api/rights', methods=['POST'])
async def get_user_roles():
    try:
        data = await request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        user_id = data.get("user_id")
        if not user_id:
            return jsonify({"error": "userID is required"}), 400

        email = data.get("email", f"test_{user_id}@example.com")
        given_name = data.get("given_name", "Test")
        surname = data.get("surname", "User")
        company = data.get("company", "TestCorp")
        position = data.get("position", "Tester")

        # Check if the user exists, if not create one with provided or test values
        user = await User.filter(user_id=user_id).first()
        if not user:
            user = await User.create(user_id=user_id, email=email, given_name=given_name, surname=surname, company=company, position=position)

        # Check if the user is a global admin
        is_admin = await ApplicationAdmins.filter(user_id=user_id).exists()
        if is_admin:
            solution_groups = await SolutionGroup.all()
            rights_data = [{"project": sg.name, "role": "admin", "project_id": sg.solution_group_id} for sg in solution_groups]
            return jsonify(rights_data), 200

        user_roles = []
        solution_groups = []

        db_user_roles = await userRole.filter(user_id=user_id).prefetch_related('solution_group')
        if db_user_roles:
            solution_groups += [ur.solution_group.id for ur in db_user_roles]
            user_roles = [{"project": ur.solution_group.name, "role": ur.role, "project_id": ur.solution_group.solution_group_id} for ur in db_user_roles]

        if not any(right["project"] == "Essencif.AI" for right in user_roles):
            user_roles.append({"project": "Essencif.AI", "role": "member", "project_id": EssencifAI_ID})

        return jsonify(user_roles), 200
    
    except IntegrityError:
        return jsonify({"error": "Database integrity error occurred"}), 500
    except OperationalError:
        return jsonify({"error": "Database operational error occurred"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
