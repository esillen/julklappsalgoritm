from users import users
from mailer import send_mail, create_message, close_mail_server
import random

num_users = len(users)
user_names = users.keys()
found_solution = False
mapping = [[0 for i in range(num_users)] for j in range(num_users)]
for i_try in range(1000): # 1000 tries before terminating
    mapping = [[0 for i in range(num_users)] for j in range(num_users)] # Reset the mapping
    for i in range(num_users):
        mapping[i][i] = -1 # cannot sent to self
        user_name = user_names[i]
        for forbidden_name in users[user_name]['forbidden']:
            forbidden_index = user_names.index(forbidden_name)
            mapping[i][forbidden_index] = -1 # remove forbidden relations
    found_issue = False
    for i in range(num_users):
        potential_receiver_indexes = []
        for j in range(num_users):
            if mapping[i][j] == 0:
                potential_receiver_indexes.append(j)
        if len(potential_receiver_indexes) == 0:
            found_issue = True
            break # solution not found, no more receivers possible
        to_give_index = random.choice(potential_receiver_indexes)
        mapping[i][to_give_index] = 1 # give to this user!!
        mapping[to_give_index][i] = -1 # this user should not give anything back!
        for k in range(num_users):
            if k != i:
                mapping[k][to_give_index] = -1 # This user should not receive from anyone else
    if not found_issue:
        # SOLUTION FOUND!!!
        found_solution = True
        break
if not found_solution:
    raise RuntimeError("Could not found the solution but tried really hard.")
else:
    # print mapping
    for i in range(num_users):
        user_name = user_names[i]
        user_email = users[user_names[i]]['email']
        to_give_index = mapping[i].index(1)
        to_give_username = user_names[to_give_index]
        # print "{0} should give {1} a present!".format(user_name, to_give_username)
        email_message = create_message(user_email, user_name, to_give_username)
        send_mail(user_email, email_message)
    close_mail_server()