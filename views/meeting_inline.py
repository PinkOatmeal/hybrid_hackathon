from telebot.types import Message, InlineQuery, CallbackQuery

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine, MeetingCallbackQuery, MeetingStatus
from views.base import BaseView


class MeetingInlineView(BaseView):

    def handle(self, query: CallbackQuery):
        answer, meeting_id = query.data.split(" ")
        answer = MeetingCallbackQuery(int(answer))
        meeting = MeetingController.get_by_id(meeting_id)
        status = MeetingStatus(meeting.status)
        if status == MeetingStatus.planned:
            self.bot.send_message(query.from_user.id, "Вы уже согласились")
            return
        if status == MeetingStatus.refuse:
            self.bot.send_message(query.from_user.id, "Вы уже отказались")
            return
        if answer == MeetingCallbackQuery.ok:
            meeting = MeetingController.set_status(meeting_id, MeetingStatus.planned)
            self.bot.send_message(meeting.initiator_id.id,
                                  f"Пользователь {meeting.companion_id.name} согласился с Вами встретиться")
        else:
            meeting = MeetingController.set_status(meeting_id, MeetingStatus.refuse)
            self.bot.send_message(meeting.initiator_id.id,
                                  f"Пользователь {meeting.companion_id.name} отказался с Вами встречаться")
