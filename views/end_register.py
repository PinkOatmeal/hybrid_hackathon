from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class EndRegisterView(BaseView):

    def handle(self, message: Message):
        bio = message.text
        user_id = message.chat.id
        UserController.fill_bio(user_id, bio)
        UserController.set_state(user_id, UserStateMachine.main_menu)

        self.bot.send_message(user_id,
                              "Вы успешно зарегистрированы")

        self.bot.send_message(user_id,
                              "Главное меню:",
                              reply_markup=MainKeyboard.build())
