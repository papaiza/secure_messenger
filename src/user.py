
all_users = {}


class User:

    def __init__(self, uid, user_name, count):
        self.msg1 = 'ERROR '
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
        elif uid in all_users.keys():
            self.msg2 = 'ID already in use.'
        elif user_name == '""' or not user_name[1].isalpha():
            self.msg2 = 'User name must start with a letter.'
        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def list_users():
    sorted_users = selectionSort(all_users.values())
    for user in sorted_users:
        print '  {}->{}'.format(user.uid, user.user_name)


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location].user_name > alist[positionOfMax].user_name:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


def list_users_pp():
    sorted_keys = sorted(all_users.keys())
    for key in sorted_keys:
        print '      {}->{}'.format(key, all_users[key].user_name)


