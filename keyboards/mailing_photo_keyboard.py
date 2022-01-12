from aiogram import types

keyboard = types.InlineKeyboardMarkup(2)
dont_add_photo = types.InlineKeyboardButton('Не добавлять фото', callback_data='no_photo')
cancel = types.InlineKeyboardButton('Отменить', callback_data='return')
keyboard.add(dont_add_photo, cancel)