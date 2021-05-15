from keyboards.base import IKeyboard
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class MainKeyboard(IKeyboard):
    find = "Найти встречу"
    active = "Активная встреча"
    history = "История"
    info = "Информация о профиле"

    @classmethod
    def build(cls):
        keyboard = ReplyKeyboardMarkup(True, False)
        keyboard.add(KeyboardButton(cls.find))
        keyboard.add(KeyboardButton(cls.active))
        keyboard.add(KeyboardButton(cls.history))
        keyboard.add(KeyboardButton(cls.info))
        return keyboard
