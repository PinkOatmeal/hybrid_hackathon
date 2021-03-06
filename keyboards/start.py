from keyboards.base import IKeyboard
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class StartKeyboard(IKeyboard):
    join = "Зарегистрироваться"

    @classmethod
    def build(cls):
        keyboard = ReplyKeyboardMarkup(True, False)
        keyboard.add(KeyboardButton(cls.join))
        return keyboard
