from typing import Union

from aiogram import types

from app import bot, dp
from utils.tools import answer_if_callback
from utils.keyboards.inline.other_markups import donate_markup
from utils.messages import base


@dp.message_handler(commands=['donate'])
@dp.callback_query_handler(lambda callback: callback.data == 'donate_button')
async def add_donate(msg_or_callabck: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callabck)

    await bot.send_message(
        msg_or_callabck.from_user.id,
        base.DONATE_MESSAGE,
        reply_markup=donate_markup
    )


@dp.callback_query_handler(lambda callback: callback.data == 'donate_done_button')
async def thank_donator(callback: types.CallbackQuery):
    await answer_if_callback(callback)
    await bot.send_message(callback.from_user.id, base.THANK_DONATOR_MESSAGE)
