from datetime import date
from typing import Union

from aiogram import types

from app import dp, bot
from utils.messages import finance
from utils.keyboards.inline import finance_markups
from controllers.finance.balance import get_balance_by_id_by_date, get_transaction_message
from utils.tools import answer_if_callback


GRAPHS_CALLBACK_DATA = ('graph1_button', 'graph2_button')


@dp.message_handler(commands=['stats'])
@dp.callback_query_handler(lambda cb: cb.data == 'statistics_button')
async def get_stats(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.STATS_MESSAGE_START,
        reply_markup=finance_markups.stats_markup
    )


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

    transaction_message = get_transaction_message(balance_data.transactions_data)
    await bot.send_message(
        msg_or_callback.from_user.id,
        transaction_message,
        reply_markup=finance_markups.back_stats_markup
    )


@dp.message_handler(commands=['graphs'])
@dp.callback_query_handler(lambda cb: cb.data == 'graphs_stats_button')
async def get_graph(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)

    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.GRAPH_STATS_MESSAGE,
        reply_markup=finance_markups.graphs_stats_markup
    )


@dp.callback_query_handler(lambda cb: cb.data in GRAPHS_CALLBACK_DATA)
async def get_expanse_by_categories_graph(callback: types.CallbackQuery):
    await callback.answer(cache_time=60)
    await bot.send_message(
        callback.from_user.id,
        finance.YOUR_GRAPH_MESSAGE + f'\n your graph is {callback.data}',
        reply_markup=finance_markups.back_stats_markup
    )
