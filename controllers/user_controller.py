from models.user import User


class UserController:

    @staticmethod
    def create_initial(_id: int) -> User:
        return User.get_or_create(id=_id)

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
        user.save()
        user.is_registered = True
        return user

    @staticmethod
    def set_state(_id: int, state: int) -> User:
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
