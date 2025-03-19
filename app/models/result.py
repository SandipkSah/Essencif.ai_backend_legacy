from tortoise import fields, models
from .document import Document
from .context import Context
from .prompt import Prompt
from .parameter import Parameter
from .solution_group import SolutionGroup

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", related_name="result", source_field="owner")
    document_id = fields.ForeignKeyField("models.Document", related_name="result", source_field="document_id")
    context_id = fields.ForeignKeyField("models.Context", related_name="result",source_field="context_id")
    prompt_id = fields.ForeignKeyField("models.Prompt", related_name="result", source_field="prompt_id")
    parameter_id = fields.ForeignKeyField("models.Parameter", related_name="result", source_field="parameter_id")
    # file = fields.CharField(max_length=1000)
    # engine = fields.CharField(max_length=50)
    # context = fields.TextField()
    # prompt = fields.TextField()
    # max_tokens = fields.IntField()
    # temperature = fields.FloatField()
    # top_p = fields.FloatField()
    # n = fields.IntField()
    # stream = fields.BooleanField()
    # presence_penalty = fields.FloatField()
    # frequency_penalty = fields.FloatField()
    result = fields.TextField()
    # filename = fields.CharField(max_length=255)


    class Meta:
        table = "result"

