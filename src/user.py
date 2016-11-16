
all_users = {}


class User:

    def __init__(self, uid, user_name):
        id_exists = (user_id == uid for user_id, user in all_users.iteritems())
        self.msg1 = 'ERROR'
        if uid > 0 and user_name[0].isalpha() and not any(id_exists):
            self.uid = uid
            self.user_name = user_name
            self.msg1 = 'OK'
            self.msg2 = '  Users: \n       1->Dr. Dolittle\n  Groups:\n    Registrations:\n  All messages:\n  New messages:\n  Old/read messages:\n'
            all_users[uid] = self
        elif uid <= 0:
            self.msg2 = 'ID must be a positive integer.\n'
        elif not user_name[0].isalpha():
            self.msg2 = 'User name must start with a letter.\n'
        elif any(id_exists):
            self.msg2 = 'ID already in use.\n'


def list_users():
    sorted_keys = sorted(all_users.keys())
    for key in sorted_keys:
        print '{}->{}\n'.format(key, all_users[key].user_name)

