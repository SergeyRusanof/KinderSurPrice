from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScope, Update


async def bot_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начало'),
        BotCommand(command='admin', description='Для админа', scope=BotCommandScope.SUPERUSER)
    ]