from app import dp

from aiogram import types
from aiogram.types.message import ContentType


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    await message.reply(f'Слушай, это незнакомая мне команда.')
