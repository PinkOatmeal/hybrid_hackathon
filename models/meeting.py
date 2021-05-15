import datetime

from peewee import IntegerField, TextField, DateTimeField, ForeignKeyField

from models.base_model import BaseModel
from models.user import User


class Meeting(BaseModel):
    user_id_1: int = ForeignKeyField(User)
    user_id_2: int = ForeignKeyField(User)
    rating_1: int = IntegerField()
    rating_2: int = IntegerField()
    feedback_1: str = TextField()
    feedback_2: str = TextField()
    meeting_time: datetime.datetime = DateTimeField()
    status: int = IntegerField()
