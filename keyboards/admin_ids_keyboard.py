from aiogram import types
import json

def keyboard():
    kb = types.InlineKeyboardMarkup(1)
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    admins = config['Bot_Data']['Admins']
    for admin in admins:
        button = types.InlineKeyboardButton(str(admin), callback_data=str(admin))
        kb.add(button)
    kb.add(types.InlineKeyboardButton('Назад', callback_data='return'))
    return kb