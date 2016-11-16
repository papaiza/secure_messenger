
all_groups = []


class Group:

    def __init__(self, gid, gname):
        gid_exists = (group.gid == gid for group in all_groups)
        if not any(gid_exists):
            self.gid = gid
            self.user_name = gname
            all_groups.append(self)
            self.users = []
