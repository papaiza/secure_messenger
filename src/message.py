from user import all_users
from group import all_groups

all_messages = {}


class Message:
    msg_id = 1
    msg_preview = 16

    def __init__(self, from_id, to_id, text, count):
        self.msg1 = 'ERROR'
        self.msg2 = None

        if from_id > 0 and to_id > 0 and text != '""' and (from_id in all_users.keys()) and (to_id in all_groups.keys()) and from_id in all_groups[to_id].users.keys():
            self.msg1 = 'OK'
            self.from_id = from_id
            self.to_id = to_id
            self.text = text[1:-1]
            self.read_ids = []
            self.unread_ids = [x for x in all_groups[to_id].users.keys() if not x == from_id]
            for unread in self.unread_ids:
                all_users[unread].unread_messages.append(Message.msg_id)
            all_messages[Message.msg_id] = self
            Message.msg_id += 1
        elif from_id <= 0 or to_id <= 0:
            self.msg2 = 'ID must be a positive integer.'
        elif text == '""':
            self.msg2 = 'A message may not be an empty string.'
        elif from_id not in all_groups[to_id].users.keys():
            self.msg2 = 'User not authorized to send messages to the specified group.'
        elif from_id not in all_users.keys() or to_id not in all_groups.keys():
            self.msg2 = 'ID does not exist.'

        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def list_messages():
    print '  All messages:'
    sorted_keys = sorted(all_messages.keys())
    if len(all_messages) > 0:
        for key in sorted_keys:
            print '      {}->{}'.format(key, all_messages[key].text[:Message.msg_preview ] + " ...")


def list_new():
    print "  New messages:"
    sorted_users = sorted(all_users.keys())
    if len(all_users) > 0:
        for key in sorted_users:
            if len(all_users[key].unread_messages) > 0:
                out = '      [{}, {}]->'.format(key, all_users[key].user_name) + '{'
                sorted_messages = sorted(all_users[key].unread_messages)
                for msg in sorted_messages:
                    out += '{}, '.format(msg)
                out = out[:-2] + '}'
                print out


def list_new_messages(uid, count):

    if uid > 0 and uid in all_users.keys() and len(all_users[uid].unread_messages) > 0:
        print "  {}:  OK".format(count)
        print "  New/unread messages for user [{}, {}]:".format(uid, all_users[uid].user_name)
        for msg in all_users[uid].unread_messages:
            print "      {}->{} ...".format(msg, all_messages[msg].text[:Message.msg_preview ])
    elif uid <= 0:
        print "  {}:  ERROR".format(count)
        print "  ID must be a positive integer."
    elif uid not in all_users.keys():
        print "  {}:  ERROR".format(count)
        print "  User with this ID does not exist."
    elif len(all_users[uid].unread_messages) == 0:
        print "  {}:  ERROR".format(count)
        print "  There are no new messages for this user."


def set_message_preview(n):
    Message.msg_preview = n