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

    # Check the IDs are valid and not 0
    if uid in user.all_users.keys() and gid in all_groups.keys():

        # Check the uid is not already registered for this group
        if uid not in all_groups[gid].users.keys():
            all_groups[gid].users[uid] = user.all_users[uid]

