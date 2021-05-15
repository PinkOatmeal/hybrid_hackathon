from telebot.types import Message

from keyboards.main import MainKeyboard
from views.base import BaseView


class InfoView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        info = "info"
        # TODO: UserController.get_info()

        self.bot.send_message(user_id,
                              info,
                              reply_markup=MainKeyboard.build())
