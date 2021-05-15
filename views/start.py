from telebot.types import Message

from keyboards.start import StartKeyboard
from views.base import BaseView


class StartView(BaseView):
    keyboard = StartKeyboard

    def handle(self, message: Message):
        self.bot.send_message(message.chat.id,
                              "Привет, я бот Random Coffee.",
                              reply_markup=self.keyboard.build())
