import asyncio

from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, Bot, types
from keyboards.inline import menu_start
from data.database import DataBase

router_commands = Router()
db = DataBase('mainbase.db')


@router_commands.message(CommandStart())
async def start(message: Message):
    if message.chat.type == 'private':
        user_id = message.chat.id
        name = message.from_user.first_name
        check_id = message.text[7:]
        referer_id = str(check_id)
        if referer_id == '':  # Если нет id реферара
            if db.in_is_narcos(user_id) is None:  # Если нет id в базе, то добавляем
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет_1, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())
                db.add_user_in_narcos(user_id, count_pay=0, bonus=0)
                db.add_user_in_refers(user_id, friends=None, your_friend=None)
                db.add_in_to_buy(user_id, prod=None, location=None, price=None)
                await db.add_users_payment(user_id, name)
            else:
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())

        else:
            if int(user_id) == int(referer_id):  # Если есть id реферера
                await message.answer('Ты пытаешься стать своим рефералом - это невозможно!')
                await asyncio.sleep(2)
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет, {message.from_user.first_name}!\n\n🔊Магаз KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())

                db.add_user_in_refers(user_id, friends=None, your_friend=None)
                db.add_user_in_narcos(user_id, count_pay=0, bonus=0)
                db.add_in_to_buy(user_id, prod=None, location=None, price=None)
                await db.add_users_payment(user_id, name)

            else:
                db.add_user_in_narcos(user_id, count_pay=0, bonus=0) # В таблицу наркоманов
                db.add_user_in_refers(user_id, friends=None, your_friend=None) # В таблицу рефералов
                db.add_in_to_buy(user_id, prod=None, location=None, price=None) # В таблицу заказа
                await db.add_users_payment(user_id, name)

                db.your_friend(user_id, referer_id)
                db.friends(referer_id, user_id)
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())


@router_commands.message(Command('admin'))
async def admin(message: Message):
    await message.answer('Привет Админ!')
