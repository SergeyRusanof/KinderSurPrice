from aiogram import types

from aiogram import F
from aiogram import Router


router_photo_filter = Router()


#@router_photo_filter.message(F.photo)
#async def photo(message: types.Message):
#    pic_id = message.photo[-1].file_id
#    print(pic_id)