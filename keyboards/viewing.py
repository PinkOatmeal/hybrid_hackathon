from keyboards.base import IKeyboard
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class ViewingKeyboard(IKeyboard):
    good = "Хочу пообщаться"
    next = "Дальше"
    back = "Меню"

    @classmethod
    def build(cls):
        keyboard = ReplyKeyboardMarkup(True, False)
        keyboard.add(KeyboardButton(cls.good), KeyboardButton(cls.next))
        keyboard.add(KeyboardButton(cls.back))
        return keyboard
