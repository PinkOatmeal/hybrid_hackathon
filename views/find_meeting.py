from telebot.types import Message

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class FindMeetingView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        UserController.set_state(user_id, UserStateMachine.find_meeting)
        candidate = UserController.find_meeting(user_id)
        if candidate is None:
            UserController.set_state(user_id, UserStateMachine.main_menu)
            self.bot.send_message(user_id,
                                  "Кандидатов для встречи нет",
                                  reply_markup=MainKeyboard.build())
        else:
            self.bot.send_message(user_id,
                                  f"{candidate.name}\n\n{candidate.bio}",
                                  reply_markup=ViewingKeyboard.build())
