from tortoise import fields, models

class DimObject(models.Model):
    object_id = fields.IntField(pk=True)

    class Meta:
        table = "dim_objects"

