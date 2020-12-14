import logging

from aiogram import Bot, Dispatcher, executor

import config
from admin.notify import notify_admin_on_startup


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp: Dispatcher):
    await notify_admin_on_startup(dp)


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)