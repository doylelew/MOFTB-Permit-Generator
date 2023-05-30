import json
import os
import re

from dotenv import load_dotenv
from cryptography.fernet import Fernet

sessions_folder = "sessions/"
user_data_folder = f"{sessions_folder}userdata/"


user_data_path = f"{user_data_folder}userdata.json"

def hashPassword(password: str):
    if not os.path.isfile('.env'):
        hash = Fernet.generate_key().decode('utf-8')
        with open('.env', 'w') as data:
            data.write(f"HASH_KEY={hash}")

    load_dotenv('.env')
    crypter = Fernet(os.getenv("HASH_KEY"))
    btye_hash = crypter.encrypt(bytes(password, encoding='utf8'))
    return btye_hash.decode('utf-8')

def unhashPassword(password: str):
    load_dotenv('.env')
    decrypter = Fernet(os.getenv("HASH_KEY"))
    try:
        password = decrypter.decrypt(bytes(password, encoding='utf8')).decode('utf-8')
    except:
        password = ""
    return password

def checkSamePass(hash_password: str, password: str):
    load_dotenv('.env')
    decrypter = Fernet(os.getenv("HASH_KEY"))
    if decrypter.decrypt(bytes(hash_password, encoding='utf8')).decode('utf-8') == password:
        return True
    return False


def saveUserData(username: str, password: str, browser: str):
    user_alias = re.sub(r'\W+', '', username.split('@', 1)[0])
    hash_password = hashPassword(password)
    user_data = {
        'users': [
            {
                'email': username,
                'alias': user_alias,
                'password': hash_password,
                'preferred browser': browser,
            },
        ]
    }

    if os.path.isfile(user_data_path):
        with open(user_data_path,'r') as data:
            saved_user_data = json.loads(data.read())

        user_list = [user['email'] for user in saved_user_data['users']]
        if username in user_list:
            saved_user_data['users'][user_list.index(username)]['preferred browser'] = browser
            if not checkSamePass(hash_password = saved_user_data['users'][user_list.index(username)]['password'], password=password ):
                saved_user_data['users'][user_list.index(username)]['password'] = hash_password
        else:
            saved_user_data['users'].append(user_data['users'][0])
        user_data = saved_user_data

    if not os.path.isdir(sessions_folder):
        os.mkdir(sessions_folder)

    if not os.path.isdir(user_data_folder):
        os.mkdir(user_data_folder)

    if not os.path.isdir(f"{sessions_folder}{user_alias}"):
        os.mkdir(f"{sessions_folder}{user_alias}")
        os.mkdir(f"{sessions_folder}{user_alias}/permits")
        os.mkdir(f"{sessions_folder}{user_alias}/drafts")


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
        browser = saved_user_data['users'][user_list.index(username)]['preferred browser']
        load_dotenv('.env')
        hash_password = saved_user_data['users'][user_list.index(username)]['password']
        password = unhashPassword(hash_password)

    return username, password, browser




