from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class MainView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        UserController.set_state(message.chat.id, UserStateMachine.main_menu)
        self.bot.send_message(user_id,
                              "Главное меню:",
                              reply_markup=MainKeyboard.build())