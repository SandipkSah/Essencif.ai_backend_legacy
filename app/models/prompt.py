from tortoise import fields, models
from .solution_group import SolutionGroup

class Prompt(models.Model):
    prompt_id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="prompt", source_field="owner")
    prompt_name = fields.CharField(max_length=255)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"