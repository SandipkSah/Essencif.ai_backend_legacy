from tortoise import fields, models
from .user_group import UserGroup

class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="implementations")
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementations"

