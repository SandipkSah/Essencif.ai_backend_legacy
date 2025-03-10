from tortoise import fields
from tortoise.models import Model
from tortoise.exceptions import IntegrityError
from quart import current_app

class ApplicationAdmins(Model):
    '''
    People who should be administrator
    '''
    class Meta:
        table = "application_admin"
    
    user_id = fields.CharField(max_length=255, primary_key=True)

    def __repr__(self):
        return f"<ApplicationAdmins(user_id={self.user_id})>"
    
    