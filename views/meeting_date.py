from telebot.types import Message

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class MeetingDateView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        UserController.set_state(message.chat.id, UserStateMachine.meeting_date)
        self.bot.send_message(user_id,
                              "Укажите дату для встречи.\n\n"
                              "Например, 10:00 22.05.2021")
