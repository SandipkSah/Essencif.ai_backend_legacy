from tortoise import fields, models
from .solution_group import SolutionGroup

class Parameter(models.Model):
    parameter_id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="parameter", source_field="owner", on_delete=fields.NO_ACTION)
    parameter_set = fields.CharField(max_length=500)
    engine = fields.CharField(max_length=50)
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    username = fields.CharField(max_length=255)
    level = fields.CharField(max_length=255)

    class Meta:
        table = "parameter"