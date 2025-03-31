from tortoise import fields, models
from .user import User
from .solution_group import SolutionGroup

class userRole(models.Model):
    user_role_id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_roles", source_field="user", on_delete=fields.NO_ACTION)
    solution_group = fields.ForeignKeyField("models.SolutionGroup", related_name="user_roles", source_field="solution_group") 
    role = fields.CharField(max_length=255)
    

    class Meta:
        table = "user_role"

