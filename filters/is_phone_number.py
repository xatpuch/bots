from aiogram.dispatcher.filters import Filter
from aiogram import types

class Is_Phone_Number(Filter):
    async def check(self, message: types.Message) -> bool:
        return message.text.startswith('+') and len(message.text) > 10 and len(message.text) < 15