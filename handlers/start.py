from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from app import dp, bot
from messages.base import START_MESSAGE, MENU_MESSAGE
from keyboards.inline.start_markups import start_markup, menu_markup


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(START_MESSAGE, reply_markup=start_markup)


@dp.callback_query_handler(lambda callback: callback.data == 'menu_button')
async def get_menu(callback: types.CallbackQuery = None):
    await callback.answer(cache_time=60)
    await bot.send_message(
        callback.from_user.id,
        MENU_MESSAGE,
        reply_markup=menu_markup
    )
