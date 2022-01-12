from aiogram.types.message import Message
from loader import dp
from aiogram import types
from filters.is_instagram_link import Is_Instagram_Link
import datetime
import asyncio
import random
import json
from keyboards import search_result_keyboard
from utils import instagram_parser

@dp.message_handler(Is_Instagram_Link())
async def search_nstagram(message: types.Message):
    username = message.text.split('instagram.com')[1].replace('/', '')
    username = username.replace('?utm_medium=copy_link', '')
    try:
        #photo = instagram_parser.get_profile_photo(username)
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        with open('data/prices.json') as json_file:
                    prices = json.load(json_file)
        loading = await message.answer('<b>Идёт поиск... 🔎</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Проверяем наши взломы... ♻️</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Проверяем наши сливы... ♻️</b>')
        await asyncio.sleep(2)
        await loading.delete()
        text = f'''<b>Взлом найден ✅</b>\n\n<b>Ник: </b>{username}\n<b>Дата взлома: </b>{random_date}\n<b>Интим фото: </b>В наличии ✅\n<b>Интим видео: </b>В наличии ✅'''
        text2 = f'''<b>{username}</b> | {prices["Archive"]} <b>🇷🇺 RUB</b>\n\n<b>🗂 Архив взломанной страницы уже сформирован. Все диалоги и вложения страницы готовы к отправке.</b>'''
        await message.answer(text)
        await message.answer(text2, reply_markup=search_result_keyboard.keyboard)
    except:
        await message.answer('<b>❌ Произошла ошибка, проверьте ссылку на страницу...</b>')