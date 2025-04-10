from tortoise import fields, models

class Fact(models.Model):
    fact_id = fields.IntField(pk=True)
    object_id = fields.IntField()
    factor_id = fields.IntField()
    date = fields.DateField()
    value = fields.FloatField()

    class Meta:
        table = "fact"

