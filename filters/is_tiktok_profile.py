from aiogram.dispatcher.filters import Filter
from aiogram import types

class Is_Tiktok_Profile(Filter):
    async def check(self, message: types.Message) -> bool:
        return message.text.startswith('@')