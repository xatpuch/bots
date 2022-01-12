from aiogram.dispatcher.filters import Filter
from aiogram import types
import json
from utils import database

class Not_Subscribed(Filter):
    async def check(self, message: types.Message) -> bool:
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        if message.from_user.id in config['Bot_Data']['Admins']:
            return False
        if not config['Bot_Data']['Subscription_Required']:
            return False
        if database.user_exists(message.from_user.id):
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            if config['Bot_Data']['Subscription_Required'] and not (database.get_user(message.from_user.id)['subscribed']):
                return True
            return False
        else:
            database.create_user(message.from_user.id, message.from_user.username)
            return True