from aiogram import Router, types, F

from keyboards.inline import MyCallBack

refs_router = Router()


@refs_router.callback_query(MyCallBack.filter(F.zap == 'refs'))
async def start(call: types.CallbackQuery):
    link = f'Привет! Вот ссылка для твоего друга:\n\nhttps://t.me/kindersur_bot?start={call.message.chat.id}\n\nКогда он перейдёт по ней, стартанёт бот, купит товар - у тебя в профиле будет виден бонус - это пятка)\n\nМожно собирать бонусы или запрашивать сразу локацию с бонусом и курануть.'
    await call.message.answer(link)

