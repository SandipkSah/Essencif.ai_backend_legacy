#!/bin/zsh

# Directory to store the models
MODEL_DIR="models"

# Create the directory if it doesn't exist
mkdir -p $MODEL_DIR

# Define an associative array with filenames and their corresponding content
declare -A files

files[user.py]='''from tortoise import fields, models

class User(models.Model):
    user_id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    given_name = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    company = fields.CharField(max_length=255, null=True)
    position = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"
'''

files[user_group.py]='''from tortoise import fields, models
from .user import User

class UserGroup(models.Model):
    user_group_id = fields.IntField(pk=True)
    group_name = fields.CharField(max_length=255, unique=True)
    admin = fields.ForeignKeyField("models.User", related_name="admin_groups")

    class Meta:
        table = "user_groups"
'''

files[user_rights.py]='''from tortoise import fields, models
from .user import User
from .user_group import UserGroup

class UserRights(models.Model):
    user = fields.ForeignKeyField("models.User", related_name="rights")
    user_group_name = fields.ForeignKeyField("models.UserGroup", related_name="user_rights")
    admin_role = fields.BooleanField()
    member_role = fields.BooleanField()

    class Meta:
        table = "user_rights"
'''

files[implementation.py]='''from tortoise import fields, models
from .user_group import UserGroup

class Implementation(models.Model):
    implementation_id = fields.IntField(pk=True)
    implementation = fields.CharField(max_length=255, unique=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="implementations")
    colour_1 = fields.CharField(max_length=50)
    colour_2 = fields.CharField(max_length=50)
    colour_3 = fields.CharField(max_length=50)
    colour_4 = fields.CharField(max_length=50)
    colour_5 = fields.CharField(max_length=50)
    colour_6 = fields.CharField(max_length=50)
    colour_7 = fields.CharField(max_length=50)

    class Meta:
        table = "implementations"
'''

files[document.py]='''from tortoise import fields, models
from .user_group import UserGroup

class Document(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", related_name="documents")
    filename = fields.CharField(max_length=500, pk=True)
    file = fields.CharField(max_length=1000)

    class Meta:
        table = "documents"
'''

files[context.py]='''from tortoise import fields, models
from .user_group import UserGroup

class Context(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", related_name="contexts")
    context_name = fields.CharField(max_length=255, pk=True)
    context = fields.TextField()

    class Meta:
        table = "context"
'''

files[prompt.py]='''from tortoise import fields, models
from .user_group import UserGroup

class Prompt(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", related_name="prompts")
    prompt_name = fields.CharField(max_length=255, pk=True)
    prompt = fields.TextField()

    class Meta:
        table = "prompt"
'''

files[parameter.py]='''from tortoise import fields, models
from .user_group import UserGroup

class Parameter(models.Model):
    owner = fields.ForeignKeyField("models.UserGroup", related_name="parameters")
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
'''

files[result.py]='''from tortoise import fields, models
from .document import Document
from .context import Context
from .prompt import Prompt
from .parameter import Parameter
from .user_group import UserGroup

class Result(models.Model):
    id_llm = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.UserGroup", related_name="results")
    filename = fields.ForeignKeyField("models.Document", related_name="results")
    context_name = fields.ForeignKeyField("models.Context", related_name="results")
    prompt_name = fields.ForeignKeyField("models.Prompt", related_name="results")
    parameter_set = fields.ForeignKeyField("models.Parameter", related_name="results")
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
'''

files[dim_fact.py]='''from tortoise import fields, models

class DimFact(models.Model):
    factor_id = fields.IntField(pk=True)
    factor_name = fields.CharField(max_length=255)
    source = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "dim_facts"
'''

files[dim_object.py]='''from tortoise import fields, models

class DimObject(models.Model):
    object_id = fields.IntField(pk=True)

    class Meta:
        table = "dim_objects"
'''

files[fact.py]='''from tortoise import fields, models
from .dim_object import DimObject
from .dim_fact import DimFact

class Fact(models.Model):
    object_id = fields.ForeignKeyField("models.DimObject", related_name="facts")
    factor_id = fields.ForeignKeyField("models.DimFact", related_name="facts")
    date = fields.DateField()
    value = fields.FloatField()

    class Meta:
        table = "facts"
'''

# Iterate over files and create them
for file in "${(@k)files}"; do
    echo "Creating $MODEL_DIR/$file..."
    echo "${files[$file]}" > "$MODEL_DIR/$file"
done

echo "All model files have been created in $MODEL_DIR!"
