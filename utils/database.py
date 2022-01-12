import sqlite3
from typing import Union
import datetime
import json

con = sqlite3.connect('data/bot.db')
cur = con.cursor()

def user_exists(user_id: int) -> bool:
    sql = f'SELECT count(*) FROM users WHERE user_id = "{user_id}"'
    count = cur.execute(sql).fetchone()[0]
    return True if count == 1 else False

def create_user(user_id: int, username: str):
    with open('data/config.json') as file:
        config = json.load(file)
    perc = config['Bot_Data']['Referal_Percentage']
    sql = f'INSERT INTO users VALUES ("{user_id}", "{username}", 0, 0, 0, 0, "{perc}")'
    cur.execute(sql)
    con.commit()

def get_user(user_id: int) -> dict:
    if str(user_id) == '0':
        return {'user_id': '0', 'username': '0', 'balance': '0', 'invited_by': '0',  'unlimited': '0', 'subscribed': '0', 'percentage': '0'}
    sql = f'SELECT * FROM users WHERE user_id = "{user_id}"'
    user_data = cur.execute(sql).fetchone()
    mapping = ['user_id', 'username', 'balance', 'invited_by', 'unlimited', 'subscribed', 'percentage']
    user_data_dictionary = dict(zip(mapping, user_data))
    if user_data[5] == 1:
        user_data_dictionary.update({'subscribed': True})
    else:
        user_data_dictionary.update({'subscribed': False})
    date = user_data_dictionary['unlimited']
    if str(date) == '0':
        date = datetime.datetime(2000, 1, 1).date()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    user_data_dictionary.update({'unlimited': date})
    return user_data_dictionary

def update_user(user_id: int, column: str, value: Union[int, str]):
    sql = f'UPDATE users SET {column} = "{value}" WHERE user_id = "{user_id}"'
    cur.execute(sql)
    con.commit()

def get_user_referals_count(user_id: int):
    sql = f'SELECT count(*) FROM users WHERE invited_by = "{user_id}"'
    count = cur.execute(sql).fetchone()[0]
    return count

def get_all_users_ids():
    sql = 'SELECT user_id FROM users'
    users = cur.execute(sql).fetchall()
    return users

def get_balances_sum():
    sql = 'SELECT balance FROM users'
    balances = cur.execute(sql).fetchall()
    total = 0
    for balance in balances:
        total += int(balance[0])
    return total

def get_referals():
    sql = 'SELECT invited_by FROM users WHERE invited_by != 0'
    users = cur.execute(sql).fetchall()
    users = list(set(users))
    map = {}
    for user in users:
        map.update({f'{user[0]}': cur.execute(f'SELECT count(*) FROM users WHERE invited_by = "{user[0]}"').fetchone()[0]})
    return map