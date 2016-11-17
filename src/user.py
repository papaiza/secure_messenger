
all_users = {}


class User:

    def __init__(self, uid, user_name, count):
        id_exists = (user_id == uid for user_id, user in all_users.iteritems())
        self.msg1 = 'ERROR'
        self.msg2 = None
        if uid > 0 and user_name[1].isalpha() and not any(id_exists):
            self.uid = uid
            self.user_name = user_name
            all_users[uid] = self
            self.msg1 = 'OK'

        elif uid <= 0:
            self.msg2 = 'ID must be a positive integer.\n'
        elif not user_name[1].isalpha():
            self.msg2 = 'User name must start with a letter.\n'
        elif any(id_exists):
            self.msg2 = 'ID already in use.\n'
        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def list_users():
    if len(all_users) > 0:
        print '  Users:'
        sorted_keys = sorted(all_users.keys())
        for key in sorted_keys:
            print '    {}->{}'.format(key, all_users[key].user_name)
    else:
        print '  There are no users registered in the system yet.\n'

