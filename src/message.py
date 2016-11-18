from user import all_users
from group import all_groups

msg_preview = 16


class Message:
    def __init__(self, from_id, to_id, text):
        self.from_id = from_id
        self.to_id = to_id
        self.test = text


def set_message_preview(n):
    msg_preview = n