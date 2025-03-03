from tortoise import fields, models
from .user_group import UserGroup

class Context(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="context", source_field="owner")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "context"
