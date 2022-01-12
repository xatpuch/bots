from loader import dp
from aiogram import types
from utils import vk_parser
import asyncio
import datetime
import json
import random
from filters.is_vk_link import Is_Vk_Link
from keyboards import search_result_keyboard

@dp.message_handler(Is_Vk_Link())
async def search_vk(message: types.Message):
    try:
        user_id = message.text.split('vk.com')[1].replace('/', '')
        user_data = vk_parser.get_user_data(user_id)
        if user_data['sex'] == 1:
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
            photo = user_data['photo']
            text = f'''<b>Взлом найден ✅</b>\n\n<b>id: </b>{user_data["id"]}\n<b>Имя: </b>{user_data["first_name"]}\n<b>Фамилия: </b>{user_data["last_name"]}\n<b>Дата взлома: </b>{random_date}\n\n<b>Скачано диалогов: </b>{str(random.randint(30, 98))}\n<b>Интим фото: </b>В наличии ✅\n<b>Интим видео: </b>В наличии ✅'''
            text2 = f'''<b>{user_data["first_name"]} {user_data["last_name"]}</b> | {prices["Archive"]} <b>🇷🇺 RUB</b>\n\n<b>🗂 Архив взломанной страницы уже сформирован. Все диалоги и вложения страницы готовы к отправке.</b>'''
            await message.answer_photo(photo, text)
            await message.answer(text2, reply_markup=search_result_keyboard.keyboard)
        else:
            loading = await message.answer('<b>Идёт поиск... 🔎</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>Проверяем наши взломы... ♻️</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>Проверяем наши сливы... ♻️</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>❌ Взлом не найден</b>')
            await message.answer_sticker('CAACAgQAAxkBAAEC3SNhNkNNMD7XRzYZ6uhRnCsB3uNz8AACCQgAAiQWWVI_eK9jUmCxFSAE')
    except:
        await message.answer('<b>❌ Произошла ошибка, проверьте ссылку на страницу...</b>')