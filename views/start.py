from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.start import StartKeyboard
from views.base import BaseView


class StartView(BaseView):
    keyboard = StartKeyboard

    def handle(self, message: Message):
        UserController.create_initial(message.chat.id)

        self.bot.send_message(message.chat.id,
                              "Привет, я бот Random Coffee.",
                              reply_markup=self.keyboard.build())
