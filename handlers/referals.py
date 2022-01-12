from loader import dp
from aiogram import types
from utils import database

@dp.message_handler(text='🤑 Реферальная система 🤑')
async def referals(message: types.Message):
    count = database.get_user_referals_count(message.from_user.id)
    balance = database.get_user(message.from_user.id)['balance']
    username = (await message.bot.me).username
    text = f'''<b>Ваша реферальная ссылка:</b>\nhttps://t.me/{username}?start={message.from_user.id}\n\n<b>Количество рефералов: </b><code>{count}</code>\n<b>Баланс: </b><code>{balance}</code>\n\n<i>Приглашайте людей по вашей ссылке и получайте 50% от их покупок!</i>\n\nЧто бы заказать выплату, напиши команду /pay'''
    await message.answer(text)