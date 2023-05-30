import json
import os

sessions_folder = "sessions/"
user_data_folder = f"{sessions_folder}users/"
user_data_path = f"{user_data_folder}userdata.json"


def saveUserData(username: str, password: str, browser: str):
    user_data = {
        'users': [
            {
                'email': username,
                'password': password,
                'preferred browser': browser,
            },
        ]
    }

    if os.path.isfile(user_data_path):
        with open(user_data_path,'r') as data:
            saved_user_data = json.loads(data.read())

        user_list = [user['email'] for user in saved_user_data['users']]
        if username in user_list:
            saved_user_data['users'][user_list.index(username)]['password'] = password
            saved_user_data['users'][user_list.index(username)]['preferred browser'] = browser
        else:
            saved_user_data['users'].append(user_data['users'][0])
        user_data = saved_user_data

    if not os.path.isdir(sessions_folder):
        os.mkdir(sessions_folder)

    if not os.path.isdir(user_data_folder):
        os.mkdir(user_data_folder)

    user_data['last user'] = username

    with open(user_data_path, 'w') as save_data:
        save_data.write(json.dumps(user_data, indent=2))


def lastUserInfo():
    username = ""
    password = ""
    browser = "Firefox"
    if os.path.isfile(user_data_path):
        with open(user_data_path,'r') as data:
            saved_user_data = json.loads(data.read())
        username = saved_user_data['last user']
        user_list = [user['email'] for user in saved_user_data['users']]
        password = saved_user_data['users'][user_list.index(username)]['password']
        browser = saved_user_data['users'][user_list.index(username)]['preferred browser']

    print(username, password)
    return username, password, browser




