from tortoise import fields, models
from .user import User

class SolutionGroup(models.Model):
    solution_group_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    admin = fields.ForeignKeyField("models.User", related_name="solution_group",source_field="admin")
    class Meta:
        table = "solution_group"

