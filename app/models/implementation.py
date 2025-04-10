from tortoise import fields, models
from .solution_group import SolutionGroup

class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="implementation", source_field="owner", on_delete=fields.NO_ACTION)
    name = fields.CharField(max_length=255)
    route = fields.CharField(max_length=255)
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementation"

