from keyboards.base import IKeyboard
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class ViewingKeyboard(IKeyboard):
    good = "Хочу пообщаться"
    next = "Дальше"

    @classmethod
    def build(cls):
        keyboard = ReplyKeyboardMarkup(True, False)
        keyboard.add(KeyboardButton(cls.good))
        keyboard.add(KeyboardButton(cls.next))
        return keyboard
