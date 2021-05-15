from enum import IntEnum


class UserStateMachine(IntEnum):
    start = 0
    enter_name = 1
    enter_bio = 2
    main_menu = 3


class UserStatus(IntEnum):
    free = 0
    busy = 1


class MeetingStatus(IntEnum):
    planned = 0
    in_progress = 1
    ended = 2
