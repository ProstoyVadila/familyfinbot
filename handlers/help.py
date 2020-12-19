from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from app import dp, bot
from messages.base import HELP_MESSAGE, HELP_MESSAGE_COMMANDS
from keyboards.inline.start_markups import back_to_menu_markup


@dp.message_handler(CommandHelp())
@dp.callback_query_handler(lambda callback: callback.data == 'about_button')
async def get_help(types_object: Union[types.Message, types.CallbackQuery]):
    help_message = HELP_MESSAGE.format(
        user_name=types_object.from_user.username) \
                   + '\n'.join(HELP_MESSAGE_COMMANDS)

    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)
    await bot.send_message(
        types_object.from_user.id,
        help_message,
        reply_markup=back_to_menu_markup
    )
