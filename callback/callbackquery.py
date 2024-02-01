from aiogram import types, Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Update
from keyboards.inline import MyCallBack, MyLocation
from keyboards.inline import sale_menu, location


call_router = Router()


@call_router.callback_query(MyCallBack.filter(F.zap == "buy"))
async def buy(call: CallbackQuery):
    await call.message.answer('🌲Выбери количество...', reply_markup=sale_menu())


@call_router.callback_query(MyCallBack.filter(F.zap == "gramm"))
async def buy(call: CallbackQuery):
    await call.message.answer('🏘 Выбери район...', reply_markup=location())
    await call.message.delete()
