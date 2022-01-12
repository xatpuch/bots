from aiogram import types

keyboard = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton('Назад', callback_data='return')
keyboard.add(button)