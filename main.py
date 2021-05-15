import telebot
from telebot.types import Message

from keyboards.start import StartKeyboard
from keyboards.viewing import ViewingKeyboard
from filters import join_name, join_about, viewing_next, viewing_good, join_successful, main_menu
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(message.chat.id,
                     "Привет, я бот Random Coffee.",
                     reply_markup=StartKeyboard.build())


@bot.message_handler(regexp=StartKeyboard.join)
@bot.message_handler(func=join_name.filter_by_state)
def join_name(message: Message):
    bot.send_message(message.chat.id,
                     "Введите своё имя.")


@bot.message_handler(func=join_about.filter_by_state)
def join_about(message: Message):
    bot.send_message(message.chat.id,
                     "Расскажите немного о себе.")


@bot.message_handler(func=join_successful.filter_by_state)
def join_successful(message: Message):
    bot.send_message(message.chat.id,
                     "Вы зарегистрировались")

    # TODO: добавить  вывод предложения с кем пообщаться
    bot.send_message(message.chat.id,
                     "lorem",
                     reply_markup=ViewingKeyboard.build())


@bot.message_handler(regexp=ViewingKeyboard.next)
@bot.message_handler(func=viewing_next.filter_by_state)
def viewing_next(message: Message):
    bot.send_message(message.chat.id,
                     "lorem",
                     reply_markup=ViewingKeyboard.build())


@bot.message_handler(regexp=ViewingKeyboard.next)
@bot.message_handler(func=viewing_good.filter_by_state)
def viewing_good(message: Message):
    bot.send_message(message.chat.id,
                     "lorem",
                     reply_markup=ViewingKeyboard.build())


@bot.message_handler(func=main_menu.filter_by_state)
def main_menu(message: Message):
    bot.send_message(message.chat.id,
                     "Главное меню",
                     reply_markup=ViewingKeyboard.build())


if __name__ == '__main__':
    bot.polling(none_stop=True)
