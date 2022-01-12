from aiogram.dispatcher.filters import Filter
from aiogram import types

class Is_Instagram_Link(Filter):
    async def check(self, message: types.Message) -> bool:
        return message.text.startswith(tuple(['instagram.com/', 'https://www.instagram.com/', 'https://instagram.com/']))