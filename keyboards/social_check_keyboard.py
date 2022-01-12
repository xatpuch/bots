from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
instagram = types.InlineKeyboardButton('Instagram', callback_data='instagram')
vk = types.InlineKeyboardButton('ВКонтакте', callback_data='vk')
phone_number = types.InlineKeyboardButton('Номер телефона', callback_data='phone_number')
tiktok = types.InlineKeyboardButton('TikTok', callback_data='tiktok')
keyboard.add(instagram, vk, phone_number, tiktok)

back_keyboard = types.InlineKeyboardMarkup()
back_button = types.InlineKeyboardButton('Назад', callback_data='social_back')
back_keyboard.add(back_button)