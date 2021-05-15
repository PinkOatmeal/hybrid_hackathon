from telebot.types import Message

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class HistoryView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        history = MeetingController.get_history(user_id)

        self.bot.send_message(user_id,
                              history,
                              reply_markup=MainKeyboard.build())
