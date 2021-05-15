from peewee import PostgresqlDatabase, Model

from config import POSTGRES_INFO

database: PostgresqlDatabase = PostgresqlDatabase(**POSTGRES_INFO)


class BaseModel(Model):
    class Meta:
        database = database
