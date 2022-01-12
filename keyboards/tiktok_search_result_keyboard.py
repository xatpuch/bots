from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
videos = types.InlineKeyboardButton('💳 Приобрести архив видео', callback_data='buy_tiktok_archive')
phone = types.InlineKeyboardButton('📱 Приобрести номер телефона', callback_data='buy_phone')
keyboard.add(videos, phone)