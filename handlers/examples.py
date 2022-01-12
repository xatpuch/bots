from loader import dp
from aiogram import types

@dp.message_handler(text='💡 Примеры 💡')
async def examples(message: types.Message):
    photo='https://sun9-69.userapi.com/impg/awSN85-juSTO7tCXY61q0X12q5sdXKun10xBNw/fVHxjQPdniY.jpg?size=640x1180&quality=96&sign=59c096d7cd0beb2bb2ac2a4393eb4da9&type=album'
    text = '🔎 Бот ищет отправленные фото и видео по слитым базам СНГ!\n\n1️⃣ База насчитывает более 10.000.000 отправленных видео/фото и разработана профессиональными кодерами и хакерами из РФ 🇷🇺!\n\nДаже удаленные медиа сохраняются мгновенно!'
    await message.answer_photo(photo, text)