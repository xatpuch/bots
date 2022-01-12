from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
leaks = types.InlineKeyboardButton('🔎 Проверить на наличие сливов', callback_data='phone_leaks')
info = types.InlineKeyboardButton('🔎 Поиск личной информации', callback_data='phone_info')
keyboard.add(leaks, info)