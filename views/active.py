from telebot.types import Message

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class ActiveView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        active = MeetingController.get_active_meeting(user_id)

        self.bot.send_message(user_id,
                              active,
                              reply_markup=MainKeyboard.build())
