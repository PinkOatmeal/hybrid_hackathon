from keyboards.base import IKeyboard
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from models.meeting import Meeting


class MeetingKeyboard(IKeyboard):
    ok = "Пойду"
    cancel = "Не пойду"

    @classmethod
    def build(cls, meeting: Meeting):
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(cls.ok, callback_data=f"0 {meeting.id}"),
                     InlineKeyboardButton(cls.cancel, callback_data=f"1 {meeting.id}"))
        return keyboard
