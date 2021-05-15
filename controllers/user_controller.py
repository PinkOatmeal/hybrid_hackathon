from typing import Optional

from peewee import fn

from models.user import User
from utils.enums import UserStateMachine, UserStatus


class UserController:

    @staticmethod
    def create_initial(_id: int) -> User:
        user = User.get_or_none(id=_id)
        if user is not None:
            user.delete_instance()
            return User.create(id=_id)
        return User.create(id=_id)

    @staticmethod
    def fill_name(_id: int, name: str) -> User:
        user: User = User.get(User.id == _id)
        user.name = name
        user.save()
        return user

    @staticmethod
    def fill_bio(_id: int, bio: str) -> User:
        user: User = User.get(User.id == _id)
        user.bio = bio
        user.is_registered = True
        user.save()
        return user

    @staticmethod
    def set_state(_id: int, state: UserStateMachine) -> User:
        user: User = User.get(User.id == _id)
        user.state = state
        user.save()
        return user

    @staticmethod
    def set_status(_id: int, state: int) -> User:
        user: User = User.get(User.id == _id)
        user.state = state
        user.save()
        return user

    @staticmethod
    def check_state(_id: int, state_list: list[UserStateMachine]):
        user: User = User.get(User.id == _id)
        current_state = UserStateMachine(user.state)
        return current_state in state_list

    @staticmethod
    def find_meeting(user_id: int) -> Optional[User]:
        query_set = User.select().where((User.id != user_id) & (User.status == UserStatus.free)).order_by(fn.Random()).limit(1)
        if query_set.exists():
            return query_set.get()
        return None

