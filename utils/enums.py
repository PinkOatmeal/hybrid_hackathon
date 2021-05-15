from enum import Enum, auto


class UserStateMachine(Enum):
    start = auto()


class UserState(Enum):
    free = auto()
    busy = auto()


class MeetingState(Enum):
    planned = auto()
    in_progress = auto()
    ended = auto()
