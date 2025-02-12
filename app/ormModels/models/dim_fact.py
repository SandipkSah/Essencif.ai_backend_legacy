from tortoise import fields, models

class DimFact(models.Model):
    factor_id = fields.IntField(pk=True)
    factor_name = fields.CharField(max_length=255)
    source = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "dim_facts"

