from enum import IntEnum


class UserStateMachine(IntEnum):
    start = 0
    enter_name = 1
    enter_bio = 2
    main_menu = 3
    find_meeting = 4
    meeting_date = 5


class UserStatus(IntEnum):
    free = 0
    busy = 1


class MeetingStatus(IntEnum):
    not_answer = 0
    planned = 1
    in_progress = 2
    ended = 3
    refuse = 4


class MeetingCallbackQuery(IntEnum):
    ok = 0
    cancel = 1
