import asyncio
from aiogram import Bot, Dispatcher
from configure.config import TOKEN
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router
from commands.commands import command_router
from filters.filters import router_filter
from callback.callbackquery import router_query


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(command_router)
    dp.include_router(router_filter)
    dp.include_router(router_query)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
