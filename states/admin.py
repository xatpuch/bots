from aiogram.dispatcher.filters.state import StatesGroup, State

class Admin(StatesGroup):
    wait_admin_id = State()
    wait_admin_id_remove = State()
    wait_for_text = State()
    wait_for_picture = State()
    wait_for_qiwi = State()
    wait_for_category = State()
    wait_for_price = State()
    wait_for_username = State()
    wait_for_link = State()
    wait_for_percentage = State()
    wait_for_yoo = State()
    wait_for_percentage_ind = State()