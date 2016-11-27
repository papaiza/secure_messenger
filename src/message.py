from user import all_users
from group import all_groups

all_messages = {}


class Message:
    msg_id = 1
    msg_preview = 15

    def __init__(self, from_id, to_id, text, count):
        self.msg1 = 'ERROR '
        self.msg2 = None

        if from_id > 0 and to_id > 0 and text != '""' and (from_id in all_users.keys()) and (to_id in all_groups.keys()) and from_id in all_groups[to_id].users.keys():
            self.msg1 = 'OK'
            self.from_id = from_id
            self.to_id = to_id
            self.text = text[1:-1]
            self.read_ids = []
            # all_users[from_id].read_messages.append(Message.msg_id)
            self.unread_ids = [x for x in all_groups[to_id].users.keys() if not x == from_id]
            for unread in self.unread_ids:
                all_users[unread].unread_messages.append(Message.msg_id)
            all_messages[Message.msg_id] = self
            Message.msg_id += 1
        elif from_id <= 0 or to_id <= 0:
            self.msg2 = 'ID must be a positive integer.'
        elif from_id not in all_users.keys():
            self.msg2 = 'User with this ID does not exist.'
        elif to_id not in all_groups.keys():
            self.msg2 = 'Group with this ID does not exist.'
        elif text == '""':
            self.msg2 = 'A message may not be an empty string.'
        elif from_id not in all_groups[to_id].users.keys():
            self.msg2 = 'User not authorized to send messages to the specified group.'
        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def read_message(uid, mid, count):
    msg = 'ERROR '
    if uid > 0 and mid > 0 and mid in all_messages.keys() and uid in all_users.keys() and uid in all_messages[mid].unread_ids and uid not in all_messages[mid].read_ids and uid in all_groups[all_messages[mid].to_id].users:
        msg = 'OK'
        all_messages[mid].unread_ids.remove(uid)
        all_messages[mid].read_ids.append(uid)
        all_users[uid].unread_messages.remove(mid)
        all_users[uid].read_messages.append(mid)
        print "  {}:  {}".format(count, msg)
        print '  Message for user [{}, {}]: [{}, "{}"]'.format(uid, all_users[uid].user_name, mid, all_messages[mid].text)
    elif uid <= 0 or mid <= 0:
        print "  {}:  {}".format(count, msg)
        print "  ID must be a positive integer."
    elif uid not in all_users.keys():
        print "  {}:  {}".format(count, msg)
        print "  User with this ID does not exist."
    elif mid not in all_messages.keys():
        print "  {}:  {}".format(count, msg)
        print "  Message with this ID does not exist."
    elif uid not in all_groups[all_messages[mid].to_id].users:
        print "  {}:  {}".format(count, msg)
        print "  User not authorized to access this message."
    elif uid in all_messages[mid].read_ids and uid not in all_messages[mid].unread_ids:
        print "  {}:  {}".format(count, msg)
        print "  Message has already been read. See `list_old_messages'."
    return msg


def delete_message(uid, mid, count):
    msg = 'ERROR '
    if uid > 0 and mid > 0 and mid in all_messages.keys() and uid in all_users.keys() and uid in all_messages[mid].read_ids:
        msg = 'OK'
        all_messages[mid].read_ids.remove(uid)
        if all_messages[mid].from_id != uid:
            all_users[uid].read_messages.remove(mid)
        print "  {}:  {}".format(count, msg)
    elif uid <= 0 or mid <= 0:
        print "  {}:  {}".format(count, msg)
        print "  ID must be a positive integer."
    elif uid not in all_users.keys():
        print "  {}:  {}".format(count, msg)
        print "  User with this ID does not exist."
    elif mid not in all_messages.keys():
        print "  {}:  {}".format(count, msg)
        print "  Message with this ID does not exist."
    elif uid not in all_messages[mid].read_ids:
        print "  {}:  {}".format(count, msg)
        print "  Message with this ID not found in old/read messages."

    return msg


def list_messages():
    print '  All messages:'
    sorted_keys = sorted(all_messages.keys())
    if len(all_messages) > 0:
        for key in sorted_keys:
            if len(all_messages[key].text) <= Message.msg_preview:
                print "      {}->{}".format(key, all_messages[key].text)
            else:
                print "      {}->{} ...".format(key, all_messages[key].text[:Message.msg_preview])


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


def list_old():
    print "  Old/read messages:"
    sorted_users = sorted(all_users.keys())
    if len(all_users) > 0:
        for key in sorted_users:
            if len(all_users[key].read_messages) > 0:
                out = '      [{}, {}]->'.format(key, all_users[key].user_name) + '{'
                sorted_messages = sorted(all_users[key].read_messages)
                for msg in sorted_messages:
                    out += '{}, '.format(msg)
                out = out[:-2] + '}'
                print out


def list_new_messages(uid, count):

    if uid > 0 and uid in all_users.keys() and len(all_users[uid].unread_messages) > 0:
        print "  {}:  OK".format(count)
        print "  New/unread messages for user [{}, {}]:".format(uid, all_users[uid].user_name)
        for msg in all_users[uid].unread_messages:
            if len(all_messages[msg].text) <= Message.msg_preview:
                print "      {}->{}".format(msg, all_messages[msg].text)
            else:
                print "      {}->{} ...".format(msg, all_messages[msg].text[:Message.msg_preview])
    elif uid <= 0:
        print "  {}:  ERROR ".format(count)
        print "  ID must be a positive integer."
    elif uid not in all_users.keys():
        print "  {}:  ERROR ".format(count)
        print "  User with this ID does not exist."
    elif len(all_users[uid].unread_messages) == 0:
        print "  {}:  OK".format(count)
        print "  There are no new messages for this user."


def list_old_messages(uid, count):
    if uid > 0 and uid in all_users.keys() and len(all_users[uid].read_messages) > 0:
        print "  {}:  OK".format(count)
        print "  Old/read messages for user [{}, {}]:".format(uid, all_users[uid].user_name)
        for msg in all_users[uid].read_messages:
            if len(all_messages[msg].text) <= Message.msg_preview:
                print "      {}->{}".format(msg, all_messages[msg].text)
            else:
                print "      {}->{} ...".format(msg, all_messages[msg].text[:Message.msg_preview])
    elif uid <= 0:
        print "  {}:  ERROR ".format(count)
        print "  ID must be a positive integer."
    elif uid not in all_users.keys():
        print "  {}:  ERROR ".format(count)
        print "  User with this ID does not exist."
    elif len(all_users[uid].read_messages) == 0:
        print "  {}:  OK".format(count)
        print "  There are no old messages for this user."


def set_message_preview(n, count):
    msg = 'ERROR '
    if n <= 0:
        print '  {}:  {}'.format(count, msg)
        print '  Message length must be greater than zero.'
    else:
        msg = 'OK'
        print '  {}:  {}'.format(count, msg)
        Message.msg_preview = n
    return msg