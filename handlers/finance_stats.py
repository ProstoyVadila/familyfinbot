from datetime import date
from typing import Union

from aiogram import types

from app import dp, bot
from messages import finance
from model.models.transaction import Finance
from keyboards.inline import finance_markups
from utils.finance.balance import get_balance_by_id_by_date


GRAPHS_CALLBACK_DATA = ('graph1_button', 'graph2_button')


@dp.message_handler(commands=['stats'])
@dp.callback_query_handler(lambda cb: cb.data == 'statistics_button')
async def get_stats(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)
    await bot.send_message(
        types_object.from_user.id,
        finance.STATS_MESSAGE_START,
        reply_markup=finance_markups.stats_markup
    )


@dp.message_handler(commands=['balance'])
@dp.callback_query_handler(lambda cb: cb.data == 'balance_stats_button')
async def get_balance(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)

    balance_data = await get_balance_by_id_by_date(types_object.from_user.id, date.today())
    answer_message = finance.BALANCE_STATS_MESSAGE.format(
        balance=balance_data.balance,
        budget=balance_data.budget
    )
    await bot.send_message(
        types_object.from_user.id,
        answer_message,
        reply_markup=finance_markups.back_stats_markup
    )
    if transactions := balance_data.transactions_data:
        trans_message = ' '.join([
            f'{item[1]} -- {item[0].value} руб. -- {item[0].created_at}\n'
            for item in transactions
        ])
        await bot.send_message(
            types_object.from_user.id,
            finance.BALANCE_TRANS_DATA_MESSAGE + trans_message,
            reply_markup=finance_markups.back_stats_markup
        )


@dp.message_handler(commands=['graphs'])
@dp.callback_query_handler(lambda cb: cb.data == 'graphs_stats_button')
async def get_graph(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)

    await bot.send_message(
        types_object.from_user.id,
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
