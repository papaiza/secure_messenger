
all_users = {}


class User:

    def __init__(self, uid, user_name, count):
        self.msg1 = 'ERROR'
        self.msg2 = None
        if uid > 0 and user_name != '""' and user_name[1].isalpha() and uid not in all_users.keys():
            self.uid = uid
            self.user_name = user_name[1:-1]
            self.groups = {}
            self.unread_messages = []
            self.read_messages = []
            all_users[uid] = self
            self.msg1 = 'OK'

        elif uid <= 0:
            self.msg2 = 'ID must be a positive integer.'
        elif user_name == '""' or not user_name[1].isalpha():
            self.msg2 = 'User name must start with a letter.'
        elif id in all_users.keys():
            self.msg2 = 'ID already in use.'
        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def list_users():
    print '  Users:'
    sorted_keys = sorted(all_users.keys())
    for key in sorted_keys:
        print '      {}->{}'.format(key, all_users[key].user_name)


