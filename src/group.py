import user
all_groups = {}


class Group:

    def __init__(self, gid, gname):
        gid_exists = (group_id == gid for group_id, group in all_groups.iteritems())
        if gid > 0 and not any(gid_exists):
            self.gid = gid
            self.gname = gname
            self.users = {}
            all_groups[gid] = self


def register_user(uid, gid):
    if uid <= 0 or gid <= 0:
        print "  ID must be a positive integer."

    # Check the IDs are valid and not 0
    if uid in user.all_users.keys() and gid in all_groups.keys():

        # Check the uid is not already registered for this group
        if uid not in all_groups[gid].users.keys():
            all_groups[gid].users[uid] = user.all_users[uid]
        else:
            print "  This registration already exists."
    else:
        print "  User with this ID does not exist."


def list_groups():
    if len(all_groups) >0:
        sorted_keys = sorted(all_groups.keys())
        for key in sorted_keys:
            print '{}->{}'.format(key, all_groups[key].gname)
    else:
        print '  There are no groups registered in the system yet.\n'


def list_registers():
    sorted_keys = sorted(all_groups.keys())
    for key in sorted_keys:
        sorted_users = sorted(all_groups[key].users.keys())
        for uid in sorted_users:
            print '[{0},{1}]->{ {2}->{3}}'.format(uid, all_groups[key].users[uid].name, key, all_groups[key].gname)