from typing import Union

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from app import dp, bot
from messages.base import START_MESSAGE, MENU_MESSAGE
from keyboards.inline.start_markups import start_markup, menu_markup


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(START_MESSAGE, reply_markup=start_markup)


@dp.message_handler(commands=['menu'])
@dp.message_handler(lambda message: message.text == 'меню')
@dp.callback_query_handler(lambda callback: callback.data == 'menu_button')
async def get_menu(answer_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(answer_object, types.Message):
        await answer_object.answer(MENU_MESSAGE, reply_markup=menu_markup)
    else:
        await answer_object.answer(cache_time=60)
        await bot.send_message(
            answer_object.from_user.id,
            MENU_MESSAGE,
            reply_markup=menu_markup
        )
