from keyboards.base import IKeyboard
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class StartKeyboard(IKeyboard):

    @classmethod
    def build(cls):
        keyboard = ReplyKeyboardMarkup(True, False)
        keyboard.add(KeyboardButton("Зарегистрироваться"))
        return keyboard
