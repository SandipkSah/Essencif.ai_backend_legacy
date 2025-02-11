from tortoise import fields, models

class Parameter(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.CharField(max_length=255)
    parameterset = fields.TextField()
    engine = fields.CharField(max_length=255, null=True)
    max_tokens = fields.IntField(null=True)
    temperature = fields.FloatField(null=True)
    top_p = fields.FloatField(null=True)
    n = fields.IntField(null=True)
    stream = fields.BooleanField(null=True)
    presence_penalty = fields.FloatField(null=True)
    frequency_penalty = fields.FloatField(null=True)
    user = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "parameter"