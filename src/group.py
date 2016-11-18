import user
all_groups = {}


class Group:

    def __init__(self, gid, gname, count):
        self.msg1 = 'ERROR'
        self.msg2 = None
        if gid > 0 and gname != '""' and gname[1].isalpha() and gid not in all_groups.keys():
            self.gid = gid
            self.gname = gname[1:-1]
            self.users = {}
            self.msg1 = 'OK'
            all_groups[gid] = self
        elif gid <= 0:
            self.msg2 = 'ID must be a positive integer.'
        elif gname == '""' or not gname[1].isalpha():
            self.msg2 = 'User name must start with a letter.'
        elif gid in all_groups.keys():
            self.msg2 = 'ID already in use.'
        print '  {}:  {}'.format(count, self.msg1)
        if self.msg2 is not None:
            print '  {}'.format(self.msg2)


def register_user(uid, gid, count):

    msg1 = 'ERROR'
    msg2 = None

    if uid > 0 and gid > 0 and uid in user.all_users.keys() and gid in all_groups.keys() and uid not in all_groups[gid].users.keys():
        msg1 = 'OK'
        all_groups[gid].users[uid] = user.all_users[uid]
    elif uid <= 0 or gid <= 0:
        msg2 = "  ID must be a positive integer."
    elif uid in all_groups[gid].users.keys():
        msg2 = "  This registration already exists."
    elif uid not in user.all_users.keys() or gid not in all_groups.keys():
        msg2 = "  User with this ID does not exist."

    print '  {}:  {}'.format(count, msg1)
    if msg2 is not None:
        print '  ' + msg2
    return msg1


def list_groups():
    print '  Groups:'
    sorted_keys = sorted(all_groups.keys())
    for key in sorted_keys:
        print '      {}->{}'.format(key, all_groups[key].gname)


def list_registers():
    print '  Registrations:'
    sorted_keys = sorted(all_groups.keys())
    for key in sorted_keys:
        sorted_users = sorted(all_groups[key].users.keys())
        for uid in sorted_users:
            print '      [{0},{1}]->'.format(uid, all_groups[key].users[uid].user_name) + '{' + '{0},{1}'.format(key, all_groups[key].gname) + '}'