from loader import dp
from aiogram import types

@dp.message_handler(text='🌐 Статистика 🌐')
async def stats(message: types.Message):
    await message.answer(f'<b>🔎 Всего было поисков сливов: 18542</b>\n<b>✅ Приобрели товар: 6832</b>\n<b>📩 Сообщений отправлено ботом: 61062</b>')
    await message.answer_sticker('CAACAgIAAxkBAAEC3R1hNjNKTzLh2La_N-VGNv8VlqRsFQACSQIAAladvQoqlwydCFMhDiAE')