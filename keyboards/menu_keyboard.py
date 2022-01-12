from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
find_leaks = types.KeyboardButton('🔍 Найти сливы 🔍')
help = types.KeyboardButton('👨🏼‍🔧 Тех. поддержка 👨🏼‍🔧')
referals = types.KeyboardButton('🤑 Реферальная система 🤑')
examples = types.KeyboardButton('💡 Примеры 💡')
statistics = types.KeyboardButton('🌐 Статистика 🌐')
keyboard.row(find_leaks)
keyboard.row(help)
keyboard.row(referals)
keyboard.row(examples, statistics)