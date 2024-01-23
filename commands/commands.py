from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router
from keyboards.inline import menu_start

command_router = Router()


@command_router.message(CommandStart())
async def start(message: Message):
    pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
    await message.answer_photo(pic,
                               caption=f'Привет - привет, {message.from_user.first_name}\n\nМагазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь!',
                               reply_markup=menu_start)


@command_router.message(Command('admin'))
async def admin(message: Message):
    await message.answer('Привет Админ!')
