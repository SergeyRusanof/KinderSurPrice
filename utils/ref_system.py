from aiogram import Router, types, F
from keyboards.inline import MyCallBack

refs_router = Router()



@refs_router.callback_query(MyCallBack.filter(F.zap == 'refs'))
async def start(message: types.Message):
    link = 'https://t.me/kindersur_bot?start={message.from_user.id}'
    if message.chat.type == 'private':
        check_id = message.text[7:]
        referer_id = str(check_id)
        result = None
        if result is None:
            pass
        if referer_id and referer_id != str(message.from_user.id):
            pass
        else:
            pass



async def is_refers(message: types.Message, user_id, referer_id):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('UPDATE referal SET referer_id=? WHERE user_id=?', (referer_id, user_id))
    con.commit()
    await bot.send_message(referer_id, 'Новый реферал перешёл по твоей ссылке!')