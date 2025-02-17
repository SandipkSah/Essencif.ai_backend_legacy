from tortoise import fields, models
from .user_group import UserGroup

class Document(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.UserGroup", related_name="document")
    filename = fields.CharField(max_length=500, unique=True)
    file = fields.CharField(max_length=1000)
    level = fields.CharField(max_length=255)

    class Meta:
        table = "documents"
