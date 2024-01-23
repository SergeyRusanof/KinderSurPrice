from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router

command_router = Router()


@command_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет - привет!')


@command_router.message(Command('admin'))
async def admin(message: Message):
    await message.answer('Привет Админ!')