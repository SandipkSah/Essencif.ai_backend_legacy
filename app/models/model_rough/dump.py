from tortoise import fields, models
from .solution_group import SolutionGroup

class Context(models.Model):
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="contexts")
    context_name = fields.CharField(max_length=255, pk=True)
    context = fields.TextField()

    class Meta:
        table = "context"

class Document(models.Model):
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="documents")
    filename = fields.CharField(max_length=500, pk=True)
    file = fields.CharField(max_length=1000)

    class Meta:
        table = "documents"

class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="implementations")
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementations"

class Parameter(models.Model):
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="parameters")
    parameter_set = fields.CharField(max_length=500, pk=True)
    engine = fields.CharField(max_length=50)
    max_tokens = fields.IntField()
    temperature = fields.FloatField()
    top_p = fields.FloatField()
    n = fields.IntField()
    stream = fields.BooleanField()
    presence_penalty = fields.FloatField()
    frequency_penalty = fields.FloatField()
    username = fields.CharField(max_length=255)

    class Meta:
        table = "parameter"

class Prompt(models.Model):
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="prompts")
    prompt_name = fields.CharField(max_length=255, pk=True)
    prompt = fields.TextField()

    class Meta:
        table = "prompt"

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="results")
    filename = fields.ForeignKeyField("models.Document", to_field="filename", related_name="results")
    context_name = fields.ForeignKeyField("models.Context", to_field="context_name", related_name="results")
    prompt_name = fields.ForeignKeyField("models.Prompt", to_field="prompt_name", related_name="results")
    parameter_set = fields.ForeignKeyField("models.Parameter", to_field="parameter_set", related_name="results")
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

class SolutionGroup(models.Model):
    solution_group_id = fields.IntField(pk=True)
    group_name = fields.CharField(max_length=255, unique=True)
    admin = fields.ForeignKeyField("models.User", related_name="solution_groups")

    class Meta:
        table = "solution_groups"

class userRoles(models.Model):
    user = fields.ForeignKeyField("models.User", related_name="user_roles")
    solution_group_name = fields.ForeignKeyField("models.SolutionGroup", to_field="group_name", related_name="user_roles") 
    admin_role = fields.BooleanField()
    member_role = fields.BooleanField()

    class Meta:
        table = "user_roles"

class User(models.Model):
    user_id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    given_name = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    company = fields.CharField(max_length=255, null=True)
    position = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

class UserPoints(models.Model):
    user_id = fields.CharField(max_length=255, primary_key=True)
    points = fields.IntField()

    class Meta:
        table = "user_points"

    def __repr__(self):
        return f"<UserPoints(user_id={self.user_id}, points={self.points})>"

class UserQuestion(models.Model):
    id = fields.IntField(pk=True) 
    user_id = fields.CharField(max_length=255)
    question = fields.TextField()  
    response = fields.JSONField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_questions"
        ordering = ["-created_at"]
