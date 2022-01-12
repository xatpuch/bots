from loader import dp
from aiogram import types
from aiogram.utils.markdown import hlink
from aiogram.dispatcher.storage import FSMContext
from utils import qiwi, yoomoneyx
from utils.get_price import get_price
from keyboards import payment_methods_keyboard, purchase_unlimited_keyboard, payment_keyboard

@dp.callback_query_handler(text='buy_archive')
async def buy_archive(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Archive')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Archive')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        print(e)
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='buy_photo')
async def buy_photo(callback: types.CallbackQuery, state: FSMContext):
    try: 
        price = get_price('Photo')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Photo')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='buy_phone')
async def buy_phone(callback: types.CallbackQuery, state: FSMContext):
    try: 
        price = get_price('Phone_Number')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Phone_Number')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='buy_messages')
async def buy_messages(callback: types.CallbackQuery, state: FSMContext):
    try: 
        price = get_price('Messages_Archive')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Messages_Archive')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='buy_unlimited')
async def buy_unlimited(callback: types.CallbackQuery):
    text = '<b>💳 Оформление подписки\n\n🔎 Безлимитный поиск -  обеспечивает доступ ко всем функциям, быстрой обработки данных.\n\n💗 Забирайте фуллы всех девочек, пока у вас есть 👉🏻 🔎 Безлимитный поиск\n\nВыберите тариф оплаты 👇</b>'
    await callback.message.edit_text(text, reply_markup=purchase_unlimited_keyboard.make_keyboard())

@dp.callback_query_handler(text='unlimited_one_day')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Unlimited_1')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Unlimited_1')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='unlimited_week')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Unlimited_7')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Unlimited_7')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='unlimited_month')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Unlimited_30')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Unlimited_30')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='phone_leaks')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Phone_Number_Leaks')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Phone_Number_Leaks')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='phone_info')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Phone_Number_Info')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Phone_Number_Info')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='buy_tiktok_archive')
async def buy_unlimited_one_day(callback: types.CallbackQuery, state: FSMContext):
    try:
        price = get_price('Tiktok_Videos')
        payment = qiwi.Payment()
        payment_yoo = yoomoneyx.PaymentYoo()
        payment_yoo.create(price, 'Archive')
        payment.create(price, 'Tiktok_Videos')
        text = f'<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
        
        await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
        async with state.proxy() as data:
            data['payment'] = payment
            data['payment_yoo'] = payment_yoo
    except Exception as e:
        if e.args[0] == 'Qiwi wallet is banned':
            await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
        else:
            await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')

@dp.callback_query_handler(text='method_qiwi')
async def qiwi_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    type = payment.type
    link = hlink('Оплата', payment.invoice())
    amount = payment.amount
    text = f'➖➖➖➖➖➖➖➖➖➖➖\n<b>♻️ Оплата QIWI | Банковской картой:</b>{link}\n<b>💰 Сумма: </b>{amount} <b>🇷🇺 RUB</b>\n<b>💭 Комментарий: </b><code>{payment.comment}</code>\n\n<b>ВАЖНО ❗️ </b>Обязательно пишите комментарий к платежу\n➖➖➖➖➖➖➖➖➖➖➖'
    await callback.message.edit_text(text, reply_markup=payment_keyboard.make_keyboard(payment.invoice(), type))

@dp.callback_query_handler(text='method_yoo')
async def qiwi_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: yoomoneyx.PaymentYoo = data['payment_yoo']
    type = payment.type
    link = hlink('Оплата', payment.invoice())
    amount = payment.amount
    text = f'➖➖➖➖➖➖➖➖➖➖➖\n<b>♻️ Оплата YOOMONEY | Банковской картой:</b>{link}\n<b>💰 Сумма: </b>{amount} <b>🇷🇺 RUB</b>\n➖➖➖➖➖➖➖➖➖➖➖'
    await callback.message.edit_text(text, reply_markup=payment_keyboard.make_keyboard(payment.invoice(), f'{type}', pref='YOO'))

@dp.callback_query_handler(text='cancel_payment')
async def cancel(callback: types.CallbackQuery):
    await callback.message.edit_text('❌ Отменено ❌')