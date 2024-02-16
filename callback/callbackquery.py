from aiogram import types, Router, F
from aiogram.types import CallbackQuery
from data.database import DataBase
from keyboards.inline import MyCallBack, MyLocation
from keyboards.inline import sale_menu, location, list_pay

db = DataBase('mainbase.db')
call_router = Router()


@call_router.callback_query(MyCallBack.filter(F.zap == "profile"))
async def buy(call: CallbackQuery):
    await call.message.answer('Твой профиль')


@call_router.callback_query(MyCallBack.filter(F.zap == "buy"))
async def buy(call: CallbackQuery):
    await call.message.answer('🌲Выбери количество...', reply_markup=sale_menu())


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
    await call.message.answer(f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.', reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'block'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Блочок')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'filtry'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Фильтровальная')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'vatut'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Ватутино')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'red'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Красный городок')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.',
        reply_markup=list_pay())
    await call.message.delete()


@call_router.callback_query(MyLocation.filter(F.loc == 'zuev'))
async def buy(call: CallbackQuery):
    user_id = call.message.chat.id
    db.add_location(user_id, 'Зуевский переезд')
    res = db.list_pay(user_id)
    await call.message.answer(
        f'Проверь заказ...\n\nТовар - {res[2]}\nРайон - {res[3]}\nСумма - {res[4]} рублей\n\nПри оплате укажи свой id-{call.message.chat.id} в комментарии к платежу.',
        reply_markup=list_pay())
    await call.message.delete()





