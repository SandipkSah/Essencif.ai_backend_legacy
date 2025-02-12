from tortoise import fields, models
from .user import User

class UserGroup(models.Model):
    user_group_id = fields.IntField(pk=True)
    group_name = fields.CharField(max_length=255, unique=True)
    admin = fields.ForeignKeyField("models.User", related_name="user_groups")
    class Meta:
        table = "user_groups"

