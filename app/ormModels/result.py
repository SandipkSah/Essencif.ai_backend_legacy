from tortoise import fields, models
from .document import Document
from .context import Context
from .prompt import Prompt
from .parameter import Parameter
from .user_group import UserGroup

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.UserGroup", related_name="result")
    document_id = fields.ForeignKeyField("models.Document", related_name="result")
    context_id = fields.ForeignKeyField("models.Context", related_name="result")
    prompt_id = fields.ForeignKeyField("models.Prompt", related_name="result")
    parameter_id = fields.ForeignKeyField("models.Parameter", related_name="result")
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
        table = "result"

