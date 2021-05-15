from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class JoinBioView(BaseView):

    def handle(self, message: Message):
        name = message.text
        user_id = message.chat.id
        UserController.fill_name(user_id, name)
        UserController.set_state(user_id, UserStateMachine.enter_bio)
        self.bot.send_message(user_id,
                              "Расскажите немного о себе.")
