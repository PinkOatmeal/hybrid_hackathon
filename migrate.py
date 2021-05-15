from models.base_model import database
from models.meeting import Meeting
from models.user import User
from models.companion_history import CompanionHistory

list_model: list = [User, Meeting, CompanionHistory]


def migrate():
    database.connect()
    database.drop_tables(list_model, cascade=True)
    database.create_tables(list_model)
    database.close()


if __name__ == '__main__':
    migrate()
    print("ok")
