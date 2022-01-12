from aiogram.dispatcher.filters import Filter
from aiogram import types
import json

class Is_Admin(Filter):
    async def check(self, message: types.Message) -> bool:
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        admins = config['Bot_Data']['Admins']
        if message.from_user.id in admins:
            return True
        return False