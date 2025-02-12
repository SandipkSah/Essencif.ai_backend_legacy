from tortoise import fields, models

class Fact(models.Model):
    object_id = fields.IntField()
    factor_id = fields.IntField()
    date = fields.DateField()
    value = fields.FloatField()

    class Meta:
        table = "facts"

