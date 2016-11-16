
all_users = []


class User:

    def __init__(self, uid, user_name):
        id_exists = (user.uid == uid for user in all_users)
        if not any(id_exists):
            self.uid = uid
            self.user_name = user_name
            all_users.append(self)

