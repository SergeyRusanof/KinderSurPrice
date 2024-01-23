from aiogram import types

from aiogram import F
from aiogram import Router


router_filter = Router()

@router_filter.message(F.photo)
async def photo(message: types.Message):
    pic_id = message.photo[-1].file_id
    print(pic_id)