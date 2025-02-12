from tortoise import fields, models
from .document import Document
from .context import Context
from .prompt import Prompt
from .parameter import Parameter
from .user_group import UserGroup

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="results")
    filename = fields.ForeignKeyField("models.Document", to_field="filename", related_name="results")
    context_name = fields.ForeignKeyField("models.Context", to_field="context_name", related_name="results")
    prompt_name = fields.ForeignKeyField("models.Prompt", to_field="prompt_name", related_name="results")
    parameter_set = fields.ForeignKeyField("models.Parameter", to_field="parameter_set", related_name="results")
    file = fields.CharField(max_length=1000)
    engine = fields.CharField(max_length=50)
    context = fields.TextField()
    prompt = fields.TextField()
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    result = fields.TextField()

    class Meta:
        table = "results"

