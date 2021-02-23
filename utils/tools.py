from typing import Union

from aiogram import types


async def answer_if_callback(msg_or_cb_object: Union[types.Message, types.CallbackQuery]):
    """close open callback query"""
    if isinstance(msg_or_cb_object, types.CallbackQuery):
        await msg_or_cb_object.answer(cache_time=60)
