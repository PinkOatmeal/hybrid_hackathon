from abc import ABCMeta, abstractmethod

import telebot

from config import TOKEN


class BaseView(metaclass=ABCMeta):
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)

    @classmethod
    def build(cls, *args, **kwargs):
        return cls().handle(*args, **kwargs)

    @abstractmethod
    def handle(self, *args, **kwargs):
        pass
