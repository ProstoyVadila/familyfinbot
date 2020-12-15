from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from app import dp, bot
from messages.base import HELP_MESSAGE, HELP_MESSAGE_COMMANDS


@dp.callback_query_handler(lambda callback: callback.data == 'about_button')
async def get_help(callback: types.CallbackQuery):
    help_message = HELP_MESSAGE + '\n'.join(HELP_MESSAGE_COMMANDS)
    if callback:
        await callback.answer(cache_time=60)
        await bot.send_message(callback.from_user.id, help_message)
