import os
import asyncio
from aiogram import Bot, Dispatcher, F
import logging
from commands.commands import router_commands, start
from filters.filters import router_photo_filter
from callback.callbackquery import call_router
from pay.pay import pay_router
from utils.ref_system import refs_router
from admin.admin import admin_router

from dotenv import load_dotenv, find_dotenv
from data.database import DataBase

load_dotenv(find_dotenv())
db = DataBase('mainbase.db')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    db.create_table()
    db.location_base()
    db.refers_table()
    db.to_buy_table()
    db.payment_table()
    dp.include_router(router_commands)
    dp.include_router(router_photo_filter)
    dp.include_router(call_router)
    dp.include_router(refs_router)
    dp.include_router(pay_router)
    dp.include_router(admin_router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
