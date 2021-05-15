from telebot.types import Message

from controllers.user_controller import UserController
from utils.enums import UserStateMachine


def filter_by_state(message: Message):
    return UserController.check_state(message.chat.id, [UserStateMachine.main_menu])


def filter_by_state_in_finded(message: Message):
    return UserController.check_state(message.chat.id, [UserStateMachine.find_meeting])
