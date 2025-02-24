from tortoise import fields, models
from .user_group import UserGroup

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="prompt", source_field="owner")
    name = fields.CharField(max_length=255)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"