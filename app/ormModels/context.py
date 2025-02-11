from tortoise import fields, models

class Context(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.CharField(max_length=255)
    contextname = fields.CharField(max_length=255)
    context = fields.TextField()

    class Meta:
        table = "Context"