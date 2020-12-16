from aiogram import types

from app import dp, bot
from messages.base import BUDGET_MESSAGE_START, BUDGET_MESSAGE_END
from keyboards.inline.finance_markups import budget_markup


@dp.callback_query_handler(lambda callback: callback.data == 'budget_button')
async def get_budget(callback: types.CallbackQuery):
    await callback.answer(cache_time=60)
    await bot.send_message(
        callback.from_user.id,
        BUDGET_MESSAGE_START,
        reply_markup=budget_markup
    )
