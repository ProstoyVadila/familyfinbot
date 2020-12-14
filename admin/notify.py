import logging

from aiogram import Dispatcher

from config import ADMIN_ID


async def notify_admin_on_startup(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, 'Bot launched')
    except Exception as err:
        logging.exception(err)
