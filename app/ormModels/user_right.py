from tortoise import fields, models
from .user import User
from .user_group import UserGroup

class UserRights(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_rights", source_field="user")
    user_group = fields.ForeignKeyField("models.UserGroup", related_name="user_rights", source_field="user_group") 
    role = fields.CharField(max_length=255)
    

    class Meta:
        table = "user_right"

