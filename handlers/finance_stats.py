from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import base, error
from keyboards.finance_keyboard import income_category_keyboard, menu_keyboard
from states.finance_states import IncomeState


@dp.message_handler(commands=['stats']
@dp.callback_query_handler(lambda callback: callback.data == 'statistics_button')
async def get_stats(answer_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(answer_object, types.CallbackQuery):
        await answer_object.answer(cache_time=60)
    await bot.send_message(
        answer_object.from_user.id,
        base.STATS_MESSAGE_START
    )
