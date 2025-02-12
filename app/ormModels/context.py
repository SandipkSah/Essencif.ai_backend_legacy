from tortoise import fields, models
from .user_group import UserGroup

class Context(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="contexts")   
    context_name = fields.CharField(max_length=255, pk=True)
    context = fields.TextField()

    class Meta:
        table = "context"

