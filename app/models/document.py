from tortoise import fields, models
from .solution_group import SolutionGroup

class Document(models.Model):
    document_id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="document", source_field="owner", on_delete=fields.NO_ACTION)
    filename = fields.CharField(max_length=500)
    file = fields.CharField(max_length=1000, Unique=True)
    level = fields.CharField(max_length=255)
    type = fields.CharField(max_length=255)

    class Meta:
        table = "document"
