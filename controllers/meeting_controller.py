import datetime
from typing import Optional

from models.meeting import Meeting
from utils.enums import MeetingStatus


class MeetingController:

    @staticmethod
    def create_meeting(*, initiator_id: int, companion_id: int) -> Meeting:
        return Meeting.create(initiator_id=initiator_id, companion_id=companion_id)

    @staticmethod
    def delete_not_is_ready(initiator_id: int):
        Meeting.delete().where((Meeting.initiator_id == initiator_id) & (Meeting.is_ready == False)).execute()

    @staticmethod
    def get_in_progress(initiator_id: int) -> Meeting:
        return Meeting.select().where((Meeting.initiator_id == initiator_id) & (Meeting.is_ready == False)).get()

    @staticmethod
    def get_by_id(meeting_id) -> Optional[Meeting]:
        query_set = Meeting.select().where(Meeting.id == meeting_id)
        if query_set.exists():
            return query_set.get()
        return None

    @staticmethod
    def rate_meeting(_id: int, rating: int) -> Meeting:
        meeting = Meeting.get((Meeting.initiator_id == _id) | (Meeting.companion_id == _id))
        if _id == meeting.initiator_id:
            meeting.initiator_rate = rating
            meeting.save()
        if _id == meeting.companion_id:
            meeting.companion_rate = rating
            meeting.save()
        return meeting

    @staticmethod
    def leave_feedback(_id: int, feedback: str) -> Meeting:
        meeting = Meeting.get((Meeting.initiator_id == _id) | (Meeting.companion_id == _id))
        if _id == meeting.initiator_id:
            meeting.initiator_feedback = feedback
            meeting.save()
        if _id == meeting.companion_id:
            meeting.companion_feedback = feedback
            meeting.save()
        return meeting

    @staticmethod
    def set_status(_id: int, status: MeetingStatus) -> Optional[Meeting]:
        meeting = Meeting.select().where(Meeting.id == _id)
        if meeting.exists():
            meeting = meeting.get()
            meeting.status = status
            meeting.save()
            return meeting
        return None



    @staticmethod
    def check_status(_id: int, status: MeetingStatus) -> bool:
        meeting = Meeting.get((Meeting.initiator_id == _id) | (Meeting.companion_id == _id))
        current_status = MeetingStatus(meeting.status)
        return current_status == status

    @staticmethod
    def set_time(_id: int, time_date: str) -> Meeting:
        time_to_db = datetime.datetime.strptime(time_date, "%H:%M %d.%m.%Y")

        meeting = Meeting.get((Meeting.initiator_id == _id) & (Meeting.is_ready == False))
        meeting.meeting_time = time_to_db
        meeting.is_ready = True
        meeting.save()
        return meeting

    @staticmethod
    def get_exist_records(user_id: int) -> list:
        results = set()
        query_set = Meeting.select().where((Meeting.initiator_id == user_id) |
                                           (Meeting.companion_id == user_id))
        for i in query_set:
            results.add(i.initiator_id.id)
            results.add(i.companion_id.id)
        return list(results)
