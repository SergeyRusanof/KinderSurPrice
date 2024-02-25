from aiogram import types, Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from keyboards.inline import admin_start
from aiogram.filters import Command, StateFilter
from configure.config import ADMIN
from keyboards.inline import ToAdmin
from data.database import DataBase

db = DataBase('mainbase.db')
admin_router = Router()


class GetId(StatesGroup):
    id = State()


class AddLocation(StatesGroup):
    product = State()
    price = State()
    area = State()
    foto = State()


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


@admin_router.message(StateFilter('*'), F.text.casefold() == ['отмена', 'jnvtyf'])
async def cancel_fsm(message: types.Message, state: FSMContext):
    await message.answer('Действия отменены', reply_markup=admin_start())


@admin_router.callback_query(StateFilter(None), ToAdmin.filter(F.adm == 'add_loc'))
async def add_product(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Отправь товар "Грамм", "Полка(0,5 грамма)"..')
    await state.set_state(AddLocation.product)


@admin_router.message(AddLocation.product, F.text)
async def add_price(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer('Отправь цену')
    await state.set_state(AddLocation.price)


@admin_router.message(AddLocation.price, F.text)
async def add_area(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Отправь район города')
    await state.set_state(AddLocation.area)


@admin_router.message(AddLocation.area, F.text)
async def add_foto(message: types.Message, state: FSMContext):
    await state.update_data(area=message.text)
    await message.answer('Отправь фото с адресом')
    await state.set_state(AddLocation.foto)


@admin_router.message(AddLocation.foto, F.photo)
async def add_foto(message: types.Message, state: FSMContext):
    await state.update_data(foto=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer(f'Готово:\n\n{data}')
    print(data)
    await state.clear()
