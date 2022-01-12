from loader import dp
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f'''👋 Привет, {message.from_user.full_name}\n\nЭтот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    if not database.user_exists(message.from_user.id):
        database.create_user(message.from_user.id, message.from_user.username)
        if message.get_args() != '':
            if database.user_exists(message.get_args()):
                database.update_user(message.from_user.id, 'invited_by', message.get_args())
        await message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)
    else:
        await message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)