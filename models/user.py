from peewee import CharField, TextField, IntegerField, BooleanField

from models.base_model import BaseModel


class User(BaseModel):
    name: str = CharField(null=True)
    bio: str = TextField(null=True)
    state: int = IntegerField(default=0)
    status: int = IntegerField(default=0)
    is_registered: bool = BooleanField(default=False)
