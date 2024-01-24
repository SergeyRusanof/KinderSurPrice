import asyncio
from aiogram import Bot, Dispatcher, F
from configure.config import TOKEN
import logging
from commands.commands import command_router, start
from filters.filters import router_filter
from callback.callbackquery import router_query
from callback.callbackquery import buy


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(command_router)
    dp.message.register(start)
    dp.message.register(buy)
    dp.include_router(router_query)
    dp.include_router(router_filter)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
