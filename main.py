import telebot
from telebot.types import Message

from keyboards.main import MainKeyboard
from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from filters import (join_name,
                     join_about,
                     viewing_next,
                     viewing_good,
                     join_successful,
                     find_meeting,
                     main_info,
                     start_registered)
from config import TOKEN
from views.info import InfoView
from views.join_name import JoinNameView
from views.join_bio import JoinBioView
from views.end_register import EndRegisterView
from views.find_meeting import FindMeetingView
from views.main import MainView
from views.meeting_create import MeetingCreateView
from views.meeting_date import MeetingDateView
from views.meeting_inline import MeetingInlineView
from views.start import StartView

bot = telebot.TeleBot(TOKEN)

bot.message_handler(commands=["start"]
                    )(StartView.build)

bot.message_handler(regexp=StartKeyboard.join,
                    func=start_registered.filter_by_state,
                    )(JoinNameView.build)

bot.message_handler(func=join_about.filter_by_state,
                    )(JoinBioView.build)

bot.message_handler(func=join_successful.filter_by_state,
                    )(EndRegisterView.build)

bot.message_handler(func=main_info.filter_by_state,
                    regexp=MainKeyboard.info,
                    )(InfoView.build)

bot.message_handler(func=find_meeting.filter_by_state,
                    regexp=MainKeyboard.find,
                    )(FindMeetingView.build)

bot.message_handler(func=find_meeting.filter_by_state_in_finded,
                    regexp=ViewingKeyboard.back,
                    )(MainView.build)

bot.message_handler(func=find_meeting.filter_by_state_in_finded,
                    regexp=ViewingKeyboard.next,
                    )(FindMeetingView.build)

bot.message_handler(func=find_meeting.filter_by_state_in_finded,
                    )(MeetingDateView.build)

bot.message_handler(func=find_meeting.filter_by_state_in_date,
                    )(MeetingCreateView.build)

bot.callback_query_handler(func=lambda call: True
                           )(MeetingInlineView.build)


if __name__ == '__main__':
    bot.polling(none_stop=True)
