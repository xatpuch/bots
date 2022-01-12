from aiogram import types
from utils import get_price

def make_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    one_day = types.InlineKeyboardButton(f'💳 {get_price.get_price("Unlimited_1")}₽ за 1 день', callback_data='unlimited_one_day')
    week = types.InlineKeyboardButton(f'💳 {get_price.get_price("Unlimited_7")}₽ за 7 дней', callback_data='unlimited_week')
    month = types.InlineKeyboardButton(f'💳 {get_price.get_price("Unlimited_30")}₽ за 30 дней', callback_data='unlimited_month')
    keyboard.row(one_day, week)
    keyboard.row(month)
    return keyboard