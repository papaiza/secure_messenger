import sys
import os.path
from user import User, list_users
from group import Group, register_user, list_groups


def pretty_print(msg):
    if msg == 'OK':
        list_users()
        list_groups()
        # list_registrations()
        # list_all_messages()
        # list_new_messages()
        # list_old_messages()


if sys.argv[1] == '-b':
    if os.path.isfile(sys.argv[2]):
        with open(sys.argv[2]) as f:
            count = 0
            print '  {}:  OK\n'.format(count)
            content = f.readlines()
            for line in content:
                count += 1
                start = line.find('(')
                mid = line.find(',')
                quote = line.find('"')
                end = line.find(')')
                tab = line.find('\t')

                if line[:start].startswith('add_user'):
                    print '->{}'.format(str.split(line, '\t')[0])
                    user = User(int(line[start+1:mid]), line[quote: end], count)
                    pretty_print(user.msg1)

                elif line[:start].startswith('add_group'):
                    print '->{}'.format(str.split(line, '\t')[0])
                    group = Group(int(line[start+1:mid]), line[quote: end], count)
                    pretty_print(group.msg1)
                    
                elif line[:start].startswith('register_user'):
                    register_user(int(line[start+1:mid]), int(line[mid+1: end]))

                elif line[:start].startswith('send_message'):
                    pass

                elif line[:start].startswith('read_message'):
                    pass

                elif line[:start].startswith('delete_message'):
                    pass

                elif line[:start].startswith('set_message_preview'):
                    pass

                elif line[:start].startswith('list_new_messages'):
                    pass

                elif line[:start].startswith('list_old_messages'):
                    pass

                elif line[:tab] == 'list_groups':
                    print '->{}'.format(line[:tab])
                    print '  {}:  OK'.format(count)
                    list_groups()

                elif line[:tab] == 'list_users':
                    print '->{}'.format(line[:tab])
                    print '  {}:  OK'.format(count)
                    list_users()

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