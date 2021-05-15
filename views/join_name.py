from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class JoinNameView(BaseView):

    def handle(self, message: Message):
        UserController.set_state(message.chat.id, UserStateMachine.enter_name)
        self.bot.send_message(message.chat.id,
                              "Введите своё имя.")
