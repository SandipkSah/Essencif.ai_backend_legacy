from tortoise import fields, models
from tortoise.models import Model
from .document import Document

class UserQuestion(Model):
    '''
    Model used to save the questions a user asked via the query
    Saves the question and response 
    '''
    class Meta:
        table = "user_question"
        ordering = ["-created_at"]  
    
    user_question_id = fields.IntField(pk=True) 
    user_id = fields.CharField(max_length=255)
    # document_id = fields.ForeignKeyField("models.Document", related_name="user_question_history", source_field="document_id")
    question = fields.TextField()  
    response = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    

