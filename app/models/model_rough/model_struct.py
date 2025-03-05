
class ApplicationAdmins(Model):
    '''
    People who should be administrator
    '''
    class Meta:
        table = "application_admin"
    
    user_id = fields.CharField(max_length=255, primary_key=True)

    def __repr__(self):
        return f"<ApplicationAdmins(user_id={self.user_id})>"
    
    

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="context")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"
from tortoise import fields, models

class DimFact(models.Model):
    factor_id = fields.IntField(pk=True)
    factor_name = fields.CharField(max_length=255)
    source = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "dim_fact"

from tortoise import fields, models

class DimObject(models.Model):
    object_id = fields.IntField(pk=True)

    class Meta:
        table = "dim_object"

from tortoise import fields, models
from .solution_group import SolutionGroup

class Document(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="document")
    filename = fields.CharField(max_length=500, unique=True)
    file = fields.CharField(max_length=1000)
    level = fields.CharField(max_length=255)

    class Meta:
        table = "documents"
from tortoise import fields, models

class Fact(models.Model):
    object_id = fields.IntField()
    factor_id = fields.IntField()
    date = fields.DateField()
    value = fields.FloatField()

    class Meta:
        table = "fact"

from tortoise import fields, models
from .solution_group import SolutionGroup

class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="implementation")
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementation"

from tortoise import fields, models
from .solution_group import SolutionGroup

class Parameter(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="parameter")
    parameter_set = fields.CharField(max_length=500)
    engine = fields.CharField(max_length=50)
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    username = fields.CharField(max_length=255)
    level = fields.CharField(max_length=255)

    class Meta:
        table = "parameter"from tortoise import fields
from tortoise.models import Model

class UserPoints(Model):
    '''
    The status points of a user
    '''
    class Meta:
        table = "user_points"
    
    user_id = fields.CharField(max_length=255, primary_key=True)
    points = fields.IntField()

    def __repr__(self):
        return f"<UserPoints(user_id={self.user_id}, points={self.points})>"
from tortoise import fields, models
from .solution_group import SolutionGroup

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="prompt")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"from tortoise import fields
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

from tortoise import fields, models
from .document import Document
from .context import Context
from .prompt import Prompt
from .parameter import Parameter
from .solution_group import SolutionGroup

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner_id = fields.ForeignKeyField("models.SolutionGroup", related_name="result")
    document_id = fields.ForeignKeyField("models.Document", related_name="result")
    context_id = fields.ForeignKeyField("models.Context", related_name="result")
    prompt_id = fields.ForeignKeyField("models.Prompt", related_name="result")
    parameter_id = fields.ForeignKeyField("models.Parameter", related_name="result")
    file = fields.CharField(max_length=1000)
    engine = fields.CharField(max_length=50)
    context = fields.TextField()
    prompt = fields.TextField()
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    result = fields.TextField()

    class Meta:
        table = "results"

from tortoise import fields, models

class User(models.Model):
    user_id = fields.CharField(max_length=255, pk=True)
    email = fields.CharField(max_length=255, unique=True)
    given_name = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    company = fields.CharField(max_length=255, null=True)
    position = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

from tortoise import fields, models
from .user import User

class SolutionGroup(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    admin = fields.ForeignKeyField("models.User", related_name="solution_group")
    class Meta:
        table = "solution_group"

from tortoise import fields
from tortoise.models import Model

class UserQuestion(Model):
    '''
    Model used to save the questions a user asked via the query
    Saves the question and response 
    '''
    class Meta:
        table = "user_questions"
        ordering = ["-created_at"]  
    
    id = fields.IntField(pk=True) 
    user_id = fields.CharField(max_length=255)
    question = fields.TextField()  
    response = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
from tortoise import fields, models
from .user import User
from .solution_group import SolutionGroup

class userRoles(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_roles")
    solution_group = fields.ForeignKeyField("models.SolutionGroup", related_name="user_roles") 
    role = fields.CharField(max_length=255)
    

    class Meta:
        table = "user_roles"

