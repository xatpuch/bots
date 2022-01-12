from aiogram.dispatcher.filters import Filter
from aiogram import types

class Is_Vk_Link(Filter):
    async def check(self, message: types.Message) -> bool:
        return message.text.startswith(tuple(['vk.com', 'https://vk.com', 'http://vk.com']))