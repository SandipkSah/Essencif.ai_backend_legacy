from tortoise import fields, models
from .user import User

class UserGroup(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    admin = fields.ForeignKeyField("models.User", related_name="user_group",source_field="admin")
    class Meta:
        table = "user_group"

