from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from app import dp
from messages.base import START_MESSAGE


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(START_MESSAGE)
