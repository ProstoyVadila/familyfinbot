from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from app import dp, bot
from messages.base import HELP_MESSAGE, HELP_MESSAGE_COMMANDS
from keyboards.inline.start_markups import back_to_menu_markup


@dp.message_handler(CommandHelp())
@dp.callback_query_handler(lambda callback: callback.data == 'about_button')
async def get_help(answer_object: Union[types.Message, types.CallbackQuery]):
    help_message = HELP_MESSAGE.format(
        user_name=answer_object.from_user.id) + '\n'.join(HELP_MESSAGE_COMMANDS)

    if isinstance(answer_object, types.Message):
        await answer_object.answer(help_message, reply_markup=back_to_menu_markup)
    else:
        await answer_object.answer(cache_time=60)
        await bot.send_message(
            answer_object.from_user.id,
            help_message,
            reply_markup=back_to_menu_markup
        )
