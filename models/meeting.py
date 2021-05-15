import datetime

from peewee import IntegerField, TextField, DateTimeField, ForeignKeyField, BooleanField

from models.base_model import BaseModel
from models.user import User


class Meeting(BaseModel):
    initiator_id: User = ForeignKeyField(User)
    companion_id: User = ForeignKeyField(User)
    initiator_rate: int = IntegerField(null=True)
    companion_rate: int = IntegerField(null=True)
    initiator_feedback: str = TextField(null=True)
    companion_feedback: str = TextField(null=True)
    meeting_time: datetime.datetime = DateTimeField(null=True)
    status: int = IntegerField(default=0)
    is_ready: bool = BooleanField(default=False)
