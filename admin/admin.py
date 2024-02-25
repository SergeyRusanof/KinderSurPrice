from aiogram import types, Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from keyboards.inline import admin_start
from aiogram.filters import Command
from configure.config import ADMIN
from keyboards.inline import ToAdmin
from data.database import DataBase

db = DataBase('mainbase.db')
admin_router = Router()


class GetId(StatesGroup):
    id = State()


@admin_router.message(Command('admin'))
async def admin(message: types.Message):
    if message.chat.id == int(ADMIN):
        await message.answer('Привет', reply_markup=admin_start())
    else:
        await message.answer('Ты не Админ!')


@admin_router.callback_query(ToAdmin.filter(F.adm == 'look_id'))
async def look_id(call: CallbackQuery, state: FSMContext):
    await state.set_state(GetId.id)
    await call.message.answer('Отправь id юзера для проверки в чат')


@admin_router.message(GetId.id)
async def catch_id(message: types.Message, state: FSMContext):
    data = await state.update_data(user_id=message.text)
    user_id = data['user_id']
    info = db.get_info(user_id)[0]
    await message.answer(f'{info}')
