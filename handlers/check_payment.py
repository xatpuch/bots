from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from utils import qiwi, database, generate_random_good, yoomoneyx
import datetime
from utils.get_price import get_price
from keyboards import payment_methods_keyboard
import asyncio
import json

@dp.callback_query_handler(text='check_payment_Archive')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nСсылка на архив: {generate_random_good.get_random_archive()}')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')
    
@dp.callback_query_handler(text='check_payment_Photo')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nСсылка на фото: {generate_random_good.get_random_photo()}')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')
    
@dp.callback_query_handler(text='check_payment_Phone_Number')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nНомер телефона: {generate_random_good.generate_phone_number()}')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Messages_Archive')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nСсылка на архив с переписками: {generate_random_good.get_random_messages()}')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Unlimited_1')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment():
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
        purchases = config['Statistics']['Purchases']
        total_earned = config['Statistics']['Total_Earned']
        config['Statistics']['Purchases'] = purchases + 1
        config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
        admins = config['Bot_Data']['Admins']
        for admin in admins:
            try:
                await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
            except:
                pass
        try:
            referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
            database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
        except Exception as e:
            print(e)
        with open('data/config.json', 'w') as json_file:
            json.dump(config, json_file)
        date = datetime.datetime.now().date() + datetime.timedelta(days=1)
        database.update_user(callback.from_user.id, 'unlimited', date)
        await callback.message.edit_text(f'Оплата получена!\n\nТеперь вы можете безлимитно пользоваться ботом в течении 1 дня!\n\n<b><i>При покупке какой-либо услуги нажмите проверить оплату, если у вас приобретен безлимит - платить не придется!</i></b>')
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Unlimited_7')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment():
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
        purchases = config['Statistics']['Purchases']
        total_earned = config['Statistics']['Total_Earned']
        config['Statistics']['Purchases'] = purchases + 1
        config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
        admins = config['Bot_Data']['Admins']
        for admin in admins:
            try:
                await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
            except:
                pass
        try:
            referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
            database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
        except Exception as e:
            print(e)
        with open('data/config.json', 'w') as json_file:
            json.dump(config, json_file)
        date = datetime.datetime.now().date() + datetime.timedelta(days=7)
        database.update_user(callback.from_user.id, 'unlimited', date)
        await callback.message.edit_text(f'Оплата получена!\n\nТеперь вы можете безлимитно пользоваться ботом в течении 7 дней!\n\n<b><i>При покупке какой-либо услуги нажмите проверить оплату, если у вас приобретен безлимит - платить не придется!</i></b>')
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Unlimited_30')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment():
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
        purchases = config['Statistics']['Purchases']
        total_earned = config['Statistics']['Total_Earned']
        config['Statistics']['Purchases'] = purchases + 1
        config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
        admins = config['Bot_Data']['Admins']
        for admin in admins:
            try:
                await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
            except:
                pass
        try:
            referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
            database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
        except Exception as e:
            print(e)
        with open('data/config.json', 'w') as json_file:
            json.dump(config, json_file)
        date = datetime.datetime.now().date() + datetime.timedelta(days=30)
        database.update_user(callback.from_user.id, 'unlimited', date)
        await callback.message.edit_text(f'Оплата получена!\n\nТеперь вы можете безлимитно пользоваться ботом в течении 30 дней!\n\n<b><i>При покупке какой-либо услуги нажмите проверить оплату, если у вас приобретен безлимит - платить не придется!</i></b>')
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Phone_Number_Leaks')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
        try:
            price = get_price('Archive')
            payment_2 = yoomoneyx.PaymentYoo()
            payment_2.create(price, 'Archive')
            await callback.message.edit_text(f'<b>Поиск...</b>')
            await asyncio.sleep(5)
            text = f'Слив найден!\n\n<b>💵 К оплате: </b>{price}₽\n\n<b>Выберите способ оплаты 👇</b>'
            await callback.message.edit_text(text, reply_markup=payment_methods_keyboard.keyboard)
            async with state.proxy() as data:
                data['payment'] = payment_2
        except Exception as e:
            if e.args[0] == 'Qiwi wallet is banned':
                await callback.message.edit_text('<b>К сожалению, кошелек заблокирован.\n\nОбратитесь в техроддержку.</b>')
            else:
                await callback.message.edit_text('<b>Произошла неизвестная ошибка.\n\nОбратитесь в техподдержку</b>')
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Phone_Number_Info')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nСсылка на информацию: https://disk.yandex.ru/d/_d1j8kWdf3zx')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')

@dp.callback_query_handler(text='check_payment_Tiktok_Videos')
async def check_payment(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        payment: qiwi.Payment = data['payment']
    if payment.check_payment() or (database.get_user(callback.from_user.id)['unlimited'] > datetime.datetime.now().date()):
        await callback.message.edit_text(f'Оплата получена!\n\nСсылка на архив с видео: https://disk.yandex.ru/d/_d1j8kWdCx3f')
        if payment.check_payment():
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            percentage = float(database.get_user(database.get_user(callback.from_user.id)['invited_by'])['percentage'])
            purchases = config['Statistics']['Purchases']
            total_earned = config['Statistics']['Total_Earned']
            config['Statistics']['Purchases'] = purchases + 1
            config['Statistics']['Total_Earned'] = int(total_earned) + int(payment.amount)
            admins = config['Bot_Data']['Admins']
            for admin in admins:
                try:
                    await bot.send_message(admin, f'<b>💵💵Новая покупка!💵💵</b>\n\n<b>Юзер: </b><code>{callback.from_user.username} ({callback.from_user.id})</code>\n<b>Сумма: </b><code>{payment.amount}</code>\n<b>Пригласил: <code>{database.get_user(database.get_user(callback.from_user.id)["invited_by"])["username"]} ({database.get_user(callback.from_user.id)["invited_by"]})</code></b>')
                except:
                    pass
            try:
                referal_balance = database.get_user(database.get_user(callback.from_user.id)['invited_by'])['balance']
                database.update_user(database.get_user(callback.from_user.id)['invited_by'], 'balance', (float(referal_balance) + int(payment.amount) * float(percentage)))
            except Exception as e:
                print(e)
            with open('data/config.json', 'w') as json_file:
                json.dump(config, json_file)
    else:
        await callback.answer('Оплата не найдена!')