from telebot.types import Message

from controllers.meeting_controller import MeetingController
from controllers.user_controller import UserController
from keyboards.main import MainKeyboard
from keyboards.meeting_inline import MeetingKeyboard
from keyboards.start import StartKeyboard
from utils.enums import UserStateMachine
from views.base import BaseView


class MeetingCreateView(BaseView):

    def handle(self, message: Message):
        user_id = message.chat.id
        date = message.text
        UserController.set_state(message.chat.id, UserStateMachine.main_menu)

        meeting = MeetingController.set_time(user_id, date)

        self.bot.send_message(user_id,
                              "Запрос на проведение встречи отправлен")

        date = meeting.meeting_time.strftime("%H:%M %d.%m.%Y")
        self.bot.send_message(meeting.companion_id.id,
                              f"C Вами хотят встретиться.\n\nВремя: {date}\n\n"
                              f"{meeting.initiator_id.name}\n"
                              f"{meeting.initiator_id.bio}",
                              reply_markup=MeetingKeyboard.build(meeting))

        self.bot.send_message(user_id,
                              "Главное меню:",
                              reply_markup=MainKeyboard.build())

