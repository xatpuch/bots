from aiogram import types
import json

def keyboard():
    kb = types.InlineKeyboardMarkup(1)
    mapping = {'Archive': 'Архив фото', 'Photo': 'Фото', 'Unlimited_1': 'Безлимит 1 день', 'Unlimited_7': 'Безлимит 7 дней', 'Unlimited_30': 'Безлимит 30 дней', 'Phone_Number_Info': 'Информация о номере', 'Messages_Archive': 'Сообщения', 'Phone_Number': 'Поиск номера', 'Hidden_Friends': 'Скрытые друзья', 'Phone_Number_Leaks': 'Архив по номеру', 'Tiktok_Videos': 'Архив ТТ'}
    with open('data/prices.json') as json_file:
        prices = json.load(json_file)
    for price in prices:
        button = types.InlineKeyboardButton(f'{mapping[price]} | {prices[price]}₽', callback_data=f'edit:{price}')
        kb.add(button)
    cancel = types.InlineKeyboardButton('Отменить', callback_data='return')
    kb.add(cancel)
    return kb