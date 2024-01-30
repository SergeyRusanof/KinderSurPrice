from aiogram import types, Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Update

from keyboards.inline import sale_menu


async def buy_handler(call: CallbackQuery, bot: Bot):
    pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
    await call.message.answear(pic, caption='Привет! Выбери товар..', reply_markup=sale_menu)
