import asyncio
from aiogram import Bot, Dispatcher, F
from configure.config import TOKEN
import logging
from commands.commands import router_commands, start
from filters.filters import router_photo_filter
from callback.callbackquery import router_query
from callback.callbackquery import buy


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router_commands)
    dp.include_router(router_photo_filter)

    dp.include_router(router_query)
    dp.callback_query

    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
