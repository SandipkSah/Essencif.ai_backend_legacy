from tortoise import fields, models
from .user import User
from .user_group import UserGroup

class UserRights(models.Model):
    user = fields.ForeignKeyField("models.User", related_name="user_rights")
    user_group_name = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="user_rights") 
    admin_role = fields.BooleanField()
    member_role = fields.BooleanField()

    class Meta:
        table = "user_rights"

