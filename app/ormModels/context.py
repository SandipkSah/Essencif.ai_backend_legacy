from tortoise import fields, models
from .user_group import UserGroup

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.UserGroup", related_name="context")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"
