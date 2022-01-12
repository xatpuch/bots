from loader import dp
from aiogram import types
from filters.is_tiktok_profile import Is_Tiktok_Profile
from utils import tiktok_parser
import asyncio
import datetime
import random
import json
from keyboards import tiktok_search_result_keyboard

@dp.message_handler(Is_Tiktok_Profile())
async def search_tiktok(message: types.Message):
    username = message.text.replace('@', '')
    try:
        # photo = tiktok_parser.get_profile_picture(username)
        loading = await message.answer('<b>Идёт поиск... 🔎</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Проверяем наши взломы... ♻️</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Проверяем наши сливы... ♻️</b>')
        await asyncio.sleep(2)
        await loading.delete()
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        with open('data/prices.json') as json_file:
            prices = json.load(json_file)
        text = f'''<b>Взлом найден ✅</b>\n\n<b>Ник: </b>{username}\n<b>Дата взлома: </b>{random_date}\n\n<b>Скачано черновиков: </b>{str(random.randint(3, 20))}\n<b>Скачано скрытых видео: </b>{str(random.randint(3, 20))}\n<b>Номер телефона: </b>Найден!'''
        text2 = f'''<b>{username}</b> | {prices["Tiktok_Videos"]} <b>🇷🇺 RUB</b>\n\n<b>🗂 Архив взломанной страницы уже сформирован. Все видео готовы к отправке.</b>'''
        await message.answer(text)
        await message.answer(text2, reply_markup=tiktok_search_result_keyboard.keyboard)
    except:
        await message.answer('<b>❌ Произошла ошибка, проверьте имя профиля...</b>')