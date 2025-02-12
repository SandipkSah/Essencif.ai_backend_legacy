from tortoise import fields, models
from .user_group import UserGroup

class Parameter(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="parameters")
    parameter_set = fields.CharField(max_length=500, pk=True)
    engine = fields.CharField(max_length=50)
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    username = fields.CharField(max_length=255)

    class Meta:
        table = "parameter"

