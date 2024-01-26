from aiogram import types, Router, F


from keyboards.inline import sale_menu

router_query = Router()


@router_query.callback_query(F.data.startswitch('buy'))
async def buy(callback: types.CallbackQuery):
    pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
    await callback.message.answear(pic, caption='Привет! Выбери товар..', reply_markup=sale_menu)
