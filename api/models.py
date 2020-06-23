from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, TextField
from api.settings_secret import DATABASES_NAME

db = SqliteDatabase(DATABASES_NAME)

class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Note(BaseModel):

    user = ForeignKeyField(User)
    text = TextField()
