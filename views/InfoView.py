from telebot.types import Message

from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from views.base import BaseView


class InfoView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        info = UserController.get_info(user_id)

        self.bot.send_message(user_id,
                              info,
                              reply_markup=MainKeyboard.build())
