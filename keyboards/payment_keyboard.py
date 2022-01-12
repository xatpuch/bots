from aiogram import types

def make_keyboard(url: str, type: str, pref = ''):
    keyboard = types.InlineKeyboardMarkup(1)
    link = types.InlineKeyboardButton('💳 Перейти к оплате', callback_data='procced_payment', url=url)
    check = types.InlineKeyboardButton('🔄 Проверить оплату', callback_data=f'{pref}check_payment_{type}')
    cancel = types.InlineKeyboardButton('❌ Отменить', callback_data='cancel_payment')
    keyboard.add(link, check, cancel)
    return keyboard