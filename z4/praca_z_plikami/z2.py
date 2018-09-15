import sys


with open(sys.argv[1], encoding='utf-8') as f:

    users_table = dict()
    users_time_login = dict()
    logi = f.read()
    logi = logi.splitlines()
    for line in logi:
        username, action, time = line.split(";")
        if action == "LOGIN":
            users_time_login[username] = int(time)
        elif action == "LOGOUT":
            login_time = int(time) - users_time_login[username]
            users_table[username] = users_table.get(username, 0) + login_time

    print(users_table.items())

    for u in sorted(users_table.items(), key=lambda x: x[1], reverse=True):
        print(u[0], u[1], 's')

