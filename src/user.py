
all_users = {}


class User:

    def __init__(self, uid, user_name):
        id_exists = (user_id == uid for user_id, user in all_users.iteritems())
        self.msg1 = 'ERROR'
        if uid > 0 and user_name[1].isalpha() and not any(id_exists):
            self.uid = uid
            self.user_name = user_name
            all_users[uid] = self
            self.msg1 = 'OK'
        elif uid <= 0:
            print '  ID must be a positive integer.\n'
        elif not user_name[1].isalpha():
            print '  User name must start with a letter.\n'
        elif any(id_exists):
            print '  ID already in use.\n'


def list_users():
    if len(all_users) > 0:
        print '  Users:'
        sorted_keys = sorted(all_users.keys())
        for key in sorted_keys:
            print '    {}->{}'.format(key, all_users[key].user_name)
    else:
        print '  There are no users registered in the system yet.\n'

