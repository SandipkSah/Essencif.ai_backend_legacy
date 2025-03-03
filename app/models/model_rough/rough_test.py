
class ApplicationAdmins(Model):
    '''
    People who should be administrator
    '''
    class Meta:
        table = "application_admin"
    
    user_id = fields.CharField(max_length=255, primary_key=True)


class Context(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="context")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "context"

class DimFact(models.Model):
    factor_id = fields.IntField(pk=True)
    factor_name = fields.CharField(max_length=255)
    source = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "dim_fact"


class DimObject(models.Model):
    object_id = fields.IntField(pk=True)

    class Meta:
        table = "dim_object"


class Document(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="document")
    filename = fields.CharField(max_length=500, unique=True)
    file = fields.CharField(max_length=1000)
    level = fields.CharField(max_length=255)

    class Meta:
        table = "document"

class Fact(models.Model):
    object_id = fields.IntField()
    factor_id = fields.IntField()
    date = fields.DateField()
    value = fields.FloatField()

    class Meta:
        table = "fact"


class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="implementation")
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementation"


class Parameter(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="parameter")
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
        table = "parameter"

class Prompt(models.Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="prompt")
    name = fields.CharField(max_length=255, unique=True)
    detailed_definition = fields.TextField()
    level = fields.CharField(max_length=255)

    class Meta:
        table = "prompt"

class Rating(Model):
    '''
    This is the rating a user gives to a document in qdrant
    '''
    class Meta:
        table = "rating"
        unique_together = (("user_id", "qdrant_id"),)
    
    user_id = fields.CharField(max_length=255)
    qdrant_id = fields.CharField(max_length=255) 
    rating = fields.FloatField()

    def __repr__(self):
        return f"<Rating(user_id={self.user_id}, qdrant_id={self.qdrant_id}, rating={self.rating})>"



class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="result")
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
        table = "result"


class User(models.Model):
    user_id = fields.CharField(max_length=255, pk=True)
    email = fields.CharField(max_length=255, unique=True)
    given_name = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    company = fields.CharField(max_length=255, null=True)
    position = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"


class UserGroup(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    admin = fields.ForeignKeyField("models.User", related_name="user_group")
    class Meta:
        table = "user_group"



class UserPoints(Model):
    '''
    The status points of a user
    '''
    class Meta:
        table = "user_point"
    
    user_id = fields.CharField(max_length=255, primary_key=True)
    points = fields.IntField()

 

class UserQuestion(Model):
    '''
    Model used to save the questions a user asked via the query
    Saves the question and response 
    '''
    class Meta:
        table = "user_question"
        ordering = ["-created_at"]  
    
    id = fields.IntField(pk=True) 
    user_id = fields.CharField(max_length=255)
    question = fields.TextField()  
    response = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

class UserRights(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_rights")
    user_group = fields.ForeignKeyField("models.UserGroup", related_name="user_rights") 
    role = fields.CharField(max_length=255)
    

    class Meta:
        table = "user_right"

