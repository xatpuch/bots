from loader import dp
from aiogram import types
from keyboards import social_check_keyboard

@dp.message_handler(text='🔍 Найти сливы 🔍')
async def find_leaks(message: types.Message):
    text=f'''👋 Привет, {message.from_user.full_name}\n\nЭтот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    await message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text)
    await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)

@dp.callback_query_handler(text='instagram')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль instagram</b>\n\nПримеры:\nhttps://www.instagram.com/karna.val/\ninstagram.com/samoylovaoxana/', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='vk')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль ВКонтакте</b>\n\nПримеры:\nhttps://vk.com/id494445129\nvk.com/id173811890', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='phone_number')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте номер телефона, начинающийся с +</b>\n\n+7...\n+3...', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='tiktok')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте никнейм пользователя</b>\n\nПримеры:\n@karinakross\n@buzova86', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='social_back')
async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)