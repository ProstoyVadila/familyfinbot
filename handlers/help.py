from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from app import dp, bot
from utils.messages.base import HELP_MESSAGE, HELP_MESSAGE_COMMANDS
from utils.keyboards.inline.start_markups import back_to_menu_markup
from utils.tools import answer_if_callback


@dp.message_handler(CommandHelp())
@dp.callback_query_handler(lambda callback: callback.data == 'about_button')
async def get_help(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    help_message = HELP_MESSAGE.format(
        user_name=msg_or_callback.from_user.username) \
                   + '\n'.join(HELP_MESSAGE_COMMANDS)

    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        help_message,
        reply_markup=back_to_menu_markup
    )
