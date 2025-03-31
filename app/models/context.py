from tortoise import fields, models
from .solution_group import SolutionGroup

class Context(models.Model):
    context_id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="context", source_field="owner", on_delete=fields.NO_ACTION)
    context_name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "context"
