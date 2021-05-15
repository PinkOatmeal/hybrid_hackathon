import telebot
from telebot.types import Message

from keyboards.start import StartKeyboard
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(message.chat.id,
                     "Привет, я бот Random Coffee.",
                     reply_markup=StartKeyboard.build())


if __name__ == '__main__':
    bot.polling(none_stop=True)
