import sys
import os.path
from user import *
from group import *
from message import *


def pretty_print(msg):
    if msg == 'OK':
        list_users()
        list_groups()
        list_registers()
        list_messages()
        list_new()
        list_old()


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

                if line[:start] == 'add_user':
                    print '->{}'.format(line[:end+1])
                    user = User(int(line[start+1:mid]), line[quote: end], count)
                    pretty_print(user.msg1)

                elif line[:start] == 'add_group':
                    print '->{}'.format(line[:end + 1])
                    group = Group(int(line[start+1:mid]), line[quote: end], count)
                    pretty_print(group.msg1)
                    
                elif line[:start] == 'register_user':
                    print '->{}'.format(line[:end + 1])
                    msg = register_user(int(line[start+1:mid]), int(line[mid+1: end]), count)
                    pretty_print(msg)

                elif line[:start] == 'send_message':
                    print '->{}'.format(line[:end + 1])
                    smid = line.find(',', mid+1)
                    from_id = int(line[start+1:mid])
                    to_id = int(line[mid+1: smid])
                    text = line[quote:end]
                    message = Message(from_id, to_id, text, count)
                    pretty_print(message.msg1)

                elif line[:start] == 'read_message':
                    print '->{}'.format(line[:end + 1])
                    msg = read_message(int(line[start+1:mid]), int(line[mid+1: end]), count)
                    pretty_print(msg)

                elif line[:start] == 'delete_message':
                    print '->{}'.format(line[:end + 1])
                    # delete_message(int(line[start+1:mid]), int(line[mid+1: end])
                    pass

                elif line[:start] == 'set_message_preview':
                    print '->{}'.format(line[:end + 1])
                    n = int(line[start+1:end])
                    set_message_preview(n)

                elif line[:start] == 'list_new_messages':
                    print '->{}'.format(line[:end + 1])
                    list_new_messages(int(line[start+1:end]), count)

                elif line[:start] == 'list_old_messages':
                    print '->{}'.format(line[:end + 1])
                    list_old_messages(int(line[start+1:end]), count)
                    pass

                elif line[:tab] == 'list_groups':
                    print '->{}'.format(line[:line.find('ps') + 2])
                    print '  {}:  OK'.format(count)
                    if len(all_groups) > 0:
                        list_groups()
                    else:
                        print '  There are no groups registered in the system yet.'

                elif line[:tab] == 'list_users':
                    print '->{}'.format(line[:line.find('rs') + 2])
                    print '  {}:  OK'.format(count)
                    if len(all_users) > 0:
                        list_users()
                    else:
                        print '  There are no users registered in the system yet.'

                else:
                    print("Not a valid command")
                print ""



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