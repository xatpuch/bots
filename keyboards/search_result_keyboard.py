from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
archive = types.InlineKeyboardButton('💳 Приобрести архив', callback_data='buy_archive')
photo = types.InlineKeyboardButton('🍑 Приобрести одну фотку', callback_data='buy_photo')
phone = types.InlineKeyboardButton('📱 Найти номер телефона', callback_data='buy_phone')
messages = types.InlineKeyboardButton('🔞 Купить скачанные переписки', callback_data='buy_messages')
unlimited = types.InlineKeyboardButton('🔎 Безлимитный поиск', callback_data='buy_unlimited')
keyboard.add(archive, photo, messages, phone, unlimited)