from aiogram import types

keyboard = types.InlineKeyboardMarkup()
check = types.InlineKeyboardButton('Я подписался', callback_data='check_subscribtion')
keyboard.add(check)