import telebot
from telebot.types import Message

from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from filters import (join_name,
                     join_about,
                     viewing_next,
                     viewing_good,
                     join_successful,
                     main_menu,
                     main_info,
                     start_registered)
from config import TOKEN
from views.InfoView import InfoView
from views.join_name import JoinNameView
from views.join_bio import JoinBioView
from views.end_register import EndRegisterView
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
                    )(InfoView.build)


if __name__ == '__main__':
    bot.polling(none_stop=True)
