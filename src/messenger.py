import sys
import os.path
from user import User
from group import Group

if sys.argv[1] == '-b':
    if os.path.isfile(sys.argv[2]):
        with open(sys.argv[2]) as f:
            content = f.readlines()
            for line in content:
                l = str.split(line)

                if l[0].startswith('add_user'):
                    User(int(l[0][9:-1]), l[1][:-1])
                elif l[0].startswith('add_group'):
                    Group(int(l[0][10:-1]), l[1][:-1])
                elif l[0].startswith('register_user'):
                    pass
                elif l[0].startswith('send_message'):
                    pass
                elif l[0].startswith('read_message'):
                    pass
                elif l[0].startswith('delete_message'):
                    pass
                elif l[0].startswith('set_message_preview'):
                    pass
                elif l[0].startswith('list_new_messages'):
                    pass
                elif l[0].startswith('list_old_messages'):
                    pass
                elif l[0] == 'list_groups':
                    pass
                elif l[0] == 'list_users':
                    pass
                else:
                    print("Not a valid command")


# add_user		        (uid: UID; user_name: USER)
#                     -- add a new user to the system
# add_group		        (gid: GID; group_name: GROUP)
#                     -- add a new group to the system
# register_user		    (uid: UID; gid: GID)
#                     -- register a user in a group
# send_message		    (uid: UID; gid: GID; txt: TEXT)
#                     -- send a message to the group members
# read_message		    (uid: UID; mid: MID)
#                     -- read a new message
# delete_message		  (uid: UID; mid: MID)
#                     -- delete an old/read message
# set_message_preview	(n: INTEGER)
#                     -- sets length (characters) for message preview
#                     -- default is 15
#
# ---------------------------------------------------------------------
# -- Secure Messenger Queries
# ---------------------------------------------------------------------
# list_new_messages	(uid: UID)
#                    -- list user's new messages
# list_old_messages	(uid: UID)
#                    -- list user's old/read message
# list_groups
#                    -- list all groups in alphabetical order
# list_users
#                    -- list all users in alphabetical order