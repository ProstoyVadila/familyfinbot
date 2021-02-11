import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import config
from admin.notify import notify_admin_on_startup
from model import db_gino
from utils.default_commands import set_default_commands


logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp: Dispatcher):
    await notify_admin_on_startup(dp)
    await db_gino.on_startup()
    await set_default_commands(dp)


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
