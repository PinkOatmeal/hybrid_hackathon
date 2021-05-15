from peewee import ForeignKeyField

from models.base_model import BaseModel
from models.user import User


class CompanionHistory(BaseModel):
    initiator_id: int = ForeignKeyField(User, backref="companions")
    companion_id: int = ForeignKeyField(User, backref="companion_of")
