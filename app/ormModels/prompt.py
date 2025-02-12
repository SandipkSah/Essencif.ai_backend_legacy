from tortoise import fields, models
from .user_group import UserGroup

class Prompt(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", to_field="group_name", related_name="prompts")
    prompt_name = fields.CharField(max_length=255, pk=True)
    prompt = fields.TextField()

    class Meta:
        table = "prompt"

