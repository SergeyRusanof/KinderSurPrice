from aiogram import types, Router, F
from aiogram.types import CallbackQuery, Message

import commands.commands
from data.database import DataBase
from keyboards.inline import MyCallBack, MyLocation, ToBuy, menu_start, ToAdmin, ToProf
from keyboards.inline import sale_menu, location, list_pay, menu_profile

db = DataBase('mainbase.db')
call_router = Router()


@call_router.callback_query(MyCallBack.filter(F.zap == "profile"))
async def buy(call: CallbackQuery):
    data = db.take_bonus(call.message.chat.id)
    await call.message.answer(f'Твой профиль {call.message.chat.first_name}'
                              f'\n\nКоличество покупок: {db.count_pays(call.message.chat.id)}'
                              f'\n\nТы привёл: {db.prof_friends(call.message.chat.id)} друзей'
                              f'\n\nБонусы: {db.check_bonus(call.message.chat.id)}', reply_markup=menu_profile())


@call_router.callback_query(MyCallBack.filter(F.zap == "buy"))
async def buy(call: CallbackQuery):
    await call.message.answer('🌲Выбери товар. Колличество указано в скобочках..', reply_markup=sale_menu())


@call_router.callback_query(MyCallBack.filter(F.zap == "gramm"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Грамм', 3000)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


@call_router.callback_query(MyCallBack.filter(F.zap == "polka"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Пол грамма', 1500)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


@call_router.callback_query(MyCallBack.filter(F.zap == "full"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Корабль', 2000)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


@call_router.callback_query(MyCallBack.filter(F.zap == "path_full"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Пол корабля', 1000)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


@call_router.callback_query(MyCallBack.filter(F.zap == "glass"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Стакан', 25000)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


@call_router.callback_query(MyCallBack.filter(F.zap == "decl"))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_product(user_id, 'Пятка', 500)
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()


### выбор локации пользователем

@call_router.callback_query(MyLocation.filter(F.loc == 'city'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Центр')
    res = db.list_pay(user_id)
    data = db.check_product_availability(res[3], res[2])
    if data != 0:
        await call.message.answer(f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n', reply_markup=list_pay())
    else:
        await call.message.answer('к сожалению в данном районе отсутствует товар\nВыберите другую локацию..')
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'block'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Блочок')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'filtry'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Фильтровальная')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'vatut'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Ватутино')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'red'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Красный городок')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'zuev'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Зуевский')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(ToBuy.filter(F.buy == 'cancel_pay'))
async def cancel_pay(call: CallbackQuery):
    await db.clear_payment_bd(call.message.chat.id)  # отчищаем после отмены
    await call.message.answer('Отмена заказа', reply_markup=menu_start())


@call_router.callback_query(ToProf.filter(F.prof == 'take_bonus'))
async def cancel_pay(call: CallbackQuery):
    await call.message.answer('Вот Бонус!')








