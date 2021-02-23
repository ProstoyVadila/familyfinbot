from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from app import bot, dp
from messages.base import START_MESSAGE, MENU_MESSAGE
from model.models.user import User
from keyboards.inline.start_markups import start_markup, menu_markup
from utils.tools import answer_if_callback


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(START_MESSAGE, reply_markup=start_markup)
    await User.get_or_create(
        message.chat.id,
        message.from_user.full_name
    )


@dp.message_handler(commands=['menu'])
@dp.message_handler(lambda message: message.text == 'меню')
@dp.callback_query_handler(lambda callback: callback.data == 'menu_button')
async def get_menu(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        MENU_MESSAGE,
        reply_markup=menu_markup
    )
