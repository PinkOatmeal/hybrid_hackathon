
from typing import Optional

from peewee import fn
from models.meeting import Meeting
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


    def get_info(_id: int) -> str:
        user = User.get(User.id == _id)

        meetings_as_initiator = Meeting.select().where(user.id == Meeting.initiator_id)
        ratings_as_initiator = []
        for meeting in meetings_as_initiator:
            ratings_as_initiator.append(meeting.companion_rate)
        try:
            rating_as_initiator = round(sum(ratings_as_initiator) / len(ratings_as_initiator), 0)
        except ZeroDivisionError:
            rating_as_initiator = 0

        meetings_as_companion = Meeting.select().where(user.id == Meeting.companion_id)
        ratings_as_companion = []
        for meeting in meetings_as_companion:
            ratings_as_companion.append(meeting.initiator_rate)
        try:
            rating_as_companion = round(sum(ratings_as_companion) / len(ratings_as_companion), 0)
        except ZeroDivisionError:
            rating_as_companion = 0

        if rating_as_initiator == 0:
            rating = rating_as_companion
        elif rating_as_companion == 0:
            rating = rating_as_initiator
        else:
            rating = (rating_as_initiator + rating_as_companion) / 2

        rating_str = "⭐" * int(rating)

        return f"Имя: \n{user.name}\n\nО себе: \n{user.bio}\n\nРейтинг: \n{rating_str if rating_str != '' else 'нет рейтинга'}"
