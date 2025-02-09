from tortoise import fields, models

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.CharField(max_length=255)
    promptname = fields.CharField(max_length=255)
    prompt = fields.TextField()

    class Meta:
        table = "prompts"