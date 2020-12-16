from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from app import dp, bot
from messages.base import HELP_MESSAGE, HELP_MESSAGE_COMMANDS
from keyboards.inline.start_markups import back_to_menu_markup


@dp.callback_query_handler(lambda callback: callback.data == 'about_button')
async def get_help(callback: types.CallbackQuery):
    help_message = HELP_MESSAGE.format(
        user_name=callback.from_user.first_name) + '\n'.join(HELP_MESSAGE_COMMANDS)
    await callback.answer(cache_time=60)
    await bot.send_message(
        callback.from_user.id,
        help_message,
        reply_markup=back_to_menu_markup
    )
