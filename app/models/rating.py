from tortoise import fields
from tortoise.models import Model

class Rating(Model):
    '''
    This is the rating a user gives to a document in qdrant
    '''
    class Meta:
        table = "rating"
        unique_together = (("user_id", "link_id"),)
    
    user_id = fields.CharField(max_length=255)
    link_id = fields.CharField(max_length=255) 
    rating = fields.FloatField()

    def __repr__(self):
        return f"<Rating(user_id={self.user_id}, link_id={self.link_id}, rating={self.rating})>"

