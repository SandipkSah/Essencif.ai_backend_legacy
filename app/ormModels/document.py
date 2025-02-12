from tortoise import fields, models
from .user_group import UserGroup

class Document(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="documents")
    filename = fields.CharField(max_length=500, pk=True)
    file = fields.CharField(max_length=1000)

    class Meta:
        table = "documents"

