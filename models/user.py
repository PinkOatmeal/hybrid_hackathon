from peewee import CharField, TextField, IntegerField

from models.base_model import BaseModel


class User(BaseModel):
    name: str = CharField()
    bio: str = TextField()
    state: int = IntegerField()
    status: int = IntegerField()
