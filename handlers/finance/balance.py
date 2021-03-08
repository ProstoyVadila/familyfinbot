from datetime import date
from typing import Union

from aiogram import types

from app import dp, bot
from utils.messages import finance
from utils.keyboards.inline import start_markups
from controllers.finance.balance import get_balance_by_id_by_date, get_transaction_message
from utils.tools import answer_if_callback


@dp.message_handler(commands=['balance'])
@dp.callback_query_handler(lambda cb: cb.data == 'balance_stats_button')
async def get_balance(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)

    balance_data = await get_balance_by_id_by_date(msg_or_callback.from_user.id, date.today())
    balance_message = finance.BALANCE_STATS_MESSAGE.format(
        balance=balance_data.balance,
        budget=balance_data.budget
    )
    await bot.send_message(
        msg_or_callback.from_user.id,
        balance_message)

    transaction_message = get_transaction_message(balance_data)
    await bot.send_message(
        msg_or_callback.from_user.id,
        transaction_message,
        reply_markup=start_markups.back_to_menu_markup
    )

