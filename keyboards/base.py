from abc import ABCMeta, abstractmethod


class IKeyboard(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def build(cls, *args, **kwargs):
        pass

