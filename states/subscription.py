from aiogram.dispatcher.filters.state import StatesGroup, State

class Subscription(StatesGroup):
    waiting = State()