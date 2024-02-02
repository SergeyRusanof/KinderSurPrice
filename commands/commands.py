from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, Bot, types
from keyboards.inline import menu_start

router_commands = Router()


@router_commands.message(CommandStart())
async def start(message: Message, bot: Bot):
    if message.chat.type == 'private':
        check_id = message.text[7:]
        referer_id = str(check_id)
        print(referer_id)
        if referer_id is None:
            print(referer_id)
        if referer_id and referer_id != str(message.from_user.id):
            await is_refers(message, message.from_user.id, referer_id)

        else:
            pass
            pic = 'AgACAgEAAxkBAAMrZa_prvjsFGrgkm9ArzDReGUdL5MAAhCsMRtuFoFFHavg8sGnsF8BAAMCAAN4AAM0BA'
            await message.answer_photo(pic,
                                       caption=f'Привет - привет, {message.from_user.first_name}\n\nМагазин KinderSurprice приветствует тебя!\n\nМы топим за качество и насыпь!',
                                       reply_markup=menu_start())


async def is_refers(message: types.Message, user_id, referer_id):
    pass


@router_commands.message(Command('admin'))
async def admin(message: Message):
    await message.answer('Привет Админ!')
