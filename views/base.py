from abc import ABCMeta

import telebot

from config import TOKEN


class BaseView(metaclass=ABCMeta):
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)