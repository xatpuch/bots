from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import storage
import json

with open('data/config.json') as json_file:
    config = json.load(json_file)
    BOT_TOKEN = config['Bot_Data']['Bot_Token']

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)