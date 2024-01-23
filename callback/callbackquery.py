from aiogram import types, Router, F
from keyboards.inline import sale_menu


router_query = Router()


@router_query.callback_query(F.data == 'buy')
async def buy(message: types.Message):
    await message.answer('Привет', reply_markup=sale_menu)
