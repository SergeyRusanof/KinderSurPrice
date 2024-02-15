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
        check_id = message.text[7:]
        referer_id = str(check_id)
        print(referer_id)
        if referer_id == '':  # Если нет id реферара
            if db.in_is_narcos(user_id) is None:  # Если нет id в базе, то добавляем
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет_1, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())
                db.add_user_in_narcos(user_id, count_pay=0, bonus=0)
                db.add_user_in_refers(user_id, friends=None, your_friend=None)
            else:
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет_2, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
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
            else:
                db.add_user_in_narcos(user_id, count_pay=0, bonus=0)
                db.add_user_in_refers(user_id, friends=None, your_friend=None)
                db.your_friend(user_id, referer_id)
                db.friends(referer_id, user_id)
                pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
                await message.answer_photo(pic,
                                           caption=f'✌️Привет - привет_4, {message.from_user.first_name}\n\n🔊Магазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь! ♥️',
                                           reply_markup=menu_start())


@router_commands.message(Command('admin'))
async def admin(message: Message):
    await message.answer('Привет Админ!')
